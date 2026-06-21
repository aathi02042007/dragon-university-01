from pydantic import BaseModel


class StudentResponse(
    BaseModel
):

    id: int

    admission_no: str

    student_id: str

    name: str

    class Config:

        from_attributes = True