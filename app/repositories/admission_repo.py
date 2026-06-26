from app.models.admission import AdmissionRequest


def get_all_admissions(
    db
):

    return db.query(
        AdmissionRequest
    ).all()
from sqlalchemy.orm import Session
from app.models.admission_request import AdmissionReq
from sqlalchemy.exc import SQLAlchemyError

class AdmissionRepository:
    # admissions create pana
    def create_admission(self, db: Session, admission: AdmissionReq):
        try:
            db.add(admission)
            db.commit()
            db.refresh(admission)

            return admission
        except SQLAlchemyError as e:

            db.rollback()
            raise e
    # admission get pana
    def get_all_admissions(self, db: Session,admissions:AdmissionReq):

        try:
            admissions = db.query(AdmissionReq).all()
            return admissions
        
        except SQLAlchemyError as e:

            raise e
    #admissions get pana by id
    def get_admission_by_id(
        self,
        db: Session,
        admission_id: int,
        admission:AdmissionReq
    ):
        try:
            admission = db.query(
                AdmissionReq
            ).filter(
                AdmissionReq.id == admission_id
            ).first()

            if not admission:
                raise ValueError(
                    f"Admission ID {admission_id} not found"
                )

            return admission

        except SQLAlchemyError as e:
            
            raise Exception(
                f"Database Error: {str(e)}"
            )
    
    def update_admission_status(
        self,
        db: Session,
        admission_id: int,
        status: str,
        admission:AdmissionReq
    ):
        
        try:
            admission = self.get_admission_by_id(
                    db,
                    admission_id
            )

            admission.status = status

            db.commit()
            db.refresh(admission)

            return admission

        except SQLAlchemyError as e:
            db.rollback()

            raise Exception(
                f"Database Error: {str(e)}"
                )
        
    def delete_admission(
    self,
    db: Session,
    admission_id: int,admission:AdmissionReq):
        try:
            admission = self.get_admission_by_id(
                db,
                admission_id
            )
            db.delete(admission)
            db.commit()

            return {
            "message": "Admission deleted successfully"
        }

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(
                f"Database Error: {str(e)}"
            )

