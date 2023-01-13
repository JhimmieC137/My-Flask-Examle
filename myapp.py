from flask import Flask, jsonify

app=Flask(__name__)


@app.route("/")
def hello_world():
    value = "name"
    name = "Olujimi David"
    age = 24
    slack_username = "jimi"
    adult = False
    if age > 18:
        adult = True
    return jsonify({
        value: name,
        "age": age,
        "username": slack_username,
        "legal":adult
        
    })

@app.route("/state")
def current_state():
    state = "Oyo"
    capital = "Ibadan"
    return jsonify({
        "state": state,
        "capital": capital
        })