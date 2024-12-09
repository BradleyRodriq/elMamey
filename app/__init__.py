from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration
    load_dotenv()
    app.config["JWT_SECRET_KEY"] = "JWT_SECRET"
    app.config["MONGO_URI"] = "MONGO_DB"
    client = MongoClient(app.config["MONGO_URI"])

    # Initialize extensions
    CORS(app)
    JWTManager(app)
    
    # Set up database
    app.db = client["elMamey"]

    # Register routes
    from .routes import api
    app.register_blueprint(api, url_prefix="/")

    return app
