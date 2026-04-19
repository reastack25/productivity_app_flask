from extensions import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)