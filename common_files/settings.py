"""Настройки чата"""

import logging

# Порт по умолчанию для сетевого взаимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка сообщений
ENCODING = 'utf-8'
# Уровень логирования
LOG_LEVEL = logging.DEBUG
# База данных чата:
SERVER_DATABASE = 'server.ini'

# Протокол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
USER_NAME = 'user_name'
SENDER = 'from'
RECIPIENT = 'to'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MSG = 'msg'
MSG_TEXT = 'msg_text'
EXIT = 'exit'
TAKE_CONTACTS = 'get_contacts'
CONTACTS_INFO = 'data_list'
ADD_CONTACT = 'add'
TAKE_USERS = 'get_users'
DELETE_CONTACT = 'remove'

# ответ сервера 200
RESPONSE_200 = {RESPONSE: 200}
# ответ сервера 202
RESPONSE_202 = {RESPONSE: 202, CONTACTS_INFO: None}
# ответ сервера 400
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}