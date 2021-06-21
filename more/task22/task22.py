"""
Напишите программу, которая обходит все файлы  директории, переданные ей как параметр
и удаляет все с расширением .tmp, чей размер задан как второй параметр.
Реализовать рекурсивный обход поддиректорий.
"""

import os
import sys


class Finder:
    """Класс для работы с файлами"""

    def __init__(self, root_dir, bytes_size):
        # Корневой каталог
        self.root_dir = root_dir
        # Размер файла в байтах, который ищем
        self.bytes_size = bytes_size
        # ЗАпуск поиска
        self.main_logic(self.root_dir)

    def main_logic(self, current_dir):
        # Текущий путь
        current_path = os.path.abspath(current_dir)
        print(f"Перешли в путь {current_path}")

        # Цикл по каждому файлу в текущем пути
        for item in os.listdir(current_path):

            # Текущий путь до конкретного файла
            buf_path = os.path.abspath(f"{current_dir}{os.sep}{item}")

            # Если это файл и размер с именем совпадают, то удаляем его
            if os.path.isfile(buf_path) and os.path.getsize(buf_path) == self.bytes_size and ".tmp" in item:
                os.remove(buf_path)
                print(f"Удалили файл {buf_path}")

            # Если директория, то рекурсивно в ней ищем файлы и также их удаляем
            elif os.path.isdir(buf_path):
                self.main_logic(buf_path)


def main():
    if len(sys.argv) != 3:
        print("Пожалуйста, передайте два параметра.\nПервый - путь, где происходит поиск\nВторой - размер файла в "
              "байтах для удаления")
        return
    else:
        file_path_input = sys.argv[1]
        file_size_input = int(sys.argv[2])

    finder = Finder(file_path_input, file_size_input)


if __name__ == "__main__":
    main()
