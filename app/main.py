from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .database import engine, Base, get_db
from .schemas import AddressCreate, AddressResponse, AddressUpdate
from .crud import get_all_adresses, get_addresses, create_address, update_new_address, delete_address, get_addresses_within_radius

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")


@app.post("/addresses/", response_model=AddressResponse)
def create_new_address(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, address)


@app.get("/addresses/",response_model = List[AddressResponse])
def list_addresses(db: Session = Depends(get_db)):
    return get_all_adresses(db)

@app.get("/addresses/{address_id}", response_model=AddressResponse)
def get_address(address_id:int, db: Session = Depends(get_db)):
    db_address = get_addresses(db, address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address id not found in db")
    else:
        return db_address


@app.put("/addresses/{address_id}", response_model=AddressResponse)
def update_addressDB(address_id: int, update_address: AddressUpdate, db: Session=Depends(get_db)):
    updated = update_new_address(db, address_id, update_address)
    if updated is not None:
        return updated
    else:
        raise HTTPException(status_code=404, detail="Address id not found in db")


@app.delete("/addresses/{address_id}")
def delete_add(address_id:int, db: Session = Depends(get_db)):
    result = delete_address(db, address_id)
    if result is not None:
        return result
    else:
        raise HTTPException(status_code=404, detail="Address id not found in db")



@app.get("/addresses/nearby/", response_model=List[AddressResponse])
def get_nearby_addresses(lat: float, lon:float, radius_km: float, db: Session = Depends(get_db)):
    results = get_addresses_within_radius(db, lat, lon, radius_km)
    return results