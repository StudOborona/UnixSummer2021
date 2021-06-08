"""
Дана функция calculate(x, y).
Напишите программу, которая создает пул из 5 процессов и распределяет в этом пуле вычисление
функции на промежутке х от 0 до 1 с шагом 0,1. у равняется 2 всегда.
"""
import multiprocessing as mp


def calculate(x, y=2):
    """
    Функция calculate, умножает 2 числа
    На самом деле может делать что угодно, смысла в этом нет
    """
    return x * y


def main():
    # Создаем пул процессов
    pool = mp.Pool(processes=5)
    # Создаем список аргументов x для функции calculate
    args_list = [round(i * 0.1, 2) for i in range(11)]

    # Получаем результат выполнения
    result_list = list(pool.map(calculate, args_list))

    # Выводим результаты на экран
    for arg, result in zip(args_list, result_list):
        print(f"x = {arg}, результат = {result}")


if __name__ == "__main__":
    main()
