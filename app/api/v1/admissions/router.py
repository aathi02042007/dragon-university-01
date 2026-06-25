from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.admission_request import AdmissionRequestSchema
from app.models.admission_request import AdmissionReqSchema
from app.database.session import get_db
from app.services.admission_services import AdmissionService
from fastapi import HTTPException
from app.auth.auth_bearer import get_current_user

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
        admission = AdmissionReqSchema(
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
   
    except Exception as e:
        raise HTTPException(
            status_code=500,
            details=str(e)
        )
    
@router.get("/")
def get_all_admissions(admission_data:AdmissionRequestSchema, # inga paru !!!!
                       db: Session = Depends(get_db)):
    try:
        return service.view_all_admissions(db)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            details=str(e)
        )
    

@router.get("/{id}")
def get_admission_by_id(id: int,db:Session = Depends(get_db)):
    try:
        return service.view_admission(db)

    except Exception as e:
        raise HTTPException(
            status_code=404,
            details=str(e)
        )

@router.put("/{id}/status")
def approve_admission(id: int,admission_datat: AdmissionReqSchema
                      ,current_user: dict = Depends(get_current_user),db:Session = Depends(get_db)):
    try:
        if current_user.role != "Admin":
            raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

        




