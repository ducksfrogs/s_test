from flask import Flask, render_template, request
from models.models import Weather

from models.database import db_session
from datetime import datetime

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_cities = Weather.query.all()
    return render_template("index.html", name=name, all_cities=all_cities)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    all_cities= Weather.query.all()
    return render_template("index.html", name=name, all_cities=all_cities)

# @app.route("/add", methods=["post"])
# def add():
#     title = request.form["title"]
#     body = request.form["body"]
#     content = Weather(title, body, datetime.now())
#     db_session.add(content)
#     db_session.commit()
#     return index()


if __name__=="__main__":
    app.run(dubug=True)
