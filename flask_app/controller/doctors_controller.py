from flask_restplus import Api, Resource, fields
from flask_app.models import Doctors, Doctor
from flask_app.rest_model import doctors_ns, doctors_rest_model
from flask import request
from flask_app import doctors_obj
import json





@doctors_ns.route('')
@doctors_ns.response(201, 'Created')
class DoctorsListResource(Resource):
    def get(self):
        doctors_list = doctors_obj.get_doctors_list()
        print(doctors_list)
        return json.dumps(doctors_list), 200

    @doctors_ns.expect(doctors_rest_model)

    def post(self):
       json_data = request.get_json(force=True)
       doctors_list = doctors_obj.get_doctors_list()
       doctor_id = len(doctors_list) + 1
       new_doctor_data = Doctor(doctor_id, json_data["name"], json_data["location"])
       doctors_obj.add(new_doctor_data)
       return doctor_id, 201




