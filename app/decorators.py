from functools import wraps
from flask import abort
from flask_login import current_user

def permission_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_role(role):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required('admin')(f)

def bartender_required(f):
    return permission_required('bartender')(f)
