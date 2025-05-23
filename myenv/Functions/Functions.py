# =================================================================================================================
# Функции - это блоки кода, которые выполняют конкретную за­дачу или набор задач в программе. 
# Они помогают структуриро­вать код, делая его более организованным, понятным и много­кратно используемым. 
# Благодаря функциям ваш код становится проще в чтении, легче в подцержке и эффективнее в выполне­нии.
# =================================================================================================================

# В Python функции объявляются с использованием ключевого слова def, за которым следуют имя функции, 
# круглые скобки (внутри которых можно указать параметры, если они есть), и блок кода, который выполняется при вызове функции.

# Пример объявления функции без параметров
def greet():
    print("Привет, мир!")
# Вызов функции
greet()

# Пример объявления функции с параметрам
def greet(name):
    print(f"Пpивeт, {name}!")
# Вызов функции
greet("Анна")

# Возврат значений из функции
def add(a, b):
    return a + b
# Вызов функции
result = add(3, 5)
print(result) # Вывод: 8

# Аргументы по умолчанию
def greet(name = "мир"):
    print(f"Привет, {name} ! ")
# Вызов функции без аргумента
greet() # Вывод: Привет, мир!

# Вызов функции с аргументом
greet("Джон") # Вывод: Привет, Джон!

# Переменное число аргументов
def rnultiply(*args):
    result = 1
    for nurn in args:
        result *= nurn
    return result
# Вызов функции
print(rnultiply(2, 3, 4)) # Вывод: 24

# Расчет среднего значения списка чисел
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)
# Вызов функции для расчета среднего значения
avg = calculate_average([5, 10, 15, 20])
print(avg) # Вывод: 12.5

# Проверка числа на четность
def is_even(number):
    return number % 2 == 0
# Проверка числа на четность
print(is_even(7)) # Вывод: False
print(is_even(10)) # Вывод: True

# Приветствие пользователя с использованием Фхнкции
def greet_user(name):
    print(f"Пpивeт, {name}!")
# Вызов функции для приветствия пользователя
greet_user("Бoб") # Вывод: Привет, Боб!

# ============================================================================================================================

