import tkinter as tk
from tkinter import ttk, messagebox, StringVar
from tkinter.font import Font
from PIL import Image, ImageTk
import socketio
import threading

from interface import draw_game_ui, draw_judge_ui, draw_results_ui, draw_graphics_ui

sio = socketio.Client()
HOST, PORT = '25.29.145.179', 5001
root = tk.Tk()
frame = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
final_frame = tk.Frame(root)

main_font = Font(family='Stem', weight='bold', size=21)
list_font = Font(family='Stem', size=12)

fonts = {'main_font': main_font, 'list_font': list_font}

icon = ImageTk.PhotoImage(Image.open('misc/icon.png').resize((145, 247)))  # Загрузка картинки

current_round = 1
counter = 0


def get_rate(value, buttons, frame):
    global counter
    if counter != 2:
        counter += 1
        buttons[value].config(state=tk.DISABLED)
        sio.emit('get_rate', {'number': value})
        if counter == 2:
            for button in buttons:
                button.config(state=tk.DISABLED)


def update_value(widget, array, index, change):
    if not (array[index] + change < 5 or array[index] + change > 30):
        array[index] += change
        widget.config(text=str(array[index]))


def send_values(values, button):  # разница функций возникает из-за разницы интерфейсов игрока и экспертизы
    button.config(state=tk.DISABLED)
    sio.emit('send_values', {'values': values})


def next_round():
    sio.emit('next_round')


def forget_every_frame():
    try:
        frame.pack_forget()
        frame2.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
    except Exception as e:
        print(e)


def send_rates(rates, button_rates):
    print("Button has been pressed!")
    print(rates)
    button_rates.config(state=tk.DISABLED)  # блокируем кнопку
    sio.emit('send_rates', {'rates': rates})


