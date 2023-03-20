from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Integer

from app.database.models.base import BaseModel


class InfotainmentModel(BaseModel):
    __tablename__ = "infotainments"

    operating_system = Column(String(100), nullable=False)
    brand = Column(String(100), nullable=False)
    is_wireless = Column(Integer, nullable=False)

    def __init__(self, operating_system, brand, is_wireless):
        self.operating_system = operating_system
        self.brand = brand
        self.is_wireless = is_wireless

    def __repr__(self):
        return f"<Infotainment {self.operating_system} with brand {self.brand} >"
