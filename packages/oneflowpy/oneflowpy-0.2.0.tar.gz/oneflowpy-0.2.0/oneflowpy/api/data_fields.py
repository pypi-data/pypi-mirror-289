from typing import Any, Dict, List
from oneflowpy.api.client import OneflowClient
from .crud import OneflowCRUD
from oneflowpy.models import DataField, DataFieldsResponse


class OneflowDataFields(OneflowCRUD):
    _resource_path = None
    _datamodel = DataField
    _list_response = DataFieldsResponse
    _uses_workspace = False
    allowed_methods = ["update", "delete"]

    @property
    def resource_path(self):
        return f"template_types/{self.template_type_id}/data_fields"

    def set_template_type(self, template_type_id: str) -> OneflowCRUD:
        self.template_type_id = template_type_id
        return self

    def update(self, data: List[Dict[str, str | None]]) -> DataField:
        assert self.template_type_id, "template_type_id must be set"

        for i in data["data_fields"]:
            DataField.model_validate(i)

        endpoint = f"{self.resource_path}"
        response = self.client.put(endpoint, data=data)

        return [DataField.model_validate(i) for i in response["data_fields"]]

    def delete(self, object_id: str) -> None:  # type: ignore
        raise NotImplementedError(
            "Delete is implemented yet because of bad api solution"
        )
