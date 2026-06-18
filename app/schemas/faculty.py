from pydantic import BaseModel, EmailStr


class FacultyResponse(
    BaseModel
):

    id: int

    staff_code: str

    name: str

    qualification: str

    experience: int

    contact_email: EmailStr

    class Config:

        from_attributes = True