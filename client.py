import asinc_chat.services as s

DESC = 'Client'

CLIENT_LOGGER = logging.getLogger('client_log')

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

    def get_data(self):
        data = None
        while data is None:
            data = self._client_socket.recv(s.BLOCK_LEN)

    def parse_response(self, response):
        resp = response.decode(s.ENCODING_)
        # print(resp)
        parsed_response = s.MessageBuilder.get_object_of_json(resp)
        print(f'Статус: {parsed_response.response}, {parsed_response.alert}')
        return parsed_response.response, parsed_response.alert

    def send_message(self, type='presence'):
        if self.login is None:
            #self.login = input("Login:")
            self.login = 'Guest'
        gen_message = s.MessageBuilder.create_presence_message(self.login)
        gen_message_json = gen_message.encode_to_json()
        self._client_socket.send(gen_message_json.encode(s.ENCODING_))

    def run(self):
        while True:
            self.send_message('presence')
            response = self._client_socket.recv(s.BLOCK_LEN)
            response, alert = self.parse_response(response)


def main():
    """Запуск клиента"""

    # Установка аргументов из командной строки
    # client.py 192.168.1.2 8079
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        CLIENT_LOGGER.critical(f'Установил значения адреса и порта сервера '
                               f'по умолчанию {server_address}:{server_port}')
    except ValueError:
        CLIENT_LOGGER.critical('адрес порта должен быть от 1024 до 65535.')
        sys.exit(1)

    # Активация сокета и обмен сообщениями
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    msg_to_server = exist_client_msg()
    send_msg(transport, msg_to_server)
    try:
        status_server_answer = server_answer(get_msg(transport))
        CLIENT_LOGGER.info(f'ответ от сервера: {status_server_answer}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.critical('Попытка декодировать сообщение от сервера '
                               'потерпела неудачу.')

if __name__ == '__main__':
    args = s.parse_cli_arguments(DESC)
    client_ = Client(host=args.host, port=args.port)
    client_.run()
