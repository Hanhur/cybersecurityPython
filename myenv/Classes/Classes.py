# ================================================================================================
# Классы являются основной концепцией объектно-ориентированного программирования (ООП) в Python. 
# Классы позволяют создавать новые типы объектов с определенными свойствами и методами. 
# В этом разделе мы рассмотрим основные аспекты классов и их использование в Python.
# ==================================================================================================

# Класс в Python создаётся с помощью ключевого слова class, за которым идёт имя класса. Обычно имя класса пишут с заглавной буквы. 
# Внутри класса задаются атрибуты (переменные) и метады (функции), которые·описывают свойства и поведение объектов этого класса.

# Пример определения класса
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Пpивeт, меня зовут {self.name} и мне {self.age} лет.")

# Создание объекта класса Person
personl = Person("Aлиca", 25)

# Вызов метода объекта
personl.greet() # Вывод: Привет, меня зовут Алиса и мне 25 лет.

# Атрибуты класса - это переменные, которые хранят данные объекта. 
# Их обычно, задают в конструкторе класса (_init_), и они доступны для использования внутри методов объекта.

# Методы класса - это функции, которые находятся внутри класса и работают с его атрибутами, выполняя разные задачи. 
# Их можно вызывать для конкретного объекта этого класса. Можно сказать, что методы - это такие "суперспособности" объекта, 
# которые позволяют ему делать то, что он умеет.

# Наследование
class Student(Person):
    def __init__ (self, name, age, student_id):
        super().__init__ (name, age)
        self.student_id = student_id
    def study(self):
        print(f"{self.name} учится на факультете.")

# Создание объекта класса Student
studentl = Student("Бoб", 20, "2021001")

# Вызов методов объекта
studentl.greet() # Вывод: Привет, меня зовут Боб и мне 20 лет.
studentl. study() # Вывод: Боб учится на факультете.

# Создание класса для представления книги
class Book:
    def __init__ (self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_info(self):
        return f"{self.title} - {self.author}, {self.pages} страниц"

# Создание объекта класса Book
bookl = Book("Война и мир", "Лев Толстой", 1225)
print(bookl.get_info()) # Вывод: Война и мир - Лев Толстой, 1225 страниц

# Создание класса для представления автомобиля
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

# Создание объекта класса Car
car1 = Car("Toyota", "Camry", 2020)
print(car1.get_description()) # Вывод: 2020 Toyota Camry

# ==============================================================================================================

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
# Пример использования:
# Создаём объект прямоугольника с шириной 5 и высотой 10
rect = Rectangle(5, 10)

# Вычисляем площадь
area = rect.calculate_area()
print(f"Площадь прямоугольника: {area}")  # Выведет: Площадь прямоугольника: 50

# __init__(self, width, height) — конструктор класса, инициализирует атрибуты width и height.
# calculate_area(self) — метод, возвращающий площадь прямоугольника (произведение ширины на высоту).

# ==================================================================================================================

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def get_info(self):
        return f"Студент: {self.name}, Возраст: {self.age}, Специальность: {self.major}"
    
# Пример использования:
# Создаём объект студента
student = Student("Иван Иванов", 20, "Информатика")

# Получаем информацию о студенте
info = student.get_info()
print(info)  # Выведет: Студент: Иван Иванов, Возраст: 20, Специальность: Информатика

# ====================================================================================================================

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Пополнение счета на указанную сумму."""
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}. Новый баланс: {self.balance}")
        else:
            print("Ошибка: сумма для пополнения должна быть положительной.")
    
    def withdraw(self, amount):
        """Снятие денег со счета (если достаточно средств)."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снято {amount}. Остаток на счете: {self.balance}")
            else:
                print("Ошибка: недостаточно средств на счете.")
        else:
            print("Ошибка: сумма для снятия должна быть положительной.")
    
    def __str__(self):
        """Возвращает информацию о счете."""
        return f"Владелец: {self.owner}, Баланс: {self.balance}"
    
# Пример использования:
# Создаем банковский счет
account = BankAccount("Иван Петров", 1000)

# Пополняем счет
account.deposit(500)  # Выведет: "Счет пополнен на 500. Новый баланс: 1500"

# Пытаемся снять деньги
account.withdraw(200)  # Выведет: "Снято 200. Остаток на счете: 1300"
account.withdraw(2000) # Выведет: "Ошибка: недостаточно средств на счете."

# Выводим информацию о счете
print(account)  # Выведет: "Владелец: Иван Петров, Баланс: 1300"

# =================================================================================================================
import math  # Для использования числа π (math.pi)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        """Вычисляет площадь круга: π * r²"""
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        """Вычисляет длину окружности: 2 * π * r"""
        return 2 * math.pi * self.radius
    
    def __str__(self):
        """Возвращает информацию о круге."""
        return f"Круг с радиусом {self.radius}"
    
# Пример использования:
# Создаем круг с радиусом 5
circle = Circle(5)

# Вычисляем площадь
area = circle.calculate_area()
print(f"Площадь круга: {area:.2f}")  # Округляем до 2 знаков после запятой

# Вычисляем длину окружности
circumference = circle.calculate_circumference()
print(f"Длина окружности: {circumference:.2f}")

# Выводим информацию о круге
print(circle)  # Выведет: "Круг с радиусом 5"

# Можно добавить проверку, что радиус положительный:
if radius <= 0:
    raise ValueError("Радиус должен быть положительным!")

# Можно добавить метод для изменения радиуса:
def set_radius(self, new_radius):
    self.radius = new_radius

# ===============================================================================================================

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def calculate_bonus(self):
        """Вычисляет бонус (10% от зарплаты)."""
        return self.salary * 0.10
    
    def __str__(self):
        """Возвращает информацию о сотруднике."""
        return f"Сотрудник: {self.name}, Должность: {self.position}, Зарплата: {self.salary}"
    
# Пример использования:
# Создаем сотрудника
employee = Employee("Алексей Петров", "Менеджер", 50000)

# Вычисляем бонус
bonus = employee.calculate_bonus()
print(f"Бонус сотрудника: {bonus:.2f} руб.")  # Выведет: Бонус сотрудника: 5000.00 руб.

# Выводим информацию о сотруднике
print(employee)  # Выведет: Сотрудник: Алексей Петров, Должность: Менеджер, Зарплата: 50000

# Можно добавить проверку на отрицательную зарплату:
if salary < 0:
    raise ValueError("Зарплата не может быть отрицательной!")

# Можно добавить метод для повышения зарплаты:
def raise_salary(self, percent):
    """Увеличивает зарплату на указанный процент."""
    self.salary *= (1 + percent / 100)