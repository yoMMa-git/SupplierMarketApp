import tkinter as tk
from tkinter import ttk

scale_labels = {
    0: 1 / 9,
    1: 1 / 8,
    2: 1 / 7,
    3: 1 / 6,
    4: 1 / 5,
    5: 1 / 4,
    6: 1 / 3,
    7: 1 / 2,
    8: 1,
    9: 2,
    10: 3,
    11: 4,
    12: 5,
    13: 6,
    14: 7,
    15: 8,
    16: 9
}


#scale_labels = [1 / 9, 1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 1 / 3, 1 / 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def update_value(widget, array, index, change, balance, balanceLabel):
    if (balance[0] - change) >= 0 and (array[index] + change) >= 0:
        array[index] += change
        balance[0] -= change
        widget.config(text=str(array[index]))
        balanceLabel.config(text=f"Баланс: {str(balance[0])}")


def scales(scale, array, index):
    array[index] = scale_labels[int(scale.get())]
    if int(scale.get()) <= 7:
        scale.config(label=f"1/{9 - int(scale.get())}")
    elif int(scale.get()) > 7:
        scale.config(label=scale_labels[int(scale.get())])


def draw_game_ui(frame, values, balance, fonts):  # поменять frame на frame3 при копировании в client.py
    label_scale_1 = ttk.Label(frame, text='Объем поставки', font=fonts['list_font'])
    scale_1 = ttk.Label(frame, text=str(values[0]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_1 = ttk.Button(frame, text='-5',
                              command=lambda: update_value(scale_1, values, 0, -5, balance, balanceLabel))
    btn_minus1_1 = ttk.Button(frame, text='-1',
                              command=lambda: update_value(scale_1, values, 0, -1, balance, balanceLabel))
    btn_plus1_1 = ttk.Button(frame, text='+1',
                             command=lambda: update_value(scale_1, values, 0, 1, balance, balanceLabel))
    btn_plus5_1 = ttk.Button(frame, text='+5',
                             command=lambda: update_value(scale_1, values, 0, 5, balance, balanceLabel))

    label_scale_1.grid(column=2, row=1)
    btn_minus5_1.grid(column=0, row=2, sticky=tk.E)
    btn_minus1_1.grid(column=1, row=2, sticky=tk.E)
    scale_1.grid(column=2, row=2, sticky=tk.NSEW)
    btn_plus1_1.grid(column=3, row=2, sticky=tk.W)
    btn_plus5_1.grid(column=4, row=2, sticky=tk.W)

    label_scale_2 = ttk.Label(frame, text='Срок поставки', font=fonts['list_font'])
    scale_2 = ttk.Label(frame, text=str(values[1]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_2 = ttk.Button(frame, text='-5',
                              command=lambda: update_value(scale_2, values, 1, -5, balance, balanceLabel))
    btn_minus1_2 = ttk.Button(frame, text='-1',
                              command=lambda: update_value(scale_2, values, 1, -1, balance, balanceLabel))
    btn_plus1_2 = ttk.Button(frame, text='+1',
                             command=lambda: update_value(scale_2, values, 1, 1, balance, balanceLabel))
    btn_plus5_2 = ttk.Button(frame, text='+5',
                             command=lambda: update_value(scale_2, values, 1, 5, balance, balanceLabel))

    label_scale_2.grid(column=2, row=3)
    btn_minus5_2.grid(column=0, row=4, sticky=tk.E)
    btn_minus1_2.grid(column=1, row=4, sticky=tk.E)
    scale_2.grid(column=2, row=4, sticky=tk.NSEW)
    btn_plus1_2.grid(column=3, row=4, sticky=tk.W)
    btn_plus5_2.grid(column=4, row=4, sticky=tk.W)

    label_scale_3 = ttk.Label(frame, text='Цена за штуку', font=fonts['list_font'])
    scale_3 = ttk.Label(frame, text=str(values[2]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_3 = ttk.Button(frame, text='-5',
                              command=lambda: update_value(scale_3, values, 2, -5, balance, balanceLabel))
    btn_minus1_3 = ttk.Button(frame, text='-1',
                              command=lambda: update_value(scale_3, values, 2, -1, balance, balanceLabel))
    btn_plus1_3 = ttk.Button(frame, text='+1',
                             command=lambda: update_value(scale_3, values, 2, 1, balance, balanceLabel))
    btn_plus5_3 = ttk.Button(frame, text='+5',
                             command=lambda: update_value(scale_3, values, 2, 5, balance, balanceLabel))

    label_scale_3.grid(column=2, row=5)
    btn_minus5_3.grid(column=0, row=6, sticky=tk.E)
    btn_minus1_3.grid(column=1, row=6, sticky=tk.E)
    scale_3.grid(column=2, row=6, sticky=tk.NSEW)
    btn_plus1_3.grid(column=3, row=6, sticky=tk.W)
    btn_plus5_3.grid(column=4, row=6, sticky=tk.W)

    label_scale_4 = ttk.Label(frame, text='Отклонения от графика платежей', font=fonts['list_font'])
    scale_4 = ttk.Label(frame, text=str(values[3]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_4 = ttk.Button(frame, text='-5',
                              command=lambda: update_value(scale_4, values, 3, -5, balance, balanceLabel))
    btn_minus1_4 = ttk.Button(frame, text='-1',
                              command=lambda: update_value(scale_4, values, 3, -1, balance, balanceLabel))
    btn_plus1_4 = ttk.Button(frame, text='+1',
                             command=lambda: update_value(scale_4, values, 3, 1, balance, balanceLabel))
    btn_plus5_4 = ttk.Button(frame, text='+5',
                             command=lambda: update_value(scale_4, values, 3, 5, balance, balanceLabel))

    label_scale_4.grid(column=2, row=7)
    btn_minus5_4.grid(column=0, row=8, sticky=tk.E)
    btn_minus1_4.grid(column=1, row=8, sticky=tk.E)
    scale_4.grid(column=2, row=8, sticky=tk.NSEW)
    btn_plus1_4.grid(column=3, row=8, sticky=tk.W)
    btn_plus5_4.grid(column=4, row=8, sticky=tk.W)

    label_scale_5 = ttk.Label(frame, text='Виды упаковки', font=fonts['list_font'])
    scale_5 = ttk.Label(frame, text=str(values[4]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_5 = ttk.Button(frame, text='-5',
                              command=lambda: update_value(scale_5, values, 4, -5, balance, balanceLabel))
    btn_minus1_5 = ttk.Button(frame, text='-1',
                              command=lambda: update_value(scale_5, values, 4, -1, balance, balanceLabel))
    btn_plus1_5 = ttk.Button(frame, text='+1',
                             command=lambda: update_value(scale_5, values, 4, 1, balance, balanceLabel))
    btn_plus5_5 = ttk.Button(frame, text='+5',
                             command=lambda: update_value(scale_5, values, 4, 5, balance, balanceLabel))

    label_scale_5.grid(column=2, row=9)
    btn_minus5_5.grid(column=0, row=10, sticky=tk.E)
    btn_minus1_5.grid(column=1, row=10, sticky=tk.E)
    scale_5.grid(column=2, row=10, sticky=tk.NSEW)
    btn_plus1_5.grid(column=3, row=10, sticky=tk.W)
    btn_plus5_5.grid(column=4, row=10, sticky=tk.W)

    balanceLabel = ttk.Label(frame, text=f"Баланс: {str(balance[0])}", font=fonts['main_font'])
    balanceLabel.grid(column=2, row=11, sticky=tk.NSEW)


def draw_judge_ui(frame, rates, fonts, locked):
    state = tk.NORMAL
    if locked:
        state = tk.DISABLED

    criterias = ['Объем поставки', 'Срок поставки', 'Цена за штуку', 'Отклонения от графика платежей', 'Виды упаковки']

    for i in range(13):
        frame.rowconfigure(i, pad=10)

    label_12_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    scale_12 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_12, rates, 0),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_12_2 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])

    label_12_1.grid(row=1, column=0, sticky=tk.E)
    scale_12.grid(row=1, column=1, sticky=tk.NSEW)
    label_12_2.grid(row=1, column=2, sticky=tk.W)

    label_13_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    scale_13 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_13, rates, 1),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_13_2 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])

    label_13_1.grid(row=2, column=0, sticky=tk.E)
    scale_13.grid(row=2, column=1, sticky=tk.NSEW)
    label_13_2.grid(row=2, column=2, sticky=tk.W)

    label_14_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    scale_14 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_14, rates, 2),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_14_2 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])

    label_14_1.grid(row=3, column=0, sticky=tk.E)
    scale_14.grid(row=3, column=1, sticky=tk.NSEW)
    label_14_2.grid(row=3, column=2, sticky=tk.W)

    label_15_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    scale_15 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_15, rates, 3),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_15_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_15_1.grid(row=4, column=0, sticky=tk.E)
    scale_15.grid(row=4, column=1, sticky=tk.NSEW)
    label_15_2.grid(row=4, column=2, sticky=tk.W)

    label_23_1 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])
    scale_23 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_23, rates, 4),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_23_2 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])

    label_23_1.grid(row=5, column=0, sticky=tk.E)
    scale_23.grid(row=5, column=1, sticky=tk.NSEW)
    label_23_2.grid(row=5, column=2, sticky=tk.W)

    label_24_1 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])
    scale_24 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_24, rates, 5),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_24_2 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])

    label_24_1.grid(row=6, column=0, sticky=tk.E)
    scale_24.grid(row=6, column=1, sticky=tk.NSEW)
    label_24_2.grid(row=6, column=2, sticky=tk.W)

    label_25_1 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])
    scale_25 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_25, rates, 6),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_25_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_25_1.grid(row=7, column=0, sticky=tk.E)
    scale_25.grid(row=7, column=1, sticky=tk.NSEW)
    label_25_2.grid(row=7, column=2, sticky=tk.W)

    label_34_1 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])
    scale_34 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_34, rates, 7),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_34_2 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])

    label_34_1.grid(row=8, column=0, sticky=tk.E)
    scale_34.grid(row=8, column=1, sticky=tk.NSEW)
    label_34_2.grid(row=8, column=2, sticky=tk.W)

    label_35_1 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])
    scale_35 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_35, rates, 8),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_35_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_35_1.grid(row=9, column=0, sticky=tk.E)
    scale_35.grid(row=9, column=1, sticky=tk.NSEW)
    label_35_2.grid(row=9, column=2, sticky=tk.W)

    label_45_1 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])
    scale_45 = tk.Scale(frame, from_=min(scale_labels), to=max(scale_labels),
                        command=lambda x: scales(scale_45, rates, 9),
                        orient='horizontal', tickinterval=0, showvalue=False, state=state)
    label_45_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_45_1.grid(row=10, column=0, sticky=tk.E)
    scale_45.grid(row=10, column=1, sticky=tk.NSEW)
    label_45_2.grid(row=10, column=2, sticky=tk.W)

    label_info = ttk.Label(frame, text="Сравните критерии по шкале Саати (первое относительно второго)",
                           font=fonts['main_font'])
    label_info.grid(row=11, columnspan=5)


