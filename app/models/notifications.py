from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    message = Column(String, nullable=False)

    receiver_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    sender_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    is_read = Column(
        String,
        default="Unread",
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )