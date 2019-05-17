# appointment-app
A simple appointment app for doctors and patients to schedule appointments
___
### Prerequisites
* PostgreSQL
* Python 3.6
* Flask

____
#### To run locally
clone the repo:
```
$ git clone git@github.com:Alweezy/appointment-app.git
```
and cd into the application:
```
$ cd appointment-app/
```
create a virtual environment for the project.
```
$ virtualenv --python=python3.6 virtualenv-name
```
and activate virtual environment
```
$ source virtualenv-name/bin/activate
```
Alternatively you can create it using virtualenvwarapper if installed:
```
$ mkvirtualenv --python=python3.6 virtualenv-name
```
> It will be automatically activated, in the future to use it just type:
```
$ workon virtualenv-name
```

* Make sure you have a `.env` file from which to `source` credentials (These can be shared separately).

Install libraries and dependencies `$ pip install -r requirements.txt`.

Create testing and development databases: `$ createdb appointment_dev`, `$ createdb appointment_testing`:

Handle migrations by running the following commands one after the other:

```
$ python manage.py db init
$ python manage.py db migrate
$  python manage.py db upgrade

```

### Api Endpoints

| Endpoint | Functionality |
| -------- | ------------- |
| POST /api/v1/doctors/ | Adds a doctor into the records|
| GET /api/v1/doctors/| Lists all the available doctors |
| GET /api/v1/doctors/doctor_id | Get a particular doctor by Id |
| DELETE /api/v1/doctors/doctor_id | Delete a particular doctor's record |
| POST /api/v1/patients/ | Adds a patient into the records|
| GET /api/v1/patients/| Lists all the patients in the records |
| GET /api/v1/patients/patient_id | Get a particular patient by Id |
| DELETE /api/v1/patients/patient_id | Delete a particular patient record |
| POST /api/v1/appointments/ | Creates a new appointment|
| GET /api/v1/appointments/| Lists all the appointments in the records |
| GET /api/v1/appointments/patient_id| Returns a particular appointment|
| DELETE /api/v1/appointments/patient_id | Deletes an appointment |
| POST /api/v1/slots/ | Creates a new slot for a doctor|
| GET /api/v1/slots/| Lists all the available slots |
| GET /api/v1/slots/slot_id| Returns a slot|
| DELETE /api/v1/slots/slot_id | Deletes slot |


# Running tests
Make sure you are connected to the testing database, `appointment_testing` and run `$ nosetests -v`

The live hosted application can be found [here](https://daktari-sessions.herokuapp.com/api/v1/).
