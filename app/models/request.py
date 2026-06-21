from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    Enum,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.database.base import Base


class Request(Base):

    __tablename__ = "requests"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    request_type = Column(
        String(100)
    )

    requested_by = Column(
        Integer
    )

    target_id = Column(
        Integer
    )

    old_data = Column(
        JSON
    )

    new_data = Column(
        JSON
    )

    status = Column(
        Enum(
            "pending",

            "approved",

            "rejected"
        )
    )

    approved_by = Column(
        Integer
    )

    created_at = Column(
        TIMESTAMP,

        server_default=func.now()
    )