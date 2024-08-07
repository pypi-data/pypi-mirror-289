from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .core import Link, PaginationLinks, ApiResponse, Permissions


class FolderPermissions(Permissions):
    folder_contract: bool
    folder_delete: bool
    folder_sub_folder_create: bool
    folder_update: bool


class Folder(BaseModel):
    id: Optional[int] = None
    name: str | None = None
    workspace_id: int | None = None

    _permissions: Optional[FolderPermissions] = None
    parent_id: Optional[int] = None
    path: Optional[List[int]] = None


class FoldersResponse(ApiResponse[Folder]):
    pass
