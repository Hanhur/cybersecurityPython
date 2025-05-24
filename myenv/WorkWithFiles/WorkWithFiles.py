# ===================================================================================================================
# Для открытия файла в Python используется функция open(). Она принимает два аргумента: путь к файлу и режим доступа. 
# Режим доступа может быть "r" (чтение), "w" (запись), "а" (добавление), 
# "rb" (чтение в бинарном режиме) или "wb" (запись в бинарном режиме).
# =====================================================================================================================

# Открытие файла для чтения
file = open("example.txt", "r")

# Чтение из файла осуществляется с помощью метода read(), который считывает содержимое файла целиком, 
# либо методов readline() и readlines(), которые считывают файл построчно или возвращают список строк соответственно.

# Чтение содержимого файла
content = file.read()
print(content)

# Чтение файла построчно
line = file.readline()
print(line)

# Чтение всех строк файла в список
lines = file.readlines()
print(lines)

# Запись в файл выполняется с использованием метода write(). Для этого файл должен быть открыт в режиме записи ("w" или "а"). 
# Метод write() при­нимает строку, которую нужно записать в файл.

# Запись в файл
file.write("Hello, World!\n")

# После окончания работы с файлом его следует закрыть с помощью мето­да close(), чтобы освободить ресурсы системы.

# Закрытие файла
file.close()

# Открываем файл для чтения
with open("example.txt", "r") as file:
    # Читаем содержимое файла
    content = file.read()
    # Выводим содержимое файла на экранS
    print(content)

# Открываем файл для записи
with open("output.txt", "w") as file:
    # Записываем строку в файл
    file.write("Hello, world!")

# Открываем файл для добавления
with open("output.txt", "a") as file:
    # Добавляем строку в конец файла
    file.write("\nNew line added!")

# ==========================================================================================================

def save_to_file(text, filename):
    """Сохраняет текст в файл"""
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(text)
    print(f"Текст сохранен в файл '{filename}'")

def read_from_file(filename):
    """Читает текст из файла и выводит его"""
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            content = file.read()
        print("\nСодержимое файла:")
        print(content)
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

def main():
    # Запрашиваем текст у пользователя
    user_text = input("Введите текст для сохранения в файл:\n")
    
    # Указываем имя файла
    filename = "user_text.txt"
    
    # Сохраняем текст в файл
    save_to_file(user_text, filename)
    
    # Читаем и выводим содержимое файла
    read_from_file(filename)

if __name__ == "__main__":
    main()

# ===========================================================================================================

# Создаем файл и записываем числа
with open('numbers.txt', 'w') as file:
    for number in range(1, 11):
        file.write(f"{number}\n")

# Читаем файл и вычисляем сумму
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        try:
            number = int(line.strip())
            total += number
        except ValueError:
            print(f"Предупреждение: нечисловое значение '{line.strip()}' пропущено")

print(f"Сумма чисел от 1 до 10: {total}")

# ===========================================================================================================

import os

def write_to_file():
    # Запрашиваем имя файла
    filename = input("Введите имя файла: ")
    
    # Запрашиваем текст для записи
    text = input("Введите текст для записи в файл: ")
    
    # Проверяем существование файла
    if os.path.exists(filename):
        print(f"Файл '{filename}' уже существует.")
        choice = input("Выберите действие:\n1 - Перезаписать файл\n2 - Добавить в конец файла\n3 - Отменить\n> ")
        
        if choice == '1':
            mode = 'w'  # Перезапись
        elif choice == '2':
            mode = 'a'  # Добавление
        else:
            print("Запись отменена.")
            return
    else:
        mode = 'w'  # Файл не существует - создаем новый
    
    # Записываем текст в файл
    with open(filename, mode, encoding = 'utf-8') as file:
        file.write(text + '\n')  # Добавляем перенос строки
    
    # Подтверждение операции
    if mode == 'w':
        print(f"Файл '{filename}' успешно перезаписан.")
    else:
        print(f"Текст добавлен в конец файла '{filename}'.")

if __name__ == "__main__":
    write_to_file()

# ============================================================================================================

def copy_file():
    # Запрашиваем имена файлов у пользователя
    source_file = input("Введите имя исходного файла: ")
    dest_file = input("Введите имя файла для копирования: ")

    try:
        # Открываем исходный файл для чтения
        with open(source_file, 'r', encoding = 'utf-8') as src:
            # Читаем всё содержимое файла
            content = src.read()
            
            # Открываем целевой файл для записи
            with open(dest_file, 'w', encoding = 'utf-8') as dest:
                # Записываем содержимое в новый файл
                dest.write(content)
                
        print(f"Содержимое файла '{source_file}' успешно скопировано в '{dest_file}'")
    
    except FileNotFoundError:
        print("Ошибка: исходный файл не найден!")
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")

if __name__ == "__main__":
    copy_file()

# ====================================================================================================================

def count_file_stats():
    # Запрашиваем имя файла у пользователя
    filename = input("Введите имя файла для анализа: ")
    
    try:
        # Инициализируем счетчики
        line_count = 0
        word_count = 0
        char_count = 0
        
        # Открываем файл для чтения
        with open(filename, 'r', encoding = 'utf-8') as file:
            for line in file:
                line_count += 1  # Считаем строки
                word_count += len(line.split())  # Считаем слова в строке
                char_count += len(line)  # Считаем символы в строке
        
        # Выводим результаты
        print("\nРезультаты анализа файла:")
        print(f"Количество строк: {line_count}")
        print(f"Количество слов: {word_count}")
        print(f"Количество символов: {char_count}")
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    count_file_stats()

