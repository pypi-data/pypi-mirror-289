from oneflowpy.api.crud import (
    OneflowCRUD,
    ListMixin,
    ReadMixin,
)
from .model import WorkspacesResponse, Workspace


class OneflowWorkspaces(
    OneflowCRUD[Workspace, WorkspacesResponse],
    ListMixin[Workspace, WorkspacesResponse],
    ReadMixin[Workspace],
):

    _resource_path = "workspaces"
    _datamodel = Workspace
    _list_response = WorkspacesResponse
    _uses_workspace = False
