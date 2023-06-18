"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата. Для этого:
    a. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
    b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;
    c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными
"""
import yaml

first_key = [
    'test text 1',
    'test text 2',
    'test text 3',
    'test text 4'
]

second_key = 100
third_key = {
    'first_value':  str(100) + u'\u20BD',
    'second_value': str(200) + u'\u20BD',
    'third_value': str(300) + u'\u20BD',
}

to_yaml = {'first_key': first_key, 'second_key': second_key, 'third_key': third_key}

with open('file.yaml', 'w', encoding='utf-16') as f:
    yaml.dump(to_yaml, f, allow_unicode=True, default_flow_style=False, default_style='"')

with open('file.yaml', 'r', encoding='utf-16') as fr:
    print(yaml.safe_load(fr) == to_yaml)
