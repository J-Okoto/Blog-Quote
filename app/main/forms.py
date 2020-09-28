from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

