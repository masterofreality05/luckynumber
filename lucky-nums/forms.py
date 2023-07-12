from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length

class LuckyNumberForm(FlaskForm):
    """Form for adding users."""

    
    name = StringField('Name', validators=[DataRequired()])
    birth_year = StringField('Birth Year', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    color = StringField('Favorite Colour', validators=[DataRequired()])
    type_of_fact = SelectField('Type of fact', choices = ['a','b','c'], validators = [DataRequired()])

