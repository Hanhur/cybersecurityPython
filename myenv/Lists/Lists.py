# ===============================================================
# Списки (list) в Python - это упорядоченные коллекции объектов,
# которые могут включать элементы самых разных типов данных:
# целые числа, строки, другие списки и даже неожиданные вещи
# вроде вашей неудачной попытки научиться танцевать.
# ===============================================================

# Индексация
my_list = ['apple', 'banana', 'orange']
print(my_list[0]) # Выводит 'apple'
print(my_list[1]) # Выводит 'banana'

# Метод append() используется для добавления элемента в конец списка.
# Добавление элементов
my_list = ['apple', 'banana']
my_list.append('orange')
print(my_list) # Выводит ['apple', 'banana', 'orange']

# Метод рор() удаляет элемент из списка по указанному индексу и возвращает его.
# Удаление элементов
my_list = ['apple', 'banana', 'orange']
fruit = my_list.pop(1)
print(fruit) # Выводит 'banana'
print(my_list) # Выводит ['apple', 'orange']

# Метод remove() удаляет первый элемент в списке, который имеетуказанное значение.
my_list = ['apple', 'banana', 'orange']
my_list.remove('banana')
print(my_list) # Выводит ['apple', 'orange']

# С помощью срезов можно извлекать подсписки из списка.
# Срезы
my_list = ['apple', 'banana', 'oiange', 'grape', 'pear']
sub_list = my_list[1:4]
print(sub_list) # Выводит ['banana', 'orange', 'grape']

# Оператор + используется для объединения двух списков в один.
# Конкатенация
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list) # Выводит [1, 2, 3, 4, 5, 6]

# Хранение и обработка данных
scores = [85, 90, 78, 92, 88]
average_score = sum(scores) / len(scores)
print(average_score) # Выводит 86.6

# Управление очередями
queue = []
queue. append('first')
queue.append('second')
queue.append('third')
print(queue.pop(0)) # Выводит 'first'
print(queue.pop(0)) # Выводит 'second'
print(queue.pop(0)) # Выводит 'third'

# Обработка строк
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words) # Выводит ['The', 'quick', 'brown', 'fox','jumps', 'over', 'the', 'lazy', 'dog']

# ==================================================================================================================

# Сумма элементов списка:
# Получаем ввод от пользователя
numbers_input = input("Введите список чисел, разделенных пробелами: ")

# Разделяем введенную строку на отдельные числа
numbers_list = numbers_input.split()

# Преобразуем строки в числа
try:
    numbers = [float(num) for num in numbers_list]
except ValueError:
    print("Ошибка: пожалуйста, вводите только числа, разделенные пробелами.")
    exit()

# Считаем сумму
total_sum = sum(numbers)

# Выводим результат
print("Сумма всех чисел в списке:", total_sum)

# ============================================================================================

# Произведение элементов списка:
# Получаем ввод от пользователя
numbers_input = input("Введите список чисел, разделенных пробелами: ")

# Разделяем строку на отдельные числа
numbers_list = numbers_input.split()

# Преобразуем строки в числа
try:
    numbers = [float(num) for num in numbers_list]
except ValueError:
    print("Ошибка: пожалуйста, вводите только числа, разделенные пробелами.")
    exit()

# Вычисляем произведение (начинаем с 1, так как умножение на 0 даст 0)
product = 1
for num in numbers:
    product *= num

# Выводим результат
print("Произведение всех чисел в списке:", product)

numbers = []
for num in numbers_list:
    try:
        numbers.append(float(num))
    except ValueError:
        pass  # Пропускаем некорректные значения

# ==================================================================================================

# Минимум и максимум:
# Получаем ввод от пользователя
numbers_input = input("Введите список чисел, разделенных пробелами: ")

# Разделяем строку на отдельные элементы
numbers_list = numbers_input.split()

try:
    # Преобразуем строки в числа (float для поддержки дробных чисел)
    numbers = [float(num) for num in numbers_list]
    
    # Проверяем, что список не пустой
    if not numbers:
        print("Ошибка: список чисел пуст.")
    else:
        # Находим минимум и максимум
        min_num = min(numbers)
        max_num = max(numbers)
        
        # Выводим результат
        print(f"Минимальное число: {min_num}")
        print(f"Максимальное число: {max_num}")
        
except ValueError:
    print("Ошибка: в списке должны быть только числа, разделенные пробелами.")

if not numbers_input.strip():
    print("Ошибка: вы ничего не ввели.")

numbers = []
for num in numbers_list:
    try:
        numbers.append(float(num))
    except ValueError:
        pass  # Пропускаем некорректные значения

# ===============================================================================================================

# Среднее значение:
# Получаем ввод от пользователя
user_input = input("Введите числа через пробел: ")

try:
    # Преобразуем строку в список чисел
    numbers = [float(num) for num in user_input.split()]
    
    # Проверяем, что список не пустой
    if not numbers:
        print("Ошибка: вы не ввели ни одного числа!")
    else:
        # Вычисляем среднее значение
        average = sum(numbers) / len(numbers)
        
        # Выводим результат с округлением до 2 знаков после запятой
        print(f"Среднее значение: {average:.2f}")
        
