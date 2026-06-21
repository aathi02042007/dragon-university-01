from datetime import date

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):

    name: str

    email: EmailStr


class UserCreate(UserBase):

    admission_no: str | None = None

    student_id: str | None = None

    dept: str | None = None

    course: str | None = None

    dob: date | None = None

    password: str

    role_id: int


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class UserResponse(UserBase):

    id: int

    role_id: int

    class Config:
        from_attributes = True