def calculate_factorial(n):
    """
    Вычисляет факториал целого числа n.
    
    Параметры:
        n (int): Число, для которого вычисляется факториал
        
    Возвращает:
        int: Факториал числа n
        
    Исключения:
        ValueError: Если n отрицательное
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(calculate_factorial(5))  # Выведет: 120
print(calculate_factorial(0))  # Выведет: 1

# Рекурсивная реализация:
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    return 1 if n <= 1 else n * calculate_factorial(n - 1)

# С использованием math.factorial (встроенная функция):
from math import factorial

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    return factorial(n)

# С проверкой типа:
def calculate_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Факториал вычисляется только для целых чисел")
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# ======================================================================================================================

def reverse_string(input_str):
    """
    Переворачивает строку задом наперёд.
    
    Параметры:
        input_str (str): Исходная строка
        
    Возвращает:
        str: Перевернутая строка
    """
    reversed_str = ""
    index = len(input_str) - 1  # Начинаем с последнего символа
    
    while index >= 0:
        reversed_str += input_str[index]  # Добавляем символы в обратном порядке
        index -= 1  # Двигаемся к началу строки
    
    return reversed_str

print(reverse_string("Hello"))  # Выведет: "olleH"
print(reverse_string("12345"))  # Выведет: "54321"
print(reverse_string("Привет")) # Выведет: "тевирП"

# С использованием срезов (оптимальный способ в Python):
def reverse_string(input_str):
    return input_str[::-1]

# Рекурсивный вариант:
def reverse_string(input_str):
    return reverse_string(input_str[1:]) + input_str[0] if input_str else ""

# С использованием списка:
def reverse_string(input_str):
    chars = list(input_str)
    left, right = 0, len(chars)-1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

# С обработкой Unicode (для сложных символов):
import unicodedata

def reverse_string(input_str):
    normalized = unicodedata.normalize('NFC', input_str)
    return normalized[::-1]

# ===================================================================================================================

def count_vowels(input_str):
    """
    Подсчитывает количество гласных букв в строке.
    
    Параметры:
        input_str (str): Строка для анализа
        
    Возвращает:
        int: Количество гласных букв в строке
    """
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
    count = 0
    
    for char in input_str:
        if char in vowels:
            count += 1
            
    return count

print(count_vowels("Hello World"))     # Выведет: 3
print(count_vowels("Привет, мир!"))    # Выведет: 3
print(count_vowels("Пылесос"))         # Выведет: 3

# С использованием множеств (более быстрая проверка):
def count_vowels(input_str):
    vowels = {'a', 'e', 'i', 'o', 'u', 'а', 'е', 'ё', 'и', 'о', 
              'у', 'ы', 'э', 'ю', 'я', 'A', 'E', 'I', 'O', 'U',
              'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'}
    return sum(1 for char in input_str if char in vowels)

# Только для английских гласных:
def count_vowels(input_str):
    return sum(1 for char in input_str.lower() if char in 'aeiou')

# С использованием регулярных выражений:
import re

def count_vowels(input_str):
    return len(re.findall('[aeiouаеёиоуыэюя]', input_str, re.IGNORECASE))

# Словарь частотности гласных:
from collections import defaultdict

def count_vowels(input_str):
    vowels = "aeiouаеёиоуыэюя"
    freq = defaultdict(int)
    for char in input_str.lower():
        if char in vowels:
            freq[char] += 1
    return sum(freq.values())

# ==========================================================================================================

def find_max(numbers):
    """
    Находит максимальное число в списке.
    
    Параметры:
        numbers (list): Список чисел
        
    Возвращает:
        int/float: Максимальное число в списке
        
    Исключения:
        ValueError: Если список пуст
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")
    
    max_num = numbers[0]  # Предполагаем, что первый элемент - максимальный
    
    for num in numbers[1:]:  # Проверяем остальные элементы
        if num > max_num:
            max_num = num
            
    return max_num

print(find_max([3, 1, 4, 1, 5, 9, 2]))  # Выведет: 9
print(find_max([-5, -2, -10]))          # Выведет: -2
print(find_max([3.14, 2.71, 1.61]))     # Выведет: 3.14

# С использованием встроенной функции max():
def find_max(numbers):
    return max(numbers)

# Рекурсивный вариант:
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    sub_max = find_max(numbers[1:])
    return numbers[0] if numbers[0] > sub_max else sub_max

# С обработкой разных типов данных:
def find_max(items):
    if not items:
        return None
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

# С использованием reduce():
from functools import reduce

def find_max(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

# =========================================================================================================

import math

def calculate_area(radius):
    """
    Вычисляет площадь круга по заданному радиусу.
    
    Параметры:
        radius (float): Радиус круга (должен быть положительным)
        
    Возвращает:
        float: Площадь круга
        
    Исключения:
        ValueError: Если радиус отрицательный
    """
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    
    return math.pi * (radius ** 2)

print(calculate_area(5))      # Выведет: 78.53981633974483
print(calculate_area(2.5))    # Выведет: 19.634954084936208

# Без импорта math (с приближенным значением π):
def calculate_area(radius):
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 3.141592653589793 * (radius ** 2)

# С округлением результата:
import math

def calculate_area(radius, decimals = 2):
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return round(math.pi * (radius ** 2), decimals)

# Для вычисления площади кольца:
import math

def calculate_ring_area(inner_radius, outer_radius):
    if inner_radius < 0 or outer_radius < 0:
        raise ValueError("Радиусы не могут быть отрицательными")
    if inner_radius >= outer_radius:
        raise ValueError("Внутренний радиус должен быть меньше внешнего")
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)

# С проверкой типа ввода:
import math

def calculate_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * (radius ** 2)