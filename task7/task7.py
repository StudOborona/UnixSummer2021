"""
Напишите программу, которая проверяет все числа от 0 на простоту
и выводит простые числа на экран по мере нахождения.
Числа должны проверяться в различных потоках (или процессах, по выбору студента)
Программа должна работать до тех пор, пока ее не остановит пользователь.
"""

import queue
import threading

# Наша очередь из чисел, которые надо обработать в worker
que = queue.Queue(10)
# Флаг остановки потоков
work_flag = True


def worker(thread_num):
    """
    Вычисление простого числа
    Вызывается в отдельном потоке
    :param thread_num:
    :return:
    """
    while work_flag:
        # Флаг того, что число простое
        is_simple_flag = True
        # Если очередь не пустая
        if not que.empty():
            # Число на проверку
            current_number = int(que.get())
            for i in range(2, current_number):
                # Если число не простое
                if current_number % i == 0:
                    is_simple_flag = False
                    break

            if is_simple_flag:
                print(f'[Поток {thread_num}] Число {current_number} простое!')


def adder():
    """
    Метод для добавления числа в очередь
    Отрабатывает в отдельном потоке
    """
    current_number = 0
    while work_flag:
        que.put(current_number)
        current_number += 1


def main():
    # Да, это флаг остановки всех потоков и он глобальный, что ты мне сделаешь я в другмо городе
    global work_flag

    t = threading.Thread(target=adder)
    t.start()

    # Запускаем 10 воркеров, которые будут осуществлять работу
    for i in range(10):
        t = threading.Thread(target=worker, args=[i], name=f"Поток {i}")
        t.start()

    # В главном потоке ожидаем ввод, как ввели что-то - завершаем прогу
    _ = input()
    work_flag = False


if __name__ == "__main__":
    main()
