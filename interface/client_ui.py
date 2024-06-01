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

    label_scale_2 = ttk.Label(frame, text='Объем поставки', font=fonts['list_font'])
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

    label_scale_3 = ttk.Label(frame, text='Объем поставки', font=fonts['list_font'])
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

    label_scale_4 = ttk.Label(frame, text='Объем поставки', font=fonts['list_font'])
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

    label_scale_5 = ttk.Label(frame, text='Объем поставки', font=fonts['list_font'])
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
