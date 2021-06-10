"""
Напишите простой многопоточный загрузчик URL. Список URL скрипт принимает как аргументы командной строки.
"""
import sys
import threading

import requests

# Словарь с ассоциацией между url и данными
responses_dict = {}


def loader(url: str):
    """Метод для загрузки ответов по URL"""
    # Получаем данные по URL
    r = requests.get(url)
    # Добавляем данные в словарь
    responses_dict[url] = r.text


def main():
    if sys.argv == 1:
        print(
            "Необходимо передать URL в аргументах при запуске скрипта (например, python3 task.py https://ya.ru"
        )
        return

    # Получаем список URL
    links_list = sys.argv
    # Удаляем 1-й параметр т.к. это название скрипта
    links_list.pop(0)

    # Для каждой ссылки запускаем отдельный поток
    for link in links_list:
        t = threading.Thread(target=loader, args=(link,))
        t.start()

    # Ждем, пока все потоки отработают
    while threading.active_count() > 1:
        pass

    for key, value in responses_dict.items():
        print(f"URL: {key}\nОтвет:\n{value}\n")


if __name__ == "__main__":
    main()
