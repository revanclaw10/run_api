import sys
import os


# Add the path to the project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routers import student, subject, marks


from fastapi import FastAPI
from app.database import engine, Base


# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student.router)
app.include_router(subject.router)
app.include_router(marks.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
