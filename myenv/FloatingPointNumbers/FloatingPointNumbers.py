# ========================================================================
# Числа с плавающей точкой (float) в Python представляют со­бой числа с десятичной частью. 
# Они могут быть положитель­ными или отрицательными и могут содержать дробную часть,
# разделенную точкой. Такие числа позволяют проводить более точные вычисления, что важно в различных приложениях, 
# вклю­чая научные расчеты и анализ данных.
# ========================================================================

def calculate_operations():
    try:
        # Ввод двух чисел от пользователя
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        # Выполнение операций
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "не определено (деление на ноль)"
        
        # Вывод результатов
        print("\nРезультаты операций:")
        print(f"{num1} + {num2} = {addition}")
        print(f"{num1} - {num2} = {subtraction}")
        print(f"{num1} * {num2} = {multiplication}")
        print(f"{num1} / {num2} = {division}")
        
    except ValueError:
        print("Ошибка: введите числа в правильном формате (например: 3.14 или 5.0)")

# Запуск программы
calculate_operations()

# ========================================================================================================
import math

def calculate_circle_area():
    try:
        # Запрос ввода радиуса у пользователя
        radius = float(input("Введите радиус круга (в см): "))
        
        # Проверка на положительное значение
        if radius <= 0:
            print("Ошибка: радиус должен быть положительным числом!")
            return
        
        # Вычисление площади по формуле S = πr²
        area = math.pi * (radius ** 2)
        
        # Вывод результата с округлением до 2 знаков
        print(f"\nРезультат:")
        print(f"Радиус круга: {radius} см")
        print(f"Площадь круга: {area:.2f} см²")
        
    except ValueError:
        print("Ошибка: введите числовое значение радиуса!")

# Запуск программы
print("Программа для вычисления площади круга")
calculate_circle_area()
# =============================================================================================================
def round_number():
    try:
        # Ввод числа от пользователя
        number = float(input("Введите число для округления: "))
        
        # Округление до 2 знаков после запятой
        rounded = round(number, 2)
        
        # Вывод результата
        print(f"Округлённое значение: {rounded:.2f}")
        
    except ValueError:
        print("Ошибка: введите число в правильном формате (например: 3.1415 или 5.0)")

# Запуск программы
round_number()
# ============================================================================================================
def celsius_to_fahrenheit():
    try:
        # Ввод температуры в градусах Цельсия
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        
        # Конвертация по формуле: F = C × 9/5 + 32
        fahrenheit = celsius * 9 / 5 + 32
        
        # Вывод результата с округлением до 1 знака после запятой
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        
    except ValueError:
        print("Ошибка: введите числовое значение температуры")

# Запуск программы
print("Конвертер температур: Цельсий → Фаренгейт")
celsius_to_fahrenheit()
# ===================================================================================================================
def convert_usd_to_eur():
    # Фиксированный курс обмена (1 USD = 0.85 EUR)
    EXCHANGE_RATE = 0.85
    
    try:
        # Ввод суммы в долларах
        usd_amount = float(input("Введите сумму в долларах (USD): $"))
        
        # Проверка на отрицательное значение
        if usd_amount < 0:
            print("Ошибка: сумма не может быть отрицательной")
            return
        
        # Конвертация в евро
        eur_amount = usd_amount * EXCHANGE_RATE
        
        # Вывод результата с округлением до 2 знаков
        print(f"\nРезультат конвертации:")
        print(f"${usd_amount:.2f} = €{eur_amount:.2f}")
        print(f"(по курсу 1 USD = {EXCHANGE_RATE} EUR)")
        
    except ValueError:
        print("Ошибка: введите числовое значение суммы")

# Запуск программы
print("Конвертер валют: Доллары (USD) → Евро (EUR)")
convert_usd_to_eur()
# =================================================================================================================
import math

def calculate_square_root():
    try:
        # Ввод числа от пользователя
        number = float(input("Введите число для вычисления квадратного корня: "))
        
        # Проверка на отрицательное значение
        if number < 0:
            print("Ошибка: нельзя извлечь квадратный корень из отрицательного числа!")
            print("Попробуйте ввести положительное число или 0.")
            return
        
        # Вычисление квадратного корня
        result = math.sqrt(number)
        
        # Вывод результата с округлением до 4 знаков
        print(f"√{number} = {result:.4f}")
        
    except ValueError:
        print("Ошибка: введите числовое значение!")

