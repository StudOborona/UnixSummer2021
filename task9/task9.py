"""
Напишите программу, которая выводит на экран список номеров открытых портов на данной машине.
Использовать команду netstat.
"""
import subprocess


def main():
    # Дергаем команду netstat через subprocess
    result = subprocess.getoutput("netstat -atun")
    # или можно через netstat -l
    print(result)


if __name__ == "__main__":
    main()
