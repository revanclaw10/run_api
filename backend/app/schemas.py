from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode: True

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int

    class Config:
        orm_mode: True

class MarksBase(BaseModel):
    student_id: int
    subject_id: int
    marks: int

class MarksCreate(MarksBase):
    pass

class Marks(MarksBase):
    id: int

    class Config:
        orm_mode: True
