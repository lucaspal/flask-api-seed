from app.database.models.todo import TodoModel
from app.schemas.base import BaseModelSchema


class TodoSchema(BaseModelSchema):
    class Meta(BaseModelSchema.Meta):
        model = TodoModel
        include_fk = True

        load_only = ("user_id", "created_at", "updated_at")
        dump_only = ("id", "created_at", "updated_at", "user_id")
