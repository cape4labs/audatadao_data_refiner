from pydantic import BaseModel, Field


class OffChainSchema(BaseModel):
    name: str
    version: str
    description: str
    dialect: str
    schema: str
