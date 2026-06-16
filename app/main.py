from fastapi import FastAPI

from app.api.v1.auth.router import router as auth_router

app = FastAPI(
    title="Dragon ERP Backend"
)
app.include_router(
    auth_router,

    prefix="/auth",

    tags=["Authentication"]
)
@app.get("/")
def root():

    return {
        "message": "Dragon ERP Backend Running"
    }