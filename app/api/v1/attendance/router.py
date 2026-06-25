from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.security import get_current_user

from app.schemas.attendance import AttendanceSchema
from app.models.attendance import Attendance
from app.services.attendance_services import AttendanceService

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

service = AttendanceService()

@router.post("/")
def mark_attendance(
    attendance_data: AttendanceSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["Faculty", "HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        attendance = Attendance(
            student_id=attendance_data.student_id,
            attendance_date=attendance_data.attendance_date,
            class_name=attendance_data.class_name,
            batch_year=attendance_data.batch_year,
            status=attendance_data.status,
            marked_by=attendance_data.marked_by
        )

        return service.mark_attendance(db, attendance)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/")
def get_all_attendance(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["Faculty", "HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.view_all_attendance(db)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/{id}")
def get_attendance_by_id(
    id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return service.view_attendance(db, id)

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put("/{id}")
def update_attendance(
    id: int,
    attendance_data: AttendanceSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["Faculty", "HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.update_attendance(
            db=db,
            attendance_id=id,
            status=attendance_data.status
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete("/{id}")
def delete_attendance(
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

        return service.remove_attendance(
            db=db,
            attendance_id=id
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


