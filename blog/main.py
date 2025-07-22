from fastapi import FastAPI  # Importing FastAPI

app = FastAPI()  # Creating an instance of FastAPI

from . import schemas  # Importing schemas from the current package

from .import models  # Importing models from the current package

from .database import Sessionlocal, engine  # Importing Sessionlocal and engine from database module

models.Base.metadata.create_all(engine)  # Creating all tables in the database

from sqlalchemy import create_engine

@app.post("/blog")
def create(request : schemas.Blog):
    return request