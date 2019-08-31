import logging
from aiohttp import web
from chambordpi import views

_LOG: logging.Logger = logging.getLogger()


def add_routes(app: web.Application) -> None:
    _LOG.debug("registering routes")
    app.add_routes([web.post("/api", views.another_handler)])
