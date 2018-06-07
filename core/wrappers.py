from flask import g, redirect, request, url_for
from functools import wraps


def authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('user.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def guest(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is not None:
            return redirect(url_for('site.index'))
        return f(*args, **kwargs)
    return decorated_function