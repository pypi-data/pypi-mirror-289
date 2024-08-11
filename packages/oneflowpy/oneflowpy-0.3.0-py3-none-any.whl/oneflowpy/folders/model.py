from typing import List
from pydantic import Field
from oneflowpy.models.core import ApiResponse, OneflowModel


class Folder(OneflowModel):
    id: int
    name: str
    workspace_id: int
    permissions: dict = Field(..., alias="_permissions")
    parent_id: int | None
    path: List[int]

    READ_FIELDS: List[str] = ["*"]
    CREATE_FIELDS: List[str] = ["name", "workspace_id"]
    UPDATE_FIELDS: List[str] = ["name"]


class FoldersResponse(ApiResponse[Folder]):
    pass
