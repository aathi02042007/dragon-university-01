from pydantic import BaseModel


class MarkResponse(BaseModel):

    id: int

    student_id: str

    subject_code: str

    total: int

    class Config:

        from_attributes = True
        