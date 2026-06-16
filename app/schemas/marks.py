from pydantic import BaseModel

class MarksSchema(BaseModel):
    student_id:str
    subject_code:str
    internal_marks:int
    external_marks:int
    total:int
    uploaded_by:int

