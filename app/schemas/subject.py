from pydantic import BaseModel


class SubjectResponse(
    BaseModel
):

    id: int

    subject_code: str

    subject_name: str

    semester: int

    class Config:

        from_attributes = True