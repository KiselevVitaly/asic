import unittest
from client import Client, DESC
from services.parse_cli_arguments import parse_cli_arguments


class ClientTest(unittest.TestCase):
    """
    Тесты клиента
    """
    
    
    def setUp(self) -> None:
        self.args = parse_cli_arguments(DESC)

    def tearDown(self) -> None:
        pass

    def test_parse_response(self):
        pass

    def test_send_message(self):
        pass


if __name__ == '__main__':
    unittest.main()
    