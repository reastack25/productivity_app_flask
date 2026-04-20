from flask import Blueprint, request, jsonify, session
from models.note import Note
from extensions import db
from utils.helper import login_required

note_bp = Blueprint("notes", __name__)

# GET ALL NOTES (with pagination)
@note_bp.route("/notes", methods=["GET"])
@login_required
def get_notes():
    user_id = session["user_id"]

    page = int(request.args.get("page", 1))
    per_page = 5

    notes = Note.query.filter_by(user_id=user_id)\
        .paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "data": [
            {"id": n.id, "title": n.title, "content": n.content}
            for n in notes.items
        ],
        "total": notes.total,
        "pages": notes.pages
    })


# CREATE
@note_bp.route("/notes", methods=["POST"])
@login_required
def create_note():
    data = request.json

    note = Note(
        title=data["title"],
        content=data["content"],
        user_id=session["user_id"]
    )

    db.session.add(note)
    db.session.commit()

    return jsonify({"message": "Note created"}), 201


# UPDATE
@note_bp.route("/notes/<int:id>", methods=["PATCH"])
@login_required
def update_note(id):
    note = Note.query.get(id)

    if note.user_id != session["user_id"]:
        return jsonify({"error": "Forbidden"}), 403

    data = request.json
    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)

    db.session.commit()

    return jsonify({"message": "Updated"})


# DELETE
@note_bp.route("/notes/<int:id>", methods=["DELETE"])
@login_required
def delete_note(id):
    note = Note.query.get(id)

    if note.user_id != session["user_id"]:
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(note)
    db.session.commit()

    return jsonify({"message": "Deleted"})