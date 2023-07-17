from flask import Flask
from api.views import blueprint
from extensions import db

app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)
app.config.from_object("config")

db.init_app(app)

if __name__ == "__main__":
    app.run(host=app.config.get("FLASK_HOST"), port=app.config.get("FLASK_PORT"), debug=app.config.get("FLASK_DEBUG"))
