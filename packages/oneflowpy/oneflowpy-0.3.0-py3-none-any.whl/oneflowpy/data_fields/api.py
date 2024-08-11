from typing import Any, Dict, Iterator, List, Optional, TypeVar
from oneflowpy.api.client import OneflowClient
from oneflowpy.api.crud import (
    OneflowCRUD,
    ListMixin,
    ReadMixin,
    CreateMixin,
    UpdateMixin,
    DestroyMixin,
)
from .model import DataField, DataFieldsResponse
from oneflowpy.template_types.model import TemplateType

G = TypeVar("G", bound="OneflowDataFields")


# we can create list based on parent path template_types
class DataFieldsListMixin(ListMixin[DataField, DataFieldsResponse]):

    def list(
        self,
        **kwargs,
    ) -> List[DataField]:
        endpoint = f"helpers/template_types/{self.template_type_id}/data_fields"
        # endpoint = f"{self._resource_path}/{self.template_type_id}"
        response = self.client.get(endpoint=endpoint, **kwargs)
        return [DataField.model_validate(i) for i in response["data_fields"]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._current_list: List[DataField] = []
        self._current_index: int = 0

    def __iter__(self) -> Iterator[DataField]:
        # Reset the index and populate the list with data from the list method
        self._current_index = 0
        self._current_list = self.list()  # Fetches all data fields at once
        return self

    def __next__(self) -> DataField:
        if self._current_index >= len(self._current_list):
            raise StopIteration

        # Fetch the current item
        result = self._current_list[self._current_index]
        self._current_index += 1
        return result


class OneflowDataFields(
    OneflowCRUD[DataField, DataFieldsResponse],
    DataFieldsListMixin,
    UpdateMixin[DataField],
    DestroyMixin[DataField],
):
    _resource_path = "template_types"
    _subresource_path = "data_fields"
    _template_type_id: int | str | None = None
    _datamodel = DataField
    _list_response = DataFieldsResponse
    _uses_workspace = False
    root_resource = TemplateType

    @property
    def resource_path(self):
        return f"{self._resource_path}/{self.template_type_id}/{self._subresource_path}"

    def set_template_type(
        self,
        template_type_id: str = None,
    ) -> G:
        new_instance = self.__class__(
            client=self.client, workspace_id=self.workspace_id
        )
        new_instance.template_type_id = template_type_id
        return new_instance

    def update(self, data: List[Dict[str, str | None]]) -> DataField:

        endpoint = f"{self.resource_path}"
        response = self.client.put(endpoint, data=data)

        return [DataField.model_validate(i) for i in response["data_fields"]]

    def delete(self, object_id: str) -> None:  # type: ignore
        raise NotImplementedError(
            "Delete is implemented yet because of bad api solution"
        )
