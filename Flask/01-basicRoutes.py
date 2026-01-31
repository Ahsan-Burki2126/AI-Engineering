from flask import Flask,jsonify

app = Flask(__name__)
@app.route("/")
def Home():
    return jsonify(name="School")