# pyre-strict
import os
from chambordpi.settings.default_settings import *  # pylint: disable=wildcard-import


def import_correct_settings() -> None:
    env = os.environ.get("environment", "DEV")
    if env == "PROD":
        pass
    if env == "QA":
        pass
    else:
        pass


import_correct_settings()
