def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                u"Please correct {0}".format(getattr(form, field).label.text).lower(),
                "warning")

from flask import render_template, url_for
from flask.ext.login import login_required, current_user
from functools import wraps
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin():
            return render_template('404.html'), 404
        return f(*args, **kwargs)
    return decorated_function
