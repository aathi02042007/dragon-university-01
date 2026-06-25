from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.admission_repo import AdmissionRepository
from app.models.admission_request import AdmissionReqSchema


class AdmissionService:

    def __init__(self):
        self.repo = AdmissionRepository()

    # admission apply pana
    def apply_admission(
        self,
        db: Session,
        admission: AdmissionReqSchema
    ):

        try:

            if not admission.student_name:
                raise ValueError(
                    "Student name is required"
                )
            if admission.hsc_percentage < 45:
                raise ValueError(
                    "you are not eligible for admission",
                    "Minimum HSC percentage required is 45%"
                )

            return self.repo.create_admission(
                db,
                admission
            )

        except ValueError as e:
                raise HTTPException(
                    status_code=400,
                    details=str(e)
                )
        


    def view_all_admissions(
        self,
        db: Session
    ):

        try:
            return self.repo.get_all_admissions(db)

        except Exception as e:
            raise 


    def view_admission(
        self,
        db: Session,
        admission_id: int,
        admission:AdmissionReqSchema
    ):

        try:

            admission = self.repo.get_admission_by_id(
                db,
                admission_id
            )

            if not admission:
                raise ValueError(
                    "Admission not found"
                )

            return admission

        except Exception:
            raise


    def update_admission_status(
        self,
        db: Session,
        admission_id: int,
        status: str
    ):

        try:

            if status not in [
                "PENDING",
                "APPROVED",
                "REJECTED"
            ]:
                raise ValueError(
                    "Invalid status"
                )

            return self.repo.update_admission_status(
                db,
                admission_id,
                status
            )

        except Exception:
            raise


    def remove_admission(
        self,
        db: Session,
        admission_id: int
    ):

        try:
            return self.repo.delete_admission(
                db,
                admission_id
            )

        except Exception:
            raise