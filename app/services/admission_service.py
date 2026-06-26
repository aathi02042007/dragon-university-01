from app.repositories.admission_repo import get_all_admissions
from app.services.admission_service import fetch_all_admissions


def fetch_all_admissions(
    db
):

    return fetch_all_admissions(
        db
    )