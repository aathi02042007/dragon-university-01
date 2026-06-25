from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.admission_request import AdmissionRequestSchema, AdmissionResponseSchema
from app.models.admission_request import AdmissionReq
from app.database.session import get_db
from app.services.admission_services import AdmissionService
from fastapi import HTTPException
from app.core.security import get_current_user

router = APIRouter(
    prefix="/admissions",
    tags=["Admissions"]
    )
service = AdmissionService()


@router.post("/")
def create_admission(
    admission_data: AdmissionRequestSchema,
    db: Session = Depends(get_db)
):
    try:
        admission = AdmissionReq(
        student_name=admission_data.name,
        email=admission_data.Email,
        phone=admission_data.Phone,
        dob=admission_data.DOB,
        gender=admission_data.Gender,
        hsc_group=admission_data.HSC_Group,
        hsc_percentage=admission_data.HSC_Percentage,
        school_name=admission_data.School_Name,
        passing_year=admission_data.Passing_Year,
        department_id=admission_data.department_id,
        course=admission_data.course
        )
        return service.apply_admission(
        db,
        admission
        )
    except HTTPException:
        raise
   
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.get("/")
def get_all_admissions(current_user = Depends(get_current_user),
                       db: Session = Depends(get_db)):
    try:
        if current_user.role != "Admin":
                    raise HTTPException(
                        status_code=403,
                        detail="Access denied"
                    )
        return service.view_all_admissions(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    

@router.get("/{id}")
def get_admission_by_id(id: int,db:Session = Depends(get_db)):
    try:
        return service.view_admission(db,id)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.put("/{id}/status")
def approve_admission(
    id: int,
    admission_data: AdmissionResponseSchema,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role != "Admin":
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.update_admission_status(
            db=db,
            admission_id=id,
            status=admission_data.status
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.delete("/{id}")
def delete_admission(
    id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        if current_user.role != "Admin":
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return service.remove_admission(
            db=db,
            admission_id=id
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        




