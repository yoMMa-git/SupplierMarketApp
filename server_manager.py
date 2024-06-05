import tkinter as tk
from tkinter.ttk import Label, Button, Combobox
from tkinter.font import Font
import socketio
import threading
import time


def send_theme():  # отправка тематики партии и блокировка кнопки
    time.sleep(1)
    sio.emit('game_theme', data={'theme': combox.get()})
    second_button.config(state=tk.DISABLED)
    third_button.config(state=tk.NORMAL)


def start_game():
    first_button.config(state=tk.DISABLED)
    sio.emit('admin_game_start')
    second_button.config(state=tk.NORMAL)


def finish_game():
    first_button.config(state=tk.DISABLED)
    second_button.config(state=tk.DISABLED)
    third_button.config(state=tk.DISABLED)
    sio.emit('finish')


size = 0
ALLOWED_PLAYERS = 2

sio = socketio.Client()
ROOM_NAME = 'MainLobby'

themes = ['Бытовая техника', 'Мебель', 'Одежда', 'Алкогольные напитки', 'Косметика']

sio.connect('http://25.29.145.179:5001')
sio.emit('admin_login')


@sio.on('lobby_update')
def update_data(data):  # перерисовка счётчика игроков и разблокировка кнопки, если набралось достаточно участников
    global size
    print("Got response!")
    size = len(data['nicknames'])
    if size >= ALLOWED_PLAYERS:
        first_button.config(state=tk.NORMAL)
    else:
        first_button.config(state=tk.DISABLED)
    players_count.config(text=f"Количество игроков: {size}")


root = tk.Tk()
root.title('Панель управления')
root.geometry('600x400')

main_font = Font(family='Times New Roman', size=24)
button_font = Font(family='Times New Roman', size=12)

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)

root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=2)

players_count = Label(text='Количество игроков: 0', font=main_font)
players_count.grid(row=0, column=1)

combox = Combobox(root, values=themes)
combox.grid(row=1, column=1)

first_button = Button(root, text='Начать игру', command=start_game, state=tk.DISABLED)
first_button.grid(row=2, column=0)

second_button = Button(root, text='Отправить тематику', command=send_theme, state=tk.DISABLED)
second_button.grid(row=2, column=1)

third_button = Button(root, text='Завершить игру', command=finish_game, state=tk.DISABLED)
third_button.grid(row=2, column=2)

threading.Thread(target=root.mainloop()).start()
