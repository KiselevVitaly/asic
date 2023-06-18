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
    def create_response_message(code, alert=None):
        """
        Формирует сообщение ответа сервера (response message)
        :param code: Код ответа
        :param alert: Дополнительный параметр "уведомление"
        :return: response message (type = MessageBuilder)
        """
        return MessageBuilder({'response': code, 'alert': alert})
