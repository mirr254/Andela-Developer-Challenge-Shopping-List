from flask import Flask, render_template, request
from app.models import addUser, system_users

app = Flask(__name__ ,template_folder='Designs')



@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/signup/", methods=['POST','GET'])
def signupUser():

    if request.method == "GET":
        return render_template("dashboard.html")

    #post request
    elif request.method() == "POST":
        
        password =request.form['password']
        email =request.form['email']
        fname =request.form['fname']    
        password_confirm =request.form['password_confirm']

        if password != password_confirm:
            err = "Password Mismatch"
            return render_template("signup.html", err = err )    
    
    addUser(fname, email, password)
    loggedin = True
    return render_template("dashboard.html", fname=fname, email=email )

"""
render signup

"""
@app.route("/signup")
def signup():
    return render_template("signup.html")


"""
check if user exists

"""
@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    #methd is post
    password=request.form['password']
    email=request.form['email']
    #check if user exists
    if email in system_users.keys():
        loggedin = True
        return render_template("dashboard.html", email=email)

    else:
        err = "Email Mismatch"
        return render_template("index.html", err=err)
    
        

@app.route("/reset-password")
def passwdReset():
    render_template("pass_reset.html")

if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0")
    app.run(debug=True)