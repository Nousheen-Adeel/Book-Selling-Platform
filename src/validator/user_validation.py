# src\validator\user_validation.py
from sqlmodel import SQLModel



class CreateUserRequest(SQLModel):
    username: str
    email: str
    uni_name: str
    Phone_number: str