# src\utils\api_response.py
from sqlmodel import SQLModel
from src.model.book_table import Book
from src.model.user_table import User



class UserResponse(SQLModel):
    status: str = "success"
    message: str = ""
    user: User



class BookResponse(SQLModel):
    status: str = "success"
    message: str = ""
    book: list[Book] = []

