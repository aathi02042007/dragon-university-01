from sqlalchemy.orm import Session

from app.repositories.notifications_repo import NotificationRepository
from app.models.notifications import Notification



class NotificationService:

    def __init__(self):
        self.repo = NotificationRepository()

    def send_notification(
        self,
        db: Session,
        notification: Notification
        ):

        return self.repo.create_notification(
            db,
            notification
        )


    def view_all_notifications(
        self,
        db: Session
        ):


        return self.repo.get_all_notifications(db)


    def view_notification(
        self,
        db: Session,
        notification_id: int
        ):

        return self.repo.get_notification_by_id(
            db,
            notification_id
            )

    def mark_as_read(
        self,
        db: Session,
        notification_id: int,
        is_read: str
        ):

        return self.repo.update_notification_status(
            db,
            notification_id,
            is_read
            )



    def remove_notification(
        self,
        db: Session,
        notification_id: int
        ):

        return self.repo.delete_notification(
            db,
            notification_id
        )


    def view_my_notifications(
    self,
    db: Session,
    user_id: int
    ):

        return self.repo.get_notifications_by_user(
        db,
        user_id
    )