"""
Напишите программу, которая выводит файл /etc/passwd с удаленного хоста

"""
import os
import sys


def main():
    # Если при запуске не были указаны параметры:
    if len(sys.argv) != 2:
        # Ввод первой части
        auth_and_ip = input(
            "Введите имя пользователя и ip адрес (например, root@127.0.0.1)\n->"
        )
    # Если были указаны параметры
    else:
        auth_and_ip = sys.argv[1]

    # Формирование итоговой строки
    command_result = f"ssh -p 22 {auth_and_ip} cat /etc/passwd"
    # Вывод на экран
    print(f"Сформировали команду: '{command_result}'")
    r = os.system(command_result)
    # Если все норм
    if r == 0:
        print("Успешно вывели файл")
    else:
        print("Что-то пошло не так")


if __name__ == "__main__":
    main()