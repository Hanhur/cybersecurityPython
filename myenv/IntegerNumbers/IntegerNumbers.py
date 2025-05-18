# ====================================================================
# Целочисленные числа (int) в Python представляют собой числа без дробной части. 
# Они могут быть положительными, отрицательными или нулевыми. 
# В Python целочисленные числа не имеют ограничения на размер, 
# и вы можете выполнять с ними различные математические операции.
# ===================================================================

# Простые арифметические операции:
# Получаем два целых числа от пользователя
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Выполняем арифметические операции
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

# Выводим результаты
print(f"Сложение: {num1} + {num2} = {sum_result}")
print(f"Вычитание: {num1} - {num2} = {difference}")
print(f"Умножение: {num1} * {num2} = {product}")
print(f"Деление: {num1} / {num2} = {division}")

# =============================================================================
# Проверка четности:
# Получаем целое число от пользователя
number = int(input("Введите целое число: "))

# Проверяем чётность
if number % 2 == 0:
    print(f"Число {number} является чётным.")
else:
    print(f"Число {number} является нечётным.")

try:
    number = int(input("Введите целое число: "))
    if number % 2 == 0:
        print(f"Число {number} является чётным.")
    else:
        print(f"Число {number} является нечётным.")
except ValueError:
    print("Ошибка: Введите целое число!")

# ====================================================================================
# Возведение в степень:
# Ввод данных
base = int(input("Введите основание (целое число): "))
exponent = int(input("Введите показатель степени (целое число): "))

# Вычисление степени
result = base ** exponent

# Вывод результата
print(f"{base} в степени {exponent} = {result}")

try:
    base = int(input("Введите основание (целое число): "))
    exponent = int(input("Введите показатель степени (целое число): "))
    result = base ** exponent
    print(f"{base} в степени {exponent} = {result}")
except ValueError:
    print("Ошибка: Введите целые числа!")

result = pow(base, exponent)

# ============================================================================================
# Наибольший общий делитель (НОД):
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ввод данных
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Вычисление НОД
result = gcd(num1, num2)

# Вывод результата
print(f"НОД чисел {num1} и {num2} = {result}")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(f"НОД чисел {num1} и {num2} = {gcd(num1, num2)}")
except ValueError:
    print("Ошибка: Введите целые числа!")

def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)

import math
print(math.gcd(num1, num2))  # Работает так же
# ============================================================================
# Факториал числа:
def factorial(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ввод числа от пользователя
try:
    num = int(input("Введите целое число для вычисления факториала: "))
    print(f"{num}! = {factorial(num)}")
except ValueError:
    print("Ошибка: пожалуйста, введите целое число.")

# ==================================================================================
# Решение квадратного уравнения: квадратного уравнения вида ахл2 + Ьх + с = О
import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "Уравнение не является квадратным" if c != 0 else "Бесконечное количество решений"
        return f"Уравнение линейное, корень: x = {-c / b:.2f}"
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Два различных корня: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"Один корень: x = {x:.2f}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (f"Комплексные корни: x1 = {real_part:.2f} + {imaginary_part:.2f}i, "
                f"x2 = {real_part:.2f} - {imaginary_part:.2f}i")

# Ввод коэффициентов
try:
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    
    print(solve_quadratic(a, b, c))
except ValueError:
    print("Ошибка: введите числовые значения коэффициентов")

# ===================================================================================================
# Сумма цифр числа:
def sum_of_digits(number):
    # Преобразуем число в строку для перебора цифр
    digits = str(abs(number))  # Используем abs для обработки отрицательных чисел
    total = 0
    for digit in digits:
        total += int(digit)
    return total

# Ввод числа от пользователя
try:
    num = int(input("Введите целое число: "))
    print(f"Сумма цифр числа {num} равна {sum_of_digits(num)}")
except ValueError:
    print("Ошибка: пожалуйста, введите целое число.")

# ===============================================================================================
# Проверка на простое число:
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

try:
    num = int(input("Введите целое число для проверки на простоту: "))
    if is_prime(num):
        print(f"{num} - простое число")
    else:
        print(f"{num} - не является простым числом")
except ValueError:
    print("Ошибка: пожалуйста, введите целое число")

# ====================================================================================================
# Перевод чисел между системами счисления:
def convert_number_systems():
    try:
        # Ввод числа от пользователя
        number = int(input("Введите целое число в десятичной системе: "))
        
        # Перевод в различные системы счисления
        binary = bin(number)
        octal = oct(number)
        hexadecimal = hex(number)
        
        # Вывод результатов
        print("\nРезультаты перевода:")
        print(f"Двоичная система (bin): {binary}")
        print(f"Восьмеричная система (oct): {octal}")
        print(f"Шестнадцатеричная система (hex): {hexadecimal}")
        
        # Альтернативный вывод без префиксов
        print("\nБез префиксов:")
        print(f"Двоичная: {binary[2:]}")
        print(f"Восьмеричная: {octal[2:]}")
        print(f"Шестнадцатеричная: {hexadecimal[2:].upper()}")  # Большие буквы для hex
        
    except ValueError:
        print("Ошибка: введите целое число!")

# Запуск программы
convert_number_systems()
# ==============================================================================================
# Обратный порядок цифр числа:
def reverse_number():
    try:
        # Ввод числа от пользователя
        number = int(input("Введите целое число: "))
        
        # Обработка отрицательных чисел
        sign = -1 if number < 0 else 1
        abs_number = abs(number)
        
        # Преобразование числа в строку и разворот
        reversed_str = str(abs_number)[::-1]
        
        # Преобразование обратно в число с сохранением знака
        reversed_number = sign * int(reversed_str)
        
        print(f"Число в обратном порядке: {reversed_number}")
        
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число")

# Запуск программы
reverse_number()

def reverse_math(number):
    reversed_num = 0
    sign = -1 if number < 0 else 1
    number = abs(number)
    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number = number // 10
    return sign * reversed_num

def reverse_recursive(number, reversed_num = 0):
    if number == 0:
        return reversed_num
    return reverse_recursive(number // 10, reversed_num * 10 + number % 10)

# ===========================================================================================
# Проверка палиндрома:
def is_palindrome(number):
    # Преобразуем число в строку для удобства сравнения
    num_str = str(abs(number))  # Работаем с абсолютным значением для отрицательных чисел
    return num_str == num_str[::-1]  # Сравниваем строку с её обратной версией

# Ввод числа от пользователя
try:
    num = int(input("Введите целое число для проверки на палиндром: "))
    
    if is_palindrome(num):
        print(f"Число {num} является палиндромом")
    else:
        print(f"Число {num} не является палиндромом")
        
except ValueError:
    print("Ошибка: пожалуйста, введите целое число")

def is_palindrome_math(number):
    original = abs(number)
    reversed_num = 0
    temp = original
    
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp = temp // 10
        
    return original == reversed_num

def is_palindrome_recursive(num_str):
    if len(num_str) <= 1:
        return True
    if num_str[0] != num_str[-1]:
        return False
    return is_palindrome_recursive(num_str[1:-1])

# ============================================================================
# Нахождение всех делителей числа:
def find_divisors(number):
    if number == 0:
        return "Все ненулевые числа являются делителями нуля"
    if number < 0:
        number = abs(number)
    
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    
    divisors.sort()
    return divisors

try:
    num = int(input("Введите целое число: "))
    result = find_divisors(num)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"Делители числа {num}: {result}")

except ValueError:
    print("Ошибка: введите целое число")