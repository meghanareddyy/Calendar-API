from flask_restplus import fields
from flask_app import api



doctors_ns = api.namespace('api/v1/doctors', description='TODO operations')


doctors_rest_model = doctors_ns.model('Todo', {
    'name': fields.String(required=True, description='The task details'),
    'location': fields.String(required=True, description='The task details')
})

appointments_ns = api.namespace('api/v1/doctors', description='TODO operations')


appointments_rest_model = appointments_ns.model('Todo1', {
    'date': fields.String(required=True, description='The task details'),
    'time': fields.String(required=True, description='The task details')
})