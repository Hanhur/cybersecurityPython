# ====================================================================================================================
# Циклы в Python - это управляющие конструкции, которые позволяют программе выполнять один и тот же блок кода несколько раз. 
# Они являются фундаментальной частью любого языка программирования и предоставляют возможность автоматизировать выполнение повторяющихся задач.
# ====================================================================================================================

# В Python есть два основных типа циклов: цикл for и цикл while.

# Цикл for: этот цикл отлично подходит для перебора элементов в последовательностях, таких как списки, кортежи или строки.
# Каждый элемент последовательно обрабатывается в теле цикла

# Пример использования цикла for
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Цикл while: этот цикл продолжает выполнять блок кода до тех пор, пока заданное условие остается истинным.

# Пример использования цикла while
i = 1
while i <= 5:
    print(i)
    i += 1

# ==================================================== Подробнее о цикле for =====================================
# Цикл for в Python - это ваш личный помощник для перебора элементов в последовательности, будь то список, кортеж, строка или диапазон чисел. 
# Если вам когда-нибудь потребуется повто­рить одну и ту же операцию для каждого элемента в коллекции, цикл for сделает это легко и быстро.

# Пример использования цикла for
fruits = [ 'apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Перебор числовых диапазонов с помощью range()
# Цикл for также может быть использован для перебора числовых диапазонов с помощью функции range():
# Перебор числовых диапазонов с помощью range()
for i in range(1, 6):
    print(i)

# Перебор строк
text = "hello"
for char in text:
    print(char)

matrix = [ [ 1, 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Использование enumerate()
# Функция enumerate() позволяет получить индекс каждого элемента в последовательности наряду с самим элементом:
# Использование enumerate()
fruits = [ 'apple', 'banana', 'cherry' ]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Перебор словарей
# Цикл for также можно использовать для перебора ключей и значений в словаре:
# Перебор словарей
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Примеры использования цикла for
# Подсчет суммы элементов списка:
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print(f"Cyммa: {total}") # Выводит "Сумма: 15"

# Поиск максимального элемента в списке:
numbers = [10, 20, 30, 40, 50]
max_number = numbers[O]
for number in numbers:
    if number > max_number:
        max_number = number
print(f"Максимальное число: {max_number}") # Выводит "Максимальное число: 50"

# Со"здание нового списка на основе существующего:
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares) # Выводит [1, 4, 9, 16, 25]

# ===================================================================================================================

# Сумма чисел в списке:
# Создаем список чисел
numbers = [10, 20, 30, 40, 50]

# Инициализируем переменную для хранения суммы
total = 0

# Проходим по каждому числу в списке и добавляем его к сумме
for num in numbers:
    total += num

# Выводим результат
print("Сумма чисел в списке:", total)

# Если список вводит пользователь:
# Ввод списка чисел с клавиатуры (через пробел)
numbers = list(map(int, input("Введите числа через пробел: ").split()))

total = 0
for num in numbers:
    total += num

print("Сумма чисел:", total)

# Сумма с использованием sum() (альтернативный способ):
numbers = [10, 20, 30, 40, 50]
print("Сумма чисел:", sum(numbers))

# Проверка на пустой список:
numbers = []
if not numbers:
    print("Список пуст!")
else:
    total = sum(numbers)
    print("Сумма чисел:", total)

# =====================================================================================================

# Вывод элементов списка:
# Создаем список
fruits = ["яблоко", "банан", "апельсин", "киви"]

# Выводим каждый элемент на новой строке
for fruit in fruits:
    print(fruit)

# Вывод списка чисел:
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)

# Вывод с нумерацией:
fruits = ["яблоко", "банан", "апельсин"]
for index, fruit in enumerate(fruits, start = 1):
    print(f"{index}. {fruit}")

# Ввод списка от пользователя:
items = input("Введите элементы списка через запятую: ").split(',')
print("\nЭлементы списка:")
for item in items:
    print(item.strip())  # strip() удаляет лишние пробелы

# Вывод в обратном порядке:
colors = ["красный", "зеленый", "синий"]
for color in reversed(colors):
    print(color)

# ==================================================================================================

# Счетчик элементов:
# Создаем список
my_list = [10, 20, 30, 40, 50, 60]

# Инициализируем счетчик
count = 0

# Подсчитываем элементы
for element in my_list:
    count += 1

# Выводим результат
print("Количество элементов в списке:", count)

# С использованием функции len() (более питонический способ):
my_list = [10, 20, 30, 40, 50, 60]
print("Количество элементов:", len(my_list))

# Для списка, вводимого пользователем:
user_list = input("Введите элементы списка через пробел: ").split()
count = 0
for _ in user_list:  # Используем _, так как значение элемента не важно
    count += 1
print("Количество элементов:", count)

# Подсчет с условием (например, только четных чисел):
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Количество четных чисел:", even_count)

# ======================================================================================================

# Поиск максимального элемента:
# Создаем список чисел
numbers = [12, 45, 23, 67, 34, 89, 56]

# Инициализируем переменную для хранения максимального значения
max_number = numbers[0]  # Предполагаем, что первый элемент - максимальный

# Проходим по всем числам в списке
for num in numbers:
    # Если текущее число больше нашего максимума, обновляем максимум
    if num > max_number:
        max_number = num

# Выводим результат
print("Самый большой элемент в списке:", max_number)

# С пустым списком (обработка ошибки):
numbers = []
if not numbers:
    print("Список пустой!")
else:
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print("Максимальное число:", max_num)

# С вводом списка от пользователя:
numbers = list(map(int, input("Введите числа через пробел: ").split()))
if numbers:
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print("Максимальное число:", max_num)
else:
    print("Вы не ввели числа!")

# С использованием встроенной функции max() (альтернативный способ):
numbers = [12, 45, 23, 67, 34, 89, 56]
print("Максимальное число:", max(numbers))

# ==========================================================================================================

# Создание нового списка:
# Исходный список чисел
original_numbers = [1, 2, 3, 4, 5]

# Создаем пустой список для хранения квадратов
squared_numbers = []

# Проходим по каждому числу в исходном списке
for num in original_numbers:
    # Возводим число в квадрат и добавляем в новый список
    squared_numbers.append(num ** 2)

# Выводим результаты
print("Исходный список:", original_numbers)
print("Список квадратов:", squared_numbers)

# С использованием list comprehension (более питонический способ):
original_numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in original_numbers]
print(squared_numbers)

# С вводом списка от пользователя:
numbers = list(map(int, input("Введите числа через пробел: ").split()))
squares = []
for n in numbers:
    squares.append(n ** 2)
print("Квадраты чисел:", squares)

# С обработкой разных типов данных:
mixed_list = [1, 2.5, 3, 4.2, 5]
squares = []
for x in mixed_list:
    if isinstance(x, (int, float)):
        squares.append(x ** 2)
print(squares)

# ===============================================================================================================

# Фильтрация списка:
# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Создаем пустой список для четных чисел
even_numbers = []

# Фильтруем числа
for num in numbers:
    if num % 2 == 0:  # Проверяем, четное ли число
        even_numbers.append(num)  # Добавляем в новый список

