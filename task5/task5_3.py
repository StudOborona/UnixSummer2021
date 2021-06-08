"""
Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера.
Количество потоков программы должно определяться параметром командной строки.
--
Существует несколько вариантов решения, это один из них
Краткая форма
"""
import threading

pi = 1


def counter(n):
    global pi
    pi += (1 / (n ** 2))


def main():
    a = int(input("Введите кол-во потоков -> "))
    for i in range(a):
        threading.Thread(target=counter, args=(i + 2,)).start()
    print(pow((pi * 6), 0.5))


if __name__ == "__main__":
    main()
