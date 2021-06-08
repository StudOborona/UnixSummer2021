"""
Напишите программу, которая обходит все файлы в директории,
переданной ей как параметр и выводит на экран имена тех, чей размер задан как второй параметр.
Реализовать рекурсивный обход поддиректорий.
"""
import os


class Trip:
    """
    Класс-путешествие по внутреннему миру ФС
    """

    def __init__(self, root_dir: str, bytes_size: int):
        self.root_dir = root_dir
        self.bytes_size = bytes_size
        self.processing(self.root_dir)

    def processing(self, current_dir: str):
        # Текущий путь
        current_path = os.path.abspath(current_dir)
        print(f"Перешли в путь {current_path}")

        # Цикл по каждому файлу в текущем пути
        for item in os.listdir(current_path):

            # Текущий путь до файла
            current_item_path = os.path.abspath(f"{current_dir}{os.sep}{item}")

            # Если это файл и размер совпадает, то выводим его
            if os.path.isfile(current_item_path) and os.path.getsize(current_item_path) == self.bytes_size:
                print(f"[ФАЙЛ] {current_item_path}")

            # Если директория
            elif os.path.isdir(current_item_path):
                # print(f"[ДИРЕКТОРИЯ] {current_item_path}")
                # Вызываем рекурсивно self.processing для этой директории
                self.processing(current_item_path)


def main():
    trip = Trip("check", 555)


if __name__ == "__main__":
    main()
