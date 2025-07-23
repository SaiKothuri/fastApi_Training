from fastapi import FastAPI, Depends  # Importing FastAPI

app = FastAPI()  # Creating an instance of FastAPI

from . import schemas  # Importing schemas from the current package

from .import models  # Importing models from the current package

from .database import Sessionlocal, engine # Importing Sessionlocal and engine from database module

models.Base.metadata.create_all(engine)  # Creating all tables in the database

from sqlalchemy import create_engine # Importing create_engine from SQLAlchemy

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM

def get_db():
    db = Sessionlocal()  # Creating a new session
    try:
        yield db  # Yielding the session for use in dependency injection
    finally:
        db.close()  # Closing the session after use

@app.post("/blog")
def create(request : schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()  # Committing the new blog to the database
    db.refresh(new_blog)
    return new_blog