# Выводим результаты
print("Исходный список:", numbers)
print("Четные числа:", even_numbers)

# С использованием list comprehension:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# С вводом списка от пользователя:
numbers = list(map(int, input("Введите числа через пробел: ").split()))
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print("Четные числа:", evens)

# Функция для фильтрации:
def filter_evens(number_list):
    return [num for num in number_list if num % 2 == 0]

print(filter_evens([11, 12, 13, 14, 15]))

# Фильтрация с сохранением индексов:
numbers = [1, 2, 3, 4, 5]
evens_with_index = [(i, num) for i, num in enumerate(numbers) if num % 2 == 0]
print(evens_with_index)  # Выведет [(1, 2), (3, 4)]

# ====================================================================================================================

# Поиск строки в списке:
# Исходный список строк
fruits = ["яблоко", "банан", "апельсин", "киви", "манго"]

# Искомая строка
search_word = input("Введите фрукт для поиска: ")

# Флаг для отслеживания найден ли элемент
found = False

# Поиск строки в списке
for index, fruit in enumerate(fruits):
    if fruit == search_word:
        print(f"Строка '{search_word}' найдена, индекс: {index}")
        found = True
        break  # Прерываем цикл после первого найденного совпадения

# Если строка не найдена
if not found:
    print(f"Строка '{search_word}' отсутствует в списке")

# Без использования break (находит все вхождения):
search_word = "привет"
words = ["привет", "мир", "привет", "python"]

found_any = False
for i, word in enumerate(words):
    if word == search_word:
        print(f"Найдено в позиции {i}")
        found_any = True

if not found_any:
    print("Не найдено")

# Регистронезависимый поиск:
search_word = input("Введите слово: ").lower()
words = ["Привет", "Мир", "Python"]

for i, word in enumerate(words):
    if word.lower() == search_word:
        print(f"Найдено в позиции {i}")
        break
else:
    print("Не найдено")

# С использованием метода index() (альтернативный способ):
try:
    index = fruits.index(search_word)
    print(f"Найдено в позиции {index}")
except ValueError:
    print("Не найдено")

# ==================================================================================================================

# Обратный вывод списка:
# Исходный список
my_list = [1, 2, 3, 4, 5]

# Выводим элементы в обратном порядке
print("Элементы списка в обратном порядке:")
for i in range(len(my_list)-1, -1, -1):
    print(my_list[i])

# Использование среза (самый питонический способ):
my_list = [1, 2, 3, 4, 5]
for item in my_list[::-1]:
    print(item)

# С помощью reversed():
my_list = [1, 2, 3, 4, 5]
for item in reversed(my_list):
    print(item)

# Для строк (работает аналогично):
word = "Привет"
for letter in reversed(word):
    print(letter)

# С сохранением обратного списка:
original = [1, 2, 3]
reversed_list = []
for item in original:
    reversed_list.insert(0, item)  # Вставляем каждый элемент в начало
print(reversed_list)  # [3, 2, 1]

# =========================================================================================================================

# Конкатенация строк:
# Исходный список строк
words = ["Hello", " ", "world", "!", " ", "This", " ", "is", " ", "Python"]

# Инициализируем пустую строку для результата
result = ""

# Объединяем строки
for word in words:
    result += word  # Добавляем каждое слово к результату

# Выводим итоговую строку
print("Результат конкатенации:", result)

# С использованием метода join() (более эффективный способ):
words = ["Hello", " ", "world", "!", " ", "This", " ", "is", " ", "Python"]
result = "".join(words)
print(result)

# С фильтрацией пустых строк:
words = ["Hello", "", "world", "!", None, "Python"]
result = ""
for word in words:
    if word:  # Проверяем, что строка не пустая и не None
        result += word
print(result)  # "Helloworld!Python"

# С добавлением разделителя:
words = ["apple", "banana", "orange"]
result = ""
for i, word in enumerate(words):
    if i > 0:  # Добавляем запятую перед всеми элементами кроме первого
        result += ", "
    result += word
print(result)  # "apple, banana, orange"

# Для списка с числами и строками:
items = [1, " apple", 2, " bananas", 3, " oranges"]
result = ""
for item in items:
    result += str(item)  # Преобразуем числа в строки
print(result)  # "1 apple2 bananas3 oranges"

# ===========================================================================================================

# Подсчет гласных в строке:
# Входная строка
text = input("Введите строку для анализа: ").lower()  # Переводим в нижний регистр

# Список гласных букв
vowels = "аеёиоуыэюяaeiou"  # Русские и английские гласные

# Инициализация счетчика
count = 0

# Подсчет гласных
for char in text:
    if char in vowels:
        count += 1

# Вывод результата
print(f"Количество гласных букв в строке: {count}")

# Только русские гласные:
vowels = "аеёиоуыэюя"  # Только русские гласные

# Подсчет каждой гласной отдельно:
from collections import defaultdict

text = input("Введите строку: ").lower()
vowels = "аеёиоуыэюяaeiou"
count = defaultdict(int)

for char in text:
    if char in vowels:
        count[char] += 1

print("Статистика гласных:")
for vowel, num in count.items():
    print(f"{vowel}: {num}")

# С использованием list comprehension:
text = input("Введите строку: ").lower()
vowels = "аеёиоуыэюяaeiou"
count = len([char for char in text if char in vowels])
print(f"Количество гласных: {count}")

# Для файла (подсчет гласных в текстовом файле):
with open("text.txt", "r", encoding = "utf-8") as file:
    text = file.read().lower()
    count = sum(1 for char in text if char in "аеёиоуыэюяaeiou")
    print(f"В файле {count} гласных букв")

# ===============================================================================================

# Создание списка пар (индекс, значение):
# Исходный список
original_list = ['яблоко', 'банан', 'апельсин', 'киви']

# Создаем новый список для пар (индекс, значение)
index_value_pairs = []

# Проходим по исходному списку и создаем пары
for index, value in enumerate(original_list):
    index_value_pairs.append((index, value))  # Добавляем кортеж в список

# Выводим результат
print("Исходный список:", original_list)
print("Список пар (индекс, значение):", index_value_pairs)

# С использованием list comprehension:
original_list = ['яблоко', 'банан', 'апельсин']
pairs = [(i, v) for i, v in enumerate(original_list)]
print(pairs)

# С начальным индексом не с 0:
original_list = ['a', 'b', 'c']
pairs = []
for i, v in enumerate(original_list, start = 1):  # Начинаем нумерацию с 1
    pairs.append((i, v))
print(pairs)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Для чисел:
numbers = [10, 20, 30, 40]
num_pairs = []
for idx, num in enumerate(numbers):
    num_pairs.append((idx, num, num ** 2))  # Можно добавлять больше элементов
print(num_pairs)  # [(0, 10, 100), (1, 20, 400), ...]

# С фильтрацией (только для определенных элементов):
words = ['apple', '', 'banana', None, 'orange']
pairs = [(i, w) for i, w in enumerate(words) if w]  # Пропускаем пустые и None
print(pairs)  # [(0, 'apple'), (2, 'banana'), (4, 'orange')]

# =====================================================================================================================

