from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.marks import Marks




class MarksRepository:

    def create_marks(
    self,
    db: Session,
    marks: Marks):
        try:
            db.add(marks)
            db.commit()
            db.refresh(marks)

            return marks

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")

    def get_all_marks(
    self,
    db: Session
):
        try:
            return db.query(Marks).all()

        except SQLAlchemyError as e:
            raise Exception(f"Database Error: {str(e)}")


    def get_marks_by_id(
    self,
    db: Session,
    marks_id: int
):
        try:
            marks = (
            db.query(Marks)
            .filter(Marks.id == marks_id)
            .first())

            if not marks:
                raise ValueError("Marks not found")

            return marks

        except SQLAlchemyError as e:
            raise Exception(f"Database Error: {str(e)}")



    def update_marks(
    self,
    db: Session,
    marks_id: int,
    internal_marks: int,
    external_marks: int
):
        try:
            marks = self.get_marks_by_id(
            db,
            marks_id)

            marks.internal_marks = internal_marks
            marks.external_marks = external_marks
            marks.total = internal_marks + external_marks

            db.commit()
            db.refresh(marks)

            return marks

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")



    def delete_marks(
    self,
    db: Session,
    marks_id: int
):
        try:
            marks = self.get_marks_by_id(
            db,
            marks_id)

            db.delete(marks)
            db.commit()

            return {
            "message": "Marks deleted successfully"
            }

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")