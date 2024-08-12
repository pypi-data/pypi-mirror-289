import json
import logging
from logging.config import dictConfig

from fastapi import FastAPI
from fastapi_playbook.routes import FastAPIFlowRouter

from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


PLAYBOOK_FILE = ".fastapi_playbook.json"


class FastAPIFlow:
    def __init__(
        self, app: FastAPI, path: str = PLAYBOOK_FILE, prefix: str = ""
    ) -> None:
        # TODO: validate prefix
        self.prefix = prefix
        self.app = app
        self.path = path
        self.__init_flow()
        self.__add_routes()
        dictConfig(LogConfig().dict())
        self.logger = logging.getLogger("mycoolapp")
        self.logger.info(
            "FastAPIFlow initialized %s", f"with path http://127.0.0.1:8000/flow"
        )

    def __init_flow(self) -> None:
        """
        Initialize the flow file
        :return:
        """

        try:
            with open(self.path, "x") as f:
                json.dump({"flows": []}, f)
        except FileExistsError:
            pass

    def __add_routes(self) -> None:
        """
        Add the routes to the FastAPI app
        :return:
        """

        router = FastAPIFlowRouter(self.path, prefix=self.prefix).setup()
        self.app.include_router(router)
