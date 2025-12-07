from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogUpdate
from typing import Optional, Tuple

def create_blog(db: Session, data: BlogCreate) -> Blog:
    blog = Blog(**data.dict())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_blog(db: Session, blog_id: int) -> Optional[Blog]:
    return db.query(Blog).filter(Blog.id == blog_id).first()

def get_blog_by_slug(db: Session, slug: str) -> Optional[Blog]:
    return db.query(Blog).filter(Blog.slug == slug).first()

def update_blog(db: Session, blog_id: int, data: BlogUpdate) -> Optional[Blog]:
    blog = get_blog(db, blog_id)
    if not blog:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(blog, field, value)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(db: Session, blog_id: int) -> bool:
    blog = get_blog(db, blog_id)
    if not blog:
        return False
    db.delete(blog)
    db.commit()
    return True

def list_blogs(db: Session, search: Optional[str], page: int = 1, page_size: int = 10) -> Tuple[int, list[Blog]]:
    query = db.query(Blog)
    if search:
        like = f"%{search}%"
        query = query.filter((Blog.title.ilike(like)) | (Blog.content.ilike(like)) | (Blog.excerpt.ilike(like)))
    total = query.count()
    items = query.order_by(Blog.created_at.desc()).offset((page-1)*page_size).limit(page_size).all()
    return total, items
