from pydantic import BaseModel


class NotificationSchema(BaseModel):
    title: str
    message: str
    receiver_id: int


class NotificationStatusSchema(BaseModel):
    is_read: str