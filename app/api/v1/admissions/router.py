from fastapi import (
    APIRouter,

    Depends
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.admission_repo import (
    get_all_admissions
)

router = APIRouter()


@router.get("/")
def all_admissions(

    db: Session = Depends(get_db)

):

    return get_all_admissions(
        db
    )