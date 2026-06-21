from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.subject_repo import get_all_subjects
from app.services.subject_service import fetch_all_subjects

router = APIRouter()


@router.get("/")
def all_subjects(

    db: Session = Depends(get_db)

):

    return fetch_all_subjects(
        db
    )