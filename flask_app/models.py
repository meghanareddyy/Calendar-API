from collections import defaultdict
import json

class Doctor:

    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

class Doctors:
    def __init__(self):
        self.doctors_list = []
    
    def add(self, doctor):
        self.doctors_list.append(doctor)

    def get_doctor(self, doctor_id):
        for doctor in self.doctors_list:
            if doctor.id == doctor_id:
                return doctor
        return None

    def get_doctors_list(self):
        print("heyyyyyyyy")
        return [json.dumps(doctor.__dict__) for doctor in self.doctors_list]
    
        

    def is_doctor_exists(self, doctor_id):
        return True if self.get_doctor(doctor_id) else False

  
        


class Appointments:
    def __init__(self):
        self.appointments_list = defaultdict(list)
    
    def add(self, doctor_id, appointment):
        self.appointments_list[doctor_id].append(appointment)
        # print(self.appointments_list)

    def get_appointment_by_doctor_and_date(self,doctor_id, appointment_date):
        # print(self.appointments_list)
        if not doctor_id in self.appointments_list:
            return None
        appointments_by_date = []

        for appointment in  self.appointments_list[doctor_id]:
            if appointment.date == appointment_date:
                appointments_by_date.append(json.dumps(appointment.__dict__))
        return appointments_by_date
    
    def get_appointments_by_date_and_time(self, doctor_id, date, time):
         # print(self.appointments_list)
        if not doctor_id in self.appointments_list:
            return 0
        appointments_cnt= 0

        for appointment in  self.appointments_list[doctor_id]:
            if appointment.date == date and appointment.time == time:
                 appointments_cnt+=1
                
        return appointments_cnt
    
    
    def delete_appointment_by_doctor_id_and_appointment_id(self, doctor_id, appointment_id):
        if not doctor_id in self.appointments_list:
            return None
        for appointment in  self.appointments_list[doctor_id]:
            if appointment.id == appointment_id:
                self.appointments_list[doctor_id].remove(appointment)
                return json.dumps(appointment.__dict__)
        return None

class Appointment:
    def __init__(self, id, date, time):
        self.id = id
        self.date = date
        self.time = time



