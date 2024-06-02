import tkinter as tk
from tkinter import ttk, messagebox, StringVar
from tkinter.font import Font
from PIL import Image, ImageTk
import socketio
import threading

from interface import draw_game_ui, draw_judge_ui

sio = socketio.Client()
HOST, PORT = '25.29.145.179', 5001
root = tk.Tk()
frame = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

main_font = Font(family='Stem', weight='bold', size=21)
list_font = Font(family='Stem', size=12)

fonts = {'main_font': main_font, 'list_font': list_font}

icon = ImageTk.PhotoImage(Image.open('misc/icon.png').resize((145, 247)))  # Загрузка картинки


def update_value(widget, array, index, change):
    if not (array[index] + change < 5 or array[index] + change > 30):
        array[index] += change
        widget.config(text=str(array[index]))


def send_values(values, button):
    button.config(state=tk.DISABLED)
    for i in range(len(values)):
        print(values[i], end='\t')
    print()


def send_rates(rates, button_rates):
    button_rates.config(state=tk.DISABLED)  # блокируем кнопку
    numbers = []  # массив, в котором будем хранить ЧИСЛЕННЫЕ значения
    success = True  # флаг успешности конвертации
    for elem in rates:
        if not elem.get().isdigit():  # если введено число
            success = False
        else:
            numbers.append(int(elem.get()))
    if success:  # если все значения - числа
        rates = numbers.copy()
    else:
        button_rates.config(state=tk.NORMAL)
    return success


def on_button_click(entry_field):  # отправка никнейма
    entered_text = entry_field.get()
    print(f"You entered: {entered_text}")
    sio.emit('register', {'nickname': entered_text, 'sid': str(sio.sid)})

    @sio.on('nickname_response')  # ожидание ответа по доступности никнейма
    def checkNick(data):
        print("Got response!")
        if data['response'] == 'exists':
            messagebox.showwarning(message="This nickname already exists!")
        elif data['response'] == 'success':
            # messagebox.showinfo(message="OK! Changing UI...")
            frame.pack_forget()

            new_label = ttk.Label(frame2, text='Ожидание игроков...', font=main_font)
            new_label.pack(pady=10)

            listbox = tk.Listbox(frame2, font=list_font)
            listbox.pack(pady=10, fill=tk.BOTH, padx=20)

            scrollbar = ttk.Scrollbar(listbox, orient='vertical', command=listbox.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            icon_label = ttk.Label(frame2, image=icon)
            icon_label.pack(pady=10)

            listbox['yscrollcommand'] = scrollbar.set

            frame2.pack()

            @sio.on('lobby_update')  # если подключился/отключился новый игрок - сервер присылает обновленный список
            def logging(data):
                listbox.delete(0, listbox.size() - 1)
                for name in data['nicknames']:
                    listbox.insert(0, name)

            @sio.on('start_game')  # получение сигнала о старте игры
            def start_game(data):
                role = data['role']
                frame2.pack_forget()
                root.geometry('1080x720')
                if role == 'player':

                    wait_label = ttk.Label(frame3, text='Ожидайте выбора тематики игры! (роль: ПОСТАВЩИК)',
                                           font=main_font)
                    wait_label.grid(row=0, columnspan=5)

                    frame3.pack(anchor=tk.CENTER)

                    @sio.on('game_info')  # получение тематики игры и её старт
                    def draw_scales(data):
                        theme = data['theme']
                        wait_label.config(text=f"Тема текущей игры: {str(theme).lower()} (ПОСТАВЩИК)", font=main_font)

                        values = [5, 5, 5, 5, 5]
                        balance = [100 - sum(values)]

                        draw_game_ui(frame3, values, balance, fonts)
                        button_accept = ttk.Button(frame3, text='Отправить распределение',
                                                   command=lambda: send_values(values, button_accept))
                        button_accept.grid(column=2, row=12, sticky=tk.NSEW)
                elif role == 'judge':

                    wait_label = ttk.Label(frame3, text='Ожидайте выбора тематики игры! (роль: ЭКСПЕРТ)',
                                           font=main_font)
                    wait_label.grid(row=0, columnspan=5)

                    frame3.pack(anchor=tk.CENTER)

                    @sio.on('game_info')
                    def draw_scales(data):
                        theme = data['theme']
                        wait_label.config(text=f"Тема текущей игры: {str(theme).lower()} (ЭКСПЕРТ)", font=main_font)

                        rates = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                                 StringVar(), StringVar(), StringVar(), StringVar()]

                        draw_judge_ui(frame3, rates, fonts)

                        button_rates = ttk.Button(frame3, text='Отправить оценку',
                                                  command=lambda: send_rates(rates, button_rates))
                        button_rates.grid(row=12, columnspan=5)


def mainWindow():  # главное меню
    sio.connect('http://25.29.145.179:5001')

    root.title("Бизнес-игра")
    root.geometry("400x500")
    root.iconbitmap('misc/window_icon.ico')

    entry_label = ttk.Label(frame, text='Добро пожаловать!\nВведите логин:', font=main_font)
    entry_label.pack(pady=10)

    entry_field = ttk.Entry(frame, width=40)
    entry_field.pack(pady=10)

    button = ttk.Button(frame, text="Войти", command=lambda entry=entry_field: on_button_click(entry))
    button.pack(pady=10)

    icon_label = ttk.Label(frame, image=icon)
    icon_label.pack(pady=10)

    frame.pack()

    root.mainloop()


if __name__ == '__main__':
    threading.Thread(target=mainWindow()).start()

# окно запускается в созданном потоке, потому что в ходе эксперимента было установлено, что это необходимо для
# грамотной параллельной работы сокета и интерфейса
