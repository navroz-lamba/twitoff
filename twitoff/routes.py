from flask import render_template
from twitoff import app, db
from twitoff.models import User

@app.route('/')
def root():
    users = User.query.all()
    return render_template('base.html', title='Home', users=User.query.all())