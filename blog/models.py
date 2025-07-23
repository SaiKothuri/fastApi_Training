from .database import Base  # Importing Base, Sessionlocal, and engine from database module

from sqlalchemy import Column, Integer, String, ForeignKey # Importing SQLAlchemy types for model definition

from sqlalchemy.orm import relationship  # Importing relationship for ORM relationships



class Blog(Base):
    __tablename__ = "blogs"  # Defining the table name for the Blog model
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the Blog model
    title = Column(String, index=True)  # Title of the blog
    body = Column(String)  # Body content of the blog
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to link to the User model

    creator = relationship("User", back_populates="blogs")  # Establishing a relationship with the User model



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the User model
    name = Column(String)
    email = Column(String)  # Unique email for the user
    password = Column(String)  # Password for the user


    blogs = relationship("Blog", back_populates="creator")  # Establishing a relationship with the Blog model