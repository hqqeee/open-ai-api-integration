from flask import Flask, current_app
from .config import Config
from flask_socketio import SocketIO
from .services.openai import OpenAIClient

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    with app.app_context():
        socketio.init_app(app)
        from .socket_events import handle_chat

    from .routes import main
    app.register_blueprint(main)

    return app
