from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_wtf.file import FileField, FileAllowed
from app.models import Subscriber
from flask_login import current_user


class SubscriptionForm(FlaskForm):
    first_name = StringField('First Name:',
                           validators=[DataRequired(), Length(min=1, max=40)])
    email = StringField('Email:',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Join the list')

    def validate_email(self, email):
        user = Subscriber.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists in our database.')