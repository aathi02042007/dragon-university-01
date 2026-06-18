from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.database.base import Base


class Subject(Base):

    __tablename__ = "subjects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    subject_code = Column(
        String(20),
        unique=True,
        nullable=False
    )

    subject_name = Column(
        String(100),
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.id")
    )

    semester = Column(
        Integer
    )