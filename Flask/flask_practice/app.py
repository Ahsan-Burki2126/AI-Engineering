from flask import Flask,render_template

app = Flask(__name__)


#Home Page
@app.route("/")
def home():
    return render_template("index.html")

#Profile Page
@app.route("/user/profile")
def profile():
    return "<h1>This is my Profile Page.</h1>"


if __name__ == "__main__":
    app.run(debug=True)