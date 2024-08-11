from typing import List
from datetime import datetime
from oneflowpy.models.core import ApiResponse, OneflowModel


class Tag(OneflowModel):
    created_time: datetime
    id: int
    is_global: bool
    name: str
    shared_workspaces: List[str]
    system: bool
    updated_time: datetime

    READ_FIELDS: List[str] = ["*"]
    CREATE_FIELDS: List[str] = ["name"]
    UPDATE_FIELDS: List[str] = ["name"]


class TagsResponse(ApiResponse[Tag]):
    pass