def on_button_click(entry_field):  # отправка никнейма
    entered_text = entry_field.get()
    print(f"You entered: {entered_text}")
    sio.emit('register', {'nickname': entered_text, 'sid': str(sio.sid)})

    @sio.on('nickname_response')  # ожидание ответа по доступности никнейма
    def checkNick(data):
        #print("Got response!")
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

                        try:
                            frame4.pack_forget()
                            frame3.pack(anchor=tk.CENTER)
                        except Exception as e:
                            print(e)

                        print("Got response GAME_INFO!")

                        global current_round
                        theme = data['theme']

                        try:
                            current_round = data['round']
                        except KeyError:
                            current_round = 1
                        wait_label.config(
                            text=f"Тема текущей игры: {str(theme).lower()} (ПОСТАВЩИК), раунд {current_round}",
                            font=main_font)

                        try:
                            values = data['values']
                        except KeyError:
                            values = [5, 5, 5, 5, 5]
                        balance = [100 + (50 * (current_round - 1)) - sum(values)]

                        draw_game_ui(frame3, values, balance, fonts)

                        button_accept = ttk.Button(frame3, text='Отправить распределение',
                                                   command=lambda: send_values(values, button_accept))
                        button_accept.grid(column=2, row=12, sticky=tk.NSEW)

                        if current_round != 1:
                            button_first = ttk.Button(frame3, text='Объем поставки',
                                                      command=lambda: get_rate(0, buttons, frame3), width=20)
                            button_second = ttk.Button(frame3, text='Срок поставки',
                                                       command=lambda: get_rate(1, buttons, frame3), width=20)
                            button_third = ttk.Button(frame3, text='Цена за штуку',
                                                      command=lambda: get_rate(2, buttons, frame3), width=20)
                            button_fourth = ttk.Button(frame3, text='Отклонения от графика платежей',
                                                       command=lambda: get_rate(3, buttons, frame3), width=20)
                            button_fifth = ttk.Button(frame3, text='Виды упаковки',
                                                      command=lambda: get_rate(4, buttons, frame3), width=20)
                            buttons = [button_first, button_second, button_third, button_fourth, button_fifth]
                            frame3.rowconfigure(index=13, weight=1)
                            button_first.grid(column=0, row=14, sticky=tk.NSEW)
                            button_second.grid(column=1, row=14, sticky=tk.NSEW)
                            button_third.grid(column=2, row=14, sticky=tk.NSEW)
                            button_fourth.grid(column=3, row=14, sticky=tk.NSEW)
                            button_fifth.grid(column=4, row=14, sticky=tk.NSEW)

                            @sio.on('set_rate')
                            def set_rate(data):
                                try:
                                    number = data['number']
                                    value = data['value']
                                    value_label = ttk.Label(frame3, text=str(round(value * 100, 2)) + "%",
                                                            font=list_font)
                                    value_label.grid(column=number, row=14, sticky=tk.NSEW)
                                except KeyError:
                                    pass

                    @sio.on('wait_for_rates')
                    def lock_everything():
                        wait_label.config(text="Ожидайте предвраительного подсчёта...")

                    @sio.on('game_results')
                    def print_data(data):
                        print('Got response about results!')

                        frame3.pack_forget()

                        frame4.pack(anchor=tk.CENTER)

                        draw_results_ui(data, frame4, fonts)

                    @sio.on('finish')
                    def finish_game(data):
                        forget_every_frame()
                        root.geometry("400x500")

                        bye_message = ttk.Label(final_frame, text='Спасибо за участие!', font=main_font)
                        bye_message.pack(pady=10)

                        text = ""
                        try:
                            stats = data['data']
                            for player in stats:
                                text += f"{data['nicknames'][player]}: {stats[player]}%\n"
                            final_list = ttk.Label(final_frame, text=text, font=list_font)
                            final_list.pack(pady=10)
                        except KeyError:
                            pass

                        icon_bye = ttk.Label(final_frame, image=icon)
                        icon_bye.pack(pady=10)

                        pie_graph_button = ttk.Button(final_frame, text='Круговая диаграмма',
                                                      command=lambda: draw_graphics_ui(data))
                        pie_graph_button.pack(pady=10)

                        final_frame.pack()

                elif role == 'judge':

                    print("Got response GAME_INFO!")

                    wait_label = ttk.Label(frame3, text='Ожидайте выбора тематики игры! (роль: ЭКСПЕРТ)',
                                           font=main_font)
                    wait_label.grid(row=0, columnspan=5)

                    frame3.pack(anchor=tk.CENTER)

                    @sio.on('game_info')
                    def draw_scales(data):

                        try:
                            frame4.pack_forget()
                            frame3.pack(anchor=tk.CENTER)
                        except Exception as e:
                            print(e)

                        theme = data['theme']
                        wait_label.config(text=f"Тема текущей игры: {str(theme).lower()} (ЭКСПЕРТ)", font=main_font)

                        try:
                            rates = data['rates']
                        except KeyError:
                            rates = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                                     StringVar(), StringVar(), StringVar(), StringVar()]
                            draw_judge_ui(frame3, rates, fonts, False)

                            button_rates = ttk.Button(frame3, text='Отправить оценку',
                                                      command=lambda: send_rates(rates, button_rates))
                            button_rates.grid(row=12, columnspan=5)
                        else:
                            text_rates = []
                            for elem in rates:
                                text_rates.append(StringVar(value=str(elem)))
                            draw_judge_ui(frame3, text_rates, fonts, True)

                            button_rates = ttk.Button(frame3, text='Отправить оценку', state=tk.DISABLED)
                            button_rates.grid(row=12, columnspan=5)

                    @sio.on('game_results')
                    def print_data(data):
                        frame3.pack_forget()
                        frame4.pack(anchor=tk.CENTER)

                        draw_results_ui(data, frame4, fonts)

                        next_button = ttk.Button(frame4, text='Следующий раунд', command=next_round)
                        next_button.grid(row=35, columnspan=5)

                    @sio.on('finish')
                    def finish_game(data):
                        forget_every_frame()
                        root.geometry("400x500")

                        bye_message = ttk.Label(final_frame, text='Спасибо за участие!', font=main_font)
                        bye_message.pack(pady=10)

                        text = ""
                        try:
                            stats = data['data']
                            for player in stats:
                                text += f"{data['nicknames'][player]}: {stats[player]}%\n"
                            final_list = ttk.Label(final_frame, text=text, font=list_font)
                            final_list.pack(pady=10)
                        except KeyError:
                            pass

                        icon_bye = ttk.Label(final_frame, image=icon)
                        icon_bye.pack(pady=10)

                        pie_graph_button = ttk.Button(final_frame, text='Круговая диаграмма',
                                                      command=lambda: draw_graphics_ui(data))
                        pie_graph_button.pack(pady=10)

                        final_frame.pack()


def mainWindow():  # главное меню
    sio.connect('http://25.29.145.179:5001')

    root.title("Бизнес-игра")
    root.geometry("400x500")
    root.iconbitmap('misc/window_icon.ico')
    root.resizable(False, False)

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
