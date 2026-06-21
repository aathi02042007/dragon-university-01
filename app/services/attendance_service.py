from app.repositories.attendance_repo import (
    get_all_attendance
)


def fetch_all_attendance(
    db
):

    return get_all_attendance(
        db
    )