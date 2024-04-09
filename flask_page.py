from flask import Flask, render_template, flash, url_for, redirect, jsonify
from forms import regForm, loginForm
import requests
app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", endpoint="Register_page", methods=['GET', 'POST'])
def register():
    form = regForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", endpoint="login_page")
def login():
    form = loginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


