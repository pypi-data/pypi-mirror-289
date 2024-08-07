from typing import Any, Dict, List
from .crud import OneflowCRUD
from oneflowpy.models import Contract, ContractsResponse


class OneflowContracts(OneflowCRUD):

    _resource_path = "contracts"
    _datamodel = Contract
    _list_response = ContractsResponse
    _uses_workspace = False
    allowed_methods = ["list", "read", "create"]

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return super().create(data, endpoint_postfix="create")
