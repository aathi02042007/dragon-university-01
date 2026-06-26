from app.repositories.subject_repo import (
    get_all_subjects
)


def fetch_all_subjects(
    db
):

    return get_all_subjects(
        db
    )