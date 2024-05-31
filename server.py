from flask import Flask, request, session
from flask_socketio import SocketIO, join_room, leave_room, emit, rooms
import time

app = Flask(__name__)
socketio = SocketIO(app)

clients = []  # just the nicknames
nicknames = {}  # map client IDs to nicknames
lobby_clients = set()  # Set to keep track of clients in the lobby (as fas as AI said c: )

ROOM_NAME = 'MainLobby'
game_start = False


@socketio.on('connect')
def connect_user():
    client_id = request.sid  # getting SID of user
    clients.append(client_id)  # adding this SID (no idea what for)
    print("A new user just connected: ", client_id)  # logging


@socketio.on('disconnect')
def disconnect_user():
    client_id = request.sid  # getting SID of user
    try:
        nicknames.pop(client_id)
    except KeyError:
        pass
    clients.remove(client_id)  # removing it from list of active clients
    print("A user just disconnected: ", client_id)  # logging


@socketio.on('register')
def register_user(data):
    print("Registration event: ", request.sid)  # logging
    client_id = request.sid
    login = data['nickname']  # getting login from
    join_room(client_id)
    if login in nicknames.values():
        emit('nickname_response', {'response': 'exists'}, room=client_id)
        leave_room(client_id)
    else:
        emit('nickname_response', {'response': 'success'}, room=client_id)
        nicknames[client_id] = login
        if len(nicknames.values()) > 2:
            game_start = True
        join_room(room=ROOM_NAME)
        data = [name for name in nicknames.values()]
        time.sleep(1)
        emit('lobby_update', {'nicknames': data}, room=client_id)
        print("Current rooms user in:", rooms(client_id))


if __name__ == '__main__':
    socketio.run(app, host='25.29.145.179', port=5001, allow_unsafe_werkzeug=True)
