from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """Hash a plaintext password."""
    return generate_password_hash(password)

def verify_password(hashed_password, plain_password):
    """Check if a hashed password matches the plaintext password."""
    return check_password_hash(hashed_password, plain_password)

def generate_token(email):
    """Generate a JWT token for the user."""
    return create_access_token(identity=email)