def draw_results_ui(data, frame, fonts):
    label_info = ttk.Label(frame, text=f"Текущее состояние рынка поставщиков (раунд {str(data['round'])})",
                           font=fonts['main_font'])
    label_info.grid(row=0, columnspan=5, sticky=tk.NSEW)

    current_label = ttk.Label(frame, text=f"Текущий раунд: {str(data['round'])}", font=fonts['main_font'])
    current_label.grid(row=1, column=0, columnspan=3, sticky=tk.W)

    prev_label = ttk.Label(frame, text=f"Предыдущий раунд", font=fonts['main_font'])
    prev_label.grid(row=1, column=3, columnspan=3, sticky=tk.E)

    current_row = 2

    info = data['data']
    prev = data['prev']
    try:
        for player in info.keys():
            ttk.Label(frame, text=f"{str(data['nicknames'][player])}: {str(info[player])}%",
                      font=fonts['list_font']).grid(row=current_row, column=0, columnspan=3, sticky=tk.W)
            try:
                ttk.Label(frame, text=f"{str(data['nicknames'][player])}: {str(prev[player])}%",
                          font=fonts['list_font']).grid(row=current_row, column=3, columnspan=3, sticky=tk.E)
            except KeyError:
                pass
            finally:
                current_row += 1
    except TypeError:
        pass

    print(data)

    return 0
