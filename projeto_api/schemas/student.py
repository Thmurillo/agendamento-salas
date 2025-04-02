from pydantic import BaseModel

class StudentCreate(BaseModel):
    user_id: int
    full_name: str
    cpf: str
    academic_registry: str
    email: str
    course: str

class StudentResponse(BaseModel):
    id: int
    user_id: int
    full_name: str
    cpf: str
    academic_registry: str
    email: str
    course: str

    class Config:
        orm_mode = True