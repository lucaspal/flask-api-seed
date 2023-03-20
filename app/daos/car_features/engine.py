from app.daos.base import BaseDAO
from app.database.models.engine import EngineModel


class EngineDao(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def create_engine(self, engine):
        self.session.add(engine)
        self.session.commit()
        return engine


engine_dao = EngineDao(EngineModel)
