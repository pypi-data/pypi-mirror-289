"""Provide main entrypoint."""
import asyncio
import inspect
import json
import logging
import os
import re
import sys
import urllib.request

import aiofiles
import yaml
from hypha_rpc.utils import ObjectProxy
from hypha_rpc.websocket_client import connect_to_server


logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("browser-runner")
logger.setLevel(logging.INFO)


async def export_service(plugin_api, config, hypha_rpc):
    try:
        wm = await connect_to_server(config)
        hypha_rpc.api.update(wm)  # make the api available to the app
        rpc = wm.rpc
        if not isinstance(plugin_api, dict) and inspect.isclass(type(plugin_api)):
            plugin_api = {a: getattr(plugin_api, a) for a in dir(plugin_api)}
        # Copy the app name as the default name
        plugin_api["id"] = "default"
        plugin_api["name"] = config.get("name", "default")
        svc = await rpc.register_service(plugin_api, overwrite=True, notify=True)
        svc = await rpc.get_remote_service(svc["id"])
        if svc.setup:
            await svc.setup()
    except Exception as exp:
        logger.exception(exp)
        loop = asyncio.get_event_loop()
        loop.stop()
        sys.exit(1)


async def patch_hypha_rpc(default_config):
    import hypha_rpc

    def export(api, config=None):
        default_config.update(config or {})
        hypha_rpc.ready = asyncio.ensure_future(
            export_service(api, default_config, hypha_rpc)
        )

    hypha_rpc.api = ObjectProxy(export=export)
    return hypha_rpc


async def run_plugin(plugin_file, default_config, quit_on_ready=False):
    """Load app file."""
    loop = asyncio.get_event_loop()
    if os.path.isfile(plugin_file):
        async with aiofiles.open(plugin_file, "r", encoding="utf-8") as fil:
            content = await fil.read()
    elif plugin_file.startswith("http"):
        with urllib.request.urlopen(plugin_file) as response:
            content = response.read().decode("utf-8")
        # remove query string
        plugin_file = plugin_file.split("?")[0]
    else:
        raise Exception(f"Invalid input app file path: {plugin_file}")

    if plugin_file.endswith(".py"):
        filename, _ = os.path.splitext(os.path.basename(plugin_file))
        default_config["name"] = filename[:32]
        hypha_rpc = await patch_hypha_rpc(default_config)
        exec(content, globals())  # pylint: disable=exec-used
        logger.info("Plugin executed")

        if quit_on_ready:

            def done_callback(fut):
                if fut.done():
                    if fut.exception():
                        logger.error(fut.exception())
                loop.stop()

            hypha_rpc.ready.add_done_callback(done_callback)

    elif plugin_file.endswith(".imjoy.html"):
        # load config
        found = re.findall("<config (.*)>\n(.*)</config>", content, re.DOTALL)[0]
        if "json" in found[0]:
            plugin_config = json.loads(found[1])
        elif "yaml" in found[0]:
            plugin_config = yaml.safe_load(found[1])
        default_config.update(plugin_config)
        hypha_rpc = await patch_hypha_rpc(default_config)
        # load script
        found = re.findall("<script (.*)>\n(.*)</script>", content, re.DOTALL)[0]
        if "python" in found[0]:
            exec(found[1], globals())  # pylint: disable=exec-used
            logger.info("Plugin executed")
            if quit_on_ready:
                hypha_rpc.ready.add_done_callback(lambda fut: loop.stop())
        else:
            raise RuntimeError(
                f"Invalid script type ({found[0]}) in file {plugin_file}"
            )
    else:
        raise RuntimeError(f"Invalid script file type ({plugin_file})")


async def start(args):
    """Run the app."""
    try:
        default_config = {
            "server_url": args.server_url,
            "workspace": args.workspace,
            "token": args.token,
        }
        await run_plugin(args.file, default_config, quit_on_ready=args.quit_on_ready)
    except Exception:  # pylint: disable=broad-except
        logger.exception("Failed to run app, exiting.")
        loop = asyncio.get_event_loop()
        loop.stop()
        sys.exit(1)


def start_runner(args):
    """Start the app runner."""
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(start(args))
    loop.run_forever()
