import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
from PIL import Image, ImageTk
import socketio
import threading

sio = socketio.Client()
HOST, PORT = '25.29.145.179', 5001
root = tk.Tk()
frame = tk.Frame(root)
frame2 = tk.Frame(root)
main_font = Font(family='Stem', weight='bold', size=21)


# Function to handle button click
def on_button_click(entry_field):
    entered_text = entry_field.get()
    print(f"You entered: {entered_text}")
    sio.emit('register', {'nickname': entered_text, 'sid': str(sio.sid)})

    @sio.on('nickname_response')
    def checkNick(data):
        print("Got response!")
        if data['response'] == 'exists':
            messagebox.showwarning(message="This nickname already exists!")
        elif data['response'] == 'success':
            messagebox.showinfo(message="OK! Changing UI...")
            secondWindow()


def secondWindow():
    frame.destroy()
    new_label = ttk.Label(root, text='Ожидание игроков...', font=main_font)
    new_label.pack(pady=10)


def mainWindow():
    # Create the main application window
    sio.connect('http://25.29.145.179:5001')

    root.title("Бизнес-игра")
    root.geometry("400x500")

    entry_label = ttk.Label(frame, text='Добро пожаловать!\nВведите логин:', font=main_font)
    entry_label.pack(pady=10)

    # Create an entry field (LineEdit)
    entry_field = ttk.Entry(frame, width=40)
    entry_field.pack(pady=10)

    # Create a button
    button = ttk.Button(frame, text="Войти", command=lambda entry=entry_field: on_button_click(entry))
    button.pack(pady=10)

    # Simulate an icon field using a label with an image
    image = ImageTk.PhotoImage(Image.open('icon.png').resize((145, 247)))  # Load the image
    icon_label = ttk.Label(root, image=image)
    icon_label.pack(pady=10)

    frame.pack()

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == '__main__':
    threading.Thread(target=mainWindow()).start()
