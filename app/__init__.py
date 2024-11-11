from flask import Flask
from .services.openai import OpenAIClient
from .config import Config
from .extentions import socketio

app = Flask(__name__)
app.config.from_object(Config)
with app.app_context():
    open_ai_client = OpenAIClient()
socketio.init_app(app)
from .routes import main
app.register_blueprint(main)

from .socket_events import handle_chat

def create_app():
    return app
