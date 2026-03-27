from flask import Flask
from flask_cors import CORS

from app.routes.instituicoes import instituicoes_bp
from app.routes.usuarios import usuarios_bp
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(instituicoes_bp, url_prefix="/api")
    app.register_blueprint(usuarios_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return {"message": "API DoarCuidar rodando 🚀"}

    return app