from flask import Blueprint, request, jsonify
from services.ml_service import predict_all

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Batch input
    if data and "texts" in data:
        texts = data["texts"]
        if not isinstance(texts, list) or len(texts) == 0:
            return jsonify({"error": "Please provide a non-empty list of texts"}), 400

        results = [predict_all(t) for t in texts]
        return jsonify({"results": results})

    # Single input
    if data and "text" in data:
        text = data["text"]
        result = predict_all(text)
        return jsonify(result)

    return jsonify({"error": "Please provide input text(s)"}), 400
