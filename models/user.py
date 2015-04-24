"""SQLAlchemy Models for User-related entities"""

from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from databases.postgres import Base


class User(Base):
    """Application Users

    Attributes:
        username (string, required, unique, indexed): Login username
        email (string, required, unique, indexed): Email address
        password (string): User password ***HASHING
    """
    #TODO need user security and authentication plug-in

    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String(128))

    datum_objects = relationship("DatumObject", backref="user")
    datum_filters = relationship("FilterSet", backref="user")