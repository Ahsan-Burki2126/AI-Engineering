from flask import Flask, render_template,request,jsonify
from model import generate_reply
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat",methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    #history of the previous chat
    chat_history = []
    bot_reply = generate_reply(chat_history,user_message)
    # Append to history 
    chat_history.append(user_message)
    chat_history.append(bot_reply)
    print(chat_history)
    return jsonify({"reply":bot_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)