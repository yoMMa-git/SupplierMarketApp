import tkinter as tk
from tkinter import ttk


def update_value(widget, array, index, change):
    if not (array[index] + change < 5 or array[index] + change > 30):
        array[index] += change
        widget.config(text=str(array[index]))


def draw_game_ui(frame, values, balance, fonts):  # поменять frame на frame3 при копировании в client.py
    label_scale_1 = ttk.Label(frame, text='Объем поставки', font=fonts['list_font'])
    scale_1 = ttk.Label(frame, text=str(values[0]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_1 = ttk.Button(frame, text='-5', command=lambda: update_value(scale_1, values, 0, -5))
    btn_minus1_1 = ttk.Button(frame, text='-1', command=lambda: update_value(scale_1, values, 0, -1))
    btn_plus1_1 = ttk.Button(frame, text='+1', command=lambda: update_value(scale_1, values, 0, 1))
    btn_plus5_1 = ttk.Button(frame, text='+5', command=lambda: update_value(scale_1, values, 0, 5))

    label_scale_1.grid(column=2, row=1)
    btn_minus5_1.grid(column=0, row=2, sticky=tk.E)
    btn_minus1_1.grid(column=1, row=2, sticky=tk.E)
    scale_1.grid(column=2, row=2, sticky=tk.NSEW)
    btn_plus1_1.grid(column=3, row=2, sticky=tk.W)
    btn_plus5_1.grid(column=4, row=2, sticky=tk.W)

    label_scale_2 = ttk.Label(frame, text='Срок поставки', font=fonts['list_font'])
    scale_2 = ttk.Label(frame, text=str(values[1]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_2 = ttk.Button(frame, text='-5', command=lambda: update_value(scale_2, values, 1, -5))
    btn_minus1_2 = ttk.Button(frame, text='-1', command=lambda: update_value(scale_2, values, 1, -1))
    btn_plus1_2 = ttk.Button(frame, text='+1', command=lambda: update_value(scale_2, values, 1, 1))
    btn_plus5_2 = ttk.Button(frame, text='+5', command=lambda: update_value(scale_2, values, 1, 5))

    label_scale_2.grid(column=2, row=3)
    btn_minus5_2.grid(column=0, row=4, sticky=tk.E)
    btn_minus1_2.grid(column=1, row=4, sticky=tk.E)
    scale_2.grid(column=2, row=4, sticky=tk.NSEW)
    btn_plus1_2.grid(column=3, row=4, sticky=tk.W)
    btn_plus5_2.grid(column=4, row=4, sticky=tk.W)

    label_scale_3 = ttk.Label(frame, text='Цена за штуку', font=fonts['list_font'])
    scale_3 = ttk.Label(frame, text=str(values[2]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_3 = ttk.Button(frame, text='-5', command=lambda: update_value(scale_3, values, 2, -5))
    btn_minus1_3 = ttk.Button(frame, text='-1', command=lambda: update_value(scale_3, values, 2, -1))
    btn_plus1_3 = ttk.Button(frame, text='+1', command=lambda: update_value(scale_3, values, 2, 1))
    btn_plus5_3 = ttk.Button(frame, text='+5', command=lambda: update_value(scale_3, values, 2, 5))

    label_scale_3.grid(column=2, row=5)
    btn_minus5_3.grid(column=0, row=6, sticky=tk.E)
    btn_minus1_3.grid(column=1, row=6, sticky=tk.E)
    scale_3.grid(column=2, row=6, sticky=tk.NSEW)
    btn_plus1_3.grid(column=3, row=6, sticky=tk.W)
    btn_plus5_3.grid(column=4, row=6, sticky=tk.W)

    label_scale_4 = ttk.Label(frame, text='Отклонения от графика платежей', font=fonts['list_font'])
    scale_4 = ttk.Label(frame, text=str(values[3]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_4 = ttk.Button(frame, text='-5', command=lambda: update_value(scale_4, values, 3, -5))
    btn_minus1_4 = ttk.Button(frame, text='-1', command=lambda: update_value(scale_4, values, 3, -1))
    btn_plus1_4 = ttk.Button(frame, text='+1', command=lambda: update_value(scale_4, values, 3, 1))
    btn_plus5_4 = ttk.Button(frame, text='+5', command=lambda: update_value(scale_4, values, 3, 5))

    label_scale_4.grid(column=2, row=7)
    btn_minus5_4.grid(column=0, row=8, sticky=tk.E)
    btn_minus1_4.grid(column=1, row=8, sticky=tk.E)
    scale_4.grid(column=2, row=8, sticky=tk.NSEW)
    btn_plus1_4.grid(column=3, row=8, sticky=tk.W)
    btn_plus5_4.grid(column=4, row=8, sticky=tk.W)

    label_scale_5 = ttk.Label(frame, text='Виды упаковки', font=fonts['list_font'])
    scale_5 = ttk.Label(frame, text=str(values[4]), anchor=tk.CENTER, font=fonts['list_font'])
    btn_minus5_5 = ttk.Button(frame, text='-5', command=lambda: update_value(scale_5, values, 4, -5))
    btn_minus1_5 = ttk.Button(frame, text='-1', command=lambda: update_value(scale_5, values, 4, -1))
    btn_plus1_5 = ttk.Button(frame, text='+1', command=lambda: update_value(scale_5, values, 4, 1))
    btn_plus5_5 = ttk.Button(frame, text='+5', command=lambda: update_value(scale_5, values, 4, 5))

    label_scale_5.grid(column=2, row=9)
    btn_minus5_5.grid(column=0, row=10, sticky=tk.E)
    btn_minus1_5.grid(column=1, row=10, sticky=tk.E)
    scale_5.grid(column=2, row=10, sticky=tk.NSEW)
    btn_plus1_5.grid(column=3, row=10, sticky=tk.W)
    btn_plus5_5.grid(column=4, row=10, sticky=tk.W)

    balance = ttk.Label(frame, text=f"Баланс: {str(balance[0])}", font=fonts['main_font'])
    balance.grid(column=2, row=11, sticky=tk.NSEW)


def draw_judge_ui(frame, rates, fonts):
    criterias = ['Объем поставки', 'Срок поставки', 'Цена за штуку', 'Отклонения от графика платежей', 'Виды упаковки']

    for i in range(13):
        frame.rowconfigure(i, pad=10)

    label_12_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    entry_12 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[0])
    label_12_2 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])

    label_12_1.grid(row=1, column=0, sticky=tk.E)
    entry_12.grid(row=1, column=1, sticky=tk.NSEW)
    label_12_2.grid(row=1, column=2, sticky=tk.W)

    label_13_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    entry_13 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[1])
    label_13_2 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])

    label_13_1.grid(row=2, column=0, sticky=tk.E)
    entry_13.grid(row=2, column=1, sticky=tk.NSEW)
    label_13_2.grid(row=2, column=2, sticky=tk.W)

    label_14_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    entry_14 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[2])
    label_14_2 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])

    label_14_1.grid(row=3, column=0, sticky=tk.E)
    entry_14.grid(row=3, column=1, sticky=tk.NSEW)
    label_14_2.grid(row=3, column=2, sticky=tk.W)

    label_15_1 = ttk.Label(frame, text=criterias[0], font=fonts['list_font'])
    entry_15 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[3])
    label_15_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_15_1.grid(row=4, column=0, sticky=tk.E)
    entry_15.grid(row=4, column=1, sticky=tk.NSEW)
    label_15_2.grid(row=4, column=2, sticky=tk.W)

    label_23_1 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])
    entry_23 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[4])
    label_23_2 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])

    label_23_1.grid(row=5, column=0, sticky=tk.E)
    entry_23.grid(row=5, column=1, sticky=tk.NSEW)
    label_23_2.grid(row=5, column=2, sticky=tk.W)

    label_24_1 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])
    entry_24 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[5])
    label_24_2 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])

    label_24_1.grid(row=6, column=0, sticky=tk.E)
    entry_24.grid(row=6, column=1, sticky=tk.NSEW)
    label_24_2.grid(row=6, column=2, sticky=tk.W)

    label_25_1 = ttk.Label(frame, text=criterias[1], font=fonts['list_font'])
    entry_25 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[6])
    label_25_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_25_1.grid(row=7, column=0, sticky=tk.E)
    entry_25.grid(row=7, column=1, sticky=tk.NSEW)
    label_25_2.grid(row=7, column=2, sticky=tk.W)

    label_34_1 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])
    entry_34 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[7])
    label_34_2 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])

    label_34_1.grid(row=8, column=0, sticky=tk.E)
    entry_34.grid(row=8, column=1, sticky=tk.NSEW)
    label_34_2.grid(row=8, column=2, sticky=tk.W)

    label_35_1 = ttk.Label(frame, text=criterias[2], font=fonts['list_font'])
    entry_35 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[8])
    label_35_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_35_1.grid(row=9, column=0, sticky=tk.E)
    entry_35.grid(row=9, column=1, sticky=tk.NSEW)
    label_35_2.grid(row=9, column=2, sticky=tk.W)

    label_45_1 = ttk.Label(frame, text=criterias[3], font=fonts['list_font'])
    entry_45 = ttk.Entry(frame, justify=tk.CENTER, textvariable=rates[9])
    label_45_2 = ttk.Label(frame, text=criterias[4], font=fonts['list_font'])

    label_45_1.grid(row=10, column=0, sticky=tk.E)
    entry_45.grid(row=10, column=1, sticky=tk.NSEW)
    label_45_2.grid(row=10, column=2, sticky=tk.W)

    label_info = ttk.Label(frame, text="Сравните критерии по шкале Саати (подробнее в Инструкции)", font=fonts['main_font'])
    label_info.grid(row=11, columnspan=5)
