from typing import Any, List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime
from .core import Link, PaginationLinks, ApiResponse, Permissions
from .folders import Folder


class SigningPeriodExpiration(BaseModel):
    expire_days_after_publish: int
    type: str


class PrivateDetails(BaseModel):
    date_format: str
    folder: Folder | None = None
    name: str
    signing_period_expiration: SigningPeriodExpiration
    value: str | None = None
    workspace_id: int


class PrivateOwnerside(BaseModel):
    created_time: datetime
    template_id: Optional[int] = None
    template_type_id: Optional[int] = None


class ParticipantPrivateOwnerside(BaseModel):
    created_time: datetime
    custom_id: str | None = None
    first_visited_time: Optional[datetime] = None
    last_visited_time: Optional[datetime] = None
    updated_time: datetime
    visits: int


class Participant(BaseModel):
    _permissions: Permissions
    _private_ownerside: ParticipantPrivateOwnerside
    delivery_channel: str
    delivery_status: str
    draft_approver: bool
    email: str
    id: int
    identification_number: str
    my_participant: bool
    name: str
    organizer: bool
    phone_number: str
    sign_method: str
    sign_state: str
    sign_state_updated_time: Optional[datetime] = None
    signatory: bool
    title: str
    two_step_authentication_method: str


class PartyPrivateOwnerside(BaseModel):
    created_time: datetime
    custom_id: str | None = None
    updated_time: datetime


class Party(BaseModel):
    _private_ownerside: PartyPrivateOwnerside
    country_code: str
    id: int
    identification_number: str
    my_party: bool
    name: str
    participants: List[Participant]
    type: str


class ContractPermissions(BaseModel):
    contract_delete: bool
    contract_download_pdf: bool
    contract_send: bool


class Contract(BaseModel):
    integration_permissions: List[str] = Field(None, alias="_integration_permissions")
    links: Dict[str, Link] = Field(None, alias="_links")
    permissions: Permissions = Field(None, alias="_permissions")
    private: PrivateDetails = Field(None, alias="_private")
    private_ownerside: PrivateOwnerside = Field(None, alias="_private_ownerside")
    draft_approval_workflow: str | None = None
    id: int | None = None
    lifecycle_settings: dict[str, Any] | None = None
    lifecycle_state: str | None = None
    parties: List[Party] = None
    published_time: Optional[datetime] = None
    sign_order: List[int] = None
    signing_period_expiry_time: Optional[datetime] = None
    state: str = None
    state_updated_time: datetime = None
    tags: List[str] = None
    updated_time: datetime = None
    workspace_id: int | None = None
    template_id: int | None = None


class ContractsResponse(ApiResponse[Contract]):
    pass