except ValueError:
    print("Ошибка: убедитесь, что вводите только числа, разделённые пробелами!")

# ==================================================================================================================

# Удаление дубликатов:
# Получаем ввод от пользователя
user_input = input("Введите числа через пробел: ")

try:
    # Преобразуем строку в список чисел (с поддержкой дробных чисел)
    numbers = [float(num) for num in user_input.split()]
    
    # Удаляем дубликаты (сохраняем порядок)
    unique_numbers = []
    seen = set()
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    
    # Выводим результат
    print("Уникальные числа:", ' '.join(map(str, unique_numbers)))
    
except ValueError:
    print("Ошибка: убедитесь, что вводите только числа, разделённые пробелами!")

# =================================================================================================================

# Поиск элемента:
# Получаем список чисел от пользователя
numbers_input = input("Введите числа через пробел: ")
search_element = input("Введите элемент для поиска: ")

try:
    # Преобразуем ввод в список чисел (с поддержкой дробных чисел)
    numbers = [float(num) for num in numbers_input.split()]
    
    # Преобразуем искомый элемент в число
    search_num = float(search_element)
    
    # Проверяем наличие элемента в списке
    is_found = search_num in numbers
    
    # Выводим результат
    print(is_found)
    
except ValueError:
    print("Ошибка: убедитесь, что вводите только числа!")

# ===================================================================================================================

# Переворот списка:
# Получаем ввод от пользователя
user_input = input("Введите элементы списка через пробел: ")

# Разбиваем строку на элементы
elements = user_input.split()

# Переворачиваем список
reversed_list = elements[::-1]

# Выводим результат
print("Перевёрнутый список:", ' '.join(reversed_list))

# Если нужно работать именно с числами, можно добавить преобразование типов:
try:
    numbers = [float(num) for num in user_input.split()]
    reversed_numbers = numbers[::-1]
    print("Перевёрнутый список чисел:", ' '.join(map(str, reversed_numbers)))
except ValueError:
    print("Ошибка: вводите только числа, разделённые пробелами!")

# ===============================================================================================================

# Сдвиг элементов:
# Получаем ввод списка от пользователя
user_list = input("Введите элементы списка через пробел: ").split()
n = input("Введите количество позиций для сдвига: ")

try:
    # Преобразуем n в целое число
    n = int(n)
    
    # Если список пустой, выводим его без изменений
    if not user_list:
        print("Результат:", user_list)
    else:
        # Вычисляем действительный сдвиг (учитываем длину списка)
        shift = n % len(user_list)
        
        # Сдвигаем элементы вправо
        shifted_list = user_list[-shift:] + user_list[:-shift]
        
        # Выводим результат
        print("Результат:", ' '.join(shifted_list))
        
except ValueError:
    print("Ошибка: количество позиций должно быть целым числом")
except ZeroDivisionError:
    print("Ошибка: список не может быть пустым для сдвига")

# Для работы только с числами можно добавить преобразование:
try:
    numbers = [float(x) for x in user_list]
    # остальной код аналогичен
except ValueError:
    print("Ошибка: все элементы списка должны быть числами")

# ===================================================================================================

# Объединение списков:
# Получаем первый список от пользователя
list1 = input("Введите элементы первого списка через пробел: ").split()

# Получаем второй список от пользователя
list2 = input("Введите элементы второго списка через пробел: ").split()

# Объединяем списки
combined_list = list1 + list2

# Выводим результат
print("Объединённый список:", ' '.join(combined_list))

# Объединение с преобразованием в числа:
try:
    # Преобразуем элементы в числа
    nums1 = [float(x) for x in list1]
    nums2 = [float(x) for x in list2]
    combined = nums1 + nums2
    print("Объединённый числовой список:", combined)
except ValueError:
    print("Ошибка: все элементы должны быть числами")

# Объединение без дубликатов:
combined_unique = list(set(list1 + list2))
print("Уникальные элементы:", ' '.join(combined_unique))

# Объединение с сохранением порядка:
from collections import OrderedDict
combined_ordered = list(OrderedDict.fromkeys(list1 + list2))
print("Объединение с сохранением порядка:", ' '.join(combined_ordered))

# ===========================================================================================

# Сортировка списка:
def sort_numbers():
    # Получаем список чисел от пользователя
    numbers_input = input("Введите числа через пробел: ")
    
    try:
        # Преобразуем в список чисел
        numbers = [float(num) for num in numbers_input.split()]
        
        # Запрашиваем тип сортировки
        sort_order = input("Выберите тип сортировки (1 - по возрастанию, 2 - по убыванию): ")
        
        # Выполняем сортировку
        if sort_order == '1':
            sorted_numbers = sorted(numbers)
            print("Отсортированный список (по возрастанию):", sorted_numbers)
        elif sort_order == '2':
            sorted_numbers = sorted(numbers, reverse=True)
            print("Отсортированный список (по убыванию):", sorted_numbers)
        else:
            print("Ошибка: выберите 1 или 2 для типа сортировки")
    
    except ValueError:
        print("Ошибка: вводите только числа, разделенные пробелами")

