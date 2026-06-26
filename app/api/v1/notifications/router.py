from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.notification_repo import get_all_notifications
from app.services.notification_service import fetch_all_notifications

router = APIRouter()


@router.get("/")
def all_notifications(

    db: Session = Depends(get_db)

):

    return fetch_all_notifications(
        db
    )
﻿from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.security import get_current_user

from app.models.notifications import Notification
from app.schemas.notifications import (
    NotificationSchema,
    NotificationStatusSchema
)
from app.services.notifications_services import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

service = NotificationService()



@router.post("/")
def send_notification(
    notification_data: NotificationSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        notification = Notification(
            title=notification_data.title,
            message=notification_data.message,
            receiver_id=notification_data.receiver_id,
            sender_id=current_user.id
        )

        return service.send_notification(db, notification)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/")
def get_all_notifications(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role not in ["HOD", "Admin"]:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.view_all_notifications(db)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# current user notifications matum
@router.get("/my")
def get_my_notifications(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return service.view_my_notifications(
            db,
            current_user.id
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{id}")
def get_notification_by_id(
    id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return service.view_notification(
            db,
            id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.put("/{id}/read")
def mark_as_read(
    id: int,
    notification_data: NotificationStatusSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return service.mark_as_read(
            db=db,
            notification_id=id,
            is_read=notification_data.is_read
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.delete("/{id}")
def delete_notification(
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

        return service.remove_notification(
            db=db,
            notification_id=id
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