# Поиск всех подстрок в строке:
# Входные данные
input_string = input("Введите строку: ")
substring_length = int(input("Введите длину подстроки: "))

# Проверка корректности длины подстроки
if substring_length <= 0:
    print("Длина подстроки должна быть положительным числом!")
elif substring_length > len(input_string):
    print("Длина подстроки больше длины строки!")
else:
    # Список для хранения подстрок
    substrings = []
    
    # Извлечение всех подстрок указанной длины
    for i in range(len(input_string) - substring_length + 1):
        substring = input_string[i:i+substring_length]
        substrings.append(substring)
    
    # Вывод результата
    print(f"Все подстроки длины {substring_length}:")
    for substr in substrings:
        print(substr)
    
    # Альтернативный вывод в одну строку
    print("\nИли в виде списка:", substrings)

# Без сохранения в список (просто вывод):
for i in range(len(string) - n + 1):
    print(string[i:i + n])

# Уникальные подстроки:
unique_substrings = set()
for i in range(len(string) - n + 1):
    unique_substrings.add(string[i:i + n])
print(f"Уникальные подстроки: {unique_substrings}")

# Подсчет частоты подстрок:
from collections import defaultdict

substring_counts = defaultdict(int)
for i in range(len(string) - n + 1):
    substring_counts[string[i:i+n]] += 1

print("Частота подстрок:")
for substr, count in substring_counts.items():
    print(f"'{substr}': {count}")

# Для биологических последовательностей (ДНК):
dna = "ATGCGATAGCTAG"
k = 4  # Длина k-mer
kmers = [dna[i:i + k] for i in range(len(dna) - k + 1)]
print(f"Все {k}-меры: {kmers}")

# ===============================================================================================================

# Создание таблицы умножения:
# Создаем таблицу умножения 10x10
print("Таблица умножения от 1 до 10:")
print("   ", end = "")
for i in range(1, 11):  # Заголовок столбцов
    print(f"{i:4}", end = "")
print("\n" + "-" * 45)

for row in range(1, 11):  # Внешний цикл для строк
    print(f"{row:2} |", end = "")  # Заголовок строки
    for col in range(1, 11):  # Внутренний цикл для столбцов
        print(f"{row * col:4}", end = "")  # Вычисляем произведение
    print()  # Переход на новую строку после каждой строки таблицы

# Более компактный вывод:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end = " ")
    print()

# С использованием list comprehension:
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for row in table:
    print(' '.join(f"{num:3}" for num in row))

# Для произвольного диапазона:
n = int(input("Введите размер таблицы: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:6}", end = "")
    print()

# С сохранением в файл:
with open("multiplication_table.txt", "w") as f:
    for i in range(1, 11):
        for j in range(1, 11):
            f.write(f"{i * j:4}")
        f.write("\n")

# ========================================================================================================

# Проверка на простоту:
# Вводим число для проверки
num = int(input("Введите число для проверки на простоту: "))

# Числа меньше 2 не являются простыми
if num < 2:
    print(f"{num} не является простым числом")
else:
    # Предполагаем, что число простое, пока не найдем делитель
    is_prime = True
    
    # Проверяем делители от 2 до квадратного корня из числа
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Нашли делитель - прерываем цикл
    
    # Выводим результат
    if is_prime:
        print(f"{num} - простое число")
    else:
        print(f"{num} - составное число")

# Улучшенная версия: ======================================================
num = int(input("Введите число: "))

if num < 2:
    print("Не простое")
elif num == 2:
    print("Простое")
elif num % 2 == 0:
    print("Составное")
else:
    is_prime = True
    # Проверяем только нечетные делители от 3 до √num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            break
    print("Простое" if is_prime else "Составное")

# Функция для проверки простоты:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True

# Поиск всех простых чисел до N:
n = int(input("Введите N: "))
primes = []
for num in range(2, n + 1):
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        primes.append(num)
print("Простые числа:", primes)

# Решето Эратосфена (более эффективный способ для диапазона):
def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

print(sieve(100))

# ============================================================================================================

# Перевод всех символов в верхний регистр:
# Исходная строка
input_string = input("Введите строку: ")

# Создаем пустую строку для результата
upper_string = ""

# Проходим по каждому символу в строке
for char in input_string:
    # Преобразуем символ в верхний регистр и добавляем к результату
    upper_string += char.upper()

# Выводим результат
print("Строка в верхнем регистре:", upper_string)

# С использованием метода upper() для всей строки (более питонический способ):
input_string = "Пример строки"
print(input_string.upper())  # ПРИМЕР СТРОКИ

# С использованием list comprehension:
input_string = "тест"
upper_string = ''.join([char.upper() for char in input_string])
print(upper_string)  # ТЕСТ

# С обработкой только букв (цифры и спецсимволы остаются без изменений):
input_string = "a1b2c3!"
upper_string = ""
for char in input_string:
    if char.isalpha():  # Проверяем, является ли символ буквой
        upper_string += char.upper()
    else:
        upper_string += char
print(upper_string)  # A1B2C3!

# Для файла (перевод содержимого файла в верхний регистр):
with open("input.txt", "r") as file:
    content = file.read()
    upper_content = content.upper()
    print(upper_content)

# ========================================================================================================

# Сложение соответствующих элементов двух списков:
# Два списка чисел одинаковой длины
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# Проверка на одинаковую длину
if len(list1) != len(list2):
    print("Ошибка: списки разной длины!")
else:
    # Создаем пустой список для результатов
    result = []
    
    # Складываем соответствующие элементы
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    
    # Выводим результат
    print("Первый список:", list1)
    print("Второй список:", list2)
    print("Сумма элементов:", result)

# С использованием zip() и list comprehension:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [x + y for x, y in zip(list1, list2)]
print(result)  # [5, 7, 9]

# Для списков разной длины (суммирование до длины короткого списка):
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30]
result = []
min_length = min(len(list1), len(list2))
for i in range(min_length):
    result.append(list1[i] + list2[i])
print(result)  # [11, 22, 33]

# С обработкой разных типов данных:
list1 = [1, 2.5, "hello"]
list2 = [3, 1.5, " world"]
result = []
for i in range(min(len(list1), len(list2))):
    if isinstance(list1[i], (int, float)) and isinstance(list2[i], (int, float)):
        result.append(list1[i] + list2[i])
    else:
        result.append(str(list1[i]) + str(list2[i]))
print(result)  # [4, 4.0, 'hello world']

# С использованием функции map():
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)  # [5, 7, 9]

# =============================================================================================================

# Подсчет слов в строке:
# Входная строка
input_string = input("Введите строку для подсчета слов: ")

# Разделяем строку на слова по пробелам
words = input_string.split()

# Инициализируем счетчик
word_count = 0

# Подсчитываем слова
for word in words:
    if word:  # Проверяем, что слово не пустое (на случай нескольких пробелов подряд)
        word_count += 1

# Выводим результат
print(f"Количество слов в строке: {word_count}")

# Без использования цикла (более питонический способ):
input_string = "Это пример строки"
word_count = len(input_string.split())
print(word_count)  # 3

# С обработкой знаков пунктуации:
import string

