from pydantic import BaseModel

class RequestSchema(BaseModel):
    request_type: str
    requested_by: int
    target_id: int
    old_data: dict
    new_data: dict
    status: str = "pending"
    approved_by: int | None = None