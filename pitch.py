from datetime import datetime
from flask import Flask, render_template, url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sindet'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post
posts = [
    {
        'author': 'Sarah Sindet',
        'title': 'Pitch post 1',
        'content': 'First post content',
        'date_posted': 'July 17, 2020'
    },
    {
        'author': 'Daniel Sindet',
        'title': 'Pitch post 2',
        'content': 'Second post content',
        'date_posted': 'July 18, 2020'
    }    
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)
    

@app.route("/category")
def category():
    return render_template('category.html', title='Category')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug = True)    