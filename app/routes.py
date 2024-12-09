from flask import request, jsonify, Blueprint, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

api = Blueprint("api", __name__)

# Sample user collection (replace with MongoDB)
users = []

@api.route("/")
def index():
    return render_template("home.html")

@api.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"])
    user = {"name": data["name"], "email": data["email"], "password": hashed_password}
    users.append(user)  # Replace this with MongoDB insertion
    return jsonify({"message": "User registered successfully"}), 201

@api.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = next((u for u in users if u["email"] == data["email"]), None)  # Replace with MongoDB query
    if user and check_password_hash(user["password"], data["password"]):
        token = create_access_token(identity=user["email"])
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@api.route("/services", methods=["POST"])
def create_service_offering():
    data = request.get_json()
    service = {
        "title": data["title"],
        "description": data["description"],
        "location": data["location"],
        "date": data["date"]
    }
    # app.db.events.insert_one(event)  # Insert into MongoDB
    return jsonify({"message": "Service created successfully"}), 201

@api.route("/services", methods=["GET"])
def list_service_offerings():
    # events = app.db.events.find()
    # return jsonify([event for event in events])
    return render_template("services.html")

@api.route("/services/<id>", methods=["GET"])
def get_service_offering(id):
    # event = app.db.events.find_one({"_id": ObjectId(id)})
    # return jsonify(event)
    return render_template("service.html")

@api.route("/requests", methods=["POST"])
def create_request_service():
    data = request.get_json()
    request = {
        "title": data["title"],
        "description": data["description"],
        "location": data["location"],
        "date": data["date"]
    }
    # app.db.requests.insert_one(request)  # Insert into MongoDB
    return jsonify({"message": "Request created successfully"}), 201

@api.route("/requests", methods=["GET"])
def list_request_services():
    # requests = app.db.requests.find()
    # return jsonify([request for request in requests])
    return render_template("requests.html")

@api.route("/requests/<id>", methods=["GET"])
def get_request_service(id):
    # request = app.db.requests.find_one({"_id": ObjectId(id)})
    # return jsonify(request)
    return render_template("request.html")
