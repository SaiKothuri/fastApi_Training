from fastapi import APIRouter, Depends

from .. import schemas, database, models  # Importing schemas from the current package

from typing import List  # Importing List for type hinting

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM



router = APIRouter()  # Creating an instance of APIRouter

@router.get("/blog", response_model=List[schemas.ShowBlog], tags=['blogs'])  # Defining a GET endpoint to retrieve all blogs
def get_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs