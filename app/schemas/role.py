from pydantic import BaseModel

class RoleBase(BaseModel):
    role_name: str

class Rolecreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id:int

    class config:
        from_attributes = True
