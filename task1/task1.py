"""
Напишите программу, которая создает нить.
Родительская и вновь созданная нити должны распечатать десять строк текста.

---
Что происходит:
main вызывает print_2 в отдельном потоке и сам вызывает print_1 в себе
print_2 вызывает print_1 в отдельном потоке и сам вызывает print_1 в себе
получается так называемая нить потоков
"""
import threading


def print_1(t_name: str):
    for v in range(10):
        print(f"[Поток {t_name}] {v}")


def print_2():
    t = threading.Thread(target=print_1, args=("Thread 3",))
    t.start()
    print_1("Thread 2")


def main():
    t = threading.Thread(target=print_2())
    t.start()
    print_1("MAIN 1")


if __name__ == "__main__":
    main()
