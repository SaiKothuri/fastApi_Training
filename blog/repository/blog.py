from sqlalchemy.orm import Session

from ..import models

from .. import schemas, database  # Importing schemas and database from the current package

from ..repository import blog  # Importing blog repository for database operations


def get_all(db: Session):
    blogs = db.query(models.Blog).all()  # Querying all blogs from the database
    return blogs  # Returning the list of blogs

