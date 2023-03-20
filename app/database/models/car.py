from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Integer

from app.database.models.base import BaseModel

from app.database.models.infotainment import InfotainmentModel
from app.database.models.interior import InteriorModel


class CarModel(BaseModel):
    __tablename__ = "cars"

    model = Column(String(100), nullable=False)
    location = Column(Integer, nullable=False)
    engine_id = Column(Integer, ForeignKey('engines.id'), nullable=False)
    infotainment_id = Column(Integer, ForeignKey('infotainments.id'), nullable=True)
    interior_id = Column(Integer, ForeignKey('interiors.id'), nullable=True)

    def __init__(self, model, location, engine_id, infotainment_id, interior_id):
        self.model = model
        self.location = location
        self.engine_id = engine_id
        self.infotainment_id = infotainment_id
        self.interior_id = interior_id

    def __repr__(self):
        return f"<Car {self.model} at location {self.location} >"

    @classmethod
    def find_by_model(cls, model: str):
        return cls.query.filter_by(model=model).first()
