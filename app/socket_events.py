from flask_socketio import emit
from . import socketio
from .services.openai import OpenAIClient

openAiClient = OpenAIClient()

@socketio.on('chat')
def handle_chat(message):
    response = openAiClient.get_openai_response(message)
    emit('chat_response', response)