input_string = "Привет, мир! Как дела?"
# Удаляем пунктуацию
translator = str.maketrans('', '', string.punctuation)
clean_string = input_string.translate(translator)
word_count = len(clean_string.split())
print(word_count)  # 4

# Сложный случай с разными разделителями:
import re

input_string = "Слово1, слово2\nслово3\tслово4"
words = re.split(r'[\s,;]+', input_string)  # Разделяем по пробелам, запятым, точкам с запятой
word_count = len([word for word in words if word])
print(word_count)  # 4

# Подсчет частоты слов:
from collections import defaultdict

input_string = "яблоко груша яблоко апельсин"
words = input_string.split()
word_freq = defaultdict(int)

for word in words:
    word_freq[word] += 1

print("Частота слов:", dict(word_freq))
# Вывод: {'яблоко': 2, 'груша': 1, 'апельсин': 1}

# ===============================================================================================================

# Удвоение всех чисел в списке:
# Исходный список чисел
numbers = [1, 2, 3, 4, 5]

# Создаем пустой список для хранения результатов
doubled_numbers = []

# Удваиваем каждое число и добавляем в новый список
for num in numbers:
    doubled_numbers.append(num * 2)

# Выводим результаты
print("Исходный список:", numbers)
print("Удвоенные числа:", doubled_numbers)

# С использованием list comprehension (более компактный способ):
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# С вводом списка от пользователя:
numbers = list(map(int, input("Введите числа через пробел: ").split()))
doubled = []
for num in numbers:
    doubled.append(num * 2)
print("Удвоенные числа:", doubled)

# С применением функции map():
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Для чисел с плавающей точкой:
floats = [1.5, 2.7, 3.14]
doubled_floats = [x * 2 for x in floats]
print(doubled_floats)  # [3.0, 5.4, 6.28]

# ==========================================================================================================

# Создание списка строк определенной длины:
# Исходный список строк
strings = ["яблоко", "груша", "апельсин", "киви", "банан"]

# Запрашиваем минимальную длину строки
min_length = int(input("Введите минимальную длину строки: "))

# Создаем пустой список для результатов
filtered_strings = []

# Фильтруем строки по длине
for s in strings:
    if len(s) > min_length:
        filtered_strings.append(s)

# Выводим результаты
print(f"Исходный список: {strings}")
print(f"Строки длиной больше {min_length}: {filtered_strings}")

# С использованием list comprehension:
min_length = 4
strings = ["cat", "dog", "elephant", "bird"]
filtered = [s for s in strings if len(s) > min_length]
print(filtered)  # ['elephant', 'bird']

# С вводом списка от пользователя:
input_strings = input("Введите строки через запятую: ").split(',')
min_len = int(input("Минимальная длина: "))
result = [s.strip() for s in input_strings if len(s.strip()) > min_len]
print(result)

# С фильтрацией и сохранением индексов:
strings = ["Python", "C++", "JavaScript", "Java"]
min_len = 4
result = [(i, s) for i, s in enumerate(strings) if len(s) > min_len]
print(result)  # [(0, 'Python'), (2, 'JavaScript'), (3, 'Java')]

# С использованием функции filter():
words = ["hello", "world", "python", "code"]
filtered = list(filter(lambda x: len(x) > 4, words))
print(filtered)  # ['hello', 'world', 'python']

# =================================================================================================================

# Генерация списка чисел в диапазоне:
# Вводим границы диапазона
start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

# Создаем пустой список
numbers = []

# Генерируем числа в диапазоне
for num in range(start, end + 1):  # end + 1 чтобы включить последнее число
    numbers.append(num)

# Выводим результат
print(f"Список чисел от {start} до {end}: {numbers}")

# С использованием list comprehension:
start, end = 5, 10
numbers = [num for num in range(start, end + 1)]
print(numbers)  # [5, 6, 7, 8, 9, 10]

# С шагом (например, только четные числа):
start, end = 2, 10
even_numbers = []
for num in range(start, end + 1, 2):  # Третий аргумент - шаг
    even_numbers.append(num)
print(even_numbers)  # [2, 4, 6, 8, 10]

# В обратном порядке:
start, end = 5, 1
numbers = []
for num in range(start, end - 1, -1):  # Отрицательный шаг
    numbers.append(num)
print(numbers)  # [5, 4, 3, 2, 1]

# Для вещественных чисел:
start, end = 1.5, 3.5
step = 0.5
numbers = []
current = start
while current <= end + 0.0001:  # Учет погрешности float
    numbers.append(round(current, 1))
    current += step
print(numbers)  # [1.5, 2.0, 2.5, 3.0, 3.5]

# ========================================= Подробнее о цикле while =======================================
# Цикл while в Python используется для выполнения блока кода, пока заданное условие остаётся истинным. 
# Цикл будет повторять выполнение этого блока до тех пор, пока условие возвра­щает значение True. 
# Как только условие перестаёт выполняться, программа выходит из цикла.
# ===========================================================================================================

# При каждой итерации цикла while сначала проверяется условие. Если ус­ловие истинно, выполняется блок кода, расположенный внутри цикла while.
# После выполнения этого блока кода программа снова возвращается к про­верке условия. 
# Если условие остаётся и�тинным, цикл продолжается; если условие становится ложным, выполнение цикла прекращается, 
# и программа переходит к следующей инструкции, идущей после цикла.

# Пример использования цикла while
i = 1
while i <= 5:
    print(i)
    i += 1

# Цикл while
while True:
    user_input = input("Введите 'стоп' для завершения: ")
    if user_input.lower() == 'стоп':
        break

# В этом примере цикл while становится бесконечным, потому что условие True всегда истинно. 
# Цикл будет продолжаться до тех пор, пока пользователь не введет слово "стоп". 
# Когда это происходит, срабатывает оператор break, и цикл завершается.

# Оператор break используется для того, чтобы сразу завершить цикл, даже если условие для продолжения цикла по-прежнему истинно.

# Оператор break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Оператор continue пропускает оставшуюся часть кода в текущей итерации цикла и сразу переходит к следующему кругу цикла.

# Оператор continue
i = о
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Примеры использования цикла while =============================================
# Подсчет суммы чисел
total = О
num = 1
while num <= 100:
    total += num
    num += 1
print(f"Cyммa чисел от 1 до 100: {total}")

# Игра угадай число
import random

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("Угaдaйтe число от 1 до 100: "))
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
print("Поздравляю! Вы угадали число.")

# ===============================================================================================================================

# Подсчет до заданного числа:
# Вводим конечное число
n = int(input("Введите конечное число: "))

# Инициализируем счетчик
count = 1

# Выводим числа с помощью цикла while
while count <= n:
    print(count)
    count += 1  # Увеличиваем счетчик на 1

print("Счет завершен!")

# Счет с произвольного числа:
start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

current = start
while current <= end:
    print(current)
    current += 1

# Счет с шагом:
n = int(input("Введите конечное число: "))
step = int(input("Введите шаг: "))

count = 1
while count <= n:
    print(count)
    count += step

# Обратный счет:
n = int(input("Введите число: "))

while n > 0:
    print(n)
    n -= 1
print("Пуск!")

# С проверкой ввода:
while True:
    try:
        n = int(input("Введите положительное число: "))
        if n > 0:
            break
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

