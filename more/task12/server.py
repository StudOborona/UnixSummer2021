"""
Модифицированный клиент/сервер (https://github.com/StudOborona/UnixSummer2021/tree/main/task2)
Когда сервер отсылает клиенту "Continue", то клиент повторяет запрос.
Если отсылает "Cancel", то клиент закрывает соединение

Тут реализация сервера
"""
# coding=utf-8

import socket
import random

# Словарь для рандомных ответов
random_dict = {1: "Continue", 2: "Cancel"}


def main():
    # Создаем сокет
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Назначаем на localhost

    server_sock.bind(("127.0.0.1", 5000))
    # Устанавлитваем кол-во соединений
    server_sock.listen(1)
    # Ждем клиента
    while True:
        conn, addr = server_sock.accept()
        # Делаем сокет не блокируемым
        conn.setblocking(False)
        while True:
            try:
                # Пытаемся получить данные
                data = conn.recv(1024)
                break
            except socket.error:
                # Ждем
                print("Ожидаем..")

        message = data.decode()  # данные, которые приняли
        print(f"Получили сообщение от клиента: {message}")
        reply_message = random_dict[random.randint(1, 2)]
        conn.send(reply_message.encode())
        print(f"Отправили ответное сообщение клиенту: {reply_message}")

        # Закрываем соединение
        conn.close()


if __name__ == "__main__":
    main()
