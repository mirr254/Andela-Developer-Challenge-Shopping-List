from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError,IntegerField
from wtforms.validators import DataRequired


class ShoppingList(FlaskForm):
    """
    Form for users to create new account
    """
    item_name = StringField('Item Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])    
    submit = SubmitField('Register')