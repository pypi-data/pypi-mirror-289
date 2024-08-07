from typing import List, Optional, Dict
from pydantic import BaseModel
from datetime import datetime
from .core import Link, PaginationLinks, ApiResponse


class DataField(BaseModel):
    name: str
    custom_id: str
    template_type_id: int | None = None
    _links: Optional[Dict[str, Link]]
    active: bool | None = None
    description: str | None = None
    id: int | None = None
    placeholder: str | None = None
    source: str | None = None
    value: str | None = None


class DataFieldsResponse(ApiResponse[DataField]):
    pass