# Запускаем функцию
sort_numbers()

# ===========================================================================================================

# Четные и нечетные числа:
# Получаем список чисел от пользователя
numbers_input = input("Введите числа через пробел: ")

try:
    # Преобразуем в список чисел (с поддержкой дробных чисел)
    numbers = [float(num) for num in numbers_input.split()]
    
    # Разделяем на чётные и нечётные
    even_numbers = []  # Чётные
    odd_numbers = []   # Нечётные
    
    for num in numbers:
        if num % 2 == 0:  # Проверка на чётность
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    # Выводим результаты
    print("Чётные числа:", even_numbers)
    print("Нечётные числа:", odd_numbers)

except ValueError:
    print("Ошибка: вводите только числа, разделённые пробелами!")

# Для работы только с целыми числами измените преобразование типов:
numbers = [int(num) for num in numbers_input.split()]

# ====================================================================================================

# Слияние двух отсортированных списков:
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    
    # Обходим оба списка, сравнивая элементы
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Добавляем оставшиеся элементы из обоих списков
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

# Получаем данные от пользователя
input1 = input("Введите первый отсортированный список чисел через пробел: ")
input2 = input("Введите второй отсортированный список чисел через пробел: ")

try:
    # Преобразуем в списки чисел
    list1 = [float(x) for x in input1.split()]
    list2 = [float(x) for x in input2.split()]
    
    # Проверяем, что списки действительно отсортированы
    if list1 != sorted(list1) or list2 != sorted(list2):
        print("Ошибка: один из списков не отсортирован!")
    else:
        # Объединяем списки
        result = merge_sorted_lists(list1, list2)
        print("Объединённый отсортированный список:", result)

except ValueError:
    print("Ошибка: вводите только числа, разделённые пробелами!")

# =================================================================================================

# Подсчет вхождений:
# Получаем список от пользователя
user_list = input("Введите элементы списка через пробел: ").split()
element = input("Введите элемент для подсчёта: ")

# Подсчитываем количество вхождений
count = user_list.count(element)

# Выводим результат
print(f"Элемент '{element}' встречается {count} раз(а) в списке.")

# Чувствительность к регистру (для строк):
# Для регистронезависимого поиска
count = sum(1 for item in user_list if item.lower() == element.lower())

# Подсчёт чисел с преобразованием типов:
try:
    numbers = [float(x) for x in user_list]
    search_num = float(element)
    count = numbers.count(search_num)
except ValueError:
    print("Ошибка: вводите только числа!")

# Подробный вывод:
if count == 0:
    print(f"Элемент '{element}' не найден в списке.")
else:
    print(f"Элемент '{element}' встречается {count} раз(а):")
    for i, item in enumerate(user_list, 1):
        if item == element:
            print(f"  - Позиция {i}: {item}")

# =====================================================================================================

# Удаление элемента:
# Получаем список от пользователя
user_list = input("Введите элементы списка через пробел: ").split()
element = input("Введите элемент для удаления: ")

# Проверяем наличие элемента в списке
if element in user_list:
    # Удаляем первое вхождение элемента
    user_list.remove(element)
    print("Обновленный список:", ' '.join(user_list))
else:
    print(f"Элемент '{element}' не найден в списке.")

# Удаление всех вхождений элемента:
user_list = [x for x in user_list if x != element]

# Работа с числами (преобразование типов):
try:
    numbers = [float(x) for x in user_list]
    del_element = float(element)
    if del_element in numbers:
        numbers.remove(del_element)
        print("Обновленный список чисел:", numbers)
    else:
        print("Элемент не найден")
except ValueError:
    print("Ошибка: вводите только числа!")

# Удаление элемента по индексу:
try:
    index = int(input("Введите индекс для удаления: "))
    if 0 <= index < len(user_list):
        del user_list[index]
        print("Обновленный список:", ' '.join(user_list))
    else:
        print("Неверный индекс")
except ValueError:
    print("Ошибка: введите целое число для индекса")

# =====================================================================================================

# Четные индексы:
# Получаем список от пользователя
user_list = input("Введите элементы списка через пробел: ").split()

# Выбираем элементы с чётными индексами
even_index_elements = user_list[::2]

# Выводим результат
print("Элементы на чётных индексах:", ' '.join(even_index_elements))

# Вывод с указанием индексов:
print("Элементы на чётных индексах:")
for index, element in enumerate(user_list):
    if index % 2 == 0:
        print(f"Индекс {index}: {element}")

# Работа с числами:
try:
    numbers = [float(x) for x in user_list]
    even_index_numbers = numbers[::2]
    print("Числа на чётных индексах:", even_index_numbers)
except ValueError:
    print("Ошибка: вводите только числа!")

# Альтернативный вариант с циклом:
result = []
for i in range(0, len(user_list), 2):
    result.append(user_list[i])
print("Результат:", ' '.join(result))