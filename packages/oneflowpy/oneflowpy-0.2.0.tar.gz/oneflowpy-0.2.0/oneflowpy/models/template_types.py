from typing import List, Optional, Dict
from pydantic import BaseModel
from datetime import datetime
from .core import Link, PaginationLinks, ApiResponse


class TemplateType(BaseModel):
    _links: Optional[Dict[str, Link]]
    created_time: Optional[datetime] = None
    description: Optional[str] = None
    extension_type: Optional[str] = None
    id: Optional[int] = None
    name: str
    updated_time: Optional[datetime] = None


class TemplateTypesResponse(ApiResponse[TemplateType]):
    pass
