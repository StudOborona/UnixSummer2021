"""
Напишите TCP-клиент, подключающийся к веб-серверу google.com и сохраняющий на локальной машине код главной страницы этого сайта
"""

import socket

def main():

    host = "www.google.com"
    port = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send('GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'.encode())

    response = client.recv(4096)
    print(response)


if __name__ == "__main__":
    main()
