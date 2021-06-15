from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from response import CustomResponse


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_admin"]:
                return fn(*args, **kwargs)
            else:
                return CustomResponse.error("Admin authorization needed!")

        return decorator
    return wrapper