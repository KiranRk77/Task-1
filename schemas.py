from typing import Optional
from pydantic import BaseModel

class AddressBase(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class AddressCreate(AddressBase):
    street: str
    city: str
    state: str
    zip: str
    latitude: float
    longitude: float

class AddressUpdate(AddressBase):
    pass

class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
