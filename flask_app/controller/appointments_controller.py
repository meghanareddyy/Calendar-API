from flask_restplus import Api, Resource, fields
from flask_app.models import Appointment
from flask_app import doctors_obj, appointments_obj
from flask_app.rest_model import appointments_ns, appointments_rest_model
from flask import request,jsonify
import json
import uuid
from datetime import datetime

@appointments_ns.route('/<int:doctor_id>/appointments')
@appointments_ns.response(201, 'Created')
class AppointmentsResource(Resource):
    @appointments_ns.expect(appointments_rest_model)
    def post(self, doctor_id):
        json_data = request.get_json(force=True)
        appointment_id  = str(uuid.uuid4())

        # check if doctor already exists
        if not doctors_obj.is_doctor_exists(doctor_id):
            return {'error': 'cannot add appointment as doctor doesnt exist'}, 400

        # check if time is a valid 15min interval
        time = datetime.strptime(json_data["time"], '%H:%M').time()
        if time.minute % 15 != 0:
            return {'error': 'Invalid time. Appointments can only start at 15 minute intervals'}, 400

        # check if doctor already has 3 appointmnets at the same time
        appointment_cnt_by_date_and_time = appointments_obj.get_appointments_by_date_and_time(doctor_id, json_data["date"], json_data["time"])
        if appointment_cnt_by_date_and_time >= 3:
            return {'error': 'Cannot add more than three appointments at the same time for a given doctor'}, 400

        new_appointment_data = Appointment(appointment_id, json_data["date"], json_data["time"])

       

        appointments_obj.add(doctor_id, new_appointment_data)
        return doctor_id, 201

@appointments_ns.route('/<int:doctor_id>/appointments/<string:appointment_date>')
@appointments_ns.response(200, 'Created')
class AppointmentListResource(Resource):
    def get(self, doctor_id, appointment_date):
       print(appointment_date)
       print("************")
       doctor_appoint_list_by_date = appointments_obj.get_appointment_by_doctor_and_date(doctor_id, appointment_date)
       return json.dumps(doctor_appoint_list_by_date), 200

@appointments_ns.route('/<int:doctor_id>/appointments/<string:appointment_id>')
@appointments_ns.response(200, 'Created')
class AppointmentDeleteResource(Resource):
    def delete(self, doctor_id, appointment_id):
       delete_appointment= appointments_obj.delete_appointment_by_doctor_id_and_appointment_id(doctor_id, appointment_id)
       return json.dumps(delete_appointment), 200


  


