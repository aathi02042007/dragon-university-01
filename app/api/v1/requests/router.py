from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.security import get_current_user

from app.models.requests import Request
from app.schemas.requests import (
    RequestSchema,
    RequestStatusSchema
)
from app.services.requests_services import RequestService


router = APIRouter(
    prefix="/requests",
    tags=["Requests"]
)

service = RequestService()


@router.post("/")
def create_request(
    request_data: RequestSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        if current_user.role not in [
            "Student",
            "Faculty",
            "HOD"
        ]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        request = Request(
            request_type=request_data.request_type,
            requested_by=current_user.id,
            target_id=request_data.target_id,
            old_data=request_data.old_data,
            new_data=request_data.new_data
        )

        return service.create_request(
            db,
            request
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/")
def get_all_requests(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        if current_user.role not in [
            "HOD",
            "Admin"
        ]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.view_all_requests(db)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{id}")
def get_request_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return service.view_request(db, id)


@router.put("/{id}/status")
def update_request_status(
    id: int,
    request_data: RequestStatusSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        if current_user.role not in [
            "HOD",
            "Admin"
        ]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.update_request_status(
            db=db,
            request_id=id,
            status=request_data.status,
            approved_by=current_user.id
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete("/{id}")
def delete_request(
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

        return service.remove_request(
            db,
            id
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )