from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

class itemForm(FlaskForm):

    name = StringField('Item Name', validators=[DataRequired()])        
    submit = SubmitField('Add Item')