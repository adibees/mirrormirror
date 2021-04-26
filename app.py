from flask import Flask, request
import helpers as sb
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route("/")
def home():
    return "<h2>Hello world</h2> Welcome to simplebot!"


@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    twily_response = sb.predict(user_input)
    msg.body(twily_response)
    return str(resp)


@app.route("/test")
def bot_response():
    user_input = request.args.get("msg").lower()
    return f"<h2>{sb.sentiment(user_input)}</h2>"


if __name__ == "__main__":
    app.run()
