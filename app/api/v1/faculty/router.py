from fastapi import (
    APIRouter,

    Depends
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.faculty_repo import (
    get_all_faculty
)

router = APIRouter()


@router.get("/")
def all_faculty(

    db: Session = Depends(get_db)

):

    return get_all_faculty(
        db
    )