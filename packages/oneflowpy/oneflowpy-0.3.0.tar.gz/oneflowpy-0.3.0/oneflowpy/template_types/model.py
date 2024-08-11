from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.core import Link, PaginationLinks, ApiResponse


class TemplateType(BaseModel):
    links: Dict[str, Link] = Field(None, alias="_links")
    created_time: datetime
    description: str
    extension_type: str | None
    id: int
    name: str
    updated_time: datetime

    READ_FIELDS: List[str] = ["*"]
    CREATE_FIELDS: List[str] = ["name"]
    UPDATE_FIELDS: List[str] = []


class TemplateTypesResponse(ApiResponse[TemplateType]):
    pass
