from oneflowpy.api.crud import (
    OneflowCRUD,
    ListMixin,
    ReadMixin,
    CreateMixin,
    UpdateMixin,
    DestroyMixin,
)
from .model import Tag, TagsResponse


class OneflowTags(
    OneflowCRUD[Tag, TagsResponse],
    ListMixin[Tag, TagsResponse],
    ReadMixin[Tag],
    CreateMixin[Tag],
    UpdateMixin[Tag],
    DestroyMixin[Tag],
):
    """
    OneflowTags class to interact with the Tags API.

    This class combines multiple mixins to provide a full suite of CRUD operations,
    specifically designed for the Tags resource. It is tailored to handle listing, reading,
    creating, updating, and deleting tag objects.

    Inherited Classes:
    ------------------
    - OneflowCRUD[Tag, TagsResponse]: Base CRUD operations class with type hints.
    - ListMixin[Tag, TagsResponse]: Provides functionality to list and iterate over tags.
    - ReadMixin[Tag]: Provides functionality to read a single tag.
    - CreateMixin[Tag]: Provides functionality to create a new tag.
    - UpdateMixin[Tag]: Provides functionality to update an existing tag.
    - DeleteMixin[Tag]: Provides functionality to delete a tag.

    Class Attributes:
    -----------------
    - _resource_path (str): The API resource path for tags.
    - _datamodel (Type[Tag]): The Pydantic data model for a tag.
    - _list_response (Type[TagsResponse]): The Pydantic response model for listing tags.
    - _uses_workspace (bool): Indicates whether workspace-specific operations are used.

    Inherited Methods:
    ------------------
    - list(self, offset=0, limit=20, filters: Optional[Dict[str, Any]] = None, **kwargs) -> TagsResponse:
        Lists all tags with optional filtering, pagination, and additional parameters.

    - read(self, tag_id: int) -> Tag:
        Reads and returns a single tag by its ID.

    - create(self, tag_data: Dict[str, Any]) -> Tag:
        Creates a new tag with the provided data.

    - update(self, tag_id: int, tag_data: Dict[str, Any]) -> Tag:
        Updates an existing tag identified by its ID with the provided data.

    - delete(self, tag_id: int) -> None:
        Deletes an existing tag identified by its ID.

    Helper Methods:
    ---------------
    - method_allowed(self, method: str) -> bool:
        Checks if a given method is allowed.

    - validate_method_allowed(self, method: str) -> None:
        Validates whether a method is allowed and raises an error if not.

    - model_validator(self, data: Dict[str, Any]) -> Tag:
        Validates the provided data against the Pydantic data model.

    Example Usage:
    --------------
    ```python

    # Instantiate the OneflowTags class
    with OneflowAPI() as api:
        # List all tags
        tags = api.tags.list()
        for tag in tags:
            print(tag)

        # Read a single tag
        tag = api.tags.read(tag_id=123)
        print(tag)

        # Create a new tag
        new_tag = api.tags.create(tag_data={"name": "New Tag"})
        print(new_tag)

        # Update an existing tag
        updated_tag = api.tags.update(tag_id=123, tag_data={"name": "Updated Tag"})
        print(updated_tag)

        # Delete a tag
        api.tags.delete(tag_id=123)

    ```
    """

    _resource_path = "tags"
    _datamodel = Tag
    _list_response = TagsResponse
    _uses_workspace = False
