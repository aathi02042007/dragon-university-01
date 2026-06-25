from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.requests import Request


class RequestRepository:

    def create_request(
        self,
        db: Session,
        request: Request
    ):
        try:
            db.add(request)
            db.commit()
            db.refresh(request)
            return request

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(str(e))


    def get_all_requests(
        self,
        db: Session
    ):
        try:
            return db.query(Request).all()

        except SQLAlchemyError as e:
            raise Exception(str(e))


    def get_request_by_id(
        self,
        db: Session,
        request_id: int
    ):
        try:
            request = db.query(Request).filter(
                Request.id == request_id
            ).first()

            if not request:
                raise ValueError("Request not found")

            return request

        except SQLAlchemyError as e:
            raise Exception(str(e))


    def update_request_status(
        self,
        db: Session,
        request_id: int,
        status: str,
        approved_by: int
    ):
        try:
            request = self.get_request_by_id(
                db,
                request_id
            )

            request.status = status
            request.approved_by = approved_by

            db.commit()
            db.refresh(request)

            return request

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(str(e))


    def delete_request(
        self,
        db: Session,
        request_id: int
    ):
        try:
            request = self.get_request_by_id(
                db,
                request_id
            )

            db.delete(request)
            db.commit()

            return {
                "message": "Request Deleted Successfully"
            }

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(str(e))