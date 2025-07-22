from sqlalchemy import create_engine  # Importing create_engine from SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL = "sqlite:///./blog.db"  # SQLite database URL

engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})  # Create the database engine

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Create a session local

Base = declarative_base()  # Create a base class for declarative models