"""
Напишите TCP-сервер, принимающий от клиента имя файла и возвращающий содержание этого файла

Это клиент
"""

import socket

PORT = 8888


def main():
    while True:
        # Создаём сокет
        sock = socket.socket()
        # Подключаемся к серверу
        sock.connect(("127.0.0.1", PORT))
        # Вводим данные для сервера
        data_input = input("Введите название файла или exit для выхода ->")
        # Если это сообщение для выхода - выходим
        if data_input == "exit":
            break

        # Отправляем данные
        sock.send(data_input.encode())
        # Получаем ответ
        data = sock.recv(4096)
        # Выводим на экран
        message = data.decode()
        print(f"Полученный ответ от сервера: {message}")
        # Закрываем сокет
        sock.close()


if __name__ == "__main__":
    main()
