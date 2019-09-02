from chambordpi import app
from aiohttp import web
import logging

_LOG: logging.Logger = logging.getLogger(__name__)


def run_application() -> None:
    logging.basicConfig(level="DEBUG")
    _LOG.info("initializing ChambordPi app")
    app_instance = app.create_app()
    _LOG.info("starting ChambordPi")
    web.run_app(app_instance)


if __name__ == "__main__":
    run_application()
