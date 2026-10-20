# src\validator\book_validation.py
from sqlmodel import SQLModel



class CreateBookRequest(SQLModel):
    title: str 
    author: str
    price: int
    condition: str
    is_sold: bool 
    user_id: int