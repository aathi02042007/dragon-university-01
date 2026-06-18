from pydantic import BaseModel


class RequestResponse(
    BaseModel
):

    id: int

    request_type: str

    status: str

    class Config:

        from_attributes = True