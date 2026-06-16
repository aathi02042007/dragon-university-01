from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_notification():
    pass

@router.get("/")
def get_all_notifications():
    pass

@router.get("/{user_id}")
def get_notifications_by_user(user_id: int):
    pass

@router.put("/{id}/read")
def mark_as_read(id: int):
    pass

@router.delete("/{id}")
def delete_notification(id: int):
    pass