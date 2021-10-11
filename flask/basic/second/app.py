from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABESE_URI'] = 'sqlite:///test.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False


@app.befor_first_request
def create_table():
    db.create_all()

@app.route('data/create', method = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form
            pass
app.run(host='localhost', port=5000)
