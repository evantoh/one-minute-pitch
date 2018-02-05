from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from ..import db
from flask_login import login_required  


#views
@main.route('/',methods = ['GET','POST'])
@login_required
def index():
    title = 'one minute pitch'
    return render_template('index.html',title = title)

@main.route('/user/<uname>')
def profile(uname)
    user = User,query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user)