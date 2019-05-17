from flask import json, request, jsonify, make_response

from models.appointment import Appointment

from api import app


@app.route('/api/v1/appointments/', methods=["POST"])
def create_appointment():
    """Creates an appointment
    :return: a success message
    """
    details = json.loads(request.data)

    appointment = Appointment(
        consultation_type=details["consultation_type"],
        resolution=details["resolution"],
        status=details["status"],
        slot_id=details["slot_id"],
        venue=details["venue"],
        patient_id=details["patient_id"],
        doctor_id=details["doctor_id"]
    )

    appointment.save()
    return make_response(jsonify({"message": "appointment created_successfully"}), 201)


@app.route('/api/v1/appointments/', methods=["GET"])
def get_appointment():
    """
    :return: A list of objects of all appointments available
    """
    appointments = Appointment.get_all()
    if appointments:
        get_results = []
        for appointment in appointments:
            appointment_object = {
                "appointment_id": appointment.id,
                "consultation_type": appointment.consultation_type,
                "resolution": appointment.resolution,
                "status": appointment.status,
                "slot_id": appointment.slot_id,
                "venue": appointment.venue,
                "patient_id": appointment.patient_id,
                "doctor_id": appointment.doctor_id
            }
            get_results.append(appointment_object)

            return make_response(jsonify({"appointments": get_results})), 200
    else:
        return make_response(jsonify({"message": "There are currently no appointments"}), 404)


@app.route('/api/v1/appointments/<int:appointment_id>', methods=["GET"])
def get_appointment_by_id(appointment_id):
    """
    :param appointment_id: The specific id whose appointment we want to get
    :return: An object for the appointment, otherwise not found
    """
    appointment = Appointment.query.filter_by(id=appointment_id).first()
    if appointment:
        appointment_object = {
            "appointment_id": appointment.id,
            "consultation_type": appointment.consultation_type,
            "resolution": appointment.resolution,
            "status": appointment.status,
            "slot_id": appointment.slot_id,
            "venue": appointment.venue,
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id
        }

        return make_response(jsonify({"appointment": appointment_object})), 200
    else:
        return jsonify({"message": "appointment {} does not exist".format(appointment_id)}), 404


@app.route('/api/v1/appointments/<int:appointment_id>', methods=["DELETE"])
def delete_appointment(appointment_id):
    """
    :param appointment_id: The specific id whose appointment we want to delete
    :return: A success message after deletion, otherwise not found
    """
    appointment = Appointment.query.filter_by(id=appointment_id).first()

    if appointment:
        appointment.delete()
        return make_response(
            jsonify({"message": "appointment {} deleted successfully".format(appointment_id)}), 204
        )
    return jsonify({"message": "appointment {} does not exist".format(appointment_id)}), 404
