from dotenv import load_dotenv
import os

load_dotenv()

FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT = os.environ.get("FLASK_PORT", 9000)
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", False)
SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
