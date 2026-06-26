from app.repositories.notification_repo import (
    get_all_notifications
)


def fetch_all_notifications(
    db
):

    return get_all_notifications(
        db
    )