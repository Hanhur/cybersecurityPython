# =========================================================================================
# Строки (str) в Python представляют собой последовательно­сти символов, заключенные в кавычки. 
# Строки могут содержать символы любого типа, включая буквы, цифры, знаки препина­ния, пробелы и специальные символы. 
# Они являются одними из основных типов данных в Python и широко используются для работы с текстом.
# ==========================================================================================

# Конкатенация - это процесс объединения двух строк в одну.
# Конкатенация
greeting = 'hello' + ' ' + 'world' # 'hello world'

# Функция len() возвращает количество символов, содержащихся в строке.
# Длина строки
length = len('hello') # 5

# Индексация позволяет получить символ строки по его индексу. Индексация начинается с нуля.
# Индексация
first_char = 'hello'[0] # 'h'

# Срезы позволяют извлекать подстроки из строки.
# Срезы (slicing)
substring = 'hello' [1:3] # 'el'
# ==========================================================================================
# Обратная строка:
def reverse_string():
    # Запрашиваем строку у пользователя
    user_input = input("Введите строку для переворачивания: ")
    
    # Переворачиваем строку с помощью среза
    reversed_str = user_input[::-1]
    
    # Выводим результат
    print("\nРезультат:")
    print(f"Исходная строка: {user_input}")
    print(f"Перевернутая строка: {reversed_str}")

# Запускаем программу
print("Программа для переворачивания строки")
reverse_string()
# ======================================================================================
# Подсчет символов:
from collections import defaultdict

def count_characters():
    # Получаем строку от пользователя
    text = input("Введите строку для анализа: ")
    
    # Создаём словарь для подсчёта символов
    char_count = defaultdict(int)
    
    # Подсчитываем каждый символ
    for char in text:
        char_count[char] += 1
    
    # Сортируем символы для красивого вывода
    sorted_chars = sorted(char_count.items(), key = lambda x: x[1], reverse = True)
    
    # Выводим результаты
    print("\nРезультат подсчёта символов:")
    for char, count in sorted_chars:
        print(f"'{char}': {count} раз(а)")

# Запускаем программу
print("Программа для подсчёта символов в строке")
count_characters()
# =============================================================================================
# Замена символов:
def replace_chars():
    print("Программа замены символов в строке")
    
    # Ввод исходной строки
    text = input("Введите строку: ")
    
    # Ввод символа для замены с проверкой
    while True:
        old_char = input("Введите символ, который нужно заменить (только один символ): ")
        if len(old_char) == 1:
            break
        print("Ошибка: введите ровно один символ!")
    
    # Ввод символа-замены с проверкой
    while True:
        new_char = input("Введите символ для замены (только один символ): ")
        if len(new_char) == 1:
            break
        print("Ошибка: введите ровно один символ!")
    
    # Замена символов
    modified_text = text.replace(old_char, new_char)
    
    # Вывод результата
    print("\nРезультат замены:")
    print(f"Исходная строка: {text}")
    print(f"Модифицированная строка: {modified_text}")

# Запуск программы
replace_chars()
# =====================================================================================
# Палиндром:
import re

def is_palindrome():
    # Ввод строки от пользователя
    text = input("Введите строку для проверки на палиндром: ")
    
    # Очистка строки: удаление всего, кроме букв и цифр, и приведение к нижнему регистру
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', text).lower()
    
    # Проверка на палиндром
    if cleaned_text == cleaned_text[::-1]:
        print(f"Строка '{text}' ЯВЛЯЕТСЯ палиндромом")
    else:
        print(f"Строка '{text}' НЕ ЯВЛЯЕТСЯ палиндромом")

# Запуск программы
print("Проверка строки на палиндром (игнорирует пробелы, знаки препинания и регистр)")
is_palindrome()

# Альтернативная реализация (без регулярных выражений):
def is_palindrome_alternative():
    text = input("Введите строку: ")
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    print("Это палиндром!" if cleaned == cleaned[::-1] else "Это не палиндром")

# ================================================================================================
# Подсчет слов:
def count_words():
    # Ввод строки от пользователя
    text = input("Введите текст для подсчёта слов: ")
    
    # Разделение строки на слова (удаление лишних пробелов и разделение по пробелам)
    words = text.split()
    
    # Подсчёт количества слов
    word_count = len(words)
    
    # Вывод результата
    print(f"\nКоличество слов в тексте: {word_count}")

