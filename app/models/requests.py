from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from app.database.base import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)

    request_type = Column(String, nullable=False)

    requested_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    target_id = Column(Integer, nullable=False)

    old_data = Column(JSON, nullable=False)

    new_data = Column(JSON, nullable=False)

    status = Column(
        String,
        default="Pending",
        nullable=False
    )

    approved_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )