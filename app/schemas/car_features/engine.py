from app.database.models.engine import EngineModel
from app.schemas.base import BaseModelSchema


class EngineSchema(BaseModelSchema):
    class Meta(BaseModelSchema.Meta):
        model = EngineModel
        include_fk = True

        # load_only = ()
        # dump_only = ()
