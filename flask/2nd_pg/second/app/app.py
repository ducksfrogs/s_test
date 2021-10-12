from flask import Flask, render_template, request
from sqlalchemy import func
from models.models import Weather

from models.database import db_session

app = Flask(__name__)

WEATHER = [Weather.A, Weather.B, Weather.C, Weather.D, Weather.E]
@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_cities = db_session.query(Weather).all()
    return render_template("index.html", name=name, all_cities=all_cities)

@app.route("/searchCity", methods=["post"])
def searchCity():
    abc = request.form["abc"] 
    cityRq = db_session.query(Weather).filter(Weather.E == abc).all()
    return render_template("searchCity.html", all_cities=cityRq)

@app.route("/s_date", methods=["post"])
def sdate():
    d_date = request.form["date"]
    cityRq = db_session.query(Weather).filter(func.Date(Weather.D) == d_date).all()
    return render_template("s_date.html", all_cities = cityRq)

@app.route('/b_date', methods=[ 'post'])
def b_date():
    be_date = request.form['date_be']
    en_date = request.form['date_en']
    cityRq = db_session.query(Weather.A, Weather.B, Weather.C, Weather.D, Weather.E).filter(Weather.D.between(be_date, en_date))

    return render_template("b_date.html", all_cities=cityRq)


if __name__=="__main__":
    app.run(dubug=True)
