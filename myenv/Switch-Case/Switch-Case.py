# ==================================================================================================================
# Switch-Case - это конструкция в программировании, которая позволяет выбирать действие на основе значения определен­ной переменной или выражения. 
# В отличие от некоторых других языков программирования, таких как С++ или Java, Python не имеет встроенной конструкции switch-case. 
# Вместо этого обыч­но используется цепочка условных операторов if-elif-else для реализации аналогичного поведения.
# ===================================================================================================================

# Давайте рассмотрим пример использования switch-case в Python и его альтернативы с использованием условных операторов.
# Пример "switch-case" в Python
def switch_case(argument):
    switcher = {
        1: "Первый случай",
        2: "Второй случай",
        3: "Третий случай",
    }
    return switcher.get(argument, "Неверный случай")

# Пример использования·
print(switch_case(1)) # Вывод: Первый случай
print(switch_case(2)) # Вывод: Второй случай
print(switch_case(3)) # Вывод: Третий случай
print(switch_case(4)) # Вывод: Неверный случай

# В этом примере мы создали функцию switch_case, которая принимает аргумент и использует словарь, чтобы сопоставить его с соответствующей строкой. 
# Если значение не найдено в словаре, функция вернет строку "Не­верный случай". 
# Если же вы предпочитаете классический подход, всегда можно использовать цепочку условных операторов if-elif-else.

# Альтернативный подход с использованием условных операторов "if-elif-else":
def switch_case(argument):
    if argument == 1:
        return "Первый случай"
    elif argument == 2:
        return "Второй случай"
    elif argument == 3:
        return "Третий случай"
    else:
        return "Неверный случай"

# Пример использования
print(switch_case(1)) # Вывод: Первый случай
print(switch_case(2)) # Вывод: Второй случай
print(switch_case(3)) # Вывод: Третий случай
print(switch_case(4)) # Вывод: Неверный случай

# Оба подхода дают одинаковый результат, но использование словаря мо­жет быть более компактным и удобным, 
# особенно когда нужно выбирать из множества вариантов. 
# С другой стороны, условные операторы if-elif-else мо­гут сделать код длиннее и многословнее, особенно если вариантов много.

# Обработка выбора дня недели
def get_weekday_name(day):
    switcher = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье",
    }
    return switcher.get(day, "Недопустимый день")
# Пример использования
print(get_weekday_name(1)) # Вывод: Понедельник
print(get_weekday_name(3)) # Вывод: Среда
print(get_weekday_name(8)) # Вывод: Недопустимый день

# Оценка студента по баллам
def get_grade(score):
    switcher = {
        10: "Отлично",
        9: "Отлично",
        8: "Хорошо",
        7: "Хорошо",
        6: "Удовлетворительно",
    }
    return switcher.get(score, "Неудовлетворительно")

# Пример использования
print(get_grade(9)) # Вывод: Отлично
print(get_grade(7)) # Вывод: Хорошо
print(get_grade(5)) # Вывод: Неудовлетворительно

# Выбор варианта действия в игре:
def perform_action(action):
    switcher = {
        "attack": "Атаковать",
        "defend": "Защищаться",
        "spell": "Использовать заклинание",
        "run": "Бежать",
    }
    return switcher.get (action, "Неверное действие")

# Пример использования
print(perform_action("attack")) # Вывод: Атаковать
print(perform_action("spell")) # Вывод: Использовать заклинание
print(perform_action("jump")) # Вывод: Неверное действие

# Эти примеры демонстрируют использование конструкции switch-case в Python для выбора определенного действия на основе переданного значения 
# аргумента. Конструкция switch-case упрощает написание кода и делает его более читаемым и легко поддерживаемым.

# ==================================================================================================================================

def greet():
    print("Привет! Как твои дела?")

def help_me():
    print("Доступные команды: hello, help, calc, exit")

def calculate():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"{a} + {b} = {a + b}")

def exit_program():
    print("Выход из программы...")
    exit()

# Словарь "команда → функция"
commands = {
    "hello": greet,
    "help": help_me,
    "calc": calculate,
    "exit": exit_program
}

def main():
    print("Программа-имитатор Switch-Case. Введите команду (hello/help/calc/exit):")
    while True:
        user_input = input("> ").strip().lower()
        if user_input in commands:
            commands[user_input]()  # Вызов соответствующей функции
        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")

