from sqlalchemy.orm import Session
from . import models, schemas

# CRUD operations for Student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# CRUD operations for Subject
def create_subject(db: Session, subject: schemas.SubjectCreate):
    db_subject = models.Subject(name=subject.name)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def get_subjects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Subject).offset(skip).limit(limit).all()

def get_subject(db: Session, subject_id: int):
    return db.query(models.Subject).filter(models.Subject.id == subject_id).first()

def delete_subject(db: Session, subject_id: int):
    db_subject = get_subject(db, subject_id)
    if db_subject:
        db.delete(db_subject)
        db.commit()
    return db_subject

# CRUD operations for Marks
def create_marks(db: Session, marks: schemas.MarksCreate):
    db_marks = models.Marks(student_id=marks.student_id, subject_id=marks.subject_id, marks=marks.marks)
    db.add(db_marks)
    db.commit()
    db.refresh(db_marks)
    return db_marks

def get_marks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Marks).offset(skip).limit(limit).all()

def get_marks_by_student(db: Session, student_id: int):
    return db.query(models.Marks).filter(models.Marks.student_id == student_id).all()

def delete_marks(db: Session, marks_id: int):
    db_marks = db.query(models.Marks).filter(models.Marks.id == marks_id).first()
    if db_marks:
        db.delete(db_marks)
        db.commit()
    return db_marks
