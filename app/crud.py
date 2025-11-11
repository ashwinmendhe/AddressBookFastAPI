from sqlalchemy.orm import Session
from . import models, schemas
from math import radians, cos, sin, asin, sqrt
from .logger import logger


def create_address(db:Session, address: schemas.AddressCreate):
    new_address = models.Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    logger.info(f"Created new address (ID: {new_address.id}, Name: {new_address.name})")
    return new_address


def get_address(db: Session, address_id:int):
    return db.query(models.Address).filter(models.Address.id==address_id).first()

def get_all_addresses(db: Session):
    return db.query(models.Address).all()

def update_address(db: Session, address_id:int, new_data: schemas.AddressUpdate):
    address = get_address(db, address_id)
    if not address:
        return None
    for key , value in new_data.dict().items():
        setattr(address, key, value)
    db.commit()
    db.refresh(address)

def delete_address(db: Session, address_id: int):
    address = get_address(db, address_id)
    if not address:
        return False
    db.delete(address)
    db.commit()
    return True

# --- Distance-based retrieval ---
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 2 * R * asin(sqrt(a))

def get_addresses_within_radius(db: Session, center_lat: float, center_lon: float, radius_km: float):
    all_addresses = db.query(models.Address).all()
    return [
        addr for addr in all_addresses
        if haversine_distance(center_lat, center_lon, addr.latitude, addr.longitude) <= radius_km
    ]

