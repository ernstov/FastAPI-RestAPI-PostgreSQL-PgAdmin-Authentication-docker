from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Book(BaseModel):
    book_name: str
    author: str
    original_compl_date: str
    published_year: int