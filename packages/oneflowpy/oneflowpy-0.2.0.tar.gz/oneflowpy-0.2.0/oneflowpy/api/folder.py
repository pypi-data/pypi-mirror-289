from .crud import OneflowCRUD
from oneflowpy.models import FoldersResponse, Folder


class OneflowFolder(OneflowCRUD):
    _resource_path = "folders"
    _datamodel = Folder
    _list_response = FoldersResponse
    _uses_workspace = False
    allowed_methods = ["list", "create", "update", "delete"]
