from flask import Flask
from config import Config
from extensions import db, bcrypt, migrate
from routes.auth_routes import auth_bp
# from routes.note_routes import note_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(note_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)