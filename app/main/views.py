from flask import render_template,request,redirect,url_for,abort
from . import main
##remember to import classes from ..requests
from .forms import pitchIdea,UpdateProfile,CommentForm
from .. import db, photos
from flask_login import login_required
from ..models import User,Pitch
'''
We then define our route decorators using the 
main blueprint instance instead of the app instance
'''


@main.route('/',methods=['GET','POST'])
@login_required
def index():
    
    pitch_form = pitchIdea()


    pitch=Pitch.query.all()
    if pitch_form.validate_on_submit():
        title=pitch_form.title.data
        body=pitch_form.body.data
        author=pitch_form.author.data
        category=pitch_form.category.data

        new_pitch=Pitch(title=title,body=body,author=author,category=category)
        db.session.add(new_pitch)
        db.session.commit()

    return render_template('index.html',pitch=pitch,pitch_form=pitch_form)

@main.route('/tech')
def tech():
    tech_pitch=Pitch.query.filter_by(category='tech').all()
    return render_template('tech.html',tech=tech_pitch)

@main.route('/jobs')
def jobs():
    job_pitch=Pitch.query.filter_by(category='jobs').all()
    return render_template('jobs.html',jobs=job_pitch)


@main.route('/new',methods=['GET','POST'])
@login_required
def new():
    
    pitch_form = pitchIdea()


    pitch=Pitch.query.all()
    if pitch_form.validate_on_submit():
        title=pitch_form.title.data
        body=pitch_form.body.data
        author=pitch_form.author.data
        category=pitch_form.category.data

        new_pitch=Pitch(title=title,body=body,author=author,category=category)
        db.session.add(new_pitch)
        db.session.commit()

    return render_template('index.html',pitch=pitch,pitch_form=pitch_form)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    pitch_form=UpdateProfile()
    if user is None:
        abort(404)

    
    if pitch_form.validate_on_submit():
        User.bio=pitch_form.bio.data
        db.session.add(user)
        db.session.commit()

    return render_template('profile/update.html',user=user.username,pitch_form=pitch_form)


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    pitch_form=UpdateProfile()

    if pitch_form.validate_on_submit():
        user.bio=pitch_form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username,pitch_form=pitch_form))

    return render_template('profile/update.html',pitch_form=pitch_form,user=user)


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


