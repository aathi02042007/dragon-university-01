from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.student_repo import get_all_students
from app.services.student_service import fetch_all_students

router = APIRouter()


@router.get("/")
def all_students(

    db: Session = Depends(get_db)

):

    return fetch_all_students(
        db
    )