if __name__ == "__main__":
    main()

# Можно добавить новые команды, просто расширив словарь:
commands["time"] = lambda: print("Сейчас: " + datetime.now().strftime("%H:%M"))

# Можно сделать регистронезависимый ввод (как в примере: lower()).
def custom_greet(name):
    print(f"Привет, {name}!")

commands["greet"] = lambda: custom_greet(input("Введите имя: "))

# =========================================================================================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

# Словарь операций: ключ → функция
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("Простой калькулятор (доступные операции: +, -, *, /)")
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        
        if operator not in operations:
            print("Ошибка: неизвестный оператор!")
        else:
            result = operations[operator](num1, num2)
            print(f"Результат: {num1} {operator} {num2} = {result}")
    except ValueError:
        print("Ошибка: введите числа корректно!")

# Запуск калькулятора
calculator()

# Можно добавить возведение в степень (**), используя:
operations["**"] = lambda a, b: a ** b

# ===============================================================================================================

def power_on():
    print("Устройство включено. Доступны все функции.")

def power_off():
    print("Устройство выключается... До свидания!")

def standby():
    print("Устройство в режиме ожидания. Нажмите кнопку для активации.")

# Словарь режимов: ключ - название режима, значение - функция
modes = {
    "включение": power_on,
    "выключение": power_off,
    "ожидание": standby
}

def device_control():
    print("Доступные режимы работы устройства:")
    print(", ".join(modes.keys()))  # Выводим все доступные режимы
    
    while True:
        user_input = input("\nВведите режим работы: ").strip().lower()
        
        if user_input in modes:
            modes[user_input]()  # Вызываем соответствующую функцию
            if user_input == "выключение":
                break  # Завершаем программу при выключении
        else:
            print("Ошибка: такого режима нет. Попробуйте еще раз.")

# Запускаем управление устройством
device_control()

# ==========================================================================================================================

import random

class GuessNumberGame:
    def __init__(self):
        self.secret_number = None
        self.attempts = 0
        self.game_active = False
        self.commands = {
            "начать игру": self.start_game,
            "ввести число": self.guess_number,
            "показать подсказку": self.show_hint,
            "выход": self.exit_game,
            "помощь": self.show_help
        }
    
    def start_game(self):
        """Начинает новую игру"""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_active = True
        print("\nНовая игра началась! Я загадал число от 1 до 100.")
        print("Попробуй угадать его за минимальное количество попыток!")
        print("Доступные команды: ввести число, показать подсказку, выход, помощь")
    
    def guess_number(self):
        """Обрабатывает попытку угадать число"""
        if not self.game_active:
            print("Сначала начните игру командой 'начать игру'")
            return
        
        try:
            guess = int(input("\nВведите ваше число: "))
            self.attempts += 1
            
            if guess == self.secret_number:
                print(f"Поздравляю! Вы угадали число за {self.attempts} попыток!")
                self.game_active = False
            elif guess < self.secret_number:
                print("Мое число больше.")
            else:
                print("Мое число меньше.")
        except ValueError:
            print("Пожалуйста, введите целое число!")
    
    def show_hint(self):
        """Показывает подсказку"""
        if not self.game_active:
            print("Сначала начните игру командой 'начать игру'")
            return
        
        if self.secret_number % 2 == 0:
            print("Подсказка: число четное")
        else:
            print("Подсказка: число нечетное")
    
    def exit_game(self):
        """Завершает игру"""
        if self.game_active:
            print(f"Игра завершена. Загаданное число было {self.secret_number}.")
        self.game_active = False
        return True  # Флаг для выхода из цикла
    
    def show_help(self):
        """Показывает список команд"""
        print("\nДоступные команды:")
        for command in self.commands:
            print(f"- {command}")
    
    def run(self):
        """Основной цикл игры"""
        print("Добро пожаловать в игру 'Угадай число'!")
        print("Введите 'начать игру' для старта или 'помощь' для списка команд.")
        
        while True:
            command = input("\nВведите команду: ").lower()
            
            if command in self.commands:
                if self.commands[command]():  # Если функция вернет True (выход)
                    break
            else:
                print("Неизвестная команда. Введите 'помощь' для списка команд.")

