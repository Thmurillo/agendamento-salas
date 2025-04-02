from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    login: str
    user_password: str
    user_type: str

class UserResponse(BaseModel):
    id: int
    user_name: str
    login: str
    user_type: str

    class Config:
        orm_mode = True
