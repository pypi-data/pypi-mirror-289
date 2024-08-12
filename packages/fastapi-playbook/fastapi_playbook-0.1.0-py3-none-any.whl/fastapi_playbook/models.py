from uuid import uuid4

from pydantic import BaseModel


class FlowStep(BaseModel):
    id: str
    name: str
    description: str
    operationId: str
    url: str
    method: str
    model: dict | None = None
    expectedResponse: dict | None = None
    expectedResponseCode: str | None = None


class Flow(BaseModel):
    id: str
    name: str
    description: str = ""
    steps: list[FlowStep] = []


class FlowListItem(BaseModel):
    id: str
    name: str


class FlowList(BaseModel):
    flows: list[FlowListItem]


class CreateFlowDTO(BaseModel):
    id: str
    name: str


class UpdateFlowDTO(BaseModel):
    id: str
    name: str
    description: str
    steps: list[FlowStep]