count = 1
while count <= n:
    print(count)
    count += 1

# ========================================================================================================================

# Сумма чисел до нуля:
# Инициализируем сумму
total = 0

# Запрашиваем первое число
num = int(input("Введите число (0 для завершения): "))

# Цикл while продолжается, пока не будет введен 0
while num != 0:
    total += num  # Добавляем число к сумме
    num = int(input("Введите число (0 для завершения): "))  # Запрашиваем следующее число

# Выводим результат
print(f"Сумма введенных чисел: {total}")

# С проверкой ввода (обработка нечисловых значений):
total = 0
while True:
    try:
        num = int(input("Введите число (0 для выхода): "))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Пожалуйста, введите целое число!")

print(f"Итоговая сумма: {total}")

# С учетом дробных чисел:
total = 0.0
while True:
    try:
        num = float(input("Введите число (0 для завершения): "))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Пожалуйста, введите число!")

print(f"Сумма: {total:.2f}")  # Вывод с 2 знаками после запятой

# С подсчетом количества введенных чисел:
total = 0
count = 0
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    total += num
    count += 1

print(f"Сумма {count} чисел: {total}")

# С сохранением всех введенных чисел:
numbers = []
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    numbers.append(num)

print(f"Введенные числа: {numbers}")
print(f"Сумма: {sum(numbers)}")

# ==========================================================================================================

# Угадай число:
import random

# Компьютер загадывает число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    try:
        # Пользователь вводит свою догадку
        guess = int(input("Твой вариант: "))
        attempts += 1
        
        # Проверяем догадку
        if guess < secret_number:
            print("Мое число больше!")
        elif guess > secret_number:
            print("Мое число меньше!")
        else:
            print(f"Поздравляю! Ты угадал за {attempts} попыток!")
            break
    except ValueError:
        print("Пожалуйста, вводи только целые числа!")

print("Спасибо за игру!")

# Ограничение попыток:
max_attempts = 10
while attempts < max_attempts:
    # ... остальной код ...
    if attempts == max_attempts:
        print(f"Увы, ты не угадал. Я загадал {secret_number}")

# Уровни сложности:
level = input("Выбери сложность (легко/средне/тяжело): ").lower()
if level == "легко":
    secret_number = random.randint(1, 20)
elif level == "средне":
    secret_number = random.randint(1, 50)
else:
    secret_number = random.randint(1, 100)

# Подсчет рекордов:
best_score = float('inf')
while input("Хочешь сыграть еще? (да/нет): ").lower() == 'да':
    # ... игра ...
    if attempts < best_score:
        best_score = attempts
        print(f"Новый рекорд: {best_score} попыток!")

# ==============================================================================================================

# Ввод корректного пароля:
# Задаем правильный пароль
correct_password = "Secure123"

# Инициализируем переменную для хранения ввода пользователя
user_input = ""

# Цикл продолжается, пока введенный пароль не совпадет с правильным
while user_input != correct_password:
    user_input = input("Введите пароль: ")
    if user_input != correct_password:
        print("Неверный пароль. Попробуйте еще раз.")

print("Доступ разрешен!")

# Ограничение попыток:
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Доступ разрешен!")
        break
    else:
        attempts += 1
        print(f"Неверный пароль. Осталось попыток: {max_attempts - attempts}")
else:
    print("Превышено количество попыток. Доступ заблокирован!")

# Скрытие ввода пароля (используя модуль getpass):
from getpass import getpass

while True:
    password = getpass("Введите пароль: ")  # Ввод не отображается на экране
    if password == correct_password:
        print("Доступ разрешен!")
        break
    print("Неверный пароль. Попробуйте еще раз.")

# Проверка сложности пароля перед установкой:
import re

def is_strong_password(pwd):
    return (len(pwd) >= 8 and 
            re.search(r"[A-Z]", pwd) and 
            re.search(r"[a-z]", pwd) and 
            re.search(r"\d", pwd))

while True:
    new_password = input("Установите новый пароль: ")
    if is_strong_password(new_password):
        correct_password = new_password
        print("Пароль установлен!")
        break
    print("Пароль должен содержать 8+ символов, буквы в разных регистрах и цифры")

# Хеширование пароля (для реальных приложений):
import hashlib

# При установке пароля
stored_hash = hashlib.sha256("Secure123".encode()).hexdigest()

# При проверке
while True:
    attempt = input("Введите пароль: ")
    if hashlib.sha256(attempt.encode()).hexdigest() == stored_hash:
        print("Доступ разрешен!")
        break
    print("Неверный пароль")

# ==========================================================================================================

# Факториал числа:
# Вводим число для вычисления факториала
n = int(input("Введите целое положительное число: "))

# Инициализируем переменные
factorial = 1
current = n

# Вычисляем факториал с помощью цикла while
while current > 1:
    factorial *= current  # Умножаем текущее значение
    current -= 1         # Уменьшаем текущее число

# Выводим результат
print(f"Факториал числа {n} равен: {factorial}")

# Проверка ввода (для отрицательных чисел):
n = -1
while n < 0:
    try:
        n = int(input("Введите целое неотрицательное число: "))
        if n < 0:
            print("Число должно быть неотрицательным!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

factorial = 1
current = n
while current > 1:
    factorial *= current
    current -= 1

print(f"{n}! = {factorial}")

# Для 0! = 1 (по математическому определению):
n = int(input("Введите число: "))
if n < 0:
    print("Факториал отрицательного числа не определен")
else:
    factorial = 1
    i = n
    while i > 0:
        factorial *= i
        i -= 1
    print(f"{n}! = {factorial}")

# Рекурсивный способ (альтернатива циклу):
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))  # 120

# С использованием math.factorial (встроенная функция):
import math
print(math.factorial(5))  # 120

# =====================================================================================================

# Проверка на простоту:
# Вводим число для проверки
num = int(input("Введите число для проверки на простоту: "))

# Обрабатываем особые случаи
if num < 2:
    print(f"{num} не является простым числом")
else:
    # Инициализация переменных
    is_prime = True  # Предполагаем, что число простое
    divisor = 2      # Первый возможный делитель
    
    # Проверяем делители до квадратного корня из числа
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False  # Нашли делитель
            break
        divisor += 1
    
    # Выводим результат
    if is_prime:
        print(f"{num} - простое число")
    else:
        print(f"{num} - составное число (делится на {divisor})")

# Проверка четности заранее (ускорение в 2 раза):
if num < 2:
    print("Не простое")
elif num == 2:
    print("Простое")
elif num % 2 == 0:
    print("Составное (четное)")
else:
    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            print(f"Составное (делится на {divisor})")
            break
        divisor += 2  # Проверяем только нечетные делители
    else:
        print("Простое")

# Подсчет количества делителей:
num = int(input("Введите число: "))
if num < 2:
    print("Не простое")
else:
    count = 0
    divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            count += 1
        divisor += 1
    print("Простое" if count == 2 else "Составное")

# Проверка нескольких чисел:
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

numbers = [17, 25, 31, 42]
for n in numbers:
    print(f"{n}: {'Простое' if is_prime(n) else 'Составное'}")

# ===============================================================================================================

