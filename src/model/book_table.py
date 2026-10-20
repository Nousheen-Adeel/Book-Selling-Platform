# src\model\book_table.py
from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional



# Book table model
class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, nullable=False)
    author: str = Field(nullable=False)
    price: int = Field(nullable=False)
    condition: str = Field(nullable=False)
    is_sold: bool = Field(default=False)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    owner: Optional["User"] = Relationship(back_populates="books")

    create_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))    


