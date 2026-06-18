from app.repositories.department_repo import (
    get_all_departments
)


def fetch_all_departments(
    db
):

    return get_all_departments(
        db
    )