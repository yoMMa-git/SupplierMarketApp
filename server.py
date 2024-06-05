from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room, emit, rooms
import time
import random

from game_math import calculate_everything, get_cofs

app = Flask(__name__)
socketio = SocketIO(app)

clients = []  # ID клиентов
nicknames = {}  # словарь ID-никнейм

ADMIN_ID = None  # ID админа
JUDGE_ID = None  # ID экспертной комиссии

ROOM_NAME = 'MainLobby'  # название главного лобби

game_start = False  # трекер старта игры
game_result = False  # трекер результатов игры (необходимо для завершения игры)
theme = None  # тема партии
current_round = 1  # текущий номер раунда

player_values = {}  # словарь ID-оценки
judge_rates = []
current_results = {}


def random_user(players):
    index = random.randint(0, len(players.values()) - 1)
    return list(players.keys())[index]


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
    if not game_start:  # регистрируем и добавляем пользователей, пока игра ещё не стартовала
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
            emit('lobby_update', {'nicknames': data}, to=ADMIN_ID)


@socketio.on('admin_game_start')  # когда админ подаёт команду старта
def start_game():
    global game_start, JUDGE_ID
    game_start = True
    time.sleep(1)
    JUDGE_ID = random_user(nicknames)  # случайное определение экспертной комиссии
    leave_room(room=ROOM_NAME, sid=JUDGE_ID)
    emit('start_game', {'role': 'player'}, room=ROOM_NAME)
    emit('start_game', {'role': 'judge'}, to=JUDGE_ID)


@socketio.on('game_theme')  # событие получения выбранной темы от админа
def start_game(data):
    global game_start, theme
    if game_start:  # если игра началась TODO: обработка преждевременной отправки темы
        theme = data['theme']
        emit('game_info', {'theme': theme, 'round': current_round}, to=list(nicknames.keys()))


@socketio.on('send_values')
def add_values(data):
    global judge_rates, player_values, JUDGE_ID, game_result, current_results
    print("Got values!")
    values = data['values']
    player_values[request.sid] = values
    if len(player_values.keys()) == len(nicknames.keys()) - 1:  # -1, потому что есть эксперты
        emit('wait_for_rates', room=ROOM_NAME)
        if len(judge_rates) > 0:
            current_results = calculate_everything(player_values, judge_rates)
            game_result = True
            emit('game_results', {'round': current_round, 'data': current_results, 'nicknames': nicknames},
                 to=list(nicknames.keys()))


@socketio.on('send_rates')
def add_rates(data):
    print("Got rates!")
    global judge_rates, player_values, game_result, current_results
    judge_rates = data['rates']
    if len(player_values.keys()) == len(nicknames.keys()) - 1:
        current_results = calculate_everything(player_values, judge_rates)
        game_result = True
        emit('game_results', {'round': current_round, 'data': current_results, 'nicknames': nicknames},
             to=list(nicknames.keys()))


@socketio.on('next_round')
def next_round():
    global current_round, player_values, judge_rates, JUDGE_ID, game_result
    print(f"NEXT ROUND: {current_round + 1}!")
    game_result = False
    if game_start:  # если игра в процессе
        current_round += 1
        for player in player_values.keys():
            emit('game_info', {'theme': theme, 'round': current_round, 'values': player_values[player]}, to=player)
        emit('game_info', {'theme': theme, 'round': current_round, 'rates': judge_rates, 'state': 'locked'},
             to=JUDGE_ID)


@socketio.on('get_rate')
def send_rate(data):
    global judge_rates
    player = request.sid
    number = data['number']
    socketio.emit('set_rate', {'number': number, 'value': get_cofs(judge_rates)[number]}, to=player)


@socketio.on('finish')
def finish():
    global game_result, game_start
    if game_result:
        game_result = False
        game_start = False
        print(current_results)
        print(player_values)
        print(nicknames)
        emit('finish', {'data': current_results, 'nicknames': nicknames}, to=clients)


if __name__ == '__main__':
    socketio.run(app, host='25.29.145.179', port=5001, allow_unsafe_werkzeug=True)
