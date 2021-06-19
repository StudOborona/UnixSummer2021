"""
Напишите программу, которая создает четыре нити
исполняющие одну и ту же функцию. Эта функция должна распечатать последовательность
текстовых строк, переданных как параметр. Каждая из созданных нитей
должна распечатать различные последовательности строк
"""

import sys
import threading

# Список для хранения информации о строках, которые выводятся
my_list = []


def my_printer(data: str):
    """Вывод строки на экран"""
    print(data)


def print_1(data: str):
    """Вывод + вывод в отдельном потоке"""
    # Стартуем новый поток с новой строкой
    t = threading.Thread(target=my_printer, args=(my_list[3],))
    t.start()
    # Выводим строку в текущем потоке
    my_printer(data)


def print_2(data: str):
    """Вывод + вывод в отдельном потоке, в котором вывод + вывод в отдельном потоке"""
    # Стартуем новый поток с новой строкой
    t = threading.Thread(target=print_1, args=(my_list[2],))
    t.start()
    # Выводим строку в текущем потоке
    my_printer(data)


def main():
    """
    Вывод + вывод в отдельном потоке, в котором вывод + вывод в отдельном потоке,
    в котором вывод + вывод в отдельном потоке
    """

    # Глобальный список строк-аргументов
    global my_list
    # Если не переданы параметры
    if len(sys.argv) != 5:
        print("Необходимо передать в качестве параметров 4 строки")
        return

    # Список аргументов
    my_list = list(sys.argv)
    # Первый удаляем т.к. это имя скирпта
    my_list.pop(0)

    # Стартуем новый поток с новой строкой
    t = threading.Thread(target=print_2, args=(my_list[1],))
    t.start()
    # Выводим строку в текущем потоке
    my_printer(my_list[0])


if __name__ == "__main__":
    main()