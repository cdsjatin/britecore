from app import app
from flask import render_template, flash, redirect, url_for
from app.data import TestData
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    data = TestData()
    return render_template('index', title='Home', user=data.user, posts=data.posts, fr=data.fr)

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login', title='Sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login', title='Sign In', form=form)