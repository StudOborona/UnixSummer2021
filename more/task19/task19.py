"""
Реализуйте простой HTTP-клиент. Он принимает один параметр командной строки - URL.
Клиент делает запрос по указанному URL и выдает тело ответа на терминал как текст. Если HTML то распечатываем без форматирования.
Вывод производится по мере того, как даннные поступают из HTTP соединения. Когда будет выведено более 25 строк, клиент должен продолжить прием данных, но должен остановить вывод и выдать приглашение "Press SPACE to scroll down".
"""

import sys
import urllib.request
from pynput import keyboard


def main():
    # Если аргумент в виде URL не был принят - вводим его
    if len(sys.argv) != 2:
        url_input = input("Введите какой-либо URL -> ")
    else:
        url_input = sys.argv[1]

    # Открываем соединение
    web_request = urllib.request.urlopen(url_input)
    print(type(web_request))

    # Получаем код результата и выводим его
    print(f"Код результата: {web_request.getcode()}")

    # Вывод данных, которые получили
    global i
    i = 0   
    counter = 1

    mark = True

    while mark:
        
        while i < 25:
            if str(web_request.readline()).strip() == "b''":
                print("----- END OF FILE -----")
                break
                return False
            else:
                line = web_request.readline()
                print(str(counter) + " | " + str(line))
                counter += 1
                i += 1
            
        
        with keyboard.Events() as events:
            for event in events:
                if (event.key == keyboard.Key.space and str(type(event)) == "<class 'pynput.keyboard.Events.Press'>"):
                    i = 0
                    print("\n------------------\n\nВывод новых строк\n\n------------------")
                    break
                if event.key == keyboard.Key.esc:
                    return False


if __name__ == "__main__":
    main()
