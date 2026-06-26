from app.models.attendance import Attendance


def get_all_attendance(
    db
):

    return db.query(
        Attendance
    ).all()
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.attendance import Attendance



class AttendanceRepository:

    def create_attendance(
    self,
    db: Session,
    attendance: Attendance):
        try:
            db.add(attendance)
            db.commit()
            db.refresh(attendance)
            return attendance
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")

    def get_all_attendance(
    self,
    db: Session):
        try:
            return db.query(Attendance).all()
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")

    def update_attendance(
    self,
    db: Session,
    attendance_id: int,
    status: str):
        try:
            attendance = self.get_attendance_by_id(
            db,
            attendance_id
        )

            attendance.status = status

            db.commit()
            db.refresh(attendance)

            return attendance

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")

    def get_attendance_by_id(
    self,
    db: Session,
    attendance_id: int):
        try:
            attendance = (
            db.query(Attendance)
            .filter(Attendance.id == attendance_id)
            .first()
            )

            if not attendance:
                raise ValueError("Attendance not found")

            return attendance

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")


    def delete_attendance(
    self,
    db: Session,
    attendance_id: int):
        try:
            attendance = self.get_attendance_by_id(
            db,
            attendance_id
            )

            db.delete(attendance)
            db.commit()

            return {
            "message": "Attendance deleted successfully"
            }

        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database Error: {str(e)}")
