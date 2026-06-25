from pydantic import BaseModel
from datetime import date



class Attendancemodel(BaseModel):
    student_id: int
    attendance_date: date
    class_name: str
    batch_year: int
    status: str
    marked_by: int