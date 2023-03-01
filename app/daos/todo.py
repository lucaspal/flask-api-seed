from app.daos.base import BaseDAO
from app.database.models.todo import TodoModel


class TodoDao(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def get_todos(self, user_id):
        # Get the user id from the token

        return self.session.query(self.model).filter_by(user_id=user_id).all()

    def get_todo_by_id(self, todo_id) -> TodoModel:
        return self.session.query(self.model).filter_by(id=todo_id).first()

    def create_todo(self, todo):
        self.session.add(todo)
        self.session.commit()
        return todo

    def update_todo(self, todo):
        # gets current todo by id
        current_todo = self.get_todo_by_id(todo.id)
        # updates current todo with new todo
        current_todo.title = todo.title
        current_todo.description = todo.description
        current_todo.completed = todo.completed
        # commits changes
        self.session.commit()
        return current_todo

    def delete_todo(self, todo):
        self.session.delete(todo)
        self.session.commit()


todo_dao = TodoDao(TodoModel)
