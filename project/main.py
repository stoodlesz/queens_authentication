from flask import Blueprint, render_template
from flask_login import login_required, current_user

# A blueprint is an object that allows defining application functions without requiring an application object ahead of
# time. It uses the same decorators as ~flask.Flask, but defers the need for an application by recording them for later
# registration.
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')  # Render a template by name with the given context


@main.route('/profile')
@login_required  # this will ensure that the current user is logged in and authenticated before calling the actual view.
def profile():
    return render_template('profile.html', name=current_user.name)
