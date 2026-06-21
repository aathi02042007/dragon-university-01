from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from app.database.base import Base


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        String(30),
        nullable=False
    )

    attendance_date = Column(
        Date,
        nullable=False
    )

    class_name = Column(
        String(20)
    )

    batch_year = Column(
        Integer
    )

    status = Column(
        String(20)
    )

    marked_by = Column(
        Integer,
        ForeignKey("faculty.id")
    )