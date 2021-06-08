"""
Напишите программу, которая выводит на экран список номеров открытых портов на данной машине.
Использовать команду netstat.

--
Можно использовать команду netstat с флагами -atun или -l на ваш выбор
Python в данном случае выступает просто в виде обёртки
"""
import subprocess


def main():
    # Дергаем команду netstat через subprocess
    result = subprocess.getoutput("netstat -atun")
    print(result)


if __name__ == "__main__":
    main()
