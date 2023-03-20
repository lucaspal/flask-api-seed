from app.database.models.infotainment import InfotainmentModel
from app.schemas.base import BaseModelSchema


class InfotainmentSchema(BaseModelSchema):
    class Meta(BaseModelSchema.Meta):
        model = InfotainmentModel
        include_fk = True

        # load_only = ()
        # dump_only = ()