# Обратный вывод строки:
# Вводим строку от пользователя
input_string = input("Введите строку: ")

# Инициализируем индекс последнего символа
index = len(input_string) - 1

# Выводим символы в обратном порядке
print("Строка в обратном порядке: ", end = "")
while index >= 0:
    print(input_string[index], end = "")
    index -= 1  # Переходим к предыдущему символу

print()  # Переход на новую строку после вывода

# С использованием срезов (более питонический способ):
text = "Пример"
print(text[::-1])  # "ремирп"

# С созданием обратной строки:
text = "Hello"
reversed_text = ""
i = len(text) - 1
while i >= 0:
    reversed_text += text[i]
    i -= 1
print(reversed_text)  # "olleH"

# Для кириллицы и сложных символов:
import sys
text = "Привет😊"
reversed_text = ""
i = len(text)
while i > 0:
    i -= 1
    # Корректная обработка surrogate pairs (эмодзи и др.)
    if 0xD800 <= ord(text[i]) <= 0xDBFF:
        reversed_text += text[i - 1] + text[i]
        i -= 1
    else:
        reversed_text += text[i]
print(reversed_text)  # "😊тевирП"

# С использованием списка:
text = "Python"
chars = list(text)
i = len(chars) - 1
while i >= 0:
    print(chars[i], end = "")
    i -= 1
print()  # "nohtyP"

# ===============================================================================================

# Нахождение наибольшего числа:
# Инициализация переменных
max_number = None  # Начальное значение (ещё нет чисел)
user_input = None  # Для хранения ввода пользователя

print("Вводите числа. Для завершения введите 0.")

while True:
    try:
        user_input = float(input("Введите число: "))  # Преобразуем в число
        
        if user_input == 0:
            break  # Выход из цикла при вводе 0
            
        # Обновляем максимальное число
        if max_number is None or user_input > max_number:
            max_number = user_input
            
    except ValueError:  # Обработка нечислового ввода
        print("Ошибка! Введите число.")

# Вывод результата
if max_number is not None:
    print(f"Наибольшее введённое число: {max_number}")
else:
    print("Вы не ввели ни одного числа.")

