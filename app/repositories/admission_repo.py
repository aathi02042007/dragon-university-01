from app.models.admission import AdmissionRequest


def get_all_admissions(
    db
):

    return db.query(
        AdmissionRequest
    ).all()