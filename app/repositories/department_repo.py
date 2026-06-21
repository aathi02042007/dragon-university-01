from app.models.department import Department


def get_all_departments(db):

    return db.query(
        Department
    ).all()