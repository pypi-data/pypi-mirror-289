from typing import Any, Dict, List

from oneflowpy.api.client import OneflowClient
from oneflowpy.api.crud import OneflowCRUD, ListMixin, CreateMixin, ReadMixin
from .model import TemplateType, TemplateTypesResponse


class OneflowTemplateTypes(
    OneflowCRUD[TemplateType, TemplateTypesResponse],
    ListMixin[TemplateType, TemplateTypesResponse],
    CreateMixin[TemplateType],
    ReadMixin[TemplateType],
):
    _resource_path = "template_types"
    _datamodel = TemplateType
    _list_response = TemplateTypesResponse
    _uses_workspace = False
