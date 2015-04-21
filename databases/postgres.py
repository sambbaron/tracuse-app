"""Primary PostgreSQL database using SQLAlchemy ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

HOST = "localhost"
PORT = 5432
USERNAME = "test"
PASSWORD = "test"
DATABASE_NAME = "tracuse"

DB_URI = "postgresql://{}:{}@{}:{}/{}".format(USERNAME,
                                              PASSWORD,
                                              HOST,
                                              PORT,
                                              DATABASE_NAME)

engine = create_engine(DB_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

def drop_create():
    print("Drop and Create PostgreSQL-{}".format(DATABASE_NAME))
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
