from app.daos.base import BaseDAO
from app.database.models.interior import InteriorModel


class InteriorDao(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def create_interior(self, interior):
        self.session.add(interior)
        self.session.commit()
        return interior


interior_dao = InteriorDao(InteriorModel)
