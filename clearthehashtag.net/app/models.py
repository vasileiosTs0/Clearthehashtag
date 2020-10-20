from datetime import datetime
from app.extensions import db, login, mail
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


@login.user_loader
def load_user(user_id):
    return Subscriber.query.get(int(user_id))

class Subscriber(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), unique=False, nullable=False)    
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Subscriber('{self.first_name}', '{self.email}')"