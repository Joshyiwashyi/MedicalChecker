from flask import Flask
from routes.predicts import predict_bp
from routes.conditions import conditions_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(predict_bp, url_prefix="/api")
app.register_blueprint(conditions_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
