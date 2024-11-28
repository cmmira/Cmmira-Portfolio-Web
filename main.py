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

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)