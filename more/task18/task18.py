"""
Напишите программу, которая копирует все файлы из домашней директории текущего пользователя в папку
переданную ей как параметр
"""

import os
import shutil
import sys
from os.path import expanduser


def main():
    # Проверяем на то, передали ли мы аргумент
    if len(sys.argv) != 2:
        print("Пожалуйста, передайте название папки в качестве параметра")
        return

    # Новая директория в переменной
    new_dir = sys.argv[1]
    print(f"Директория, переданная как параметр: {new_dir}")

    # Проверяем на существование директории, если что - создаем
    if os.path.isdir(new_dir):
        print(f"Директория {new_dir} существует")
    else:
        os.mkdir(new_dir)
        print(f"Директории {new_dir} не существует")

    # Получаем домашнюю директорию пользователя
    home = expanduser("~")
    print(f"Домашняя директория пользователя: {home}")

    # Цикл по каждому файлу в домашнем каталоге пользователя
    for current_file in os.listdir(home):
        # Полный путь файла (для os.path)
        currentfile_fullname = os.path.join(home, current_file)
        # Если это файл - копируем его
        if os.path.isfile(currentfile_fullname):
            # Само копирование
            shutil.copy(currentfile_fullname, new_dir)
            print(f"Скопировали файл {currentfile_fullname} в {new_dir}")


if __name__ == '__main__':
    main()
