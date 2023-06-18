import asinc_chat.services as s

import logging
from asinc_chat.log import server_log_config

DESC = 'Server'
LOG = logging.getLogger('server')


class Server:
    """
    Сервер, работает по протоколу TCP
    """
    _server_socket = s.socket.socket(s.socket.AF_INET, s.socket.SOCK_STREAM)
    connections = []

    def __init__(self, host:str, port: int) -> None:
         self._server_socket.bind((host, port))
         self._server_socket.listen(5)
         self._server_socket.settimeout(0.5)
         print(f'Сервер запущен по адресу {host}:{port}')

    def parse_message(self, message):
        msg = message.decode(s.ENCODING_)
        print(msg)
        parsed_msg = s.MessageBuilder.get_object_of_json(msg)
        return parsed_msg

    def send_responce(self, client, code, alert=None):
        gen_response = s.MessageBuilder.create_response_message(code, alert)
        gen_response_json = gen_response.encode_to_json()
        client.send(gen_response_json.encode(s.ENCODING_))

    def run(self) -> None:
        while True:
            try:
                client, address = self._server_socket.accept()
            except OSError:
                pass
            else:
                print(f'Получен запрос на соединение от: {address}')
                self.connections.append(client)
            finally:
                responce_ = []
                write_ = []
                try:
                    responce_, write_, excepttions_ = s.select.select(self.connections, self.connections, [], 0)
                except Exception:
                    pass
                for c in responce_:
                    data = c.recv(s.BLOCK_LEN)
                    parsed_message = self.parse_message(data)
                    try:
                        if parsed_message.action == 'presence' and (c in write_):
                            self.send_responce(client=c, code=200, alert=f'{parsed_message.user.name} в настоящее время присутствует')
                    except:
                        self.connections.remove(c)

    def close(self):
        self._server_socket.close()


if __name__ == '__main__':
    args = s.parse_cli_arguments(DESC)
    server = Server(host=args.host, port=args.port)
    server.run()
