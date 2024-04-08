from fastapi import FastAPI, Depends
import models
from typing import List
from database import engine, get_db
import crud
from sqlalchemy.orm import Session
from haversine import haversine
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get(
    "/get-address",
    response_model=List[schemas.AddressCreate],
    summary="Search address in database",
    status_code=200,
)
async def search_address(
    search_latitude: float,
    search_longitude: float,
    distance_in_kms: float,
    db: Session = Depends(get_db),
):
    """
    This is for searching the address based on latitude, longitude and
    distance entered by user.
    """
    print(
        crud.get_address(
            db=db,
            search_latitude=search_latitude,
            search_longitude=search_longitude,
            distance_in_kms=distance_in_kms,
        )
    )
    return crud.get_address(
        db=db,
        search_latitude=search_latitude,
        search_longitude=search_longitude,
        distance_in_kms=distance_in_kms,
    )


@app.post("/create", response_model=schemas.AddressCreate, status_code=201)
async def create_address(
    address: schemas.AddressCreate,
    db: Session = Depends(get_db),
):
    """
    This is for adding new address data
    """
    return crud.create_address(db=db, address=address)


@app.put("/{address_id}", response_model=schemas.AddressCreate, status_code=201)
async def update_address(
    address_id: int,
    address_update: schemas.AddressCreate,
    db: Session = Depends(get_db),
):
    """
    This is for updating the address data based on address_id
    """
    return crud.update_address(
        db=db, address_id=address_id, address_update=address_update
    )


@app.delete("/{address_id}")
async def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    This is for deleting the data based on address ids
    """
    crud.delete_address(db=db, address_id=address_id)


@app.get(
    "/get-all-addresses", response_model=List[schemas.AddressCreate], status_code=200
)
async def all_address(db: Session = Depends(get_db)):
    """
    This is for getting data of all the addresses
    """
    return db.query(models.Address).all()
