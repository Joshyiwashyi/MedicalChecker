from flask import Blueprint, jsonify

# define the Blueprint object
conditions_bp = Blueprint("conditions", __name__)

# Example route
@conditions_bp.route("/conditions", methods=["GET"])
def get_conditions():
    return jsonify({"message": "Conditions route working!"})
