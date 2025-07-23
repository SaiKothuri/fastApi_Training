from .database import Base  # Importing Base, Sessionlocal, and engine from database module

from sqlalchemy import Column, Integer, String, Boolean  # Importing SQLAlchemy types for model definition

class Blog(Base):
    __tablename__ = "blogs"  # Defining the table name for the Blog model
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the Blog model
    title = Column(String, index=True)  # Title of the blog
    body = Column(String)  # Body content of the blog

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the User model
    name = Column(String)
    email = Column(String)  # Unique email for the user
    password = Column(String)  # Password for the user