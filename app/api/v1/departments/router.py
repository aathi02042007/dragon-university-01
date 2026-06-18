from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.department_repo import (
    get_all_departments
)


router = APIRouter()


@router.get("/")
def all_departments(

    db: Session = Depends(get_db)

):

    return get_all_departments(
        db
    )