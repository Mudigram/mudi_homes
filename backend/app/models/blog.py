from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func, Boolean
from app.database import Base

class Blog(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), nullable=False, unique=True, index=True)
    excerpt = Column(String(500), nullable=True)
    content = Column(Text, nullable=False)
    author = Column(String(100), nullable=True)
    published = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
