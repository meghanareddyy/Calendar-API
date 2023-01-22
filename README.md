# Calendar API

## Local Environment Set up

### Create Virtual Environment
- open up a terminal and navigate to the root directory:
- pip install virtualenv
- virtualenv <virtual env name>
- source <virtual env name>/bin/activate

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```

Running the server

```
python3 main.py
```

By default, swagger will run at http://127.0.0.1:5000/

Endpoints
- GET /api/v1/doctors: Retrieves a list of all doctors
- POST /api/v1/doctors: Adds a doctor

- GET /api/v1/doctors/{doctor_id}/appointments/{appointment_date} : Get a list of all appointments for a particular doctor and particular day
- DELETE /api/v1/doctors/{doctor_id}/appointments/{appointment_date} : Delete an existing appointment from a doctor's calendar
- POST /api/v1/doctors/{doctor_id}/appointments: Add a new appointment to a doctor's calendar
    ○ New appointments can only start at 15 minute intervals (ie, 8:15AM is a valid time
    but 8:20AM is not)
    ○ A doctor can have multiple appointments with the same time, but no more than 3
    appointments can be added with the same time for a given doctor