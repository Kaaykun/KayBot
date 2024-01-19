from flask_wtf import FlaskForm #type: ignore
from wtforms import StringField,TextAreaField,SubmitField #type: ignore
from wtforms.validators import DataRequired #type: ignore

class kaybotform(FlaskForm):
    user_input=StringField(validators=[DataRequired()])
    send=SubmitField('Send')
