# ==============================================================================================
# Работа с СSV-файлами (Comma Separated Values) - это процесс чтения, записи и обработки данных, 
# которые хранятся в этом популярном формате. В Python для работы с CSV используется модуль csv.
# ===============================================================================================

# CSV - это как лёгкая версия Excel, которая часто применяется для хра­нения и обмена информацией. 
# Весьма удобно, если вы хотите записать дан­ные в файл, а затем с лёгкостью их извлечь, без лишнего "веса" табличного редактора. 
# Можно сказать, что CSV - это как бутерброд с данными: всё просто, удобно и без лишних "ингредиентов"!

# Мы рассматриваем этот формат, потому что в следующих главах будем работать с данными в формате CSV, и важно научиться с ним взаимодей­ ствовать. 
# Данные в СSV-файле организованы в виде таблицы. Когда мы чи­таем или записываем такой файл, 
# данные обычно обрабатываются как сло­варь или список в Python.

# Если вам нужно работать с большим количеством строк и анализиро­вать данные, рекомендую использовать специализированную библиотеку pandas. 
# Она значительно облегчает эту задачу и делает работу с данными более удобной и эффективной.

# Основные функции библиотеки csv похожи на работу с обычными файлами - запись, чтение и представление данных в разных форматах.

# Чтение данных в СSV-файле выполняется так же, как и с обычным файлом, - через открытие и чтение. 
# Единственное отличие заключается в следующем:

# Чтение данных из CSV
import csv

# Открытие файла CSV для чтения
with open('data.csv', 'r') as file:
    # Создание объекта чтения CSV
    reader = csv.reader(file)
    # Чтение данных из файла построчно
    for row in reader:
        print(row)

# Запись данных в CSV
import csv

# Данные для записи в CSV
data = [
    [ 'Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Alic::e', '25', 'Los Angeles'],
    ['ВоЬ', '35', 'Chicago']
]
# Открытие файла CSV для записи
with open('output.csv', 'w', newline = '') as file:
    # Создание объекта записи CSV
    writer = csv.writer(file)
    # Запись данных в файл
    for row in data:
        writer.writerow(row)

# Загрузка данных из CSV в словарь
import csv

# Открытие файла CSV для чтения
with open('data.csv', 'r') as file:
    # Создание объекта чтения CSV с указанием заголовков
    reader = csv.DictReader(file)
    # Чтение данных из файла и преобразование в словарь
    for row in reader:
        print(row)

# Запись данных из словаря в CSV
import csv

# Данные в виде словаря
data = [
    {'Name': 'John', 'Age': '30', 'City': 'New York'},
    {'Name': 'Alice', 'Age': '25', 'City': 'Los Angeles'},
    {'Name': 'Bob', 'Age': '35', 'City': 'Chicago'}
]

# Заголовки столбцов
fields = [ 'Name', 'Age', 'City']

# Открытие файла CSV для записи
with open('output.csv', 'w', newline = '') as file:
    # Создание объекта записи CSV с указанием заголовков
    writer = csv.DictWriter(file, fieldnames = fields)
    # Запись заголовков
    writer.writeheader()
    # Запись данных в файл
    writer.writerows(data)

# Чтение данных из CSV файла и вывод на экран
import csv

