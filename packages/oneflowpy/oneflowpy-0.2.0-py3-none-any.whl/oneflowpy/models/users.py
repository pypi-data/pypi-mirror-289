from typing import Optional, Dict
from pydantic import BaseModel
from .core import Link, ApiResponse


class User(BaseModel):
    _links: Optional[Dict[str, Link]]
    active: bool
    email: str
    id: int
    is_admin: bool
    name: str
    phone_number: str
    state: str
    title: str


class UsersResponse(ApiResponse[User]):
    pass
