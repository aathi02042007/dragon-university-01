from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_marks():
    pass

@router.get("/")
def get_all_marks():
    pass

@router.get("/{student_id}")
def get_marks_by_student(student_id: str):
    pass

@router.put("/{id}")
def update_marks(id: int):
    pass

@router.delete("/{id}")
def delete_marks(id: int):
    pass
