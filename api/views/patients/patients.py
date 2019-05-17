from flask import json, request, jsonify, make_response

from models.patient import Patient

from api import app


@app.route('/api/v1/patients/', methods=["POST"])
def create_patient():
    """Creates a patient entity
    :return: a success message
    """
    details = json.loads(request.data)

    patient = Patient(
        first_name=details["first_name"],
        last_name=details["last_name"]
    )

    patient.save()
    return make_response(jsonify({"message": "Patient added successfully"}), 201)


@app.route('/api/v1/patients/', methods=["GET"])
def get_patient():
    """
    :return: A list of objects of all the patients available
    """
    patients = Patient.get_all()
    if patients:
        get_results = []
        for patient in patients:
            patient_object = {
                "patient_id": patient.id,
                "first_name": patient.first_name,
                "last_name": patient.last_name
            }
            get_results.append(patient_object)

        return make_response(jsonify({"patients": get_results})), 200
    else:
        return make_response(jsonify({"message": "No patient records found"}), 404)


@app.route('/api/v1/patients/<int:patient_id>', methods=["GET"])
def get_patient_by_id(patient_id):
    """
    :param patient_id: The specific id whose patient we want to get
    :return: An object for the patient, otherwise not found
    """
    patient = Patient.query.filter_by(id=patient_id).first()
    if patient:
        patient_object = {
            "patient_id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name
        }

        return make_response(jsonify({"patient": patient_object})), 200
    else:
        return jsonify({"message": "patient {} does not exist".format(patient_id)}), 404


@app.route('/api/v1/patients/<int:patient_id>', methods=["DELETE"])
def delete_patient(patient_id):
    """
    :param patient_id: The specific id whose patient we want to delete
    :return: A success message after deletion, otherwise not found
    """
    patient = Patient.query.filter_by(id=patient_id).first()

    if patient:
        patient.delete()
        return make_response(
            jsonify({"message": "patient record {} deleted successfully".format(patient_id)}), 200
        )
    return jsonify({"message": "patient record {} does not exist".format(patient_id)}), 404




