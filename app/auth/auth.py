from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from .manager import get_user_manager
from .models import User
from ..config import SECRET
from fastapi_users import FastAPIUsers

cookie_transport = CookieTransport(cookie_name="ordercourier",cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)