from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.listings import Listing
from app.schemas.listing import ListingCreate, ListingUpdate
from typing import Optional, List


def create_listing(db: Session, data: ListingCreate) -> Listing:
    listing = Listing(**data.dict())

    try:
        db.add(listing)
        db.commit()
        db.refresh(listing)
        return listing
    except IntegrityError:
        db.rollback()
        raise ValueError("Slug already exists. Slug must be unique.")


def get_listing(db: Session, listing_id: int) -> Optional[Listing]:
    return db.query(Listing).filter(Listing.id == listing_id).first()


def get_listing_by_slug(db: Session, slug: str) -> Optional[Listing]:
    return db.query(Listing).filter(Listing.slug == slug).first()


def delete_listing(db: Session, listing_id: int) -> bool:
    listing = get_listing(db, listing_id)
    if not listing:
        return False

    db.delete(listing)
    db.commit()
    return True


def update_listing(db: Session, listing_id: int, data: ListingUpdate) -> Optional[Listing]:
    listing = get_listing(db, listing_id)
    if not listing:
        return None

    for field, value in data.dict(exclude_unset=True).items():
        setattr(listing, field, value)

    try:
        db.commit()
        db.refresh(listing)
        return listing
    except IntegrityError:
        db.rollback()
        raise ValueError("Slug already exists. Slug must be unique.")
