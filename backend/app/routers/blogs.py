from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.blog import BlogCreate, BlogOut, BlogUpdate, PaginatedBlogs
from app.services.blog_service import create_blog, get_blog, update_blog, delete_blog, list_blogs, get_blog_by_slug

router = APIRouter(prefix="/blogs", tags=["blogs"])

# Public: list with search + pagination
@router.get("/", response_model=PaginatedBlogs)
def read_blogs(
    search: str | None = Query(None, description="search term"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    total, items = list_blogs(db, search, page, page_size)
    return {"total": total, "page": page, "page_size": page_size, "items": items}

# Public: get by id
@router.get("/{blog_id}", response_model=BlogOut)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

# Public: get by slug
@router.get("/slug/{slug}", response_model=BlogOut)
def read_blog_by_slug(slug: str, db: Session = Depends(get_db)):
    blog = get_blog_by_slug(db, slug)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

# Admin: create (protect with auth dependency later)
@router.post("/", response_model=BlogOut, status_code=status.HTTP_201_CREATED)
def create_blog_endpoint(payload: BlogCreate, db: Session = Depends(get_db)):
    # TODO: require admin (Depends(get_current_user))
    # check for slug uniqueness
    existing = get_blog_by_slug(db, payload.slug)
    if existing:
        raise HTTPException(status_code=400, detail="Slug already exists")
    blog = create_blog(db, payload)
    return blog

# Admin: update
@router.put("/{blog_id}", response_model=BlogOut)
def update_blog_endpoint(blog_id: int, payload: BlogUpdate, db: Session = Depends(get_db)):
    # TODO: require admin
    blog = update_blog(db, blog_id, payload)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

# Admin: delete
@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_endpoint(blog_id: int, db: Session = Depends(get_db)):
    # TODO: require admin
    ok = delete_blog(db, blog_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Blog not found")
    return None
