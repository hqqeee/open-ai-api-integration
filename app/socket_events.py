from flask_socketio import emit
from flask import request
from .extentions import socketio
from . import open_ai_client

@socketio.on('chat')
def handle_chat(message):
    print(request.sid)
    response = open_ai_client.get_openai_response(message, request.sid)
    emit('chat_response', response)

@socketio.on('connect')
def handle_connect():
    open_ai_client.open_session(request.sid)
    print(f"Client with SID {request.sid} connected")

@socketio.on('disconnect')
def handle_disconnect():
    open_ai_client.close_session(request.sid)
    print(f"Client with SID {request.sid} disconnected. Session cleaned")
