from flask import render_template
from app import app

#views
@app.route('/')
def index():
    title = 'one minute pitch'
    return render_template('index.html',title = title)