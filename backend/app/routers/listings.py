from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.listings import Listing
from app.schemas.listing import ListingCreate, ListingUpdate, ListingResponse
from app.services.listing_service import (
    create_listing,
    get_listing,
    get_listing_by_slug,
    update_listing,
    delete_listing
)

router = APIRouter(prefix="/listings", tags=["listings"])

# ---------------------
# PUBLIC ROUTES
# ---------------------

@router.get("/", response_model=list[ListingResponse])
def fetch_all_listings(
    db: Session = Depends(get_db),
    location: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    bedrooms: int | None = None,
    bathrooms: int | None = None,
    property_type: str | None = None,
    
    # Pagination
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
):
    query = db.query(Listing)

    # ---- filters ----
    if location:
        query = query.filter(Listing.location.ilike(f"%{location}%"))

    if min_price:
        query = query.filter(Listing.price >= min_price)

    if max_price:
        query = query.filter(Listing.price <= max_price)

    if bedrooms:
        query = query.filter(Listing.bedrooms == bedrooms)

    if bathrooms:
        query = query.filter(Listing.bathrooms == bathrooms)

    if property_type:
        query = query.filter(Listing.property_type.ilike(f"%{property_type}%"))

    # ---- pagination ----
    skip = (page - 1) * page_size
    results = query.offset(skip).limit(page_size).all()

    return results



@router.get("/slug/{slug}", response_model=ListingResponse)
def fetch_listing_by_slug(slug: str, db: Session = Depends(get_db)):
    listing = get_listing_by_slug(db, slug)
    if not listing:
        raise HTTPException(404, "Listing not found")
    return listing


# ---------------------
# ADMIN / INTERNAL ROUTES
# ---------------------

@router.post("/", response_model=ListingResponse, status_code=status.HTTP_201_CREATED)
def create_new_listing(data: ListingCreate, db: Session = Depends(get_db)):
    return create_listing(db, data)


@router.get("/id/{listing_id}", response_model=ListingResponse)
def fetch_listing_by_id(listing_id: int, db: Session = Depends(get_db)):
    listing = get_listing(db, listing_id)
    if not listing:
        raise HTTPException(404, "Listing not found")
    return listing


@router.put("/id/{listing_id}", response_model=ListingResponse)
def update_existing_listing(listing_id: int, data: ListingUpdate, db: Session = Depends(get_db)):
    updated = update_listing(db, listing_id, data)
    if not updated:
        raise HTTPException(404, "Listing not found")
    return updated


@router.delete("/id/{listing_id}", status_code=204)
def delete_existing_listing(listing_id: int, db: Session = Depends(get_db)):
    success = delete_listing(db, listing_id)
    if not success:
        raise HTTPException(404, "Listing not found")
