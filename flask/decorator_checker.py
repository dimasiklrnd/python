from flask import session, render_template
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return render_template('viewlog.html',
                                the_title='Вы НЕ вошли в систему и не можете видеть содержимое этой страницы.',
                                the_row_titles=(),
                                the_data=(),)
    return wrapper
