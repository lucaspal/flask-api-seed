from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.exceptions import abort

from app.daos.base import BaseDAO
from app.database.models.user import UserModel
from app.helpers.localization import gettext
from app.daos.demand import demand_dao


class UserDAO(BaseDAO):
    def __init__(self, model):
        super().__init__(model)

    def authenticate(self, creds):
        user = self._find_by_email(creds["email"])

        if user and user.is_correct_password(creds["password"]):
            access_token = create_access_token(identity=user.email)
            return user, access_token

        abort(401, {"message": gettext("wrong_credentials")})

    def create_user(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def delete_user(self, user):
        has_demands = demand_dao.has_any_demand(user.id)

        if has_demands:
            Exception(400, {"message": gettext("user_has_demands")})
        else:
            self.session.delete(user)
            self.session.commit()

    def check_email_available(self, _email):
        return self.session.query(self.model).filter_by(email=_email).count() == 0

    def get_current_user(self):
        email = get_jwt_identity()
        return self._find_by_email(email)

    def _find_by_email(self, _email):
        return self.session.query(self.model).filter_by(email=_email).first()


user_dao = UserDAO(UserModel)
