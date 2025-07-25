from fastapi import APIRouter, Depends, status, HTTPException  # Importing FastAPI components

from .. import schemas, database, models  # Importing schemas from the current package

from typing import List  # Importing List for type hinting

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM

router = APIRouter(
    prefix="/users",  # Setting a prefix for the router
    tags=['users']  # Setting tags for the router
)  # Creating an instance of APIRouter

get_db = database.get_db  # Importing get_db function from database module

from ..import hashing  # Importing Hash class for password hashing

from ..hashing import Hash  # Importing Hash class for password hashing

@router.get('/{id}', response_model=schemas.ShowUser)  # Defining a GET endpoint to retrieve a user by ID
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")
    return user
