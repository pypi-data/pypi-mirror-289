from oneflowpy.api.crud import OneflowCRUD, ListMixin, ReadMixin
from .model import LogsResponse, LogEntry


class OneflowLogs(
    OneflowCRUD[LogEntry, LogsResponse], ListMixin[LogEntry, LogsResponse]
):
    _resource_path = "logs"
    _datamodel = LogEntry
    _list_response = LogsResponse
    _uses_workspace = False
