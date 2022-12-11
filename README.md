# queens_authentication

A login application designed with security in mind. Demonstrating SHA-2 cryptographic hash functions and input validation, which can be used when preventing XSS, SQL Injection and other attacks, along with other security methods.

## First Step

Download the .zip file!

## Imported Libraries

In `auth.py`

```python
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db
```

in `__init__.py`

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
```

in `models.py`

```python
from flask_login import UserMixin
from . import db
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

There are three main packages required for this program to run:

- Flask
- Flask-Login: important for post authentication
- Flask-SQLAlchemy: user model and database interface.

To make the virtual environment is set up appropriately use this command:

```bash
$ python -m venv auth
```

then:

```bash
$ source auth/bin/activate
```

```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-login
```

## Usage

To use the app the flask environment must have instructions on how to load the program.
With the auth bin activated, type this into command:

```bash
(auth)$ export FLASK_APP=project
(auth)$ export FLASK_DEBUG=1
```

This will direct the flask environment to load the program directory.

Following this, to run the program, enter the following:

```bash
(auth)$ flask run
```

## App Notes

- Navigate to http://127.0.0.1:5000/signup and put in a email, name, and password (Hashed in the database)
- It should auto redirect to the `/login` url
- Put in your email/password and you will be redirected to the /profile url (This is a protected URL that can only be accessed after login)

## Connecting to the database and pulling the data

- Install SQLite3 CLI: apt install sqlite3
- cd into project directory
- Run sqlite3 application.db and it will open the sqlite terminal
- Run select \* from user;

## Supporting Documents

Please watch the video called `WatchMe.mp4` to see a video demo of this application working.
