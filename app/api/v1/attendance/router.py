from  fastapi import APIRouter


router = APIRouter()


@router.post("/")
def create_admission():
    pass

@router.get("/")
def get_all_admissions():
    pass

@router.get("/{id}")
def get_admission_by_id(id: int):
    pass

@router.put("/{id}")
def approve_admission(id: int):
    pass

@router.delete("/{id}")
def reject_admission(id: int):
    pass
