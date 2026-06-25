from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.notifications import Notification




class NotificationRepository:



   def create_notification(
    self,
    db: Session,
    notification: Notification):
      try:
        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification
      except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Database Error: {str(e)}")

   def get_all_notifications(
    self,
    db: Session):
      try:
        return db.query(Notification).all()

      except SQLAlchemyError as e:
        raise Exception(f"Database Error: {str(e)}")


   def get_notification_by_id(self,
                              db: Session,notification_id: int):
      try:
        notification = (
            db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )

        if not notification:
            raise ValueError("Notification not found")

        return notification

      except SQLAlchemyError as e:
        raise Exception(f"Database Error: {str(e)}")



   def update_notification_status(
    self,
    db: Session,
    notification_id: int,
    is_read: str):
    try:
        notification = self.get_notification_by_id(
            db,
            notification_id
        )

        notification.is_read = is_read

        db.commit()
        db.refresh(notification)

        return notification

    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Database Error: {str(e)}")


   def delete_notification(
    self,
    db: Session,
    notification_id: int
    ):
        try:
            notification = self.get_notification_by_id(
            db,
            notification_id)

            db.delete(notification)
            db.commit()

            return {
            "message": "Notification deleted successfully"
            }

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")


   def get_notifications_by_user(
    self,
    db: Session,
    user_id: int):
      try:


         return (
            db.query(Notification)
            .filter(Notification.receiver_id == user_id)
            .all()
        )
      except SQLAlchemyError as e:
         raise Exception(f"Database Error: {str(e)}")