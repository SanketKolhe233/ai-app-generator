from pydantic import BaseModel
from typing import Dict, List


class IntentSchema(BaseModel):

    app_type: str
    features: List[str]
    roles: List[str]


class ArchitectureSchema(BaseModel):

    entities: List[dict]
    pages: List[dict]
    api_modules: List[dict]
    permissions: Dict


class GeneratedSchema(BaseModel):

    database_schema: Dict
    api_schema: Dict
    ui_schema: Dict
    auth_schema: Dict
