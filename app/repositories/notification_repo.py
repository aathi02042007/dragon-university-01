from app.models.notification import Notification


def get_all_notifications(
    db
):

    return db.query(
        Notification
    ).all()