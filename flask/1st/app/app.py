from flask import Flask, render_template, request
import psycopg2
from psycopg2._psycopg import *

app = Flask(__name__)


#users = 'postgres'
#dbname = 'test2'
#password = '0310'
#conn = psycopg2.connect(" user="+users+" dbname="+dbname+" password="+password)
#cur = conn.cursor()
#cur.execute('select * from actor')
#results = cur.fetchall()

@app.route("/")
# def hello():
    # return "Hello world"


@app.route("/index")
def index():
    name = request.args.get("name")
    animals = ['panda', 'coara', 'rakko', 'cat']
    return render_template("index.html", name=name, animals=animals)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    animals = ['panda', 'coara', 'rakko', 'cat']
    return render_template("index.html", name=name, animals=animals)



if __name__=="__main__":
    app.run(dubug=True)
