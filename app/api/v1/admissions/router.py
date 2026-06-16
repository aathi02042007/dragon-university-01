from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.admission_request import AdmissionRequestSchema
from app.models.admission_request import AdmissionRequest
from app.database.session import get_db
from app.services.admission_services import AdmissionService
from fastapi import HTTPException

router = APIRouter()
service = AdmissionService()


@router.post("/")
def create_admission(
    admission_data: AdmissionRequestSchema,
    db: Session = Depends(get_db)
):
    try:
        admission = AdmissionRequest(
        student_name=admission_data.name,
        email=admission_data.Email,
        phone=admission_data.Phone,
        dob=admission_data.DOB,
        gender=admission_data.Gender,
        hsc_group=admission_data.HSC_Group,
        hsc_percentage=admission_data.HSC_Percentage,
        school_name=admission_data.School_Name,
        passing_year=admission_data.Passing_Year,
        department_id=admission_data.Department,
        course=admission_data.course
        )
        return service.apply_admission(
        db,
        admission
        )
   
    except Exception as e:
        raise HTTPException(
            status_code=500,
            details=str(e)
        )
    
@router.get("/")
def get_all_admissions():
    pass

@router.get("/{id}")
def get_admission_by_id(id: int):
    pass

@router.put("/{id}/approve")
def approve_admission(id: int):
    pass

@router.put("/{id}/reject")
def reject_admission(id: int):
    pass
