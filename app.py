from flask import Flask
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = '17ea8b95909637c15d7c3370f11d0825'

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


if __name__ == '__main__':
    app.run(debug=True)
