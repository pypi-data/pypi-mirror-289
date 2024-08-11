from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from oneflowpy.models.core import Link, ApiResponse


class User(BaseModel):
    links: Dict[str, Link] = Field(None, alias="_links")
    active: bool
    email: str
    id: int
    is_admin: bool
    name: str
    phone_number: str
    state: str
    title: str

    READ_FIELDS: List[str] = ["*"]
    CREATE_FIELDS: List[str] = []
    UPDATE_FIELDS: List[str] = []


class UsersResponse(ApiResponse[User]):
    pass
