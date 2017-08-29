from flask import Flask, render_template, request, flash
from app.forms import SignIn, RegistrationForm

app = Flask(__name__ ,template_folder='Designs')

#set up secret key for crsf
app.secret_key = "M@0$"

#route users to home page
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

#route user to registration or signup form
@app.route("/signup")
def signup():
    form = RegistrationForm()
    #if it is a post request make sure to validate all fields
    if request.method == 'POST':
        if form.validate() == False:
            flash('Please fill up all fields.')
            return render_template("signup.html", form = form)
        else:
            return render_template("dashboard.html")
    elif request.method == "GET":
        return render_template("signup.html", form = form)
    

#this will be after user is logged in
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


#redirect admin to his page
@app.route("/admin/")
def adminDashboard():
    return render_template("admin.html")

#run the app

if __name__ == "__main__":
    app.run( debug=True,host='0.0.0.0' )
    