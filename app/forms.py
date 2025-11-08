from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
import sqlalchemy as sa
from app import db
from app.models import Subscriber

class WaitlistForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Join Waitlist')
    
    def validate_email(self, email):
        user = db.session.scalar(sa.select(Subscriber).where(
            Subscriber.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')