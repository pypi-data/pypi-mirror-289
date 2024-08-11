from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Iterator, List, Optional, Union, Type, TypeVar

from pydantic import BaseModel
from .client import OneflowClient
from oneflowpy.models.core import ApiResponse

T = TypeVar("T", bound=BaseModel)
R = TypeVar("R", bound=ApiResponse)


class OneflowCRUD(ABC, Generic[T, R]):
    """
    Abstract base class for implementing LCRUD operations against the Oneflow API.
    """

    allowed_methods: List[str] = ["*"]
    _resource_path: str
    _datamodel: Type[T]
    _response_model: Type[R]
    _uses_workspace: bool = True

    def __init__(
        self, client: OneflowClient, workspace_id: Optional[str] = None
    ) -> None:
        self.client = client
        self.workspace_id = workspace_id
        if self._uses_workspace and not workspace_id:
            raise ValueError("Workspace ID must be provided for this resource")

    def method_allowed(self, method: str) -> bool:
        """
        Checks if the given LCRUD method is allowed for the current class instance.
            method (str): The LCRUD method to check.
        Returns:
            bool: True if the method is allowed, False otherwise.
        """
        return method in self.allowed_methods or "*" in self.allowed_methods

    def validate_method_allowed(self, method: str) -> None:
        """
        Raises a NotImplementedError if the given LCRUD method is not allowed for the current class instance.
        """
        if not self.method_allowed(method):
            raise NotImplementedError(
                f"{method} method not allowed for {self.__class__.__name__}"
            )

    def model_validator(
        self, data: Union[Dict[str, Any], BaseModel], method_name: str = "read"
    ) -> BaseModel:
        """
        Validates the data against the Pydantic data model. This method handles both dictionary inputs
        and model instances. If a dictionary is provided, it validates and converts it to the model.
        If a model instance is provided, it re-validates it (useful if the model was modified).

        Parameters:
            data (Union[Dict[str, Any], BaseModel]): The data to validate, either as a dictionary or a model instance.

        Returns:
            BaseModel: The validated and possibly transformed Pydantic model instance.
        """
        if isinstance(data, self.datamodel):
            data = data.model_dump()

        if isinstance(data, Dict):
            # Convert dictionary to Pydantic model instance
            data["operation"] = method_name
            return self.datamodel(**data)
        else:
            raise TypeError(
                "Input must be a dictionary or an instance of the defined data model"
            )

    @property
    def resource_path(self) -> str:
        """
        Defines the specific path of the resource relative to the company slug.
        Must be implemented by subclasses to return the resource-specific part of the URL.
        """
        assert (
            self._resource_path is not None
        ), "Resource path must be defined in subclass"
        return self._resource_path

    @property
    def datamodel(self) -> BaseModel:
        """
        Returns the Pydantic data model for the resource.
        Must be implemented by subclasses to return the appropriate Pydantic model.
        """
        assert self._datamodel is not None, "Data model must be defined in subclass"
        return self._datamodel


class ListMixin(Generic[T, R]):

    @staticmethod
    def build_filter_params(filters: Dict[str, Any]) -> Dict[str, str]:
        filter_params = {}
        for key, value in filters.items():
            if isinstance(value, list):
                value = ",".join(map(str, value))
            filter_params[f"filter[{key}]"] = value
        return filter_params

    @property
    def list_response(self) -> ApiResponse:
        """
        Returns the response object for the list_response method.
        Must be implemented by subclasses to return the appropriate response object.
        """
        assert (
            self._list_response is not None
        ), "List response object must be defined in subclass"
        return self._list_response

    def list(
        self,
        offset=0,
        limit=100,
        sort=None,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> R:
        """
        Retrieve a list of items.
        Args:
            offset (int, optional): The offset for pagination. Defaults to 0.
            limit (int, optional): The maximum number of items to retrieve. Defaults to 100.
            sort (str, optional): The sorting criteria. Defaults to None.
            filters (Dict[str, Any], optional): The filters to apply. Defaults to None.
            **kwargs: Additional keyword arguments.
        Returns:
            ApiResponse: An API response object of the model type.
        Raises:
            SomeException: If an error occurs.
        """

        endpoint = f"{self.resource_path}"
        params = {"offset": offset, "limit": limit}

        if sort:
            params["sort"] = sort

        if filters:
            params.update(self.build_filter_params(filters))

        if self._uses_workspace:
            params["workspace_id"] = self.workspace_id
        kwargs["params"] = {**kwargs.get("params", {}), **params}

        response = self.client.get(endpoint=endpoint, **kwargs)
        return self.list_response.model_validate(response)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._current_list: List[T] = []
        self._current_index: int = 0
        self._next_link: Optional[str] = None

    def __iter__(self) -> Iterator[T]:
        self._current_index = 0
        initial_response = self.list(offset=0, limit=20)
        self._current_list = [
            self.model_validator(item) for item in initial_response.data
        ]
        self._next_link = initial_response.links.next.href
        return self

    def __next__(self) -> T:
        if self._current_index >= len(self._current_list):
            if not self._next_link:
                raise StopIteration
            response = self.client.get(self._next_link)
            response_data = response.json()
            api_response = self.list_response.model_validate(response_data)
            self._current_list = [
                self.model_validator(item) for item in api_response.data
            ]
            self._next_link = api_response.links.next.href
            self._current_index = 0

        if not self._current_list:
            raise StopIteration

        result = self._current_list[self._current_index]
        self._current_index += 1
        return result


class ReadMixin(Generic[T]):
    def read(self, object_id: str) -> T:
        """
        Retrieves a single object by its ID.

        Parameters:
            object_id (str): The ID of the object to retrieve.

        Returns:
            OneflowModel: The created object model.
        """

        self.validate_method_allowed("read")

        endpoint = f"{self.resource_path}/{object_id}"
        response = self.client.get(endpoint=endpoint)
        return self.model_validator(response)


class CreateMixin(Generic[T]):
    def create(self, data: Dict[str, Any], endpoint_postfix: str | None = None) -> T:
        """
        Creates a new object with the provided data.
        Must be implemented by subclasses due to potentially varying data structures.

        Parameters:
            data (Dict[str, Any]): Data for creating the new object.

        Returns:
            OneflowModel: The created object model.
        """

        endpoint = (
            f"{self.resource_path}/{endpoint_postfix}"
            if endpoint_postfix
            else self.resource_path
        )

        # self.model_validator(data, "create")

        response = self.client.post(endpoint, data=data)

        return self.model_validator(response)


class UpdateMixin(Generic[T]):
    def update(self, object_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing object identified by its ID with the given data.
        Must be implemented by subclasses due to potentially varying data structures.

        Parameters:
            object_id (str): The ID of the object to update.
            data (Dict[str, Any]): New data for updating the object.

        Returns:
            Dict[str, Any]: The updated object data.
        """

        endpoint = f"{self.resource_path}/{object_id}"
        response = self.client.put(endpoint, data=data)
        return self.model_validator(response)


class DestroyMixin(Generic[T]):
    def destroy(self, object_id: str) -> None:
        """
        Deletes an object identified by its ID.

        Parameters:
            object_id (str): The ID of the object to delete.
        """

        endpoint = f"{self.resource_path}/{object_id}"
        self.client.delete(endpoint)
