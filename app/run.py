from app import create_app, socketio

app = create_app()

def start_server():
    socketio.run(app, debug=True)


if __name__ == '__main__':
    start_server()
