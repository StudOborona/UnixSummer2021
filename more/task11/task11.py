#!/bin/python3
"""
Напишите программу, которая принимает как параметр имя исполняемого файла,
копирует его в директорию /usr/local/bin, регистриурует его в системе
как демона и запускает.
Предполагается использование systemd
Предположим, что скрипт имеет шебанг
"""
from shutil import copyfile
import sys
import os

# Необходимо запускать под sudo, пример запуска:
# sudo main.py myservice.service
def main():

    # Проверка на кол-во переданных аргументов
    if len(sys.argv) != 2:
        print("Введите имя исполняемого файла в виде аргумента!")
        return

    # Имя файла, которое принимаем
    file_from = sys.argv[1]

    # Проверяем есть ли у файла право на запуск (x)
    is_executable = os.access(file_from, os.X_OK)
    if not is_executable:
        print("Переданный файл не является исполняемым!")
        return

    # Директория, куда копируем
    file_to = f"/usr/local/bin/{file_from}"

    # Само копирование
    copyfile(file_from, file_to)

    # Регистрация в качестве демона в системе и запуск
    os.system(f"systemctl start {file_from}")
    os.system(f"systemctl enable {file_from}")


if __name__ == "__main__":
    main()
