import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QListWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic
import socketio

sio = socketio.Client()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("NETI BUSINESS")
        uic.loadUi('form.ui', self)
        self.pushButton.clicked.connect(self.registerNickname)

    def registerNickname(self):
        text = self.lineEdit.text()
        print(text)
        global sio
        sio.connect('http://127.0.0.1:5001')
        sio.emit('register', {'nickname': text, 'sid': str(sio.sid)})

        @sio.on('lobby_update')
        def update_list(data):
            print('Need to update the list:')
            print(data)

        # self.setGeometry(100, 100, 800, 600)

        # self.login_input = QLineEdit(self)
        # self.login_label = QLabel(self).setText('Enter your nickname')
        # self.register_button = QPushButton('Register', self)
        # self.nickname_list = QListWidget(self)
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.login_label, alignment=Qt.AlignTop)
        # layout.addWidget(self.login_input)
        # layout.addWidget(self.register_button)
        # layout.addWidget(self.nickname_list)
        #
        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
