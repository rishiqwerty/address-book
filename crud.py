from sqlalchemy.orm import Session

import models, schemas
from haversine import haversine


def get_address(
    db: Session, search_latitude: float, search_longitude: float, distance_in_kms: float
):
    input_cord = (search_latitude, search_longitude)
    address_list = []
    address_model = db.query(models.Address).all()
    if address_model:
        for i in address_model:
            add_cor = (i.latitude, i.longitude)
            print(add_cor)
            # if the input cordinates and the cordinates in of address in db is within the distance input by user
            if haversine(input_cord, add_cor) <= distance_in_kms:
                address_list.append(i)
        if address_list:
            return address_list

        else:
            print(
                f"No data found input cordinates was --> {input_cord}, distance --> {distance_in_kms}"
            )
            return []
    else:
        return []


def create_address(db: Session, address: schemas.AddressCreate):
    """
    New Address entry in database
    """
    db_address = models.Address(
        user_id=address.user_id,
        address=address.address,
        latitude=address.latitude,
        longitude=address.longitude,
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def update_address(db: Session, address_id: int, address_update: schemas.AddressCreate):
    address_model = (
        db.query(models.Address).filter(models.Address.id == address_id).first()
    )
    if address_model:
        address_model.user_id = address_update.user_id
        address_model.address = address_update.address
        address_model.latitude = address_update.latitude
        address_model.longitude = address_update.longitude

        db.add(address_model)
        db.commit()
        db.refresh(address_model)
        return address_model


def delete_address(db: Session, address_id: int):
    address_model = (
        db.query(models.Address).filter(models.Address.id == address_id).first()
    )
    if address_model:
        db.query(models.Address).filter(models.Address.id == address_id).delete()
        db.commit()
        return f"id: {address_id} deleted"

    else:
        return f"id: {address_id} not present"
