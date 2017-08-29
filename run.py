from flask import Flask, render_template, request, flash
from app.forms import SignIn 

app = Flask(__name__ ,template_folder='Designs')

#set up secret key for crsf
app.secret_key = "M@0$"

@app.route("/", methods = ["GET", "POST"])
def index():
    form = SignIn()
    if request.method == 'POST':
        if form.validate() == False:
            flash('Please fill up all fields.')
            return render_template("index.html", form = form)
        else:
            return render_template("dashboard.html")
    elif request.method == "GET":
        return render_template("index.html", form = form)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

#run the app

if __name__ == "__main__":
    app.run( debug=True,host='0.0.0.0' )
    