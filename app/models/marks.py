from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class Marks(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(String, nullable=False)
    subject_code = Column(String, nullable=False)

    internal_marks = Column(Integer, nullable=False)
    external_marks = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )