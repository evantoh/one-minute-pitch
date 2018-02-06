from flask import render_template,request,redirect,url_for,abort
from . import main
##remember to import classes from ..requests
from .forms import pitchIdea,UpdateProfile
from .. import db, photos
from flask_login import login_required
from ..models import User,Pitch,Category
'''
We then define our route decorators using the 
main blueprint instance instead of the app instance
'''
@main.route('/',methods=['GET','POST'])
@login_required
def index():

    form=pitchIdea()


    pitch=Pitch.query.all()
    if form.validate_on_submit():
        title=form.title.data
        body=form.pitch.data
        category=form.pitch.data

        new_pitch=Pitch(head=title,body=body,category=category)
        db.session.add(new_pitch)
        db.session.commit()

    return render_template('index.html',pitch=pitch,form=form)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    form=UpdateProfile()
    if user is None:
        abort(404)

    
    if form.validate_on_submit():
        User.bio=form.bio.data
        db.session.add(user)
        db.session.commit()

    return render_template('profile/update.html',user=user.username,form=form)


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form=UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username,form=form))

    return render_template('profile/update.html',form=form,user=user)


@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def  update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photos' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_pic_path=path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


