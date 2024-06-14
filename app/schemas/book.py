from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    is_available: bool

    class Config:
        orm_mode = True
