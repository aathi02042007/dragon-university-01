from app.models.faculty import Faculty


def get_all_faculty(
    db
):

    return db.query(
        Faculty
    ).all()