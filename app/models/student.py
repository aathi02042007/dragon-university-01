from sqlalchemy import Column,Integer,String,Date,ForeignKey
from app.database.base import Base
from sqlalchemy.orm import relationship


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    admission_no = Column(
        String(30),
        unique=True
    )

    student_id = Column(
        String(30),
        unique=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    dept_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    course = Column(
        String(100)
    )

    batch_year = Column(
        Integer
    )

    dob = Column(
        Date
    )

    gender = Column(
        String(20)
    )

    phone = Column(
        String(15)
    )

    email = Column(
        String(100)
    )

    address = Column(
        String(255)
    )

    parent_name = Column(
        String(100)
    )

    parent_phone = Column(
        String(15)
    )
    department = relationship(

    "Department",

    back_populates="students"
    
    )