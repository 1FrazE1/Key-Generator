import random
import string
import sys
import time
import os
import pygetwindow as gw
from colorama import Fore, Back, Style, init


def generate_random_key():
    # Задаем формат ключа
    key_format = 'AAAAA-BBBBB-CCCCC-DDDDD'

    # Генерируем 10 ключей
    generated_keys = []
    for _ in range(10):
        new_key = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            if char.isalnum() else char
            for char in key_format
        )
        generated_keys.append(new_key)

    return generated_keys

def keysconsole(keys):
    # Вывод ключей в консоль
    for key in keys:
        print(key)

def keystxt(keys, filename='generated_keys.txt'):
    # Вывод ключей в текстовый файл
    with open(filename, 'w') as file:
        for key in keys:
            file.write(key + '\n')

def set_fullscreen():
    window = gw.getWindowsWithTitle("")[0]
    window.maximize()
    

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
# Инициализация colorama
init(autoreset=True)

def dragon(color):
    print( Fore.BLUE + 
        """
   __________________________¶¶_______________
__________________¶¶____¶¶_________________
__________¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶______________
______¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________
__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶_____¶¶___¶¶¶¶________
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶______
____¶¶¶¶¶¶__¶¶____¶¶¶¶¶¶_________¶¶¶¶¶¶____
____¶¶______¶¶¶¶______¶¶¶¶¶¶___¶¶¶¶¶¶¶¶____
____________¶¶________¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶__
________¶¶__¶¶________¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶__
__________¶¶________¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶
________________¶¶¶¶¶¶¶¶¶¶_¶¶____¶¶¶¶__¶¶¶¶
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶__¶¶¶__¶¶¶¶____¶¶¶¶¶¶__¶¶
¶¶__¶¶¶¶¶¶¶¶____¶¶__¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶__¶¶
¶__¶¶¶¶¶¶¶¶____________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶___¶
___¶¶¶¶¶¶____¶¶¶¶________¶¶__________¶¶____
__¶¶¶¶¶¶_______¶¶¶¶____________________¶¶__
__¶¶¶¶¶¶¶_______¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
__¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____
_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶__
_______¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶____¶¶¶¶¶¶__
_________¶¶¶¶¶¶____________¶¶¶¶¶¶__¶¶¶¶¶¶¶¶
___________¶¶____________¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
__________________________¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶
_____¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶______
___¶¶¶¶______________¶¶¶¶¶¶______¶¶________
___¶¶__¶¶______________¶¶__________________
_¶¶__¶¶____________________________________
___¶¶___________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶___________
___¶¶___¶¶¶______¶¶__¶¶¶¶_______¶¶_________
_¶¶____¶¶¶¶¶¶¶__¶¶¶¶¶¶_________¶¶¶_________
_¶¶¶¶__¶¶__¶¶¶¶¶¶¶¶¶_________¶¶¶¶__________
_¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶_____________________
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶___________________
_____¶¶¶¶¶¶¶¶¶¶¶___________________________
______________¶¶___________________________ 
        """ )

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_keys_menu():
    print(Fore.LIGHTBLUE_EX + "Выберите способ генерации ключей:")
    print()
    print(Fore.LIGHTGREEN_EX + "1. Вывести в консоль")
    print(Fore.LIGHTGREEN_EX + "2. Записать в текстовый файл")
    
    print()
    choice = input("Введите номер варианта (1 или 2): ")
    print()

    keys = generate_random_key()

    if choice == '1':
        print()
        keysconsole(keys)
    elif choice == '2':
        print()
        filename = input("Введите имя файла (по умолчанию generated_keys): ")
        if not filename.endswith('.txt'):
            filename += '.txt'
        keystxt(keys, filename)
    else:
        print(Fore.RED + "Неверный вариант. Пожалуйста, введите 1 или 2❌")



def useful_menu():
    while True:
        clear_screen()
        print(Fore.LIGHTGREEN_EX + "======================================================")
        print(Fore.LIGHTBLUE_EX + "Генерация ключей:")
        print(Fore.LIGHTBLUE_EX + "1) Сгенерировать ключи")
        print(Fore.LIGHTGREEN_EX + "======================================================")

        choice = input("Выберите действие в полезном меню🔎: ")

        if choice == '1':
            generate_keys_menu()
        else:
            print(Fore.RED + "Неверный выбор❌. Попробуй еще разочек")
        print()    
        input(Fore.LIGHTGREEN_EX + "Нажми Enter чтобы войти в меню выбора⌨️") 

def main_menu():
    set_fullscreen()
    dragon(Fore.BLUE)
    print("============================================================================================================")
    type_text("Привет!👋 Это маленькое приложение было сделано FrazE👑 для генерации ключей", delay=0.03)
    print()
    input(Fore.LIGHTGREEN_EX + "Нажми Enter чтобы войти в меню выбора⌨️")
    
    while True:
        clear_screen()
        print(Fore.LIGHTGREEN_EX + "======================================================")
        print(Fore.LIGHTMAGENTA_EX + "1). Генерация ключей")
        print(Fore.LIGHTGREEN_EX + "======================================================")    
        
        choice = input("Выберите действие в главном меню🔎: : ")

        if choice == '1':
            useful_menu()    
        if choice == 'x':
            break
        else:
            print(Fore.RED + "Неверный выбор❌. Попробуй еще разочек")

if __name__ == "__main__":
    main_menu()