from flask import json, request, jsonify, make_response

from models.doctor import Doctor

from api import app


@app.route('/api/v1/doctors/', methods=["POST"])
def create_doctor():
    """Creates a doctor
    :return: a success message
    """
    details = json.loads(request.data)

    doctor = Doctor(
        first_name=details["first_name"],
        last_name=details["last_name"]
    )

    doctor.save()
    return make_response(jsonify({"message": "Doctor added successfully"}), 201)


@app.route('/api/v1/doctors/', methods=["GET"])
def get_doctor():
    """
    :return: A list of objects of all the doctors available
    """
    doctors = Doctor.get_all()
    if doctors:
        get_results = []
        for doctor in doctors:
            doctor_object = {
                "doctor_id": doctor.id,
                "first_name": doctor.first_name,
                "last_name": doctor.last_name
            }
            get_results.append(doctor_object)

        return make_response(jsonify({"doctors": get_results})), 200
    else:
        return make_response(jsonify({"message": "No doctor records found"}), 404)


@app.route('/api/v1/doctors/<int:doctor_id>', methods=["GET"])
def get_doctor_by_id(doctor_id):
    """
    :param doctor_id: The specific id whose doctor we want to get
    :return: An object for the doctor, otherwise not found
    """
    doctor = Doctor.query.filter_by(id=doctor_id).first()
    if doctor:
        doctor_object = {
            "doctor_id": doctor.id,
            "first_name": doctor.first_name,
            "last_name": doctor.last_name
        }

        return make_response(jsonify({"doctor": doctor_object})), 200
    else:
        return jsonify({"message": "doctors {} does not exist".format(doctor_id)}), 404


@app.route('/api/v1/doctors/<int:doctor_id>', methods=["DELETE"])
def delete_doctor(doctor_id):
    """
    :param doctor_id: The specific id whose doctor we want to delete
    :return: A success message after deletion, otherwise not found
    """
    doctor = Doctor.query.filter_by(id=doctor_id).first()

    if doctor:
        doctor.delete()
        return make_response(
            jsonify({"message": "doctor record {} deleted successfully".format(doctor_id)}), 200
        )
    return jsonify({"message": "doctor record {} does not exist".format(doctor_id)}), 404




