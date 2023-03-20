from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.schemas.car_features.engine import EngineSchema
from app.schemas.car_features.infotainment import InfotainmentSchema
from app.schemas.car_features.interior import InteriorSchema
from app.daos.car_features.engine import engine_dao
from app.daos.car_features.infotainment import infotainment_dao
from app.daos.car_features.interior import interior_dao

from app.helpers.localization import gettext

car_features_bp = Blueprint("car-features", __name__)
engine_schema = EngineSchema()
infotainment_schema = InfotainmentSchema()
interior_schema = InteriorSchema()


@car_features_bp.route("/engine", methods=["POST"])
@jwt_required()
def create_engine():
    engine_json = request.get_json()
    engine = engine_schema.load(engine_json)

    created_engine = engine_dao.create_engine(engine)
    return engine_schema.dump(created_engine), 201


@car_features_bp.route("/infotainment", methods=["POST"])
@jwt_required()
def create_infotainment():
    infotainment_json = request.get_json()
    infotainment = infotainment_schema.load(infotainment_json)

    created_infotainment = infotainment_dao.create_infotainment(infotainment)
    return infotainment_schema.dump(created_infotainment), 201


@car_features_bp.route("/interior", methods=["POST"])
@jwt_required()
def create_interior():
    interior_json = request.get_json()
    interior = interior_schema.load(interior_json)

    created_interior = interior_dao.create_interior(interior)
    return interior_schema.dump(created_interior), 201
