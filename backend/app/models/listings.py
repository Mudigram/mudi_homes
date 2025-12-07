from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Info
    title = Column(String, nullable=False, index=True)
    slug = Column(String, nullable=False, unique=True, index=True)

    property_type = Column(String, nullable=False, index=True)  # e.g., "apartment", "land", "duplex"

    location = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False, index=True)  # e.g., "available", "sold"

    # Media
    thumbnail = Column(String, nullable=False)  # URL string, not integer
    images = Column(ARRAY(String), nullable=True)  # array of image URLs

    # Details
    lease_length = Column(String, nullable=True)
    agent_details = Column(Text, nullable=True)

    # Map Coordinates
    long = Column(Float, nullable=True)
    lat = Column(Float, nullable=True)

    # Features list (ARRAY example)
    features = Column(ARRAY(String), nullable=True)

    description = Column(Text, nullable=True)
    land_size = Column(String, nullable=True)  # e.g. "600sqm", "1 plot"
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)

    # Timestamp fields
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
