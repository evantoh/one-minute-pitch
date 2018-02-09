from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class UpdateProfile(FlaskForm):
     bio=TextAreaField('Tell us about you',validators=[Required()])
     submit=SubmitField('submit')

    

class pitchIdea(FlaskForm):
   
    title=StringField('Pitch Title',validators=[Required()])
    author=StringField('Author',validators=[Required()])
    body=TextAreaField('Tell us about your Idea',validators=[Required()])
    category = RadioField('Pick your pitch Category', choices=[('business', 'business'), ('jobs', 'jobs'),('science', 'science'),('tech', 'tech'),('interview', 'interview')], validators=[Required()])

    submit=SubmitField('submit')




class CommentForm(FlaskForm):

    comment=TextAreaField('Comment here',validators=[Required()])
    submit=SubmitField('submit')
