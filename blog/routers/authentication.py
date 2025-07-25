from fastapi import APIRouter

from .. import schemas  # Importing schemas from the current package    

from ..import database, models  # Importing database and models from the current package

from fastapi import Depends, status, HTTPException

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM

from ..hashing import Hash  # Importing Hash class for password hashing

from ..import token  # Importing token creation function and Token model

from fastapi.security import OAuth2PasswordRequestForm  # Importing OAuth2PasswordRequestForm for login



router = APIRouter(
    tags=['authentication']  # Setting tags for the router
)  # Creating an instance of APIRouter 

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()  # Querying the user by email
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

    access_token = token.create_access_token(data={"sub":user.email}) # Creating an access token with the user's email as the subject
    return {"access_token":access_token, "token_type":"bearer"}