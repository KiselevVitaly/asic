import subprocess
import chardet
from locale import getpreferredencoding


def __var_info(var) -> None:
    """
    Принимает на вход переменную и выводит ее тип, содержимое и длинну
    """
    print(f'Type: {type(var)}\n Var: {var}\n Lenth: {len(var)}')


def __ping(adres: str) -> None:
    """
    Принимает на вход адрес веб-ресурса,
    пингует указанный в адресе ресурс и выводит результаты
    """
    args = ['ping']
    args.append(adres)
    subprocess_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subprocess_ping.stdout:
        default_encoding = chardet.detect(line)
        print(line.decode(default_encoding.get('encoding')))


if __name__ == '__main__':
    print('1. ---------------------------------------------------->')
    """
    Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
    проверить тип и содержание соответствующих переменных. Затем с помощью
    онлайн-конвертера преобразовать строковые представление в формат Unicode и также
    проверить тип и содержимое переменных.
    """
    word_1, word_2, word_3 = 'разработка', 'сокет', 'декоратор'
    __var_info(word_1)
    __var_info(word_2)
    __var_info(word_3)
    __var_info(word_1.encode('utf-8'))
    __var_info(word_2.encode('utf-8'))
    __var_info(word_3.encode('utf-8'))

    print('2. ---------------------------------------------------->')
    """
    Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
    последовательность кодов (не используя методы encode и decode) и определить тип,
    содержимое и длину соответствующих переменных.
    """
    b_word_1, b_word_2, b_word_3 = b'class', b'function', b'method'
    __var_info(b_word_1)
    __var_info(b_word_2)
    __var_info(b_word_3)

    print('3. ---------------------------------------------------->')
    """
    Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
    байтовом типе.
    """
    print("""
    Ответ:
        В байтовом типе невозможео записать слова содержащие кириллицу(класс, функция), 
        так как байты кодируются в ascii кодировке. 
    """)

    print('4. ---------------------------------------------------->')
    """
    Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
    строкового представления в байтовое и выполнить обратное преобразование (используя
    методы encode и decode).
    """
    words_list = ['разработка', 'администрирование', 'protocol', 'standart']

    words_list_encode = []
    for word in words_list:
        words_list_encode.append(word.encode('utf-8'))
    print(f'Encoding with utf-8:\n{words_list_encode}')

    words_list_dencode = []
    for word in words_list_encode:
        words_list_dencode.append(word.decode('utf-8'))
    print(f'Decode with utf-8:\n{words_list_dencode}')

    print('5. ---------------------------------------------------->')
    """
    Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
    байтовового в строковый тип на кириллице.
    """
    __ping('yandex.ru')
    __ping('youtube.com')

    print('6. ---------------------------------------------------->')
    """
    Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
    программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
    Принудительно открыть файл в формате Unicode и вывести его содержимое.
    """
    line_list = ['сетевое программирование', 'сокет', 'декоратор']

    with open('test_file.txt', 'w') as f:
        f.writelines(line_list)

    print(f'Кодировка поумолчанию: {getpreferredencoding()}')

    with open('test_file.txt', 'r', encoding='utf-8', errors='replace') as f:
        print(f.read())
