from app.repositories.faculty_repo import (
    get_all_faculty
)


def fetch_all_faculty(
    db
):

    return get_all_faculty(
        db
    )