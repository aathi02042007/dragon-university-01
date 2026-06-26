from sqlalchemy.orm import Session

from app.repositories.marks_repo import MarksRepository
from app.models.marks import Marks





class MarksService:
    def __init__(self):
        self.repo = MarksRepository()


    def upload_marks(
    self,
    db: Session,
    marks: Marks):
        return self.repo.create_marks(
        db,
        marks
    )

    def view_all_marks(
    self,
    db: Session):

        return self.repo.get_all_marks(db)

    def view_marks(
    self,
    db: Session,
    marks_id: int):

        return self.repo.get_marks_by_id(
        db,
        marks_id)

    def update_marks(
    self,
    db: Session,
    marks_id: int,
    internal_marks: int,
    external_marks: int):

        return self.repo.update_marks(
        db,
        marks_id,
        internal_marks,
        external_marks)

    def remove_marks(
    self,
    db: Session,
    marks_id: int):

        return self.repo.delete_marks(
        db,
        marks_id
    )