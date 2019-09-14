"""
module for db interactions
"""
# pyre-strict
import logging
import pydgraph
from aiohttp import web
from chambordpi import settings

_LOG: logging.Logger = logging.getLogger(__name__)


def initialize_db(app: web.Application) -> None:
    _LOG.debug("connecting to db: localhost:9080")
    client_stub = pydgraph.DgraphClientStub(f"{settings.DB_HOST}:{settings.DB_PORT}")
    client = pydgraph.DgraphClient(client_stub)
    app["db"] = client
    _LOG.debug("connected to db: localhost:9080")


async def get_drinks(db: pydgraph.DgraphClient) -> None:
    txn = db.txn()
    return
