from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Integer

from app.database.models.base import BaseModel


class InteriorModel(BaseModel):
    __tablename__ = "interiors"

    color = Column(String(100), nullable=False)
    material = Column(String(100), nullable=False)

    def __init__(self, color, material):
        self.color = color
        self.material = material

    def __repr__(self):
        return f"<Interior {self.color} with material {self.material} >"
