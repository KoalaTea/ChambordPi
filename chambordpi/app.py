# pyre-strict
import logging
from typing import Dict, Any
from aiohttp import web
from chambordpi import routes

_LOG: logging.Logger = logging.getLogger(__name__)


async def handler(request: web.Request) -> web.Response:
    return web.Response(text="abc")


def create_app(**kwargs: Any) -> web.Application:
    app = web.Application()
    app.add_routes([web.get("/", handler)])
    routes.add_routes(app)

    return app


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    web.run_app(create_app())
