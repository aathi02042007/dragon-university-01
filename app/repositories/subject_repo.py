from app.models.subject import Subject


def get_all_subjects(
    db
):

    return db.query(
        Subject
    ).all()