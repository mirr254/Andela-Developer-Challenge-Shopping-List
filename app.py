from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hallo world flask"

app.run(debug=True)