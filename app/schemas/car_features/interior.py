from app.database.models.interior import InteriorModel
from app.schemas.base import BaseModelSchema


class InteriorSchema(BaseModelSchema):
    class Meta(BaseModelSchema.Meta):
        model = InteriorModel
        include_fk = True

        # load_only = ()
        # dump_only = ()
