"""
Напишите программу, которая выводит список всех выполняющихся в текущий момент системных демонов.
Рядом с каждым вывести адрес его конфигурационного файла.
"""
import os
import subprocess


def main():
    # Команда для получения всех демонов, которые работают сейчас
    my_command = "systemctl --type=service --state=active | awk '{print $1}'"

    # Создаем процесс с выполнением этой команды
    p = subprocess.Popen(my_command, stdout=subprocess.PIPE, shell=True)

    # Получаем результат работы процесса
    out, err = p.communicate()

    # Формируем список демонов, которые присутствуют в системе
    daemon_list = [d for d in out.decode().split("\n") if ".service" in d]

    # Для каждого демона выполняем команду systemctl show -p FragmentPath, которая выводит путь до его файла
    for d in daemon_list:
        os.system(f"echo '\n{d}' && systemctl show -p FragmentPath {d} | sed 's/FragmentPath=//g'")


if __name__ == "__main__":
    main()
