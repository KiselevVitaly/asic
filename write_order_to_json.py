"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
    a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
    b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""
import json


def write_order_to_json(
    item: list[str], quantity: list[int], price:list[int], buyer:list[str], date: list[str]
) -> None:
    """
    Записывает полученные данные в файл orders.json

    Args:
        item (list[str]): товар
        quantity (list[int]): количество
        price (list[int]): цена
        buyer (list[str]): покупатель
        date (list[str]): дата
    """
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('data_s2/orders.json', 'r', encoding='utf-8') as f:
        orders_list = json.load(f)
        orders_list['orders'].append(data)

    with open('data_s2/orders.json', 'w', encoding='utf-8') as f:
        json.dump(orders_list, f, sort_keys=True, indent=4)


if __name__ == '__main__':
    write_order_to_json(
        item=['игрушки', 'книги', 'посуда'],
        quantity=[5, 4, 10],
        price=[100.00, 10.00, 50.50],
        buyer=['Василий Иванович'],
        date=['10.10.10'])
        