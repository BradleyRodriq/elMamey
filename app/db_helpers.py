from pymongo import MongoClient
import os

db_connection_string = os.environ.get("MONGO_DB")

client = MongoClient(db_connection_string)
db = client["your_database_name"]
users_collection = db["users"]

def add_user(user):
    """Insert a new user into the database."""
    users_collection.insert_one(user)

def find_user_by_email(email):
    """Retrieve a user from the database by email."""
    return users_collection.find_one({"email": email})
