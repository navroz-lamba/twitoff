from flask import render_template
from twitoff import app, db

@app.route('/')
def root():
    return render_template('base.html', title='Home')