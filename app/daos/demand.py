from app.daos.base import BaseDAO
from app.database.models.demand import DemandModel


class DemandDao(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def has_any_demand(self, user_id):
        return self.session.query(self.model).filter_by(user_id=user_id).count() > 0


demand_dao = DemandDao(DemandModel)
