from pydantic import (
    BaseModel,

    EmailStr
)


class AdmissionResponse(
    BaseModel
):

    id: int

    student_name: str

    email: EmailStr

    status: str

    class Config:

        from_attributes = True
        