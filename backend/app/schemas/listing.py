from typing import List, Optional
from pydantic import BaseModel, Field

class ListingBase(BaseModel):
    title: str
    property_type: str
    location: str
    price: float
    status: str

    thumbnail: str
    images: Optional[List[str]] = None

    description: Optional[str] = None
    land_size: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None

    lease_length: Optional[str] = None
    agent_details: Optional[str] = None

    long: Optional[float] = None
    lat: Optional[float] = None

    features: Optional[List[str]] = None


class ListingCreate(ListingBase):
    slug: str = Field(..., description="Must be unique")

class ListingUpdate(BaseModel):
    title: Optional[str] = None
    property_type: Optional[str] = None
    location: Optional[str] = None
    price: Optional[float] = None
    status: Optional[str] = None

    thumbnail: Optional[str] = None
    images: Optional[List[str]] = None

    description: Optional[str] = None
    land_size: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None

    lease_length: Optional[str] = None
    agent_details: Optional[str] = None

    slug: Optional[str] = None  # allow slug update

    long: Optional[float] = None
    lat: Optional[float] = None

    features: Optional[List[str]] = None




class ListingResponse(ListingBase):
    id: int
    slug: str
    created_at: str
    updated_at: Optional[str]

    class Config:
        from_attributes = True
