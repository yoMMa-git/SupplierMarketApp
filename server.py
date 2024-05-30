from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
socketio = SocketIO(app)

clients = []  # just the nicknames
nicknames = {}  # map client IDs to nicknames
lobby_clients = set()  # Set to keep track of clients in the lobby (as fas as AI said c: )

ROOM_NAME = 'MainLobby'
game_start = False

@socketio.on('connect')
def connect_user():
    client_id = request.sid
    clients.append(client_id)
    print("A new user just connected: ", client_id)
    #emit('connected', room=client_id)


@socketio.on('register')
def register_user(data):
    print(data)
    client_id = data['sid']
    login = data['nickname']
    join_room(client_id)
    if login in nicknames.values():
        emit('nickname_response', {'response': 'exists'}, room=client_id)
        leave_room(client_id)
    else:
        emit('nickname_response', {'response': 'success'}, room=client_id)
        nicknames[client_id] = login
        print(nicknames)
        if len(nicknames.values()) > 2:
            game_start = True
        join_room(room=ROOM_NAME)
        data = [name for name in nicknames.values()]
        emit('lobby_update', {'nicknames': data}, room=ROOM_NAME)


if __name__ == '__main__':
    socketio.run(app, host='25.29.145.179', port=5001, allow_unsafe_werkzeug=True)
