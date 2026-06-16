from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_request():
    pass

@router.get("/")
def get_all_requests():
    pass

@router.get("/{id}")
def get_request_by_id(id: int):
    pass

@router.put("/{id}/status")
def update_status(id: int, status: str):
    pass

@router.delete("/{id}")
def delete_request(id:int):
    pass