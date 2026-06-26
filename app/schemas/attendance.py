from pydantic import BaseModel


class AttendanceResponse(
    BaseModel
):

    id: int

    student_id: str

    status: str

    class Config:

        from_attributes = True
from datetime import date

class AttendanceSchema(BaseModel):
    student_id:int
    attendance_date:date
    class_name:str
    batch_year:int
    status:str
    marked_by:int

    
