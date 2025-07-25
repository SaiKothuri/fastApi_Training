from fastapi import APIRouter, Depends

from .. import schemas, database, models  # Importing schemas from the current package

from typing import List  # Importing List for type hinting

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM

from ..repository import blog  # Importing blog repository for database operations

from .. import oauth2  # Importing OAuth2 for authentication



router = APIRouter(
    prefix="/blog",  # Setting a prefix for the router
    tags=['blogs']  # Setting tags for the router
)  # Creating an instance of APIRouter

@router.get("/", response_model=List[schemas.ShowBlog])  # Defining a GET endpoint to retrieve all blogs
def get_all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).all()
    return blog.get_all(db)  # Using the repository function to get all blogs