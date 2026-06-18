from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.mark_repo import get_all_marks


router = APIRouter()


@router.get("/")
def all_marks(

    db: Session = Depends(get_db)

):

    return get_all_marks(
        db
    )