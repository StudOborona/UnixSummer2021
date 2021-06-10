# coding=utf-8
import socket


def main():
    cont_flag = True
    while cont_flag:
        # Создаём сокет
        sock = socket.socket()
        # Подключаемся к localhost
        sock.connect(("127.0.0.1", 5000))
        # Сообщение для сервера
        data_input = "What must I do?"
        # Отправляем данные
        sock.send(data_input.encode())
        # Получаем ответ
        data = sock.recv(1024)
        # Выводим на экран
        message = data.decode()
        print(f"Полученный ответ от сервера: {message}")
        # Если получили cancel, то завершаем работу
        if message == "Cancel":
            cont_flag = False
        # Закрываем сокет
        sock.close()


if __name__ == "__main__":
    main()
