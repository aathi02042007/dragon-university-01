from sqlalchemy.orm import Session

from app.repositories.attendance_repo import AttendanceRepository
from app.models.attendance import Attendancemodel as Attendance





class AttendanceService:


    def __init__(self):
            self.repo = AttendanceRepository()

    def mark_attendance(
    self,
    db: Session,
    attendance: Attendance):
        return self.repo.create_attendance(
        db,
        attendance)

    def view_all_attendance(
    self,
    db: Session):
        return self.repo.get_all_attendance(db)


    def view_attendance(
    self,
    db: Session,
    attendance_id: int):
        return self.repo.get_attendance_by_id(
        db,
        attendance_id)

    def update_attendance(
    self,
    db: Session,
    attendance_id: int,
    status: str):
        return self.repo.update_attendance(
        db,
        attendance_id,
        status)



    def remove_attendance(
    self,
    db: Session,
    attendance_id: int):
        return self.repo.delete_attendance(
        db,
        attendance_id
    )

    