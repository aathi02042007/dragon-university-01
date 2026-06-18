from app.repositories.student_repo import (
    get_all_students
)


def fetch_all_students(
    db
):

    return get_all_students(
        db
    )