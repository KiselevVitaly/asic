import asinc_chat.services as s
from threading import Thread

import logging
from asinc_chat.log import client_log_config

from asinc_chat.ui.py_form import Ui_MainWindow
import sys
from PyQt5 import QtWidgets

DESC = 'Client'
LOG = logging.getLogger('client')


class Client:
    """
    Клиент, подключается по протоколу TCP
    """
    _client_socket = s.socket.socket(s.socket.AF_INET, s.socket.SOCK_STREAM)

    def __init__(self, host:str, port: int) -> None:
        self._client_socket.connect((host, port))
        self.login = None

    def __del__(self):
        self._client_socket.close()

    @s.Log(LOG)
    def get_data(self):
        self.data = None
        while self.data is None:
            self.data = self._client_socket.recv(s.BLOCK_LEN)
        return self.data

    @s.Log(LOG)
    def parse_response(self, response):
        resp = response.decode(s.ENCODING_)
        # print(resp)
        parsed_response = s.MessageBuilder.get_object_of_json(resp)
        print(f'Статус: {parsed_response.response}, {parsed_response.alert}')
        return parsed_response.response, parsed_response.alert

    def read_server_response(self):
        while True:
            response = self.get_data()
            response, alert = self.parse_response(response)

    @s.Log(LOG)
    def send_message(self, type=None, msg=None):
        if self.login is None:
            self.login = input('Login:')
            # self.login = 'Guest'
        if type == 'presence':
            gen_message = s.MessageBuilder.create_presence_message(self.login)
            gen_message_json = gen_message.encode_to_json()
            self._client_socket.send(gen_message_json.encode(s.ENCODING_))
        if type == 'chat':
            gen_message = s.MessageBuilder.create_message_to_chat(self.login, msg)
            gen_message_json = gen_message.encode_to_json()
            self._client_socket.send(gen_message_json.encode(s.ENCODING_))

    @s.Log(LOG)
    def run(self):
        self.send_message(type='presence')
        response = self.get_data()
        response, alert = self.parse_response(response)
        # запускаем поток вычитывания серверных сообщений
        th_sender = Thread(target=self.read_server_response)
        th_sender.daemon = True
        th_sender.start()
        while True:
            msg = input('> ')
            if msg == '/q':
                break
            self.send_message(type='chat', msg=msg)
                  

if __name__ == '__main__':
    args = s.parse_cli_arguments(DESC)
    client_ = Client(host=args.host, port=args.port)
    client_.run()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)
    window.show()
    sys.exit(app.exec_())
