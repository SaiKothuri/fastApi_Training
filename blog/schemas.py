from pydantic import BaseModel

from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str



class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []  # Assuming a user can have multiple blogs
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body : str
    creator: ShowUser  # Assuming creator is a string, adjust as necessary
    class Config:
        orm_mode = True

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None