# =======================================================================================================

def replace_word_in_file():
    # Запрашиваем данные у пользователя
    filename = input("Введите имя исходного файла: ")
    search_word = input("Введите слово для поиска: ")
    replace_word = input("Введите слово для замены: ")
    output_filename = input("Введите имя нового файла для сохранения результатов: ")

    try:
        # Открываем файлы
        with open(filename, 'r', encoding = 'utf-8') as input_file, \
             open(output_filename, 'w', encoding = 'utf-8') as output_file:
            
            # Читаем файл построчно
            for line in input_file:
                # Заменяем слово в строке
                modified_line = line.replace(search_word, replace_word)
                # Записываем измененную строку в новый файл
                output_file.write(modified_line)
        
        print(f"\nЗамена завершена. Результаты сохранены в файл '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    replace_word_in_file()

# ==================================================================================================================

def reverse_file_lines():
    # Запрашиваем имя файла у пользователя
    filename = input("Введите имя файла: ")
    
    try:
        # Читаем все строки из файла
        with open(filename, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
        
        # Выводим строки в обратном порядке
        print("\nСодержимое файла в обратном порядке:")
        for line in reversed(lines):
            print(line.strip())  # Удаляем лишние пробелы и переносы строк
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    reverse_file_lines()

# Для работы с очень большими файлами можно использовать альтернативный подход:
import os

def reverse_large_file(filename):
    """Эффективный метод для больших файлов"""
    with open(filename, 'rb') as file:
        # Перемещаемся в конец файла
        file.seek(0, os.SEEK_END)
        position = file.tell()
        line = ''
        
        # Читаем файл с конца
        while position >= 0:
            file.seek(position)
            char = file.read(1).decode('utf-8')
            
            if char == '\n':
                yield line[::-1]
                line = ''
            else:
                line += char
            position -= 1
        
        yield line[::-1]

# Использование:
for reversed_line in reverse_large_file('large_file.txt'):
    print(reversed_line)

# ===============================================================================================================

import datetime

def log_program_start():
    # Указываем имя файла журнала
    log_file = "program_log.txt"
    
    # Получаем текущую дату и время
    current_time = datetime.datetime.now()
    
    # Форматируем строку для записи
    log_entry = f"Программа запущена: {current_time}\n"
    
    # Открываем файл в режиме добавления (append)
    with open(log_file, "a", encoding = "utf-8") as file:
        file.write(log_entry)
    
    print(f"Запись добавлена в журнал: {log_entry.strip()}")

if __name__ == "__main__":
    log_program_start()

# ==================================================================================================================

def write_to_file(filename, lines):
    """Записывает строки в файл."""
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.writelines(lines)

def replace_in_file(filename, old_word, new_word):
    """Заменяет все вхождения old_word на new_word в файле."""
    with open(filename, 'r', encoding = 'utf-8') as file:
        content = file.read()
    
    updated_content = content.replace(old_word, new_word)
    
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(updated_content)

def main():
    # Запрашиваем у пользователя строки текста
    print("Введите текст (для завершения введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line + '\n')  # Добавляем перевод строки
    
    # Сохраняем текст в файл
    filename = "user_text.txt"
    write_to_file(filename, lines)
    print(f"Текст сохранен в файл '{filename}'.")
    
    # Запрашиваем слова для замены
    old_word = input("\nВведите слово, которое нужно заменить: ")
    new_word = input("Введите слово, на которое нужно заменить: ")
    
    # Выполняем замену
    replace_in_file(filename, old_word, new_word)
    print(f"Все вхождения слова '{old_word}' заменены на '{new_word}'.")
    
    # Выводим обновленный текст
    print("\nОбновленный текст:")
    with open(filename, 'r', encoding = 'utf-8') as file:
        print(file.read())

if __name__ == "__main__":
    main()

# ===============================================================================================================

import csv

def read_csv(filename):
    """Читает CSV-файл и возвращает данные в виде списка списков."""
    with open(filename, 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

def write_csv(filename, data):
    """Записывает данные в CSV-файл."""
    with open(filename, 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def edit_data(data):
    """Позволяет пользователю редактировать данные."""
    print("\nТекущие данные:")
    for i, row in enumerate(data):
        print(f"{i}: {row}")
    
    print("\nВыберите строку для редактирования (номер) или нажмите Enter для завершения:")
    while True:
        choice = input("> ")
        if choice == "":
            break
        
        try:
            row_idx = int(choice)
            if 0 <= row_idx < len(data):
                print(f"Редактирование строки {row_idx}: {data[row_idx]}")
                new_values = input("Введите новые значения через запятую: ").split(',')
                data[row_idx] = [value.strip() for value in new_values]
                print("Строка обновлена.")
            else:
                print("Некорректный номер строки.")
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    print("Программа для редактирования CSV-файлов")
    
    # Запрос имени файла
    input_file = input("Введите имя CSV-файла для чтения: ")
    output_file = input("Введите имя нового CSV-файла для сохранения: ")
    
    try:
        # Чтение данных
        data = read_csv(input_file)
        
        # Редактирование
        edit_data(data)
        
        # Сохранение
        write_csv(output_file, data)
        print(f"\nДанные успешно сохранены в файл '{output_file}'")
        
        # Показ первых 5 строк нового файла
        print("\nПервые 5 строк нового файла:")
        new_data = read_csv(output_file)
        for row in new_data[:5]:
            print(row)
            
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()