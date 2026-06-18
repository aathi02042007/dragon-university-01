from app.models.attendance import Attendance


def get_all_attendance(
    db
):

    return db.query(
        Attendance
    ).all()