from oneflowpy.api.crud import OneflowCRUD, ListMixin, ReadMixin

from .model import UsersResponse, User


class OneflowUsers(
    OneflowCRUD[User, UsersResponse], ListMixin[User, UsersResponse], ReadMixin[User]
):
    _resource_path = "users"
    _datamodel = User
    _list_response = UsersResponse
    _uses_workspace = False

    def read(self, object_id: str) -> User:
        users = super().list()
        for i in users.data:
            if i.id == object_id:
                return i
