from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.attendance_repo import get_all_attendance
from app.services.attendance_service import fetch_all_attendance
router = APIRouter()


@router.get("/")
def all_attendance(

    db: Session = Depends(get_db)

):

    return fetch_all_attendance(
        db
    )