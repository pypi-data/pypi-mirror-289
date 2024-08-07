from typing import Any, Dict, List

from oneflowpy.api.client import OneflowClient
from .crud import OneflowCRUD
from oneflowpy.models import TemplateType, TemplateTypesResponse


class OneflowTemplateTypes(OneflowCRUD):
    _resource_path = "template_types"
    _datamodel = TemplateType
    _list_response = TemplateTypesResponse
    _uses_workspace = False
    allowed_methods = ["read", "list", "create"]
