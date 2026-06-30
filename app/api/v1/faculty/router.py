from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.department import DepartmentCreate

from app.services.department_service import (
    fetch_all_departments,
    fetch_department_by_id,
    add_department,
    edit_department,
    remove_department
)

router = APIRouter()


@router.get("/")
def all_departments(

    db: Session = Depends(get_db)

):

    return fetch_all_departments(
        db
    )


@router.get("/{department_id}")
def department_by_id(

    department_id: int,

    db: Session = Depends(get_db)

):

    return fetch_department_by_id(

        db,

        department_id

    )


@router.post("/")
def create_department(

    department: DepartmentCreate,

    db: Session = Depends(get_db)

):

    return add_department(

        db,

        department

    )


@router.put("/{department_id}")
def update_department(

    department_id: int,

    department: DepartmentCreate,

    db: Session = Depends(get_db)

):

    return edit_department(

        db,

        department_id,

        department

    )


@router.delete("/{department_id}")
def delete_department(

    department_id: int,

    db: Session = Depends(get_db)

):

    return remove_department(

        db,

        department_id

    )