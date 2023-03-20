from app.database.models.car import CarModel
from app.schemas.base import BaseModelSchema


class CarSchema(BaseModelSchema):
    class Meta(BaseModelSchema.Meta):
        model = CarModel
        include_fk = True
        allow_none = True

        load_only = ("engine_id", "created_at", "updated_at")
        dump_only = ("id", "created_at", "updated_at")
