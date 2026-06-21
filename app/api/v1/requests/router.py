from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.request_repo import get_all_requests
from app.services.request_service import fetch_all_requests

router = APIRouter()


@router.get("/")
def all_requests(

    db: Session = Depends(get_db)

):

    return fetch_all_requests(
        db
    )