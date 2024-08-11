from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List, Dict, Union, Any
from datetime import datetime
from oneflowpy.models.core import ApiResponse


class LogEntry(BaseModel):
    api_version: int
    integration_key: str
    request_body: Optional[Union[str, Dict[str, Any]]] = None
    request_duration: int
    request_endpoint: str
    request_headers: Optional[Dict[str, str]] = None
    request_id: str
    request_method: str
    request_path: str
    request_time: datetime
    response_body: Optional[Union[str, Dict[str, Any]]] = None
    response_code: int


class LogsResponse(ApiResponse[LogEntry]):
    pass