with open('data._csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Запись данных в CSV файл
import csv

data = [
    [ 'Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Alice', '25', 'Los Angeles'],
    ['Bob', '35', 'Chicago']
]
with open('output.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Чтение данных из CSV файла в виде словаря
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Запись данных из словаря в CSV файл
import csv

data = [
    { 'Name': ' John', 'Age': '30', 'City': 'New York'},
    { 'Name': 'Alice', 'Age': '25', 'City': 'Los Angeles'},
    { 'Name': ' Bob', 'Age': '35', 'City': 'Chicago'}
]

fields = ['Name', 'Age', 'City']

with open('output.csv', 'w', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader()
    writer.writerows(data)

# =======================================================================================================================

import csv

def load_students_data(filename):
    """Загружает данные о студентах из CSV-файла."""
    students = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                'name': row['Имя'],
                'age': int(row['Возраст']),
                'grades': [float(grade) for grade in row['Оценки'].split(';')]
            })
    return students

def calculate_average(grades):
    """Вычисляет средний балл."""
    return sum(grades) / len(grades) if grades else 0

def display_students_info(students):
    """Выводит информацию о студентах."""
    print("\nИнформация о студентах:")
    print("{:<20} {:<10} {:<15}".format("Имя", "Возраст", "Средний балл"))
    print("-" * 45)
    
    for student in students:
        avg_grade = calculate_average(student['grades'])
        print("{:<20} {:<10} {:<15.2f}".format(
            student['name'],
            student['age'],
            avg_grade
        ))

def main():
    print("Программа для анализа успеваемости студентов")
    
    try:
        filename = input("Введите имя CSV-файла с данными студентов: ")
        students = load_students_data(filename)
        display_students_info(students)
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except KeyError as e:
        print(f"Ошибка: в файле отсутствует обязательное поле {str(e)}")
    except ValueError as e:
        print(f"Ошибка в данных: {str(e)}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()

# =========================================================================================================================

import csv
from datetime import datetime
from collections import defaultdict

def load_sales_data(filename):
    """Загружает данные о продажах из CSV-файла."""
    sales = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                date = datetime.strptime(row['Дата'], '%Y-%m-%d')
                amount = float(row['Сумма'])
                sales.append({'date': date, 'amount': amount})
            except ValueError as e:
                print(f"Ошибка в строке {reader.line_num}: {e}")
    return sales

def calculate_monthly_revenue(sales):
    """Вычисляет выручку по месяцам."""
    monthly_revenue = defaultdict(float)
    for sale in sales:
        month_key = sale['date'].strftime('%Y-%m')
        monthly_revenue[month_key] += sale['amount']
    return monthly_revenue

def display_monthly_revenue(revenue):
    """Выводит отчет о выручке по месяцам."""
    print("\nОтчет о выручке по месяцам:")
    print("{:<15} {:<15}".format("Месяц", "Выручка"))
    print("-" * 30)
    
    for month, total in sorted(revenue.items()):
        print("{:<15} {:<15.2f}".format(month, total))

def main():
    print("Анализатор продаж - расчет выручки по месяцам")
    
    try:
        filename = input("Введите имя CSV-файла с данными о продажах: ")
        sales_data = load_sales_data(filename)
        
        if not sales_data:
            print("Нет данных для анализа")
            return
            
        monthly_revenue = calculate_monthly_revenue(sales_data)
        display_monthly_revenue(monthly_revenue)
        
        # Дополнительная статистика
        total_revenue = sum(monthly_revenue.values())
        print("\nОбщая выручка за период: {:.2f}".format(total_revenue))
        print("Среднемесячная выручка: {:.2f}".format(total_revenue / len(monthly_revenue)))
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()

# ========================================================================================================================

import csv

def get_employee_data():
    """Запрашивает данные о сотруднике у пользователя"""
    print("\nВведите данные сотрудника (для завершения оставьте имя пустым)")
    name = input("Имя: ")
    if not name:
        return None
    
    while True:
        try:
            age = int(input("Возраст: "))
            if age < 18 or age > 100:
                print("Возраст должен быть от 18 до 100 лет")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число для возраста")
    
    position = input("Должность: ")
    
    return {'name': name, 'age': age, 'position': position}

def save_to_csv(filename, employees):
    """Сохраняет данные сотрудников в CSV-файл"""
    with open(filename, 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = ['Имя', 'Возраст', 'Должность'])
        writer.writeheader()
        for emp in employees:
            writer.writerow({
                'Имя': emp['name'],
                'Возраст': emp['age'],
                'Должность': emp['position']
            })

def main():
    print("Система учёта сотрудников")
    employees = []
    
    while True:
        emp_data = get_employee_data()
        if not emp_data:
            break
        employees.append(emp_data)
    
    if not employees:
        print("Не введено ни одного сотрудника")
        return
    
    filename = input("\nВведите имя файла для сохранения (например: employees.csv): ")
    
    try:
        save_to_csv(filename, employees)
        print(f"\nДанные успешно сохранены в файл {filename}")
        print(f"Всего сохранено сотрудников: {len(employees)}")
    except Exception as e:
        print(f"Произошла ошибка при сохранении: {e}")

if __name__ == "__main__":
    main()

# ====================================================================================================================

import csv
import os
from pathlib import Path

def get_csv_files(directory):
    """Возвращает список CSV-файлов в указанной директории"""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def read_csv_file(filepath):
    """Читает CSV-файл и возвращает его данные"""
    with open(filepath, 'r', encoding = 'utf-8') as file:
        return list(csv.reader(file))

def write_combined_csv(output_file, data, headers):
    """Записывает объединенные данные в новый CSV-файл"""
    with open(output_file, 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    print("Программа для объединения CSV-файлов")
    
    # Запрашиваем директорию с файлами
    input_dir = input("Введите путь к папке с CSV-файлами: ")
    
    try:
        # Получаем список CSV-файлов
        csv_files = get_csv_files(input_dir)
        
        if not csv_files:
            print("В указанной папке нет CSV-файлов")
            return
        
        print(f"\nНайдено CSV-файлов: {len(csv_files)}")
        for i, filename in enumerate(csv_files, 1):
            print(f"{i}. {filename}")
        
        # Запрашиваем имя выходного файла
        output_filename = input("\nВведите имя для объединенного файла (например: combined.csv): ")
        output_path = os.path.join(input_dir, output_filename)
        
        # Проверяем, что файл с таким именем не существует
        if os.path.exists(output_path):
            print(f"Ошибка: файл '{output_filename}' уже существует")
            return
        
        # Объединяем данные
        all_data = []
        headers = None
        
        for filename in csv_files:
            filepath = os.path.join(input_dir, filename)
            data = read_csv_file(filepath)
            
            if not data:
                continue
                
            if headers is None:
                headers = data[0]  # сохраняем заголовки из первого файла
                all_data.extend(data[1:])  # добавляем данные без заголовков
            else:
                # Проверяем совпадение заголовков
                if data[0] != headers:
                    print(f"Предупреждение: заголовки в файле {filename} не совпадают с основными")
                    continue
                all_data.extend(data[1:])
        
        # Записываем объединенный файл
        write_combined_csv(output_path, all_data, headers)
        
        print(f"\nОбъединение завершено! Создан файл: {output_path}")
        print(f"Всего строк данных: {len(all_data)}")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()

# ==================================================================================================================

import csv
from datetime import datetime
from collections import defaultdict
import statistics

def analyze_website_stats(file_path):
    """
    Анализирует статистику посещений сайта из CSV-файла
    и возвращает среднее количество посещений по месяцам
    """
    monthly_visits = defaultdict(list)
    
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                try:
                    date = datetime.strptime(row['date'], '%Y-%m-%d')
                    visits = int(row['visits'])
                    month_key = date.strftime('%Y-%m')
                    monthly_visits[month_key].append(visits)
                except (ValueError, KeyError) as e:
                    print(f"Ошибка в строке {csv_reader.line_num}: {e}")
                    continue
        
        # Вычисляем среднее по каждому месяцу
        monthly_avg = {
            month: statistics.mean(visits) 
            for month, visits in monthly_visits.items()
        }
        
        return monthly_avg
    
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def display_results(monthly_avg):
    """Выводит результаты анализа в удобном формате"""
    if not monthly_avg:
        print("Нет данных для отображения")
        return
    
    print("\nСреднее количество посещений по месяцам:")
    print("{:<15} {:<15}".format("Месяц", "Средние посещения"))
    print("-" * 30)
    
    for month, avg in sorted(monthly_avg.items()):
        print("{:<15} {:<15.2f}".format(month, avg))

def main():
    print("Анализатор статистики посещений сайта")
    file_path = input("Введите путь к CSV-файлу со статистикой: ")
    
    monthly_avg = analyze_website_stats(file_path)
    display_results(monthly_avg)

if __name__ == "__main__":
    main()