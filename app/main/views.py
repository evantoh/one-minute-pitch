from flask import render_template,request,redirect,url_for
from . import main
from ..models import User
from .forms import RegistrationForm
from ..import db
from flask_login import login_required  


#views
@main.route('/',methods = ['GET','POST'])
@login_required
def index():
    title = 'one minute pitch'
    return render_template('index.html',title = title)