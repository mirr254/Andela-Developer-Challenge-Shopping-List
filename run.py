from flask import Flask, render_template, request
from app.models import addUser

app = Flask(__name__ ,template_folder='Designs')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup/", methods=['POST'])
def signupUser():
    password =request.form['password']
    email =request.form['email']
    fname =request.form['fname']    
    password_confirm =request.form['password_confirm']

    if password != password_confirm:
        err = "Password Mismatch"
        return render_template("signup.html", err = err )    
    
    addUser(fname, email, password)
    return render_template("dashboard.html", fname=fname, email=email )

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard", methods=["POST"])
def dashboard():
    password=request.form['password']
    email=request.form['email']
    return render_template("dashboard.html", email=email)

@app.route("/reset-password")
def passwdReset():
    render_template("pass_reset.html")

app.run(debug=True)