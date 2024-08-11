from typing import List, Optional
from datetime import datetime
from oneflowpy.models.core import ApiResponse, OneflowModel


class Contact(OneflowModel):
    id: int
    name: str
    email: str
    workspace_id: int

    company_name: str | None
    company_registration_number: str | None
    country_code: str | None
    created_time: datetime
    date_of_birth: str | None
    notes: str | None
    phone_number: str | None
    title: str | None
    updated_time: datetime

    READ_FIELDS: List[str] = ["*"]
    CREATE_FIELDS: List[str] = ["email", "name", "workspace_id"]
    UPDATE_FIELDS: List[str] = []


class ContactsResponse(ApiResponse[Contact]):
    pass
