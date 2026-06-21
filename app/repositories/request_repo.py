from app.models.request import Request


def get_all_requests(
    db
):

    return db.query(
        Request
    ).all()