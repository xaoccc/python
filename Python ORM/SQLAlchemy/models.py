from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from main import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


Base.metadata.create_all(engine)
