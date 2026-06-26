from sqlalchemy import (
    Column,
    Integer,
    Text,
    Boolean,
    TIMESTAMP,
    ForeignKey
)

from sqlalchemy.sql import func

from app.database.base import Base


class Notification(Base):

    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    message = Column(
        Text
    )

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )