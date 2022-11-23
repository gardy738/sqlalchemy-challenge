from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "This is my homework"

@app.route("/api/v1.0/precipitation")
def precipitation():
    """ return the dictionary """
    return precipitation

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(list)

@app.route("/api/v1.0/tobs")
def tobs():
    return list
 