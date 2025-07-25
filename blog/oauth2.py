from fastapi import Depends, FastAPI, HTTPException, status, Response  # Importing FastAPI components

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM

import token

from . import schemas  # Importing schemas from the current package

from fastapi.security import OAuth2PasswordBearer  # Importing OAuth2PasswordBearer for token authentication

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") 
 # Setting up OAuth2 password bearer token


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(token, credentials_exception)  # Verifying the token