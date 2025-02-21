import pandas as pd
from flask import Flask, jsonify, render_template, redirect, request

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/meet_the_team")
def about_us():
    return render_template("meet_the_team.html")

@app.route("/works_cited")
def work_cited():
    return render_template("works_cited.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

#################################################
# API Routes
#################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA_Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-chace, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

if __name__ == '__main__':
    app.run(debug=True)
    