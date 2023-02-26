from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.schemas.user import UserSchema
from app.daos.user import user_dao

from app.helpers.localization import gettext

user_bp = Blueprint("user", __name__)
user_schema = UserSchema()


@user_bp.route("/", methods=["POST"])
def create_user():
    user_json = request.get_json()
    is_available = user_dao.check_email_available(user_json['email'])

    if is_available:
        user = user_schema.load(user_json)

        created_user = user_dao.create_user(user)
        return user_schema.dump(created_user), 201
    else:
        return gettext('user_exists'), 403


@user_bp.route("/all", methods=["GET"])
@jwt_required()
def get_all_users():
    users = user_dao.get_all()
    return user_schema.dump(users, many=True)
