"""
Напишите TCP-сервер, принимающий от клиента имя файла и возвращающий содержание этого файла

Это сервер
"""
import os
import socket
from typing import Union

PORT = 8888


class FileProcessing:
    """Работа с файлами"""

    def __init__(self) -> None:
        self.sep = os.sep
        # Путь, где хранятся файлы
        self.root_path = "./server_storage"

    def ls(self) -> str:
        """Вывод содержимого директории на экран"""

        # Список файлов, которые есть в директории
        result_list = []

        # Список всех файлов в текущей директории
        files_list = os.listdir(self.root_path)
        for current_file in files_list:
            current_path = self.root_path + self.sep + current_file

            # Если это файл (не папка), то добавляем в результирующий список
            if os.path.isfile(current_path):
                result_list.append(current_file)

        # Возвращаем результат в виде строки
        r = "\n".join(result_list)
        return f"Содержимое {self.root_path}:\n{r}"

    def reader(self, filename: str) -> Union[None, str]:
        """Просмотр содержимого текстового файла"""

        # Полный путь до файла
        current_path = self.root_path + self.sep + filename

        # Пытаемся прочитать
        try:
            with open(current_path, "r") as file:
                return file.read()

        # Если файл не найден
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
            return None
        # Если это не файл (мало ли)
        except IsADirectoryError:
            print(f"Файл {filename} является директорией")
            return None


def main():
    # Создаем сокет
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Назначаем на localhost
    server_sock.bind(("127.0.0.1", PORT))
    # Устанавливаем кол-во соединений
    server_sock.listen(1)

    # экземпляр FileProcessing для работы с файлами
    file_logic = FileProcessing()
    # Ждем клиента
    while True:
        conn, addr = server_sock.accept()
        # Делаем сокет не блокируемым
        conn.setblocking(False)

        # Собираем данные
        while True:
            try:
                # Пытаемся получить данные
                data = conn.recv(4096)
                break
            except socket.error:
                # Ждем
                pass

        file_name = data.decode()  # данные, которые приняли
        print(f"Получили сообщение от клиента: {file_name}")

        # Пытаемся прочитать файл с таким именем
        reply_message = file_logic.reader(file_name)
        # Если файла нет - отдаем список всех доступных файлов для чтения
        if reply_message is None:
            reply_message = file_logic.ls()

        # Отправляем результат клиенту
        conn.send(reply_message.encode())
        print(f"Отправили ответное сообщение клиенту: {reply_message}")

        # Закрываем соединение
        conn.close()


if __name__ == "__main__":
    main()
