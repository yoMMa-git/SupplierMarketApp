import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, \
    QListWidget, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from asyncqt import QEventLoop
from PyQt5 import uic
import socketio
import asyncio
import threading

# Initialize socketio.Client() globally
sio = socketio.Client()


def connect():
    global sio
    sio.connect('http://25.29.145.179:5001')


def createPopup(title, icon, msg):
    w = QMessageBox()
    w.setWindowTitle(title)
    w.setIcon(icon)
    w.setText(msg)
    w.show()


class MainWindow(QMainWindow):
    uiUpdated = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("NETI BUSINESS")
        self.ui = uic.loadUi('form.ui', self)
        self.pushButton.clicked.connect(self.registerNickname)

    @sio.on('nickname_response')
    def checkNickUI(self, data):
        print("Got response!")
        if data['response'] == 'exists':
            self.pushButton.setEnabled(True)
            print("This nickname already exists")
        elif data['response'] == 'success':
            print("Changing UI...")
            # Ensure proper re-initialization of the UI components
            self.ui = uic.loadUi('gamewindow.ui', self)
            self.update()

    def registerNickname(self):
        text = self.lineEdit.text()
        self.pushButton.setEnabled(False)
        print(text)
        global sio
        sio.emit('register', {'nickname': text, 'sid': str(sio.sid)})

        #def checkNick(data):
        #self.checkNickUI(data)


def handle_nickname_response(main_window, data):
    print("Handling nickname response:", data)
    # Update the main window based on the response
    main_window.checkNickUI(data)


def main():
    # Start the connection in a separate thread
    t1 = threading.Thread(target=connect).start()
    # Create the QApplication and start the event loop
    app = QApplication([])
    window = MainWindow()
    window.show()
    # Register the event handler with the MainWindow instance
    sio.on('nickname_response', lambda data: handle_nickname_response(window, data))
    # Wait for the application to exit
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
