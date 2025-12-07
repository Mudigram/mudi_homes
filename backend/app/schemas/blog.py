from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BlogBase(BaseModel):
    title: str = Field(..., max_length=255)
    slug: str = Field(..., max_length=255)
    excerpt: Optional[str] = None
    content: str
    author: Optional[str] = None
    published: Optional[bool] = False

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str]
    slug: Optional[str]
    excerpt: Optional[str]
    content: Optional[str]
    author: Optional[str]
    published: Optional[bool]

class BlogOut(BlogBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class PaginatedBlogs(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[BlogOut]
