from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#70ShreeHari07
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'mydata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):
    date_time = db.Column(db.String(900), primary_key=True)
    District_state = db.Column(db.String(900), index=True)
    current_temp_city= db.Column(db.Float, index=True)
    weather_desc = db.Column(db.String(256),index=True)
    max_temp_city = db.Column(db.Float, index=True)
    min_temp_city= db.Column(db.Float, index=True)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.String(200),index=True)
    wind_speed= db.Column(db.String(120), index=True)
    country = db.Column(db.String(6),index=True)

db.create_all()


@app.route('/')
def index():
    users = User.query
    return render_template('bootstrap_table.html', title='Bootstrap Table',
                           users=users)



if __name__ == '__main__':

    app.run()