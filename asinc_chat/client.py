import services as s

DESC = 'Client'


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


if __name__ == '__main__':
    args = s.parse_cli_arguments(DESC)
    client_ = Client(host=args.host, port=args.port)
    client_.run()