# Запуск игры
if __name__ == "__main__":
    game = GuessNumberGame()
    game.run()

# =================================================================================================================

def handle_zero_division():
    return "Ошибка: деление на ноль!"

def handle_value_error():
    return "Ошибка: введите корректное число!"

def handle_generic_error():
    return "Произошла неизвестная ошибка!"

# Словарь обработчиков ошибок
error_handlers = {
    ZeroDivisionError: handle_zero_division,
    ValueError: handle_value_error,
    Exception: handle_generic_error
}

def calculate():
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            return "Ошибка: неверный оператор!"
        
        return f"Результат: {num1} {operator} {num2} = {result}"
    
    except Exception as e:
        # Получаем тип ошибки и находим соответствующий обработчик
        error_type = type(e)
        handler = error_handlers.get(error_type, error_handlers[Exception])
        return handler()

def main():
    print("Калькулятор с обработкой ошибок")
    print("Доступные операции: +, -, *, /")
    
    while True:
        print("\n" + "="*30)
        result = calculate()
        print(result)
        
        choice = input("\nПродолжить? (да/нет): ").lower()
        if choice != 'да':
            print("Работа программы завершена.")
            break

if __name__ == "__main__":
    main()

# =========================================================================================================

def show_english():
    print("Hello! Welcome to our program.")

def show_russian():
    print("Привет! Добро пожаловать в нашу программу.")

def show_spanish():
    print("¡Hola! Bienvenido a nuestro programa.")

def show_french():
    print("Bonjour! Bienvenue dans notre programme.")

def show_german():
    print("Hallo! Willkommen in unserem Programm.")

# Словарь языков и соответствующих функций
languages = {
    "английский": show_english,
    "русский": show_russian,
    "испанский": show_spanish,
    "французский": show_french,
    "немецкий": show_german
}

def main():
    print("Доступные языки:")
    print(", ".join(languages.keys()))
    
    while True:
        choice = input("\nВыберите язык или введите 'выход' для завершения: ").lower()
        
        if choice == 'выход':
            print("Программа завершена.")
            break
            
        if choice in languages:
            print(f"\nВыбран язык: {choice.capitalize()}")
            languages[choice]()  # Вызываем соответствующую функцию
        else:
            print("Такого языка нет в списке. Попробуйте еще раз.")

if __name__ == "__main__":
    main()

# Добавьте запись в словарь languages:
def show_chinese():
    print("你好! 欢迎来到我们的程序。")

languages["китайский"] = show_chinese

# =================================================================================================================================

tasks = []  # Список для хранения задач

def add_task():
    """Добавляет новую задачу"""
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена!")

def remove_task():
    """Удаляет задачу"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("Текущие задачи:")
    show_tasks()
    
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Задача '{removed}' удалена!")
        else:
            print("Неверный номер задачи!")
    except ValueError:
        print("Пожалуйста, введите число!")

def show_tasks():
    """Показывает все задачи"""
    if not tasks:
        print("Список задач пуст!")
    else:
        print("\nТекущие задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def edit_task():
    """Редактирует существующую задачу"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    show_tasks()
    
    try:
        index = int(input("Введите номер задачи для редактирования: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Введите новый текст задачи: ")
            old_task = tasks[index]
            tasks[index] = new_task
            print(f"Задача '{old_task}' изменена на '{new_task}'")
        else:
            print("Неверный номер задачи!")
    except ValueError:
        print("Пожалуйста, введите число!")

def exit_program():
    """Завершает программу"""
    print("Выход из программы...")
    return True

# Словарь команд
commands = {
    "добавить": add_task,
    "удалить": remove_task,
    "показать": show_tasks,
    "изменить": edit_task,
    "выход": exit_program
}

def main():
    print("Программа для управления списком задач")
    print("Доступные команды: добавить, удалить, показать, изменить, выход")
    
    while True:
        command = input("\nВведите команду: ").lower()
        
        if command in commands:
            if commands[command]():  # Если функция вернет True (выход)
                break
        else:
            print("Неизвестная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()

# Добавьте команду в словарь commands:
def clear_tasks():
    """Очищает список задач"""
    tasks.clear()
    print("Все задачи удалены!")

commands["очистить"] = clear_tasks