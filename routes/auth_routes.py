from flask import Blueprint, request, jsonify, session
from extensions import db
from models.user import User

auth_bp = Blueprint("auth", __name__)

# SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    user = User(email=data["email"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    session["user_id"] = user.id
    return jsonify({"message": "Logged in"}), 200


# LOGOUT
@auth_bp.route("/logout", methods=["DELETE"])
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out"}), 200


# CHECK SESSION
@auth_bp.route("/me", methods=["GET"])
def me():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    user = User.query.get(user_id)

    return jsonify({
        "id": user.id,
        "email": user.email
    }), 200