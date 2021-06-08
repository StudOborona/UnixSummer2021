"""
Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера.
Количество потоков программы должно определяться параметром командной строки.
--
Существует несколько вариантов решения, это один из них
"""
import threading
import time

pi = 1.0


def pi_val(i, iter):
    global pi
    for num in range(i - iter, iter):
        if num % 2 == 1:
            pi += 1 / num ** 2
        else:
            pi -= 1 / num ** 2


def pi_counter(count: int, start_time: time):
    global pi
    # Интервалы
    inter = 100000 // count
    for i in range(2 + inter, 100000 + 1, inter):
        t = threading.Thread(target=pi_val, args=(i, inter,)).start()

    pi = pow((pi * 12), 0.5)
    time_diff = time.time() - start_time
    print(f"Вычисленное значение Pi: {pi}\nВремя вычисления: {time_diff}")


def main():
    start_time = time.time()
    pi_counter(3, start_time)


if __name__ == "__main__":
    main()
