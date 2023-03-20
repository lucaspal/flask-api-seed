from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Integer

from app.database.models.base import BaseModel


class EngineModel(BaseModel):
    __tablename__ = "engines"

    power = Column(Integer, nullable=False)
    engine_type = Column(String(100), nullable=False)
    weight = Column(Integer, nullable=False)

    def __init__(self, power, engine_type, weight):
        self.power = power
        self.engine_type = engine_type
        self.weight = weight

    def __repr__(self):
        return f"<Engine {self.engine_type} with power {self.power} >"
