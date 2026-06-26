from sqlalchemy import Column, Integer, String
from app.database.base import Base
from sqlalchemy.orm import relationship


class Department(Base):

    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    department_name = Column(
        String(100),
        nullable=False
    )
    faculty = relationship("Faculty",back_populates="department")
    students = relationship("Student",back_populates="department")
    subjects = relationship("Subject",back_populates="department")