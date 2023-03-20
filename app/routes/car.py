from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.schemas.car import CarSchema
from app.daos.car import car_dao

from app.helpers.localization import gettext

car_bp = Blueprint("car", __name__)
car_schema = CarSchema()


@car_bp.route("/", methods=["POST"])
def create_car():
    car_json = request.get_json()

    # if there is no infotainment_id key add None
    if "infotainment_id" not in car_json:
        car_json["infotainment_id"] = None
    if "interior_id" not in car_json:
        car_json["interior_id"] = None

    car = car_schema.load(car_json)
    created_car = car_dao.create_car(car)
    return car_schema.dump(created_car), 201


@car_bp.route("/<int:car_id>", methods=["DELETE"])
@jwt_required()
def delete_user(car_id: int):
    car = car_dao.get_by_id(car_id)
    car_dao.delete_car(car)
    return gettext("car_deleted"), 200


# update car location
@car_bp.route("/<int:car_id>", methods=["PUT"])
@jwt_required()
def update_car_location(car_id: int):
    car_json = request.get_json()
    car = car_dao.get_by_id(car_id)
    car.location = car_json['location']
    car_dao.update_car(car)
    return car_schema.dump(car), 200


@car_bp.route("/all", methods=["GET"])
@jwt_required()
def get_all_cars():
    cars = car_dao.get_all()
    return car_schema.dump(cars, many=True)
