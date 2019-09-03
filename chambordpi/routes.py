"""
module for managing uris to the application
"""
# pyre-strict
import logging
from aiohttp import web
from chambordpi import views

_LOG: logging.Logger = logging.getLogger(__name__)


def add_routes(app: web.Application) -> None:
    """
    register routes on an aiohttp web.Application
    """
    new_routes = [web.get("/", views.handler), web.post("/api", views.another_handler)]
    _LOG.debug("registering routes: %s", [(route.method, route.path) for route in new_routes])
    app.add_routes(new_routes)
