from pydantic import BaseModel
from typing import Optional


class ProviderModel(BaseModel):
    name: str
    description: Optional[str]
    logo: Optional[str]
    provider_id: int
    req_integration_params: dict


class ModelCreatorModel(BaseModel):
    name: str
    description: Optional[str]
    logo: Optional[str]
    creator_id: int


class AvailableModelModel(BaseModel):
    provider: ProviderModel
    creator: ModelCreatorModel
    model_type: str
    name: str
    model_name: Optional[str]
    model_version: Optional[str]
    is_verified: bool
    cost_input_token: float
    cost_output_token: float

