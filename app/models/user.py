from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    admission_no = Column(
        String(30),
        unique=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    student_id = Column(
        String(30),
        unique=True
    )

    dept = Column(
        String(100)
    )

    course = Column(
        String(100)
    )

    dob = Column(
        Date
    )

    email = Column(
        String(100),
        unique=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    joined_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )