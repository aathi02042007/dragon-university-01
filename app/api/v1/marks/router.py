from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.mark_repo import get_all_marks
from app.services.mark_service import fetch_all_marks

router = APIRouter()


@router.get("/")
def all_marks(

    db: Session = Depends(get_db)

):

    return fetch_all_marks(
        db
    )
﻿from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.security import get_current_user

from app.schemas.marks import MarksSchema
from app.models.marks import Marks
from app.services.marks_services import MarksService


router = APIRouter(
    prefix="/marks",
    tags=["Marks"]
)

service = MarksService()



@router.post("/")
def upload_marks(
    marks_data: MarksSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["Faculty", "HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        marks = Marks(
            student_id=marks_data.student_id,
            subject_code=marks_data.subject_code,
            internal_marks=marks_data.internal_marks,
            external_marks=marks_data.external_marks,
            total=marks_data.internal_marks + marks_data.external_marks,
            uploaded_by=current_user.id
        )

        return service.upload_marks(db, marks)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/")
def get_all_marks(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["Faculty", "HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.view_all_marks(db)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/{id}")
def get_marks_by_id(
    id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return service.view_marks(db, id)

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put("/{id}")
def update_marks(
    id: int,
    marks_data: MarksSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["Faculty", "HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.update_marks(
            db=db,
            marks_id=id,
            internal_marks=marks_data.internal_marks,
            external_marks=marks_data.external_marks
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete("/{id}")
def delete_marks(
    id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role != "Admin":
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.remove_marks(
            db=db,
            marks_id=id
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
