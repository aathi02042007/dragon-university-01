from app.models.mark import Mark


def get_all_marks(db):

    return db.query(
        Mark
    ).all()