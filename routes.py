from os import getenv

from flask_cors import CORS
from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projektit")
def projektit():
    return render_template("projektit.html")

@app.route("/ansioluettelo")
def ansioluettelo():
    return render_template("ansioluettelo.html")