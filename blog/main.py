from fastapi import FastAPI, Depends, status, Response, HTTPException # Importing FastAPI

app = FastAPI()  # Creating an instance of FastAPI

from . import schemas  # Importing schemas from the current package

from .import models  # Importing models from the current package

from .database import Sessionlocal, engine # Importing Sessionlocal and engine from database module

models.Base.metadata.create_all(engine)  # Creating all tables in the database

from sqlalchemy import create_engine # Importing create_engine from SQLAlchemy

from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy ORM

from typing import List, Optional  # Importing List and Optional for type hinting

from passlib.context import CryptContext  # Importing CryptoContext for password hashing

def get_db():
    db = Sessionlocal()  # Creating a new session
    try:
        yield db  # Yielding the session for use in dependency injection
    finally:
        db.close()  # Closing the session after use

@app.post("/blog", status_code=status.HTTP_201_CREATED)  # Defining a POST endpoint to create a new blog
def create(request : schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()  # Committing the new blog to the database
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", response_model=List[schemas.ShowBlog])  # Defining a GET endpoint to retrieve all blogs
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)  # Defining a GET endpoint to retrieve a blog by ID
def get_blog(id, response:Response,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
        # return {"error": "Blog not found"}
        
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)  # Defining a DELETE endpoint to remove a blog by ID
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()  # Deleting the blog by ID
    return 'Deleted successfully'  # Returning a success message

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)  # Defining a PUT endpoint to update a blog by ID
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update({"title": request.title, "body": request.body}, synchronize_session=False)
    db.commit()  # Updating the blog by ID
    return 'Updated successfully'  # Returning a success message


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Creating a password context for hashing


@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashedpassword = pwd_cxt.hash(request.password)  # Hashing the password
    new_user = models.User(name=request.username, email=request.email, password=hashedpassword)  # Creating a new user model instance
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user  # Returning the newly created user
