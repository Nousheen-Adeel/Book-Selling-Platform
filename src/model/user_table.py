# src\model\user_table.py
from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List




# User table model
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False)
    email: str = Field(nullable=False, unique=True)
    uni_name: str = Field(nullable=False)
    Phone_number: str = Field(nullable=False)
    
    # one user can have many books
    books: List["Book"] = Relationship(back_populates="owner")
    
    create_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))    