# Подсчёт количества чисел:
count = 0
while True:
    num = float(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    if count == 0 or num > max_number:
        max_number = num
    count += 1
print(f"Из {count} чисел наибольшее: {max_number}")

# Сохранение всех чисел:
numbers = []
while True:
    num = float(input("Введите число: "))
    if num == 0:
        break
    numbers.append(num)
    
if numbers:
    print(f"Наибольшее из {len(numbers)} чисел: {max(numbers)}")

# Работа с целыми числами:
max_num = None
print("Вводите целые числа. 0 - выход.")
while True:
    try:
        num = int(input("> "))
        if num == 0:
            break
        max_num = num if max_num is None else max(max_num, num)
    except ValueError:
        print("Целое число, пожалуйста!")

# Вывод нескольких статистик:
count = sum = 0
max_num = min_num = None

while True:
    num = float(input("Число (0 - стоп): "))
    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num
    count += 1
    sum += num

print(f"""Статистика:
    Количество: {count}
    Максимум: {max_num}
    Минимум: {min_num}
    Среднее: {sum / count if count else 0}""")

# ==================================================================================================================

# Числа Фибоначчи:
# Вводим верхнюю границу последовательности
limit = int(input("Введите верхнюю границу для последовательности Фибоначчи: "))

# Инициализируем первые два числа Фибоначчи
a, b = 0, 1

# Выводим начальные числа
print("Последовательность Фибоначчи до", limit, ":", end = " ")
print(a, end = " ")

# Генерируем числа Фибоначчи с помощью цикла while
while b <= limit:
    print(b, end = " ")
    a, b = b, a + b  # Обновляем значения: a становится b, b становится суммой a и b

# С сохранением последовательности в список:
limit = 100
fib_sequence = [0, 1]
while fib_sequence[-1] + fib_sequence[-2] <= limit:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(fib_sequence)

# Генерация N чисел Фибоначчи:
n = int(input("Сколько чисел Фибоначчи вывести? "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end = " ")
    a, b = b, a + b
    count += 1

# С проверкой ввода:
while True:
    try:
        limit = int(input("Введите положительное число: "))
        if limit >= 0:
            break
        print("Число должно быть положительным!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

a, b = 0, 1
print(a, end=" ")
while b <= limit:
    print(b, end = " ")
    a, b = b, a + b

# Функция для генерации Фибоначчи:
def fibonacci_up_to(limit):
    a, b = 0, 1
    result = [a]
    while b <= limit:
        result.append(b)
        a, b = b, a + b
    return result

print(fibonacci_up_to(100))

# ========================================================================================

# Список чисел до нуля:
# Создаем пустой список для хранения чисел
numbers = []

# Запрашиваем первое число
num = int(input("Введите число (0 для завершения): "))

# Цикл while продолжается, пока не будет введен 0
while num != 0:
    numbers.append(num)  # Добавляем число в список
    num = int(input("Введите число (0 для завершения): "))  # Запрашиваем следующее число

# Выводим результат
print("Введенные числа:", numbers)

# С обработкой нечислового ввода:
numbers = []
while True:
    try:
        num = int(input("Введите число (0 для выхода): "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Пожалуйста, введите целое число!")

print("Список введенных чисел:", numbers)

# Сохранение только положительных чисел:
numbers = []
num = int(input("Введите число (0 для завершения): "))
while num != 0:
    if num > 0:
        numbers.append(num)
    num = int(input("Введите число (0 для завершения): "))

print("Положительные числа:", numbers)

# Подсчет суммы введенных чисел:
numbers = []
total = 0
num = int(input("Введите число (0 для завершения): "))
while num != 0:
    numbers.append(num)
    total += num
    num = int(input("Введите число (0 для завершения): "))

print("Список чисел:", numbers)
print("Сумма чисел:", total)

# Сохранение в файл:
numbers = []
num = int(input("Введите число (0 для завершения): "))
while num != 0:
    numbers.append(num)
    num = int(input("Введите число (0 для завершения): "))

with open("numbers.txt", "w") as file:
    file.write(str(numbers))

print("Числа сохранены в файл numbers.txt")

# =========================================================================================================

# Создание пароля:
# Задаем длину пароля
password_length = 8

# Инициализируем переменные
password = ""
current_length = 0

print(f"Создайте пароль длиной {password_length} символов:")

# Цикл для ввода символов
while current_length < password_length:
    char = input(f"Введите символ {current_length + 1} / {password_length}: ")
    
    # Проверяем, что введен ровно один символ
    if len(char) == 1:
        password += char
        current_length += 1
    else:
        print("Пожалуйста, введите ровно один символ!")

# Выводим результат
print("\nВаш пароль создан:", password)

# Скрытие ввода пароля (используя модуль getpass):
from getpass import getpass

password = ""
while len(password) < 8:
    char = getpass("Введите символ (не отображается): ")
    if len(char) == 1:
        password += char
    else:
        print("Нужно ввести ровно один символ!")
print("Пароль создан!")

# Проверка сложности пароля:
import re

def is_strong(pwd):
    return (len(pwd) >= 8 and
            re.search(r"[A-Z]", pwd) and
            re.search(r"[a-z]", pwd) and
            re.search(r"\d", pwd))

password = ""
while True:
    char = input(f"Символ {len(password)+1}/мин.8 (0-завершить): ")
    if char == '0':
        if len(password) >= 8:
            break
        print("Минимум 8 символов!")
    elif len(char) == 1:
        password += char
    else:
        print("1 символ!")
    
    if is_strong(password):
        print("Пароль достаточно надежный!")
        break

# Случайный порядок ввода:
import random

chars_needed = ['A', 'a', '1', '!']  # Пример требований
password = []

while len(password) < 10 or not all(c in password for c in chars_needed):
    req = random.choice(chars_needed)
    char = input(f"Введите {req}: ")
    if char == req:
        password.append(char)
        chars_needed.remove(req)
    else:
        print(f"Нужно ввести {req}")

print("Пароль:", ''.join(password))

# С ограниченным количеством попыток:
max_attempts = 3
password = ""

while len(password) < 6 and max_attempts > 0:
    char = input(f"Осталось попыток: {max_attempts}. Введите символ: ")
    if len(char) == 1:
        password += char
    else:
        max_attempts -= 1
        print("Ошибка! Используйте 1 символ.")

if len(password) == 6:
    print("Пароль создан!")
else:
    print("Не удалось создать пароль")

# ======================================================================================================

# Удвоение чисел:
# Исходный список чисел
numbers = [1, 2, 3, 4, 5]

# Создаем новый список для удвоенных чисел
doubled_numbers = []

# Инициализируем счетчик
index = 0

# Цикл while проходит по каждому элементу списка
while index < len(numbers):
    # Удваиваем текущее число и добавляем в новый список
    doubled_numbers.append(numbers[index] * 2)
    # Увеличиваем счетчик
    index += 1

# Выводим результат
print("Исходный список:", numbers)
print("Удвоенные числа:", doubled_numbers)

# Изменение исходного списка (без создания нового):
numbers = [1, 2, 3]
index = 0
while index < len(numbers):
    numbers[index] *= 2
    index += 1
print(numbers)  # [2, 4, 6]

# С использованием срезов:
numbers = [10, 20, 30]
doubled = []
i = 0
while i < len(numbers):
    doubled += [numbers[i] * 2]
    i += 1
print(doubled)  # [20, 40, 60]

# Для списка с разными типами данных:
mixed = [1, 2.5, 'a', 4]
result = []
i = 0
while i < len(mixed):
    if isinstance(mixed[i], (int, float)):
        result.append(mixed[i] * 2)
    else:
        result.append(mixed[i])
    i += 1
print(result)  # [2, 5.0, 'a', 8]

# С обработкой ввода пользователя:
numbers = []
print("Вводите числа по одному (0 для завершения):")
while True:
    num = input("> ")
    if num == '0':
        break
    try:
        numbers.append(float(num))
    except ValueError:
        print("Пожалуйста, введите число!")

# Удваиваем
i = 0
while i < len(numbers):
    numbers[i] *= 2
    i += 1

print("Удвоенные числа:", numbers)

# =================================================================================================

# Отгадай слово:
# Загаданное слово (можно заменить на random.choice из списка)
secret_word = "программирование"
guessed_letters = []  # Уже угаданные буквы
attempts = 0          # Количество попыток

print("Добро пожаловать в игру 'Угадай слово'!")
print("Слово состоит из", len(secret_word), "букв.")

# Основной игровой цикл
while True:
    # Формируем текущее состояние слова
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nТекущее состояние:", display_word)
    
    # Проверяем, угадано ли слово полностью
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nПоздравляем! Вы угадали слово '{secret_word}' за {attempts} попыток!")
        break
    
    # Запрашиваем букву у пользователя
    guess = input("Введите букву: ").lower()
    
    # Проверка ввода
    if len(guess) != 1 or not guess.isalpha():
        print("Пожалуйста, введите одну букву!")
        continue
    
    attempts += 1
    
    # Проверяем, есть ли буква в слове
    if guess in secret_word and guess not in guessed_letters:
        print("Верно! Такая буква есть в слове.")
        guessed_letters.append(guess)
    elif guess in guessed_letters:
        print("Вы уже называли эту букву.")
    else:
        print("К сожалению, такой буквы нет в слове.")

# Случайный выбор слова:
import random
words = ["программирование", "компьютер", "алгоритм", "информатика"]
secret_word = random.choice(words)

# Ограничение попыток:
max_attempts = 10
while attempts < max_attempts:
    # ... игровой процесс ...
    if attempts == max_attempts:
        print(f"Вы проиграли! Загаданное слово: {secret_word}")

# Визуализация виселицы:
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', ...]  # Добавьте все стадии
print(hangman_pics[attempts])

# Поддержка всей фразы:
secret_phrase = "я люблю python"
# При проверке игнорируем пробелы:
if all(letter in guessed_letters or letter == ' ' for letter in secret_phrase):
    print("Вы угадали!")

# ========================================================================================================

# Создание таблицы умножения:
# Инициализация переменных
i = 1  # Счетчик для строк

print("Таблица умножения от 1 до 10:")
print("----------------------------------------")

# Внешний цикл для строк (множители)
while i <= 10:
    j = 1  # Счетчик для столбцов
    row = ""  # Строка для вывода
    
    # Внутренний цикл для столбцов
    while j <= 10:
        product = i * j
        # Форматируем вывод для ровных столбцов
        row += f"{product:4}"  # Каждое число занимает 4 символа
        j += 1
    
    # Выводим строку таблицы
    print(f"{i:2} |{row}")  # Номер строки с выравниванием
    i += 1

print("----------------------------------------")

# С заголовками столбцов:
print("    ", end = "")
for k in range(1, 11):
    print(f"{k:4}", end = "")
print("\n" + "-" * 44)

i = 1
while i <= 10:
    print(f"{i:2} |", end = "")
    j = 1
    while j <= 10:
        print(f"{i * j:4}", end = "")
        j += 1
    print()
    i += 1

# Вертикальная таблица:
j = 1
while j <= 10:
    i = 1
    while i <= 10:
        print(f"{i} x {j} = {i * j:2}", end = "   ")
        i += 1
    print()
    j += 1

# Сохранение в файл:
with open("multiplication_table.txt", "w") as f:
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            f.write(f"{i * j:4}")
            j += 1
        f.write("\n")
        i += 1

# =========================================================================================================

# Валидация ввода:
while True:
    user_input = input("Введите целое число: ")
    
    try:
        # Пытаемся преобразовать ввод в целое число
        number = int(user_input)
        print(f"Вы ввели корректное число: {number}")
        break  # Выход из цикла при успешном вводе
    except ValueError:
        # Если преобразование не удалось
        print("Ошибка! Введите целое число. Попробуйте еще раз.")

# Проверка диапазона чисел:
while True:
    try:
        num = int(input("Введите число от 1 до 100: "))
        if 1 <= num <= 100:
            print("Число в допустимом диапазоне!")
            break
        else:
            print("Число должно быть от 1 до 100!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

# Для положительных чисел:
while True:
    try:
        num = int(input("Введите положительное число: "))
        if num > 0:
            print(f"Вы ввели: {num}")
            break
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Ошибка ввода! Введите целое число.")

# С ограничением попыток:
attempts = 3
while attempts > 0:
    try:
        num = int(input(f"Попытка {4 - attempts}/3. Введите число: "))
        print("Успех!")
        break
    except ValueError:
        attempts -= 1
        print(f"Неверный ввод. Осталось попыток: {attempts}")
else:
    print("Вы исчерпали все попытки.")

# Для дробных чисел:
while True:
    try:
        num = float(input("Введите число: "))
        print(f"Вы ввели: {num}")
        break
    except ValueError:
        print("Ошибка! Введите число (например: 3.14).")

# =======================================================================================================

# Вывод четных чисел:
# Запрашиваем у пользователя верхнюю границу
max_number = int(input("Введите число: "))

# Инициализируем счетчик
current_number = 2

print(f"Четные числа от 2 до {max_number}:")

# Цикл while для вывода четных чисел
while current_number <= max_number:
    print(current_number, end = " ")
    current_number += 2  # Увеличиваем на 2 для следующего четного числа

print()  # Переход на новую строку после вывода

# С проверкой ввода:
while True:
    try:
        max_number = int(input("Введите положительное число больше 1: "))
        if max_number > 1:
            break
        print("Число должно быть больше 1!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

current = 2
while current <= max_number:
    print(current, end = " ")
    current += 2

# В обратном порядке:
max_num = int(input("Введите число: "))
current = max_num if max_num % 2 == 0 else max_num - 1

while current >= 2:
    print(current, end = " ")
    current -= 2

# С сохранением в список:
n = int(input("Введите число: "))
evens = []
current = 2

while current <= n:
    evens.append(current)
    current += 2

print("Четные числа:", evens)

# С использованием range() (альтернативный способ):
n = int(input("Введите число: "))
print(*range(2, n + 1, 2))  # Вывод четных чисел через пробел

# =============================================================================================

# Проверка палиндрома:
# Вводим строку для проверки
input_string = input("Введите строку для проверки: ").lower()  # Приводим к нижнему регистру

# Удаляем пробелы (если нужно проверять фразы)
processed_string = input_string.replace(" ", "")

# Инициализируем индексы
left = 0
right = len(processed_string) - 1
is_palindrome = True

# Проверяем символы с двух сторон
while left < right:
    if processed_string[left] != processed_string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

# Выводим результат
if is_palindrome:
    print(f"Строка '{input_string}' является палиндромом")
else:
    print(f"Строка '{input_string}' не является палиндромом")

# Без учета регистра и пробелов:
s = "Madam I'm Adam".lower()
s = ''.join(c for c in s if c.isalnum())  # Удаляем все не-буквы и не-цифры

# Рекурсивная проверка:
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# С использованием срезов (альтернативный способ):
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Для чисел:
num = 12321
s = str(num)
is_palindrome = s == s[::-1]

# ==============================================================================================

# Вычисление среднего значения:
# Инициализация переменных
sum_numbers = 0
count = 0

print("Вводите числа (0 для завершения):")

# Основной цикл ввода
while True:
    try:
        number = float(input("> "))  # Преобразуем ввод в число
        
        if number == 0:
            break  # Выход из цикла при вводе 0
            
        sum_numbers += number  # Добавляем число к сумме
        count += 1            # Увеличиваем счётчик чисел
        
    except ValueError:  # Обработка нечислового ввода
        print("Пожалуйста, введите число!")

# Вычисление и вывод результата
if count > 0:
    average = sum_numbers / count
    print(f"Среднее значение {count} введённых чисел: {average:.2f}")
else:
    print("Вы не ввели ни одного числа!")

# Сохранение всех чисел:
numbers = []
while True:
    num = float(input("Число (0 - стоп): "))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    avg = sum(numbers) / len(numbers)
    print(f"Среднее: {avg:.2f}")

# Подсчёт положительных и отрицательных:
pos = neg = total = count = 0
while True:
    num = float(input("> "))
    if num == 0:
        break
    total += num
    count += 1
    if num > 0: pos += 1
    else: neg += 1

# С ограничением попыток:
max_attempts = 5
attempts = sum_num = count = 0
while attempts < max_attempts:
    num = float(input(f"Попытка {attempts + 1} / {max_attempts}: "))
    if num == 0:
        break
    sum_num += num
    count += 1
    attempts += 1

# Для целых чисел:
total = count = 0
while True:
    try:
        num = int(input("Целое число (0 - выход): "))
        if num == 0:
            break
        total += num
        count += 1
    except ValueError:
        print("Только целые числа!")

# ========================================================================================================

# Нахождение НОД (наибольшего общего делителя):
# Вводим два числа
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Сохраняем оригинальные числа для вывода
original_a, original_b = a, b

# Алгоритм Евклида с циклом while
while b != 0:
    # Если a < b, меняем их местами
    if a < b:
        a, b = b, a
    # Заменяем a на разность a и b
    a = a - b

# Выводим результат
print(f"НОД чисел {original_a} и {original_b} равен {a}")

# Оптимизированная версия (с использованием остатка от деления): ============================================
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

original_a, original_b = a, b

while b != 0:
    a, b = b, a % b  # Используем операцию взятия остатка

print(f"НОД чисел {original_a} и {original_b} равен {a}")

# Рекурсивная реализация:
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(54, 24))  # 6

# Для нескольких чисел:
from math import gcd
from functools import reduce

numbers = [36, 48, 60, 108]
result = reduce(gcd, numbers)
print(f"НОД {numbers} равен {result}")

# С проверкой ввода:
while True:
    try:
        a = int(input("Первое число (>0): "))
        b = int(input("Второе число (>0): "))
        if a > 0 and b > 0:
            break
        print("Числа должны быть положительными!")
    except ValueError:
        print("Пожалуйста, введите целые числа!")

# Визуализация шагов:
a = 54
b = 24
print(f"Начальные значения: a={a}, b={b}")

while b != 0:
    print(f"a={a}, b={b} → a % b = {a % b}")
    a, b = b, a % b

print(f"НОД: {a}")

# ============================================================================================================

# Обратный отсчет:
# Вводим начальное число
number = int(input("Введите число для обратного отсчёта: "))

# Обратный отсчёт с помощью цикла while
while number >= 0:
    print(number)
    number -= 1  # Уменьшаем число на 1

print("Обратный отсчёт завершён!")

# С задержкой между числами (1 секунда):
import time

number = int(input("Введите число: "))
while number >= 0:
    print(number)
    time.sleep(1)  # Пауза 1 секунда
    number -= 1

# Обратный отсчёт с сообщениями:
number = 3
while number > 0:
    print(f"{number}...")
    number -= 1
print("Старт!")

# Для отрицательных чисел (счёт вверх):
number = int(input("Введите отрицательное число: "))
while number <= 0:
    print(number)
    number += 1

# С обработкой ввода:
while True:
    try:
        n = int(input("Введите положительное число: "))
        if n >= 0:
            break
        print("Число должно быть положительным!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

while n >= 0:
    print(n)
    n -= 1