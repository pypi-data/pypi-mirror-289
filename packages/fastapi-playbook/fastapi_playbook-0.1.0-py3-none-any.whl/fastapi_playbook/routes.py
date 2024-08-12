import os
from http import HTTPStatus

from fastapi import APIRouter, FastAPI
from starlette.responses import HTMLResponse

from fastapi_playbook import config
from fastapi_playbook.models import CreateFlowDTO, UpdateFlowDTO
from fastapi_playbook.repository import FastAPIFlowRepository


class FastAPIFlowRouter:
    def __init__(self, file, prefix: str = "") -> None:
        self.prefix = prefix
        self.router = APIRouter()
        self.repository = FastAPIFlowRepository(file)

    def setup(self):
        @self.router.get(
            "/flow/api/info", status_code=HTTPStatus.OK, include_in_schema=False
        )
        async def flow_api_info():
            """
            Library information and settings

            Version,
            API Prefix
            """

            return {"version": "0.0.1", "api_prefix": self.prefix}

        @self.router.get(
            "/flow/api/", status_code=HTTPStatus.OK, include_in_schema=False
        )
        async def read_flow():
            return self.repository.fetch_flow_list()

        @self.router.get(
            "/flow/api/{flow_id}", status_code=HTTPStatus.OK, include_in_schema=False
        )
        async def read_flow(flow_id: str):
            return self.repository.fetch_flow(flow_id)

        @self.router.put(
            "/flow/api/", status_code=HTTPStatus.OK, include_in_schema=False
        )
        async def read_flow(dto: UpdateFlowDTO):
            return self.repository.update_flow(dto)

        @self.router.post(
            "/flow/api/", status_code=HTTPStatus.OK, include_in_schema=False
        )
        async def create_flow(dto: CreateFlowDTO):
            return self.repository.create(dto)

        @self.router.delete(
            "/flow/api/{flow_id}", status_code=HTTPStatus.OK, include_in_schema=False
        )
        async def create_flow(flow_id: str):
            return self.repository.delete_flow(flow_id)

        @self.router.get(
            "/flow/bundle", status_code=HTTPStatus.OK, include_in_schema=False
        )
        def bundle():
            current_file_path = os.path.realpath(__file__)
            current_dir = os.path.dirname(current_file_path)
            with open(current_dir + "/bundle.js", "r") as f:
                js_content = f.read()
            return HTMLResponse(content=js_content, media_type="application/javascript")

        @self.router.get(
            "/flow",
            response_class=HTMLResponse,
            status_code=HTTPStatus.OK,
            include_in_schema=False,
        )
        @self.router.get(
            "/flow/{id}",
            response_class=HTMLResponse,
            status_code=HTTPStatus.OK,
            include_in_schema=False,
        )
        async def render():
            bundle_path = (
                "/flow/bundle"
                if config.config.env == "production"
                else "http://127.0.0.1:3001/bundle.js"
            )

            return HTMLResponse(
                content=f"""
                    <!DOCTYPE html>
                    <html lang="en">
    
                    <head>
                      <meta charset="UTF-8" />
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <title>Fast API Flow</title>
                    </head>
                    <body>
                      <div id="root"></div>
                      <script src="{bundle_path}"></script>
                    </body>
                    </html>
                """,
                status_code=200,
            )

        return self.router
