from pydantic import BaseModel, Field, HttpUrl, model_validator
from typing import Any, Dict, Optional, List, TypeVar, Generic


class Link(BaseModel):
    href: Optional[HttpUrl] = None


class PaginationLinks(BaseModel):
    next: Optional[Link] = None
    previous: Optional[Link] = None
    self: Link


T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    links: PaginationLinks = Field(..., alias="_links")
    count: int
    data: List[T]


class OneflowModel(BaseModel):
    READ_FIELDS: List[str] = []
    CREATE_FIELDS: List[str] = []
    UPDATE_FIELDS: List[str] = []

    operation: str = Field(default="default")

    @classmethod
    def get_fields(cls, operation_fields: str) -> List[str]:
        return getattr(cls, operation_fields, [])

    @model_validator(mode="before")
    @classmethod
    def validate_fields(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        operation = values.get("operation", "default")
        if operation in {"create", "update", "read"}:
            fields = cls.get_fields(f"{operation.upper()}_FIELDS")
            if fields == ["*"]:
                fields = list(cls.__annotations__.keys())
            missing_fields = [field for field in fields if values.get(field) is None]
            if missing_fields:
                raise ValueError(
                    f"Missing fields for {operation} operation: {', '.join(missing_fields)}"
                )
        return values

    class ConfigDict:
        extra = "forbid"
