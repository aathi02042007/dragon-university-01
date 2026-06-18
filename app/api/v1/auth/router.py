from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.user_repo import get_user_by_email
from app.core.security import create_access_token
from app.schemas.user import UserLogin
from app.core.security import create_access_token,verify_password
from app.core.dependencies import get_current_user
from app.services.auth_service import login_user


router = APIRouter()


@router.get("/test")
def auth_test():

    return {
        "message": "Auth Working"
    }


@router.post("/login")
def login(
    data: UserLogin,

    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        data.email,
        data.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="User not found")
    if token is False:
        raise HTTPException(
            status_code=401,
            detail="Invalid password")

    return {

        "access_token": token,

        "token_type": "bearer"

    }

@router.get("/profile")
def profile(

    current_user=Depends(
        get_current_user
    )

):

    return {

        "user": current_user

    }