from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.notification_repo import get_all_notifications
from app.services.notification_service import fetch_all_notifications

router = APIRouter()


@router.get("/")
def all_notifications(

    db: Session = Depends(get_db)

):

    return fetch_all_notifications(
        db
    )