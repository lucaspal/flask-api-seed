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


# params: id (int)
@todo_bp.route("/<int:todo_id>", methods=["GET"])
@jwt_required()
def get_todo_by_id(todo_id: int):
    # gets the id from the url
    todo = todo_dao.get_todo_by_id(todo_id)
    # return the todo
    return todo_schema.dump(todo), 200


# params: id (int)
# query params: completed (bool)
@todo_bp.route("/<int:todo_id>", methods=["PUT"])
@jwt_required()
def mark_todo_as_done(todo_id: int):
    # gets the completed value from the query params
    completed_argument = request.args.get("completed", default=False, type=lambda v: v.lower() == 'true')

    if completed_argument is not None and type(completed_argument) == bool:
        # gets the id from the url
        todo = todo_dao.get_todo_by_id(todo_id)
        todo.completed = completed_argument
        todo_dao.update_todo(todo)
        return todo_schema.dump(todo), 200
    else:
        # Returns error saying that either the completed argument is missing or it is not a boolean
        return {"error": "Missing or invalid completed argument"}, 400
