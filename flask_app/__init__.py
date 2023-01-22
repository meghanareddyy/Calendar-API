from flask import Flask
from flask_restplus import Api, Resource, fields
from flask_app.models import Appointments, Doctors

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

appointments_obj = Appointments()
doctors_obj = Doctors()

if __name__ == '__main__':
    app.run(debug=True)