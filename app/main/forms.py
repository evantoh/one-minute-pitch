from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class UpdateProfile(FlaskForm):
     bio=TextAreaField('Tell us about you',validators=[Required()])
     submit=SubmitField('submit')

    

class pitchIdea(FlaskForm):
    category = [('business', 'business'),('science', 'science'),('tech', 'tech'),('interview', 'interview')]
    title=StringField('Pitch Title',validators=[Required()])
    pitch=TextAreaField('Tell us about your Idea',validators=[Required()])
    submit=SubmitField('submit')
