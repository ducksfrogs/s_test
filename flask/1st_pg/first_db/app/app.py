from flask import Flask, render_template, request
from models.models import Weather

from models.database import db_session

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_cities = Weather.query.all()
    return render_template("index.html", name=name, all_cities=all_cities)

@app.route("/searchCity", methods=["post"])
def searchCity():
    city = request.form["city"]
    cityRq = db_session.query(Weather.city,
                            Weather.temp_hi,
                            Weather.temp_lo).filter(Weather.city==city).all()
    return render_template("searchCity.html", all_cities=cityRq)

@app.route("/s_date", methods=["post"])
def sdate():
    d_date = request.form["date"]
    cityRq = db_session.query(Weather.city,
                            Weather.temp_hi,
                            Weather.date_inputed).filter(Weather.date_inputed == d_date).all()
    return render_template("s_date.html", all_cities = cityRq)



if __name__=="__main__":
    app.run(dubug=True)
