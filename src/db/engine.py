# src\db\engine.py
from sqlmodel import create_engine, SQLModel, Session
from src.model.user_table import User
from src.model.book_table import Book


database_url = "sqlite:///book_selling.db"
engine = create_engine(database_url, echo=True)


# create table
def create_tables():
    SQLModel.metadata.create_all(engine) 


# open/close DB connection
def get_session():
   with Session(engine) as session:
       yield session
       