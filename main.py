from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
import smtplib
from info import Info
me = Info()

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def info():
    return render_template("index.html", me=me)

if __name__ == "__main__":
    app.run(debug=True)