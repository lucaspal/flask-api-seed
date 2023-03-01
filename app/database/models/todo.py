from app.database.models.base import BaseModel
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, String, Boolean, Integer


class TodoModel(BaseModel):
    __tablename__ = "todo"

    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    completed = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, completed, user_id):
        self.title = title
        self.description = description
        self.completed = completed
        self.user_id = user_id

    def __repr__(self):
        return f"<Todo {self.title} for user with id: {self.user_id} >"

    @classmethod
    def find_by_title(cls, title: str):
        return cls.query.filter_by(title=title).first()
