from app.repositories.request_repo import (
    get_all_requests
)


def fetch_all_requests(
    db
):

    return get_all_requests(
        db
    )