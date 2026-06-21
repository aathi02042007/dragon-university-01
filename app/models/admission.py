from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DECIMAL,
    ForeignKey,
    Enum
)

from app.database.base import Base


class AdmissionRequest(Base):

    __tablename__ = "admission_requests"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_name = Column(
        String(100)
    )

    email = Column(
        String(100)
    )

    phone = Column(
        String(15)
    )

    dob = Column(
        Date
    )

    gender = Column(
        String(20)
    )

    hsc_group = Column(
        String(50)
    )

    hsc_percentage = Column(
        DECIMAL(5,2)
    )

    school_name = Column(
        String(100)
    )

    passing_year = Column(
        Integer
    )

    department_id = Column(
        Integer,
        ForeignKey(
            "departments.id"
        )
    )

    course = Column(
        String(100)
    )

    status = Column(
        Enum(
            "pending",
            "approved",
            "rejected"
        )
    )