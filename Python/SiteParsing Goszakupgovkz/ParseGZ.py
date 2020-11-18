# Yun Sergey
# Парсинг сайта goszakup.gov.kz для создания списка:
# "Перечень товаров, работ, услуг, закупки которых осуществляются с применением специального порядка"
# v 1.0
# info@mhelp.kz

import requests as rq
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()


def get_request(parse_url):
    """ Функция получения текста с url"""
    parse_text = rq.get(parse_url, verify=False).text
    parse_text = BeautifulSoup(parse_text, 'lxml')
    return parse_text


def parse_sheet(parse_text):
    """Парсинг 2,3 элемента в таблице из 5 элементов на странице.
       Создание списка содержащего данные из полей:
       Поле 2: Код КТРУ
       Поле 3: Наименование товара"""

    global list_item
    field_counter = 0
    for index, tag in enumerate(parse_text.find_all("td")):
        field_counter += 1
        if field_counter == 2:
            list_item.append((parse_text.find_all("td")[index].text, parse_text.find_all("td")[index + 1].text))
        if field_counter == 5:
            field_counter = 0
    return


def file_write(file_name, export_list):
    """ Функция записи в файл file_name, списка export_list"""

    with open(file_name, mode='w+', encoding='utf-8') as content:
        for item in export_list:
            content.write(f'{item[0]}\t{item[1]}' + '\n')
    return


list_item = []  # Список Код КТРУ и Наименование товара

url = 'https://www.goszakup.gov.kz/ru/spec_order?&page=1'  # Формат web адреса страницы парсинга
END_SHEET = 155  # Конечный номер страницы

for i in range(1, END_SHEET):
    print(f'Считываем страницу: https://www.goszakup.gov.kz/ru/spec_order?&page={i}')

    url = f'https://www.goszakup.gov.kz/ru/spec_order?&page={i}'

    soup_text = get_request(parse_url=url)

    parse_sheet(parse_text=soup_text)

export_list = set(list_item)  # Удаляем дубликаты
export_list = sorted(list(export_list))  # Сортируем по возрастаю, по полю "КОД КТРУ"


file_write(file_name='parse.txt', export_list=export_list)  # Запись в файл с названием parse.txt

print('Работа программы завершена')