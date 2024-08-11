from typing import Any, Dict, List
from oneflowpy.api.crud import (
    OneflowCRUD,
    ListMixin,
    ReadMixin,
    CreateMixin,
    UpdateMixin,
    DestroyMixin,
)
from .model import Contract, ContractsResponse


class OneflowContracts(
    OneflowCRUD[Contract, ContractsResponse],
    ListMixin[Contract, ContractsResponse],
    ReadMixin[Contract],
    CreateMixin[Contract],
    UpdateMixin[Contract],
    DestroyMixin[Contract],
):

    _resource_path = "contracts"
    _datamodel = Contract
    _list_response = ContractsResponse
    _uses_workspace = False

    def create(self, data: Dict[str, Any]) -> Contract:
        return super().create(data, endpoint_postfix="create")

    def move(self, object_id: str, folder_id) -> Contract:
        data = {"folder_id": folder_id}
        data["workspace_id"] = self.workspace_id
        response = self.client.post(
            f"{self._resource_path}/{object_id}/move", data=data
        )
        return self.model_validator(response)

    def publish(self, object_id: str, subject: str, message: str) -> Contract:
        data = {"subject": subject, "message": message}
        response = self.client.post(
            f"{self._resource_path}/{object_id}/publish", data=data
        )
        return self.model_validator(response)

    def decline(self, object_id: str) -> Contract:
        response = self.client.post(f"{self._resource_path}/{object_id}/decline")
        return self.model_validator(response)

    def copy(
        self,
        object_id: str,
        folder_id: str | int | None = None,
        name: str | None = None,
    ) -> Contract:
        data = {"workspace_id": self.workspace_id}
        if folder_id:
            data["folder_id"] = folder_id
        if name:
            data["name"] = name

        response = self.client.post(
            f"{self._resource_path}/{object_id}/copy", data=data
        )
        return self.model_validator(response)

    def mark_as_signed(self, object_id: str) -> Contract:
        response = self.client.post(f"{self._resource_path}/{object_id}/mark_as_signed")
        raise NotImplementedError("mark_as_signed not implemented yet")
