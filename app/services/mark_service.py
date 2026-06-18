from app.repositories.mark_repo import (
    get_all_marks
)


def fetch_all_marks(
    db
):

    return get_all_marks(
        db
    )