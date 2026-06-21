from fastapi import FastAPI
from app.api.v1.auth.router import router as auth_router
from app.api.v1.departments.router import router as department_router
from app.api.v1.faculty.router import router as faculty_router
from app.api.v1.students.router import router as student_router
from app.api.v1.subjects.router import router as subject_router
from app.api.v1.attendance.router import router as attendance_router
from app.api.v1.marks.router import router as marks_router
from app.api.v1.admissions.router import router as admissions_router
from app.api.v1.requests.router import router as requests_router
from app.api.v1.notifications.router import router as notifications_router


app = FastAPI(
    title="Dragon ERP Backend"
)
app.include_router(

notifications_router,

prefix="/notifications",

tags=["Notifications"]

)
app.include_router(

requests_router,

prefix="/requests",

tags=["Requests"]

)
app.include_router(

admissions_router,

prefix="/admissions",

tags=["Admissions"]

)
app.include_router(

marks_router,

prefix="/marks",

tags=["Marks"]

)
app.include_router(
    auth_router,

    prefix="/auth",

    tags=["Authentication"]
)
app.include_router(
    department_router,

    prefix="/departments",

    tags=["Departments"]
)
app.include_router(

faculty_router,

prefix="/faculty",

tags=["Faculty"]

)
app.include_router(

student_router,

prefix="/students",

tags=["Students"]

)
app.include_router(

subject_router,

prefix="/subjects",

tags=["Subjects"]

)
app.include_router(

attendance_router,

prefix="/attendance",

tags=["Attendance"]

)
@app.get("/")
def root():

    return {
        "message": "Dragon ERP Backend Running"
    }