# Запуск программы
print("Программа для подсчёта слов в тексте")
count_words()
# ===================================================================================================
# Извлечение подстроки:
def extract_substring():
    # Ввод строки от пользователя
    text = input("Введите строку: ")
    length = len(text)
    
    try:
        # Ввод начального и конечного индексов
        start = int(input(f"Введите начальный индекс (0-{length-1}): "))
        end = int(input(f"Введите конечный индекс (0-{length-1}): "))
        
        # Проверка корректности индексов
        if start < 0 or end >= length:
            print(f"Ошибка: индексы должны быть в диапазоне 0-{length-1}")
            return
        if start > end:
            print("Ошибка: начальный индекс должен быть меньше или равен конечному")
            return
        
        # Извлечение подстроки
        substring = text[start:end+1]
        
        # Вывод результата
        print(f"\nИсходная строка: '{text}' (длина: {length})")
        print(f"Подстрока с {start} по {end} позицию: '{substring}'")
        
    except ValueError:
        print("Ошибка: введите целочисленные значения индексов")

# Запуск программы
print("Программа для извлечения подстроки по индексам")
extract_substring()
# ============================================================================================
# Смена регистра:
def swap_case():
    # Ввод строки от пользователя
    text = input("Введите строку для смены регистра: ")
    
    # Смена регистра каждого символа
    swapped_text = text.swapcase()
    
    # Вывод результата
    print("\nРезультат:")
    print(f"Исходная строка: {text}")
    print(f"Строка с изменённым регистром: {swapped_text}")

# Запуск программы
print("Программа для смены регистра символов (swap case)")
swap_case()

# Альтернативная реализация (без использования swapcase()):
def manual_swap_case():
    text = input("Введите строку: ")
    swapped = []
    for char in text:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)
    print(''.join(swapped))

# ==========================================================================================
# Удаление пробелов:
def remove_spaces():
    # Ввод строки от пользователя
    text = input("Введите строку для удаления пробелов: ")
    
    # Удаление всех пробелов
    no_spaces = text.replace(" ", "")
    
    # Вывод результата
    print("\nРезультат:")
    print(f"Исходная строка: '{text}'")
    print(f"Без пробелов: '{no_spaces}'")

# Запуск программы
print("Программа для удаления всех пробелов из строки")
remove_spaces()
# no_spaces = ''.join(text.split())
# import re
# no_spaces = re.sub(r'\s+', '', text)
# no_spaces = ''.join([char for char in text if char != ' '])
# no_whitespace = text.translate(str.maketrans('', '', ' \t\n\r\x0b\x0c'))
# ===================================================================================================
# Дублирование символов:
def duplicate_chars():
    # Ввод строки от пользователя
    text = input("Введите строку для дублирования символов: ")
    
    # Дублирование каждого символа
    duplicated = ''.join([char * 2 for char in text])
    
    # Вывод результата
    print("\nРезультат:")
    print(f"Исходная строка: {text}")
    print(f"С дублированными символами: {duplicated}")

# Запуск программы
print("Программа для дублирования символов в строке")
duplicate_chars()

# Альтернативные реализации:
# duplicated = ''
# for char in text:
#     duplicated += char * 2

# duplicated = ''.join(map(lambda x: x * 2, text))
# triplicated = ''.join([char * 3 for char in text])
# ==============================================================================================================
# Форматирование строки:
def capitalize_words():
    # Ввод строки от пользователя
    text = input("Введите строку для форматирования: ")
    
    # Приведение каждого слова к заглавному формату
    formatted_text = text.title()
    
    # Вывод результата
    print("\nРезультат форматирования:")
    print(f"Исходная строка: {text}")
    print(f"Форматированная строка: {formatted_text}")

# Запуск программы
print("Программа для форматирования строки с заглавными буквами в начале каждого слова")
capitalize_words()

# Альтернативная реализация (более точный контроль):
# import re

# def smart_title(text):
#     return re.sub(r"\b(\w)", lambda m: m.group(1).upper(), text)

# # Использование:
# formatted_text = smart_title(text)

# formatted_text = ' '.join(word.capitalize() for word in text.split())

# import string
# formatted_text = string.capwords(text)

# Метод title() уже работает с кириллицей
formatted_text = "привет мир".title()  # вернет "Привет Мир"