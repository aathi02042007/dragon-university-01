# -*- coding: utf-8 -*-
"""
DRAGON ERP Backend - Main Entrypoint
This is an architectural placeholder for the FastAPI backend service.
No real business logic is implemented.
"""

# TODO: Implement FastAPI server configuration and startup handlers.
# In a real environment, uncomment the following import block and configure routers.

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.core.config import settings
# from app.api.v1 import (
#     auth, students, faculty, departments, subjects, 
#     attendance, marks, requests, notifications, admissions
# )

# app = FastAPI(
#     title=settings.PROJECT_NAME,
#     version=settings.VERSION,
#     openapi_url=f"{settings.API_V1_STR}/openapi.json"
# )

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include Routers
# app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
# app.include_router(students.router, prefix=f"{settings.API_V1_STR}/students", tags=["students"])
# app.include_router(faculty.router, prefix=f"{settings.API_V1_STR}/faculty", tags=["faculty"])
# app.include_router(departments.router, prefix=f"{settings.API_V1_STR}/departments", tags=["departments"])
# app.include_router(subjects.router, prefix=f"{settings.API_V1_STR}/subjects", tags=["subjects"])
# app.include_router(attendance.router, prefix=f"{settings.API_V1_STR}/attendance", tags=["attendance"])
# app.include_router(marks.router, prefix=f"{settings.API_V1_STR}/marks", tags=["marks"])
# app.include_router(requests.router, prefix=f"{settings.API_V1_STR}/requests", tags=["requests"])
# app.include_router(notifications.router, prefix=f"{settings.API_V1_STR}/notifications", tags=["notifications"])
# app.include_router(admissions.router, prefix=f"{settings.API_V1_STR}/admissions", tags=["admissions"])

# @app.get("/")
# def root():
#     return {"message": "Welcome to DRAGON ERP API service. Architectural scaffolding active."}

if __name__ == "__main__":
    print("DRAGON ERP Backend Scaffolding is active. Run with uvicorn in dev mode.")
