from pydantic import BaseModel, Field


class Permissions(BaseModel):
    contract_delete: bool | None = Field(None, alias="contract:delete")
    contract_download_pdf: bool | None = Field(None, alias="contract:download:pdf")
    contract_send: bool | None = Field(None, alias="contract:send")


class PermissionsMixin(BaseModel):
    permissions: Permissions = Field(..., alias="_permissions")
