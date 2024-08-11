from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/marks/", response_model=schemas.Marks)
def create_marks(marks: schemas.MarksCreate, db: Session = Depends(get_db)):
    return crud.create_marks(db=db, marks=marks)

@router.get("/marks/", response_model=List[schemas.Marks])
def read_marks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    marks = crud.get_marks(db, skip=skip, limit=limit)
    return marks

@router.delete("/marks/{marks_id}", response_model=schemas.Marks)
def delete_marks(marks_id: int, db: Session = Depends(get_db)):
    db_marks = crud.get_marks_by_student(db, marks_id)
    if db_marks is None:
        raise HTTPException(status_code=404, detail="Marks not found")
    return crud.delete_marks(db=db, marks_id=marks_id)
