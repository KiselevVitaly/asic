import pytest
import socket as s

from asinc_chat.services.JIMProtocol import MessageBuilder
from server import Server
from client import Client


@pytest.fixture
def socket():
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    _socket.bind(('localhost', 7777))
    yield _socket
    _socket.close()


@pytest.fixture
def client():
    _client = Client(host='localhost', port=7777)
    yield _client
    

@pytest.fixture
def responce():
    msg = MessageBuilder.create_presence_message('Guest')
    yield msg


def test_server_connect(socket):
    socket.connect(('localhost', 7777))
    assert socket
