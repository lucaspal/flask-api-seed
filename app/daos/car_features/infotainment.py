from app.daos.base import BaseDAO
from app.database.models.infotainment import InfotainmentModel


class InfotainmentDao(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def create_infotainment(self, infotainment):
        self.session.add(infotainment)
        self.session.commit()
        return infotainment


infotainment_dao = InfotainmentDao(InfotainmentModel)
