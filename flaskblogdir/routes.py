from flask import render_template, redirect, flash, url_for
from flaskblogdir.forms import RegistrationForm, LoginForm
from flaskblogdir.models import User, Post
from flaskblogdir import app

posts = [
    {
        "author": "Rafael Mkhitaryan",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 30.11.2021",

    },

    {
        "author": "Vitali Oboladze",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 31.11.2021",

    }

]


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account Created For {}!".format(form.username.data), "success")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been Logged in!", "success")
            return redirect(url_for("index"))
        else:
            flash("Login Unsuccessful.", "danger")

    return render_template("login.html", title="Login", form=form)
