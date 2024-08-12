import json

from fastapi_playbook.models import Flow, CreateFlowDTO, UpdateFlowDTO


class FastAPIFlowRepository:
    def __init__(self, file):
        self.file = file

    def read(self) -> list:
        with open(self.file, "r") as f:
            return json.load(f)["flows"]

    def write(self, data: list) -> None:
        with open(self.file, "w") as f:
            json.dump({"flows": data}, f)

    def fetch_flow_list(self) -> list[Flow]:
        return [Flow(**flow) for flow in self.read()]

    def fetch_flow(self, flow_id: str) -> Flow:
        flows = self.read()
        for flow in flows:
            if flow["id"] == flow_id:
                return Flow(**flow)
        else:
            raise ValueError(f"Flow with id {flow_id} not found")

    def update_flow(self, dto: UpdateFlowDTO) -> Flow:
        flows = self.read()
        for flow in flows:
            if flow["id"] == dto.id:
                print(dto.dict())
                flow.update(dto.dict())
                self.write(flows)
                return Flow(**flow)
        else:
            raise ValueError(f"Flow with id {dto.id} not found")

    def create(self, dto: CreateFlowDTO) -> Flow:
        flows = self.read()
        new_flow = dto.dict()
        flows.append(new_flow)
        self.write(flows)
        return Flow(**new_flow)

    def delete_flow(self, flow_id: str) -> Flow:
        flows = self.read()
        for flow in flows:
            if flow["id"] == flow_id:
                flows.remove(flow)
                self.write(flows)
                return Flow(**flow)
        else:
            raise ValueError(f"Flow with id {flow_id} not found")
