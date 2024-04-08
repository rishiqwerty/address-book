from sqlalchemy import Column, CheckConstraint, Integer, String, Float

from database import Base

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    address = Column(String(100))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint('latitude >= -90 AND latitude <= 90'),
        CheckConstraint('longitude <= 180 AND longitude >= -180')
    )
