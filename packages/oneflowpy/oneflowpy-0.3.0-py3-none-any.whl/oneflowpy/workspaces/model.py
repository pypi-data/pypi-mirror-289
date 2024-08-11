from pydantic import BaseModel, Field
from typing import Any, List, Dict, Optional
from datetime import datetime
from ..models.core import Link, ApiResponse, Permissions


class Workspace(BaseModel):
    _integration_permissions: List[Dict[str, Any]] = []
    _links: Dict[str, Link] = {}
    id: int
    name: str
    permissions: dict = Field(..., alias="_permissions")
    company_name: Optional[str] = None
    country_code: Optional[str] = None
    created_time: Optional[datetime] = None
    date_format: Optional[str] = None
    description: Optional[str] = None
    registration_number: Optional[str] = None
    type: Optional[str] = None
    updated_time: Optional[datetime] = None

    READ_FIELDS: List[str] = ["*"]
    CREATE_FIELDS: List[str] = []
    UPDATE_FIELDS: List[str] = []


class WorkspacesResponse(ApiResponse[Workspace]):
    pass
