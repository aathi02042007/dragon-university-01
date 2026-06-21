from pydantic import BaseModel


class AttendanceResponse(
    BaseModel
):

    id: int

    student_id: str

    status: str

    class Config:

        from_attributes = True