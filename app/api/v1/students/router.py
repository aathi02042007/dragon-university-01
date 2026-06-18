from fastapi import (
    APIRouter,

    Depends
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.student_repo import (
    get_all_students
)

router = APIRouter()


@router.get("/")
def all_students(

    db: Session = Depends(get_db)

):

    return get_all_students(
        db
    )