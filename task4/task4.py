"""
Реализуйте простой HTTP-клиент. Он принимает один параметр командной строки - URL.
Клиент делает запрос по указанному URL и выдает тело ответа на терминал как текст.

--
Еще проще сделать через requests, но здесь, кажется, нужно через urllib (или вообще сокеты?)
Можно также сделать через os.system(curl ...)
Кароч неоднозначное задание
"""
import sys
import urllib.request


def main():

    # Если аргумент в виде URL не был принят - вводим его
    if len(sys.argv) != 2:
        url_input = input("Введите какой-либо URL ->")
    else:
        url_input = sys.argv[1]

    # Открываем соединение
    web_request = urllib.request.urlopen(url_input)
    # получаем код результата и выводим его
    print(f"Код результата: {web_request.getcode()}")
    # Вывод данных, которые получили
    data = web_request.read()
    print(data)


if __name__ == "__main__":
    main()
