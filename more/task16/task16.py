"""
Напишите программу, которая выводит на экран все ссылки, которые содержатся в скачанном HTML документе

"""

def main():
    with open('test.html', 'r', encoding='utf-8') as f:
        text = f.read()
        s_index = 6 + text.find("href=\"")
        while s_index != 5:
            length = text[s_index:].find("\"")
            if length > 0:
                print(text[s_index:s_index+length])
            elif length == -1:
                break
            text = text[s_index+length+2:]
            s_index = 6 + text.find("href=\"")

if __name__ == "__main__":
    main()