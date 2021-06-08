"""
Напишите простой эхо-сервер, использующий неблокирующие сокеты и клиент к нему.
Тут реализация сервера
"""
import socket


def main():
    # Создаем сокет
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Назначаем на localhost

    server_sock.bind(("", 9095))
    # Устанавлитваем кол-во соединений
    server_sock.listen(1)
    # Ждем клиента
    conn, addr = server_sock.accept()
    # Делаем сокет не блокируемым
    conn.setblocking(False)
    while True:
        try:
            # Пытаемся получить данные, если они не готовы - ждём
            data = conn.recv(1024)
            break
        except socket.error:
            # Ждем
            print("Ожидаем..")

    # Декодируем, переворачиваем ответ и кодируем заново (или можно просто вернутьзапрос клиента)
    conn.send(data.decode()[::-1].encode())
    # Закрываем соединение
    conn.close()
    # Закрываем сокет
    server_sock.close()


if __name__ == "__main__":
    main()
