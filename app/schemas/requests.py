from pydantic import BaseModel

class RequestSchema(BaseModel):
    request_type: str
    target_id: int
    old_data: dict
    new_data: dict

class RequestStatusSchema(BaseModel):
    status: str