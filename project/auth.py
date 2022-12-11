from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

# Represents a blueprint, a collection of routes and other app-related functions that can be registered on a real
# application later. A blueprint is an object that allows defining application functions without requiring an
# application object ahead of time. It uses the same decorators as ~flask.Flask, but defers the need for an
# application by recording them for later registration.
auth = Blueprint('auth', __name__)
app = Flask(__name__)

@auth.route('/login')
def login():
    return render_template('login.html')

# Decorate a view function to register it with the given URL rule and options. Calls add_url_rule,
# which has more details about the implementation.
@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

#input validation

    # template_name_or_list – The name of the template to render. If a list is given, the first name to exist will be
    # rendered. context – The variables to make available in the template.
    if not email:
        flash('Email is required')
        return render_template('login.html', emailRequired="is-danger")

    if not password:
        flash('Password is required')
        return render_template('login.html', passwordRequired="is-danger")

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password): # Check a password against a given salted and hashed password value.
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    password = request.form.get('password')
    email = request.form.get('email')
    name = request.form.get('name')
# input validation
    app.logger.info('%s Email supplied', email)

    if not email:
        flash('Email is required')
        return render_template('signup.html', emailRequired="is-danger")

    if not  name:
        flash('Name is required')
        return render_template('signup.html', nameRequired="is-danger")

    if not password:
        flash('Password is required')
        return render_template('signup.html', passwordRequired="is-danger")
    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database


    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))
