from flask import session
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'Вы НЕ вошли в систему и не можете видеть содержимое этой страницы.'
    return wrapper
