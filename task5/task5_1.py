"""
Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера.
Количество потоков программы должно определяться параметром командной строки.
--
Существует несколько вариантов решения, это один из них
"""
import threading

#Начальная переменная для pi
pi = 0


def worker(start, end):
    global pi

    for num in range(start, end):

        if num % 2 == 1:
            pi += 1 / num ** 2
        else:
            pi -= 1 / num ** 2


def main():
    count = int(input("Введите кол-во потоков (1-100) -> "))
    # Рассчитываем, сколько элементов яда будет приходиться на 1 поток
    section_length = 10000000 // count

    # Начало последнего запущенного потока
    start_num = 1

    #Цикл по кол-ву потоков
    for i in range(count):
        t = threading.Thread(target=worker, args=(start_num, start_num + section_length,))
        t.start()
        start_num += section_length

    # Ожидаем конца выполнения всех потоков
    while threading.active_count() > 1:
        pass

    # См. тождество Фурье
    result = pow((pi * 12), 0.5)
    print(f"Вычисленное значение Pi: {result}")


if __name__ == "__main__":
    main()
