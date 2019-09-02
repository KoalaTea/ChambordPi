# pyre-strict
import logging
from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    return web.Response(text="abc")


async def another_handler(request: web.Request) -> web.Response:
    return web.json_response({"data": "exists"})
