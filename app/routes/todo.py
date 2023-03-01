import json

from flask import Blueprint, request

from flask_jwt_extended import jwt_required, get_jwt_identity
from app.daos.todo import todo_dao
from app.daos.user import user_dao
from app.schemas.todo import TodoSchema
from marshmallow import EXCLUDE

todo_bp = Blueprint("todo", __name__)
todo_schema = TodoSchema()


@todo_bp.route("/all", methods=["GET"])
@jwt_required()
def get_todos():
    user = user_dao.get_current_user()
    todos = todo_dao.get_todos(user.id)
    dumps = todo_schema.dumps(todos, many=True)
    return dumps, 200


# Method to create a new todo
@todo_bp.route("/create", methods=["POST"])
@jwt_required()
def create_todo():
    todo_json = request.get_json()

    user = user_dao.get_current_user()
    todo_json["user_id"] = user.id

    todo = todo_schema.load(todo_json)

    created_todo = todo_dao.create_todo(todo)
    return todo_schema.dump(created_todo), 201
