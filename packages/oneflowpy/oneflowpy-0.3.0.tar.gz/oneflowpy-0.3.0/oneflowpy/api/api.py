import os
from typing import Any, Optional

from oneflowpy.contacts.api import OneflowContacts
from oneflowpy.contracts.api import OneflowContracts
from oneflowpy.data_fields.api import OneflowDataFields
from oneflowpy.folders.api import OneflowFolder
from oneflowpy.logs.api import OneflowLogs
from oneflowpy.template_types.api import OneflowTemplateTypes
from oneflowpy.templates.api import OneflowTemplates
from oneflowpy.users.api import OneflowUsers
from oneflowpy.workspaces.api import OneflowWorkspaces
from .client import OneflowClient

from oneflowpy.tags.api import OneflowTags

# i need to create context manager for the api class


class OneflowAPI:
    """
    Main class to interact with the Oneflow API, providing access to various
    resources like contacts, contracts and more through a unified interface.
    It attempts to retrieve the access token from an environment variable;
    if not available, the token must be passed explicitly.
    """

    def _raise_value_error(self, env_var_name):
        raise ValueError(
            f"A value must be provided or set in the environment variable '{env_var_name}'."
        )

    def _initialize_client(self):
        if not self.client:
            self.client = OneflowClient()
            self.users = OneflowUsers(self.client, self.workspace_id)
            self.tags = OneflowTags(self.client, self.workspace_id)
            self.workspaces = OneflowWorkspaces(self.client, self.workspace_id)
            self.folders = OneflowFolder(self.client, self.workspace_id)
            self.contacts = OneflowContacts(self.client, self.workspace_id)
            self.templates = OneflowTemplates(self.client, self.workspace_id)
            self.template_types = OneflowTemplateTypes(self.client, self.workspace_id)
            self.data_fields = OneflowDataFields(self.client, self.workspace_id)
            self.contracts = OneflowContracts(self.client, self.workspace_id)
            self.logs = OneflowLogs(self.client, self.workspace_id)

    def __enter__(self):
        self._initialize_client()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self.client.session:
            self.client.session.close()
            self.client.session = None
            self.client = None

    def __init__(
        self,
        workspace_id: Optional[str] = None,
    ) -> None:
        """
        Initializes the OneflowAPI with the necessary authentication token and company slug.
        Attempts to use the access token from the environment variable API_KEY
        if not explicitly passed.

        Parameters:
            workspace_id (Optional[str]): The workspace to perform operations for.
            api_key (Optional[str]): The API_KEY to authenticate against the Oneflow API.
            user_email (Optional[str]): The email of the user to authenticate as.
                                          If api_key or user_email not provided, attempts to fetch from environment.
        """
        self.workspace_id = (
            workspace_id
            or int(os.environ.get("HOME_WORKSPACE"))
            or self._raise_value_error("HOME_WORKSPACE")
        )

        self.client = None
        self._initialize_client()

    def use_custom_resource(self, resource_class: Any, *args, **kwargs) -> Any:
        """
        Allows for the dynamic use of custom resources that follow the OneflowCRUD structure,
        enabling the extension of the API without modifying the core OneflowAPI class.

        Parameters:
            resource_class (Any): The class of the custom resource to be instantiated.
            *args: Positional arguments to pass to the resource class constructor.
            **kwargs: Keyword arguments to pass to the resource class constructor.

        Returns:
            An instance of the specified resource class, initialized with the provided arguments.
        """
        return resource_class(self.client, self.workspace_id, *args, **kwargs)
