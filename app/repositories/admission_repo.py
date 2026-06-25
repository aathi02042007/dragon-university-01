from sqlalchemy.orm import Session
from app.models.admission_request import AdmissionReqSchema
from sqlalchemy.exc import SQLAlchemyError

class AdmissionRepository:
    # admissions create pana
    def create_admission(self, db: Session, admission: AdmissionReqSchema):
        try:
            db.add(admission)
            db.commit()
            db.refresh(admission)

            return admission
        except SQLAlchemyError as e:

            db.rollback()
            raise e
    # admission get pana
    def get_all_admissions(self, db: Session,admissions:AdmissionReqSchema):

        try:
            admissions = db.query(AdmissionReqSchema).all()
            return admissions
        
        except SQLAlchemyError as e:

            raise e
    #admissions get pana by id
    def get_admission_by_id(
        self,
        db: Session,
        admission_id: int,
        admission:AdmissionReqSchema
    ):
        try:
            admission = db.query(
                AdmissionReqSchema
            ).filter(
                AdmissionReqSchema.id == admission_id
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
        admission:AdmissionReqSchema
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
    admission_id: int,admission:AdmissionReqSchema):
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

