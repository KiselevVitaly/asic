import json
import time


class JSONMessageEncoder(json.JSONEncoder):
    """
    Собственный JSONEncoder расширяющий стандартный JSONEncoder,
    необходим для кодирования пользовательских объектов в формат,
    сериализуемый в JSON
    """
    def default(self, obj):
        return obj.__dict__


class MessageBuilder:
    """
    Класс описывающий фабричные методы, генерирующие соответствующие сообщения
    """
    def __init__(self, msg):
        """
        Генерируем сообщение из словаря в зависимости от любого количества элементов
        """
        for key, val in msg.items():
            if isinstance(val, dict):
                sub_val = MessageBuilder(val)
                setattr(self, key, sub_val)
            else:
                setattr(self, key, val)

    def encode_to_json(self):
        """
        Кодирует объект в json
        :return: json представление MessageBuilder
        """
        return JSONMessageEncoder().encode(self)

    @staticmethod
    def get_object_of_json(json_obj):
        """
        Декодирует из json в MessageBuilder
        :return: presence message (type = MessageBuilder)
        """
        return json.JSONDecoder(object_hook=MessageBuilder).decode(json_obj)

    @staticmethod
    def create_presence_message(name, time=time.ctime()):
        """
        Формирует сообщение о присутствии(presence message)
        :param name: Имя пользователя
        :param time: время, по умолчанию текущее.
        :return: presence message (type = MessageBuilder)
        """
        return MessageBuilder(
            {
                'action': 'presence', 
                'time': time,
                'user':{
                    'name': name,
                    'status': 'here'
                }
            }
        )

    @staticmethod
    def create_message_to_user(from_user, to_user, msg, time=time.ctime()):
        return MessageBuilder(
            {
                'action': 'msg',
                'time': time,
                'to_user': to_user,
                'from_user': {
                    'name': from_user,
                    'status': 'here'
                },
                'message': msg
            }
        )

    @staticmethod
    def create_message_to_chat(from_user, msg, time=time.ctime()):
        """
        Формирует сообщение в чат

        Args:
            from_user (_type_): Пользователь отправивший сообщение
            msg (_type_): Сообщение
            time (_type_, optional): Время. Поумолчанию time.ctime().

        Returns:
            create_message_to_chat (type = MessageBuilder)
        """
        return MessageBuilder(
            {
                'action': 'msg',
                'time': time,
                'to_user': 'ALL',  # вообще-то здесь указывается room name,
                              # пока упрощенный чат в котором участвуют все подключенные
                'from_user': {
                    'name': from_user,
                    'status': 'here'
                },
                'message': msg
            }
        )

    @staticmethod
    def join_chat(from_user, room_name, time=time.ctime()):
        """
        Присоединиться к чату
        """
        return MessageBuilder(
            {
                'action': 'join',
                'time': time,
                'from': from_user,
                'room': room_name
            }
        )

    @staticmethod
    def leave_chat(from_user, room_name, time=time.ctime()):
        """
        Покинуть чат
        """
        return MessageBuilder(
            {
                'action': 'leave',
                'time': time,
                'from': from_user,
                'room': room_name
            }
        )

    @staticmethod
    def create_response_message(code, alert=None):
        """
        Формирует сообщение ответа сервера (response message)
        :param code: Код ответа
        :param alert: Дополнительный параметр "уведомление"
        :return: response message (type = MessageBuilder)
        """
        return MessageBuilder({'response': code, 'alert': alert})

    @staticmethod
    def get_contact_list(login, time=time.ctime()):
        """
        Получение списка контактов
        """
        return MessageBuilder(
            {
                'action': 'get_contacts',
                'time': time,
                'user_login': login
            }
        )

    @staticmethod
    def add_contact(login, user_id, time=time.ctime()):
        """
        Добавление контакта
        """
        return MessageBuilder(
            {
                'action': 'add_contact',
                'user_id': user_id,
                'time': time,
                'user_login': login

            }
        )

    @staticmethod
    def dell_contact(login, user_id, time=time.ctime()):
        """
        Удалние контакта
        """
        return MessageBuilder(
            {
                'action': 'del_contact',
                'user_id': user_id,
                'time': time,
                'user_login': login
            }
        )
