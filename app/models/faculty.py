from sqlalchemy import Column,Integer,String,ForeignKey

from app.database.base import Base


class Faculty(Base):

    __tablename__ = "faculty"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    staff_code = Column(
        String(20),
        unique=True,
        nullable=False
    )

    name = Column(
        String(100),
        nullable=False
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    dept_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    qualification = Column(
        String(200)
    )

    experience = Column(
        Integer
    )

    contact_email = Column(
        String(100)
    )