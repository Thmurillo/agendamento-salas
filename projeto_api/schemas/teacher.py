from pydantic import BaseModel

class TeacherCreate(BaseModel):
    user_id: int
    full_name: str
    cpf: str
    academic_registry: str
    email: str
    academic_title: str

class TeacherResponse(BaseModel):
    id: int
    user_id: int
    full_name: str
    cpf: str
    academic_registry: str
    email: str
    academic_title: str

    class Config:
        orm_mode = True