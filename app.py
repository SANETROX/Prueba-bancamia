from flask import Flask, abort, make_response, request, redirect, url_for
from flask_migrate import Migrate
from flask.templating import render_template


from flask_sqlalchemy import SQLAlchemy

###Modelo User




app = Flask(__name__)



@app.route('/')
def index():
    return {"hi":"hello"}

@app.route('/inicio/')
def inicio():
    return render_template('inicio.html', data = {"hi":"sanetrox"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

