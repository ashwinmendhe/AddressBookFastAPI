from sqlalchemy.orm import Session
from math import radians, cos, sin, asin, sqrt
from .logger import logger
from .models import Address
from .schemas import  AddressCreate, AddressUpdate, AddressResponse


def create_address(db: Session, address: AddressCreate):
    new_address = Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    logger.info(f"Created new address with ID : {new_address.id}, Name: {new_address.name}")
    return new_address

def get_addresses(db: Session, address_id:int):
    return db.query(Address).filter(Address.id==address_id).first()

def get_all_adresses(db: Session):
    return db.query(Address).all()


def update_new_address(db: Session, address_id:int, update_address: AddressUpdate):
    db_address = get_addresses(db, address_id)
    if not db_address:
        return None
    else:
        for key, value in update_address.dict().items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
        return db_address


def delete_address(db: Session, address_id: int):
    address = get_addresses(db, address_id)
    if not address:
        return None
    db.delete(address)
    db.commit()
    return f"address deleted ID: {address.id}"

# # --- Distance-based retrieval ---
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2-lat1, lon2-lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 2 * R * asin(sqrt(a))

def get_addresses_within_radius(db: Session, center_lat: float, center_lon: float, radius_km: float):
    all_addresses = db.query(Address).all()
    return [
        addr for addr in all_addresses
        if haversine_distance(center_lat, center_lon, addr.latitude, addr.longitude) <= radius_km
    ]