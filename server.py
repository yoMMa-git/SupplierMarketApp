from flask import Flask, request, session
from flask_socketio import SocketIO, join_room, leave_room, emit, rooms
import time

app = Flask(__name__)
socketio = SocketIO(app)

clients = []  # ID клиентов
nicknames = {}  # словарь ID-никнейм

ADMIN_ID = None  # ID админа

ROOM_NAME = 'MainLobby'  # название главного лобби
game_start = False  # трекер старта игры


@socketio.on('connect')
def connect_user():
    client_id = request.sid  # получение SID пользователя
    clients.append(client_id)  # добавление в массив SID клиентов
    print("A new user just connected: ", client_id)  # логгинг


@socketio.on('admin_login')
def set_admin_id():
    print("An admin just joined!")  # логгинг
    global ADMIN_ID
    ADMIN_ID = request.sid  # установка SID админа
    emit('lobby_update', {'nicknames': [name for name in nicknames.values()]}, to=ADMIN_ID)


@socketio.on('disconnect')  # событие отключения (закрытие приложения, вылет и т.п.)
def disconnect_user():
    client_id = request.sid  # получение SID пользователя
    try:  # try-except используется для обработки случаев преждевременного отключения (т.е. перед вводом никнейма)
        nicknames.pop(client_id)  # удаление пользователя (включая его никнейм)
    except KeyError:
        pass
    clients.remove(client_id)  # удаление пользователя (только SID)
    print("A user just disconnected: ", client_id)  # логгинг
    emit('lobby_update', {'nicknames': [name for name in nicknames.values()]}, room=ROOM_NAME)
    emit('lobby_update', {'nicknames': [name for name in nicknames.values()]}, to=ADMIN_ID)  # события для обновления
    # списка игроков (клиент) или количества игроков (админ)


@socketio.on('register')  # событие регистрации (клиент нажал кнопку "Зарегистрироваться")
def register_user(data):
    global game_start
    print("Registration event: ", request.sid)
    client_id = request.sid
    login = data['nickname']
    join_room(client_id)  # подключение к комнате (для индивидуальных сообщений)
    if login in nicknames.values():  # если никнейм существует
        emit('nickname_response', {'response': 'exists'}, room=client_id)
        leave_room(client_id)  # выход из комнаты (т.к. требуется перерегистрация)
    else:
        emit('nickname_response', {'response': 'success'}, room=client_id)
        nicknames[client_id] = login  # прикрепление логина к SID
        join_room(room=ROOM_NAME)  # подключение к общему каналу
        data = [name for name in nicknames.values()]
        time.sleep(1)  # в целях обеспечения корректности работы даём время клиенту на отрисовку/включение слушателя
        emit('lobby_update', {'nicknames': data}, room=ROOM_NAME)  # событие перерисовки списка/счётчика клиентов
        try:
            emit('lobby_update', {'nicknames': data}, to=ADMIN_ID)
        except:
            pass
        print("Current rooms user in:", rooms(client_id))
        if 2 == len(nicknames.values()):  # TODO: сделать старт игры по команде от админа
            game_start = True
            #time.sleep(1)
            #emit('start_game', room=ROOM_NAME)


@socketio.on('admin_game_start')
def start_game():
    time.sleep(1)
    emit('start_game', room=ROOM_NAME)


@socketio.on('game_theme')  # событие получения выбранной темы от админа
def start_game(data):
    global game_start
    if game_start:  # если игра началась TODO: обработка преждевременной отправки темы
        theme = data['theme']
        emit('game_info', {'theme': theme}, room=ROOM_NAME)


if __name__ == '__main__':
    socketio.run(app, host='25.29.145.179', port=5001, allow_unsafe_werkzeug=True)
