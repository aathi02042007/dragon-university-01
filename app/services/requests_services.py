from sqlalchemy.orm import Session

from app.models.requests import Request
from app.repositories.requests_repo import RequestRepository


class RequestService:

    def __init__(self):
        self.repo = RequestRepository()


    def create_request(
        self,
        db: Session,
        request: Request
    ):
        return self.repo.create_request(db, request)


    def view_all_requests(
        self,
        db: Session
    ):
        return self.repo.get_all_requests(db)


    def view_request(
        self,
        db: Session,
        request_id: int
    ):
        return self.repo.get_request_by_id(
            db,
            request_id
        )


    def update_request_status(
        self,
        db: Session,
        request_id: int,
        status: str,
        approved_by: int
    ):
        return self.repo.update_request_status(
            db,
            request_id,
            status,
            approved_by
        )


    def remove_request(
        self,
        db: Session,
        request_id: int
    ):
        return self.repo.delete_request(
            db,
            request_id
        )