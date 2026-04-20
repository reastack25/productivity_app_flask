from app import app
from extensions import db
from models.user import User
from models.note import Note

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(email="morty@rick.com")
    user.set_password("123423455")

    db.session.add(user)
    db.session.commit()

    note1 = Note(title="First Note", content="Hello", user_id=user.id)
    note2 = Note(title="Second Note", content="World", user_id=user.id)

    db.session.add_all([note1, note2])
    db.session.commit()

    print("Seeded!")