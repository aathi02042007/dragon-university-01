from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.database.base import Base


class Mark(Base):

    __tablename__ = "marks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        String(30),
        nullable=False
    )

    subject_code = Column(
        String(20),
        nullable=False
    )

    internal_mark = Column(
        Integer,
        default=0
    )

    external_mark = Column(
        Integer,
        default=0
    )

    total = Column(
        Integer,
        default=0
    )

    uploaded_by = Column(
        Integer,
        ForeignKey("faculty.id")
    )