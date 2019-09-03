"""
Module to manage the web application
"""
# pyre-strict
import logging
from typing import Dict, Any
from aiohttp import web
from chambordpi import routes
from chambordpi import db

_LOG: logging.Logger = logging.getLogger(__name__)


def create_app(**kwargs: Any) -> web.Application:
    """
    initialize chambordpi aiohttp web.Application
    """
    app = web.Application()
    routes.add_routes(app)
    # this can move to extras if I go that route of defining a full logging setup.
    registered_routes = [(route.method, route.get_info()["path"]) for route in app.router.routes()]
    _LOG.debug("routes registered: %s", registered_routes)
    db.initialize_db(app)

    return app


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    web.run_app(create_app())
