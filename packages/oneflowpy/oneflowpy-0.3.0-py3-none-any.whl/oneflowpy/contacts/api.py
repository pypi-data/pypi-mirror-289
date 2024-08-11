from typing import Any, Dict, List
from oneflowpy.api.crud import (
    OneflowCRUD,
    ListMixin,
    ReadMixin,
    CreateMixin,
    UpdateMixin,
    DestroyMixin,
)
from .model import Contact, ContactsResponse


class OneflowContacts(
    OneflowCRUD[Contact, ContactsResponse],
    ListMixin[Contact, ContactsResponse],
    ReadMixin[Contact],
    CreateMixin[Contact],
    UpdateMixin[Contact],
    DestroyMixin[Contact],
):

    _resource_path = "contacts"
    _datamodel = Contact
    _list_response = ContactsResponse
