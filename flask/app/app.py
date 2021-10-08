from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
# def hello():
    # return "Hello world"


@app.route("/index")
def index():
    name = request.args.get("name")
    okyo = ["shikisoku", "panda",'lion','Momonga']
    return render_template("index.html", name=name, okyo=okyo)



if __name__=="__main__":
    app.run(dubug=True)
