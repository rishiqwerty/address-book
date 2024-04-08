from pydantic import BaseModel, validator


def validate_latitude(cls, value):
    if value <= -90 and value >= 90:
        raise ValueError("Invalid latitude, it should be in range of 90, -90")
    return value


def validate_longitude(cls, value):
    if value <= -180 and value >= 180:
        raise ValueError("Invalid longitude, it should be in range of 180, -180")
    return value


class AddressCreate(BaseModel):
    user_id: int
    address: str
    latitude: int
    longitude: int
    _validate_latitude = validator("latitude")(validate_latitude)
    _validate_longitude = validator("longitude")(validate_longitude)
