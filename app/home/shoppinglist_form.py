from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, TextField
from wtforms.validators import DataRequired


class ShoppingList(FlaskForm):
    
    #Form for users to create new account
    
    title = StringField('Title', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    description = TextField('Description')    
    submit = SubmitField('Add')

