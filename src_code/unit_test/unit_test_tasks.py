class AuthorizationError(Exception):
    pass


def access_resource(role):
    if role != "admin":
        raise AuthorizationError("Access denied")
    return "Access granted"
