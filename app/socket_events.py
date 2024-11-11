from flask_socketio import emit
from .extentions import socketio
from . import open_ai_client

@socketio.on('chat')
def handle_chat(message):
    print(message)
    response = open_ai_client.get_openai_response(message)
    emit('chat_response', response)



