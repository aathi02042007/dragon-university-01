from pydantic import BaseModel, Field
from app.core import current_user

class MarksSchema(BaseModel):
    student_id:str
    subject_code:str
    internal_marks: int = Field(ge=0, le=50)
    external_marks: int = Field(ge=0, le=100)
    
    

