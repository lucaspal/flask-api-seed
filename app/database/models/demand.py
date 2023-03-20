from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Integer

from app.database.models.base import BaseModel


class DemandModel(BaseModel):
    __tablename__ = "demands"

    pick_up_date = Column(Date, nullable=False)
    drop_off_location = Column(Integer, nullable=False)
    earliest_pick_up_time = Column(Integer, nullable=False)
    latest_drop_off_time = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, pick_up_date, drop_off_location, earliest_pick_up_time, latest_drop_off_time):
        self.pick_up_date = pick_up_date
        self.drop_off_location = drop_off_location
        self.earliest_pick_up_time = earliest_pick_up_time
        self.latest_drop_off_time = latest_drop_off_time

    def __repr__(self):
        return f"<Demand {self.pick_up_date} at location {self.drop_off_location} for user with id {self.user_id} >"
