#from datetime import datetime
from flask import Blueprint, render_template, flash, redirect, request, url_for, abort, Flask, current_app
from flask_login import current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.urls import url_parse
from sqlalchemy import and_
#from app import create_db as db
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd
import csv
import os
import datetime
from flask_mail import Message
from app.extensions import db, mail
from app.forms import SubscriptionForm
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple



server_bp = Blueprint('main', __name__)
from app.models import Subscriber


@server_bp.route('/', methods=['GET', 'POST'])
def index():
    form = SubscriptionForm()
    if form.validate_on_submit():
        new_subscriber = Subscriber(first_name=form.first_name.data, email=form.email.data)
        # Add user to the database
        db.session.add(new_subscriber)
        db.session.commit()
        flash(f'Thank you for subscribing {form.first_name.data}!', 'success')
    return render_template("index.html", title='Home Page', form=form)


@server_bp.route("/about")
def about():
    return render_template('about.html', title='About')




@server_bp.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@server_bp.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@server_bp.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500