# Запуск программы
print("Калькулятор квадратного корня")
calculate_square_root()

def calculate_square_root():
    try:
        number = float(input("Введите число: "))
        if number < 0:
            raise ValueError("Отрицательное число")
        result = number ** 0.5
        print(f"√{number} ≈ {result:.4f}")
    except ValueError:
        print("Ошибка: введите неотрицательное число!")
# =====================================================================================
def calculate_average():
    numbers = []  # Список для хранения введённых чисел
    
    print("Введите 5 чисел для расчёта среднего арифметического:")
    
    try:
        # Ввод пяти чисел
        for i in range(5):
            num = float(input(f"Число {i + 1}: "))
            numbers.append(num)
        
        # Вычисление среднего арифметического
        average = sum(numbers) / len(numbers)
        
        # Вывод результата с округлением до 2 знаков
        print(f"\nСреднее арифметическое: {average:.2f}")
        
    except ValueError:
        print("Ошибка: введите числовые значения!")

# Запуск программы
calculate_average()

# Альтернативный вариант с однострочником
try:
    nums = [float(input(f"Число {i + 1}: ")) for i in range(5)]
    print(f"Среднее: {sum(nums) / 5:.2f}")
except ValueError:
    print("Некорректный ввод!")

# ===============================================================================================
def compare_numbers():
    try:
        # Ввод двух чисел от пользователя
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        # Сравнение с точностью до 3 знаков после запятой
        if abs(num1 - num2) < 0.001:
            print(f"Числа {num1} и {num2} равны с точностью до 3 знаков после запятой")
        else:
            print(f"Числа {num1} и {num2} НЕ равны с точностью до 3 знаков после запятой")
            
    except ValueError:
        print("Ошибка: введите числовые значения!")

# Запуск программы
print("Сравнение чисел с точностью до 0.001")
compare_numbers()

# Вариант с округлением до 3 знаков
# if round(num1, 3) == round(num2, 3):
#     print("Числа равны")
# else:
#     print("Числа не равны")

# =====================================================================================================
def calculate_sum():
    try:
        # Ввод количества чисел
        count = int(input("Введите количество чисел для суммирования: "))
        
        if count <= 0:
            print("Ошибка: количество чисел должно быть положительным!")
            return
        
        # Ввод чисел и вычисление суммы
        total = 0.0
        for i in range(1, count + 1):
            while True:
                try:
                    num = float(input(f"Введите число {i}: "))
                    total += num
                    break
                except ValueError:
                    print("Ошибка: введите корректное число!")
        
        # Вывод результата
        print(f"\nСумма {count} чисел: {total:.2f}")
        
    except ValueError:
        print("Ошибка: введите целое число для количества!")

# Запуск программы
print("Вычисление суммы ряда чисел")
calculate_sum()

# Альтернативная реализация (с обработкой всех ошибок ввода):
def calculate_sum_safe():
    while True:
        try:
            count = int(input("Сколько чисел будем суммировать? "))
            if count <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка: введите целое положительное число!")

    total = 0.0
    for i in range(count):
        while True:
            try:
                num = float(input(f"Число {i + 1}: "))
                total += num
                break
            except ValueError:
                print("Ошибка: введите число!")

    print(f"Итоговая сумма: {total:.2f}")

# ==================================================================================================
import math

def calculate_cylinder_volume():
    print("Программа для вычисления объёма цилиндра")
    print("Формула: V = π × r² × h")
    print("где π ≈ 3.14159, r - радиус основания, h - высота цилиндра\n")
    
    try:
        # Ввод радиуса с проверкой
        radius = float(input("Введите радиус основания цилиндра (в см): "))
        if radius <= 0:
            print("Ошибка: радиус должен быть положительным числом!")
            return
        
        # Ввод высоты с проверкой
        height = float(input("Введите высоту цилиндра (в см): "))
        if height <= 0:
            print("Ошибка: высота должна быть положительным числом!")
            return
        
        # Вычисление объёма по формуле V = πr²h
        volume = math.pi * (radius ** 2) * height
        
        # Вывод результата с округлением до 2 знаков
        print(f"\nРезультат вычислений:")
        print(f"Радиус основания: {radius} см")
        print(f"Высота цилиндра: {height} см")
        print(f"Объём цилиндра: {volume:.2f} см³")
        
    except ValueError:
        print("Ошибка: введите числовые значения!")

# Запуск программы
calculate_cylinder_volume()