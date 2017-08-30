from flask import Flask, render_template, request

app = Flask(__name__ ,template_folder='Designs')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard", methods=["POST"])
def dashboard():
    name=request.form['password']
    email=request.form['email']
    return render_template("dashboard.html")

app.run(debug=True)