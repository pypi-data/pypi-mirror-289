from oneflowpy.api.crud import (
    OneflowCRUD,
    ListMixin,
    ReadMixin,
    CreateMixin,
    UpdateMixin,
    DestroyMixin,
)
from .model import FoldersResponse, Folder


class OneflowFolder(
    OneflowCRUD[Folder, FoldersResponse],
    ListMixin[Folder, FoldersResponse],
    CreateMixin[Folder],
    UpdateMixin[Folder],
    DestroyMixin[Folder],
    ReadMixin[Folder],
):
    _resource_path = "folders"
    _datamodel = Folder
    _list_response = FoldersResponse
    _uses_workspace = False

    def read(self, object_id: str) -> Folder:
        folders = super().list()
        for i in folders.data:
            if i.id == object_id:
                return i
