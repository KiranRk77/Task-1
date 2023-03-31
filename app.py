from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import SessionLocal, engine

app = FastAPI()


# Dependency to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, 
                   db: Session = Depends(get_db)
                   ):

    '''
    create new address object 
    add data of street, latitude, longitude, city, state, zip
    '''

    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address



@app.get("/addresses/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, 
                 db: Session = Depends(get_db)
                 ):
    
    '''
    Get addresses by id 
    '''
    db_address = db.query(models.Address)\
                    .filter(models.Address.id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


# Update an address
@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, 
                   address: schemas.AddressUpdate, 
                   db: Session = Depends(get_db)
                   ):
    db_address = db.query(models.Address)\
        .filter(models.Address.id == address_id)\
        .first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    for attr, value in address.dict(exclude_unset=True).items():
        setattr(db_address, attr, value)
    db.commit()
    db.refresh(db_address)
    return db_address


# Delete an address
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, 
                   db: Session = Depends(get_db)
                   ):
    
    db_address = db.query(models.Address)\
                    .filter(models.Address.id == address_id)\
                    .first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()
    return {"message": "Address deleted successfully"}


# Get all addresses
@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses(skip: int = 0, 
                   limit: int = 100, 
                   db: Session = Depends(get_db)
                   ):
    addresses = db.query(models.Address)\
                .offset(skip).limit(limit)\
                .all()
    return addresses


# Get addresses within a given distance and location
@app.get("/addresses/nearby/", response_model=List[schemas.Address])
def read_nearby_addresses(latitude: float, 
                          longitude: float, 
                          distance: float = 10, 
                          db: Session = Depends(get_db)
                          ):
    addresses = db.query(models.Address).filter(
        models.Address.latitude <= latitude + distance,
        models.Address.latitude >= latitude - distance,
        models.Address.longitude <= longitude + distance,
        models.Address.longitude >= longitude - distance)\
        .all()
    return addresses
