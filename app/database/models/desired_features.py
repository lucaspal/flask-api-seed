from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Integer

from app.database.models.base import BaseModel


class DesiredFeaturesModel(BaseModel):
    __tablename__ = "desired_features"

    interior_color = Column(String(100), nullable=False)
    wireless_infotainment = Column(Integer, nullable=False)
    engine_power = Column(Integer, nullable=False)
    demand_id = Column(Integer, ForeignKey('demands.id'), nullable=False)

    def __init__(self, interior_color, wireless_infotainment, engine_power, demand_id):
        self.interior_color = interior_color
        self.wireless_infotainment = wireless_infotainment
        self.engine_power = engine_power
        self.demand_id = demand_id

    def __repr__(self):
        return f"<DesiredFeatures {self.interior_color} with wireless infotainment {self.wireless_infotainment} >"
