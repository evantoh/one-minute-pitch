from flask import render_template,request,redirect,url_for
from . import main


#views
@main.route('/')
def index():
    title = 'one minute pitch'
    return render_template('index.html',title = title)