from app.models.student import Student


def get_all_students(
    db
):

    return db.query(
        Student
    ).all()