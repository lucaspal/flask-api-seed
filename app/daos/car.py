from app.daos.base import BaseDAO
from app.database.models.car import CarModel


class CarDao(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def get_cars(self):
        return self.session.query(self.model).all()

    def get_car_by_id(self, car_id) -> CarModel:
        return self.session.query(self.model).filter_by(id=car_id).first()

    def create_car(self, car):
        self.session.add(car)
        self.session.commit()
        return car

    def update_car(self, car):
        current_car = self.get_car_by_id(car.id)

        current_car.model = car.model
        current_car.location = car.location
        current_car.engine_id = car.engine_id
        current_car.infotainment_id = car.infotainment_id
        current_car.interior_id = car.interior_id

        self.session.commit()

        return current_car

    def delete_car(self, car):
        self.session.delete(car)
        self.session.commit()


car_dao = CarDao(CarModel)
