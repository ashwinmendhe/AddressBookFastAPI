from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

@app.post("/addresses/", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

@app.get("/addresses/", response_model=List[schemas.AddressResponse])
def list_addresses(db: Session = Depends(get_db)):
    return crud.get_all_addresses(db)

@app.get("/addresses/{address_id}", response_model=schemas.AddressResponse)
def get_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    updated = crud.update_address(db, address_id, address)
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    success = crud.delete_address(db, address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}

@app.get("/addresses/nearby/", response_model=List[schemas.AddressResponse])
def get_nearby_addresses(lat: float, lon: float, radius_km: float, db: Session = Depends(get_db)):
    results = crud.get_addresses_within_radius(db, lat, lon, radius_km)
    return results
