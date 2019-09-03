"""
module for db interactions
"""
# pyre-strict
import logging
import pydgraph
from aiohttp import web

_LOG: logging.Logger = logging.getLogger(__name__)


def initialize_db(app: web.Application) -> None:
    _LOG.debug("connecting to db: localhost:9080")
    client_stub = pydgraph.DgraphClientStub("localhost:9080")
    client = pydgraph.DgraphClient(client_stub)
    app["db"] = client
    _LOG.debug("connected to db: localhost:9080")
    return
