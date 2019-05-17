from flask import json, request, jsonify, make_response

from models.slot import Slot

from api import app


@app.route('/api/v1/slots/', methods=["POST"])
def create_slot():
    """Creates a slot entity
    :return: a success message
    """
    details = json.loads(request.data)
    if details["start_time"] <= details["end_time"]:
        slot = Slot(
            doctor_id=details["doctor_id"],
            start_time=details["start_time"],
            end_time=details["end_time"]
        )

        slot.save()
        return make_response(jsonify({"message": "Slot created successfully"}), 201)
    return make_response(jsonify({"message": "Start time cannot be later than stop time"}), 400)


@app.route('/api/v1/slots/', methods=["GET"])
def get_slot():
    """
    :return: A list of objects of all the slots available
    """
    slots = Slot.get_all()
    if slots:
        get_results = []
        for slot in slots:
            slot_object = {
                "doctor_id": slot.doctor_id,
                "slot_id": slot.id,
                "start_time": slot.start_time,
                "end_time": slot.end_time
            }
            get_results.append(slot_object)

        return make_response(jsonify({"slots": get_results})), 200
    else:
        return make_response(jsonify({"message": "No slots found"}), 404)


@app.route('/api/v1/slots/<int:slot_id>', methods=["GET"])
def get_slot_by_id(slot_id):
    """
    :param slot_id: The specific id whose slot we want to get
    :return: An object for the slot, otherwise not found
    """
    slot = Slot.query.filter_by(id=slot_id).first()
    if slot:
        slot_object = {
            "slot_id": slot.id,
            "start_time": slot.start_time,
            "end_time": slot.end_time
        }

        return make_response(jsonify({"slot": slot_object})), 200
    else:
        return jsonify({"message": "slot {} does not exist".format(slot_id)}), 404


@app.route('/api/v1/slots/<int:slot_id>', methods=["DELETE"])
def delete_slot(slot_id):
    """
    :param slot_id: The specific id whose slot we want to delete
    :return: A success message after deletion, otherwise not found
    """
    slot = Slot.query.filter_by(id=slot_id).first()

    if slot:
        slot.delete()
        return make_response(
            jsonify({"message": "slot record {} deleted successfully".format(slot_id)}), 200
        )
    return jsonify({"message": "slot record {} does not exist".format(slot_id)}), 404
