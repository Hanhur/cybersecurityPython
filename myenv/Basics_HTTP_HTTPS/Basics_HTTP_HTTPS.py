# =====================================================================================================================
# Веб-приложения представляют собой интерактивные программы, которые работают через веб-браузер, 
# тогда как веб-сайты это коллекции связанных веб-страниц, доступных по URL

# На клиентской стороне (frontend) находятся все элементы, с которыми взаимодействует пользователь через веб-браузер. 
# Здесь используются такие технологии, как HTML, CSS и JavaScript.

# HTML (Hypertext Markup Language) структурирует контент на веб­-страницах, создавая каркас веб-страницы с элементами, 
# такими как за­головки, абзацы, списки и формы.

# CSS (Cascading Style Sheets) отвечает за стилизацию и оформление веб­-страниц, управляя цветами, шрифтами, макетом и визуальными эффек­тами.

# JavaScript добавляет интерактивность и динамическое поведение веб­-страницам, позволяя реагировать на действия пользователя, 
# манипулиро­вать DOM и делать асинхронные запросы.
# ========================================================================================================================

# Серверная сторона (backend) отвечает за обработку запро­сов от клиента, взаимодействие с базами данных и выполнение бизнес-логики. 
# Здесь используются серверы, такие как Node.js, Apache, Nginx и другие, а также серверные языки программиро­вания, 
# включая Python, Ruby, РНР, Java и С#. Веб-приложения могут использовать реляционные базы данных, такие как MySQL и PostgreSQL, 
# или NoSQL базы данных, такие как MongoDB и CouchDB.

# Веб-сервисы и API позволяют различным программным компонентам взаимодействовать друг с другом. 
# REST (Representational State Transfer) яв­ляется архитектурным стилем для создания веб-сервисов, 
# использующим НТТР методы (GET, POST, PUT, DELETE) для взаимодействия с ресурсами. 
# GraphQL - это язык запросов для API, позволяющий клиентам запращивать только необходимые данные.

# Веб-страницы состоят из НТМL-кода и могут включать встроенные CSS и JavaScript. Они загружаются в браузере и отображаются пользователю.
# Использование фреймворков и библиотек ускоряет разработку и упрощает управление кодом. На клиентской стороне популярными являются React,
# Angular и Vue.js, а на серверной стороне - Django (Python), Ruby on Rails (Ruby), Laravel (РНР) и Express.js (Node.js).

# Обеспечение безопасности веб-приложений включает меры по защите от различных угроз и атак, таких как SQL-инъекции, 
# кросс-сайтовый скриптинг (XSS) и кросс-сайтовая подделка запроса (CSRF). 
# Использование HTT PS с шифрованием данных между клиентом и сервером повышает уровень без­опасности.

# Процесс развертывания включает перенос веб-приложения из среды раз­работки в производственную среду. 
# Автоматизация процессов интеграции и развертывания кода достигается с помощью CI/CD (Continuous Integration/Continuous Deployment). 
# Веб-приложения размещаются на серверах или в облачных сервисах, таких как АWS, Google Cloud и Azure.

# ===================================================== Основы НТТР и HTTPS ==============================================================
# НТТР (Hypertext Transfer Protocol) и НПРS (Hypertext Transfer Protocol Secure) являются протоколами передачи данных в сети Интернет. 
# Они используются для обмена информацией между 

# Принцип работы: НТТР - это протокол, используемый для передачи гипертекстовой информации, такой как веб-страницы, 
# между клиент­скими и серверными приложениями. В основе протокола лежит модель запрос-ответ, где клиент отправляет НТТР-запросы серверу, 
# а сервер от­вечает на них НТТР-ответами.

# Методы запросов: НТТР определяет различные методы запросов, кото­рые определяют тип операции, которую клиент хочет выполнить на сер­вере. 
# Основные методы включают:

# GET - запрашивает данные с сервера. Этот метод используется для получения информации, такой как НТМL-страницы или изображения.

# POST - отправляет данные на сервер для обработки. Используется для передачи данных формы, загрузки файлов и других операций, 
# из­ меняющих состояние сервера.

# PUT - заменяет все текущие представления ресурса данными, пере­данными в теле запроса.

# DЕLЕТЕ-удаляет указанный ресурс на сервере.

# HEAD - запрашивает заголовки ресурса, но не его тело. Этот метод полезен для получения метаданных.

# OPTIONS - возвращает методы НТТР, поддерживаемые сервером для указанного ресурса.

# РАТСН- частично обновляет ресурс.

# ================================================= Основные принципы работы HTTPS =================================================
# Принцип работы: HTTPS - это защищенная версия протокола НТТР, которая использует шифрование для обеспечения конфиденциальности 
# и целостности данных, передаваемых· между клиентом и сервером. Для этого применяются криптографические протоколы SSL/TLS.

# Шифрование данных: при использовании HTTPS данные, передаваемые между клиентом и сервером, шифруются с использованием криптографи­ческих 
# алгоритмов, таких как AES (Advanced Encryption Standard) или RSA (Rivest-Shamir-Adleman), что обеспечивает их конфиденциальность.
# Это предотвращает перехват и просмотр данных злоумышленниками.

# Сертификаты безопасности: HTTPS также включает проверку подлин­ности сервера с использованием цифровых сертификатов SSL/TLS. 
# Сер­тификаты предоставляются доверенными удостоверяющими центрами (СА- Certificate Authority) и содержат информацию о владельце 
# сертифи­ката и открытый ключ, который используется для шифрования данных.

# Порт: HTTPS использует стандартный порт 443 для обмена данными между клиентом и сервером, в отличие от НТТР, который использует порт 80.

# GET - запрашивает данные.
# POST - отправляет данные на сервер.
# PUT - создает или обновляет ресурс.
# DELETE - удаляет ресурс.
# РАТСН - частично обновляет ресурс.
# HEAD - запрашивает только заголовки ответа.

# Отправка GЕТ-запроса с помощью библиотеки requests:
# GET
import requests

# Отправляем GЕТ-запрос на указанный URL
response = requests.get("https://api.example.com/data")

# Выводим статус-код и содержимое ответа
print("Status Code:", response.status_code)
print("Response Body:", response.text)

# Отправка РОSТ-запроса с данными с помощью библиотеки requests:
# POST
import requests

# Данные для отправки
data = { "username": "example_user", "password": "example_password"}

# Отправляем РОSТ-запрос на указанный URL с данными
response = requests.post("https://api.example.com/login", data = data)

# Выводим статус-код и содержимое ответа
print("Status Code:", response.status_code)
print("Response Body:", response.text)

# Отправка РUТ-запроса с данными с помощью библиотеки requests:
# PUT
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userld": 1
}
response = requests.put(url, json = data)

print(response.status_code)
print(response.json())

# Отправка DЕLЕТЕ-запроса с данными с помощью библиотеки requests:
# DELETE
import requests

url = "https://jsonplaceholder.typicod�.com/posts/1"
response = requests.delete(url)

print(response.status_code)
print(response.text)

# Отправка РАТСН-запроса с данными с помощью библиотеки requests:
# РАТСН
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "foo"
}
response = requests.patch(url, json = data)

print(response.status_code)
print(response.json())

# Отправка НЕАD-запроса с данными с помощью библиотеки requests:
# HEAD
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.head(url)

print(response.status_code)
print(response.headers)

# ==============================================================================================================================

# Программа для отправки GET-запросов и проверки статус-кодов
# Установите необходимую библиотеку, если её нет: pip install requests
import requests
from urllib.parse import urlparse

def check_url_status(url):
    try:
        # Добавляем схему http://, если она отсутствует
        if not urlparse(url).scheme:
            url = 'http://' + url
            
        response = requests.get(url, timeout = 10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def main():
    print("Введите URLs для проверки (разделяйте их пробелами или запятыми):")
    user_input = input().strip()
    
    # Разделяем ввод на отдельные URLs
    urls = [url.strip() for url in user_input.replace(',', ' ').split()]
    
    if not urls:
        print("Не введено ни одного URL.")
        return
    
    print("\nРезультаты проверки:")
    print("-" * 50)
    for url in urls:
        status = check_url_status(url)
        print(f"{url.ljust(40)} | {status}")
    print("-" * 50)

if __name__ == "__main__":
    main()

# Для более подробного вывода вы можете модифицировать функцию check_url_status():
def check_url_status(url):
    try:
        if not urlparse(url).scheme:
            url = 'http://' + url
            
        response = requests.get(url, timeout = 10)
        return {
            'status': response.status_code,
            'url': response.url,  # конечный URL после редиректов
            'time': response.elapsed.total_seconds(),
            'size': len(response.content)
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    
# =============================================================================================================================

# Программа для отправки POST-запросов на различные API
# Убедитесь, что у вас установлена библиотека requests: pip install requests
import requests
import json

def send_post_request(url, data = None, json_data = None, headers = None):
    """
    Отправляет POST-запрос на указанный URL
    :param url: URL API
    :param data: Данные для отправки (form-encoded)
    :param json_data: Данные для отправки в формате JSON
    :param headers: Заголовки запроса
    :return: Ответ сервера
    """
    try:
        response = requests.post(
            url,
            data = data,
            json = json_data,
            headers = headers,
            timeout = 10
        )
        
        # Пытаемся преобразовать ответ в JSON, если это возможно
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
            
        return {
            'status_code': response.status_code,
            'response': response_data,
            'headers': dict(response.headers)
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def main():
    print("Демонстрация отправки POST-запросов на различные API\n")
    
    # Примеры API для тестирования
    api_endpoints = [
        {
            'name': 'JSONPlaceholder (тестовое API)',
            'url': 'https://jsonplaceholder.typicode.com/posts',
            'json_data': {
                'title': 'foo',
                'body': 'bar',
                'userId': 1
            },
            'headers': {
                'Content-type': 'application/json; charset=UTF-8'
            }
        },
        {
            'name': 'ReqRes (тестовое API для регистрации)',
            'url': 'https://reqres.in/api/register',
            'json_data': {
                'email': 'eve.holt@reqres.in',
                'password': 'pistol'
            }
        },
        {
            'name': 'HTTPBin (эхо-сервер)',
            'url': 'https://httpbin.org/post',
            'data': {
                'key1': 'value1',
                'key2': 'value2'
            }
        }
    ]
    
    for api in api_endpoints:
        print(f"\nОтправка запроса к: {api['name']}")
        print(f"URL: {api['url']}")
        
        result = send_post_request(
            url = api['url'],
            data = api.get('data'),
            json_data = api.get('json_data'),
            headers = api.get('headers')
        )
        
        if 'error' in result:
            print(f"Ошибка: {result['error']}")
        else:
            print(f"Статус код: {result['status_code']}")
            print("Ответ сервера:")
            print(json.dumps(result['response'], indent = 2, ensure_ascii = False))
        
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()

# Для ввода данных пользователем можно добавить такой код:
def user_input_mode():
    print("Введите данные для POST-запроса:")
    url = input("URL API: ").strip()
    
    print("\nВыберите тип данных:")
    print("1. Form-encoded (data)")
    print("2. JSON (application/json)")
    choice = input("Ваш выбор (1/2): ").strip()
    
    data = None
    json_data = None
    
    if choice == '1':
        print("\nВведите данные в формате key=value (по одному на строку, пустая строка - завершение):")
        data = {}
        while True:
            line = input().strip()
            if not line:
                break
            if '=' in line:
                key, value = line.split('=', 1)
                data[key.strip()] = value.strip()
    elif choice == '2':
        print("\nВведите JSON данные (одна строка):")
        json_str = input().strip()
        try:
            json_data = json.loads(json_str)
        except json.JSONDecodeError:
            print("Ошибка: Неверный формат JSON")
            return
    
    headers = {}
    print("\nВведите заголовки (key: value, пустая строка - завершение):")
    while True:
        line = input().strip()
        if not line:
            break
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    
    result = send_post_request(url, data = data, json_data = json_data, headers = headers)
    
    print("\nРезультат:")
    if 'error' in result:
        print(f"Ошибка: {result['error']}")
    else:
        print(f"Статус код: {result['status_code']}")
        print("Ответ сервера:")
        print(json.dumps(result['response'], indent = 2, ensure_ascii = False))

# =================================================================================================================================

# Утилита для тестирования веб-сайтов на уязвимости
# Установите зависимости: pip install requests
# Запустите сканер с параметрами: python scanner.py -u http://example.com -v -o results.json
import requests
import json
from urllib.parse import urljoin
import argparse
import time

class VulnerabilityScanner:
    def __init__(self, target_url, verbose = False, delay = 1):
        self.target_url = target_url
        self.verbose = verbose
        self.delay = delay
        self.session = requests.Session()
        self.vulnerabilities = []
        
        # Полезные нагрузки для тестирования
        self.payloads = {
            'xss': [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "'\"><script>alert(1)</script>"
            ],
            'sql': [
                "' OR '1'='1",
                "' OR 1=1--",
                "'; DROP TABLE users--",
                "admin'--"
            ],
            'path_traversal': [
                "../../../../etc/passwd",
                "..%2F..%2F..%2F..%2Fetc%2Fpasswd",
                "%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
            ],
            'command_injection': [
                "; ls -la",
                "| cat /etc/passwd",
                "&& whoami",
                "`id`"
            ]
        }
        
        # Заголовки для обхода защиты
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'X-Forwarded-For': '127.0.0.1'
        }
    
    def log(self, message):
        if self.verbose:
            print(f"[*] {message}")
    
    def add_vulnerability(self, type, url, payload, evidence):
        vuln = {
            'type': type,
            'url': url,
            'payload': payload,
            'evidence': evidence
        }
        self.vulnerabilities.append(vuln)
        print(f"[!] Найдена уязвимость {type.upper()} в {url}")
        print(f"    Полезная нагрузка: {payload}")
        print(f"    Признак уязвимости: {evidence}\n")
    
    def check_response(self, response, payload, vuln_type):
        indicators = {
            'xss': [
                "<script>alert('XSS')</script>",
                "onerror=alert('XSS')"
            ],
            'sql': [
                "SQL syntax",
                "MySQL server",
                "syntax error",
                "unclosed quotation mark"
            ],
            'path_traversal': [
                "root:x:0:0",
                "/bin/bash",
                "daemon:x:1:1"
            ],
            'command_injection': [
                "root:x:0:0",
                "www-data:x:33:33",
                "uid=",
                "gid="
            ]
        }
        
        text = response.text.lower()
        for indicator in indicators.get(vuln_type, []):
            if indicator.lower() in text:
                return True
        return False
    
    def test_get_requests(self, params):
        for param in params:
            for vuln_type, payloads in self.payloads.items():
                for payload in payloads:
                    try:
                        url = f"{self.target_url}?{param}={payload}"
                        self.log(f"Тестируем GET {url}")
                        
                        response = self.session.get(
                            url,
                            headers = self.headers,
                            timeout = 10,
                            allow_redirects = False
                        )
                        
                        if self.check_response(response, payload, vuln_type):
                            self.add_vulnerability(
                                vuln_type,
                                url,
                                payload,
                                "Ответ содержит признаки уязвимости"
                            )
                        
                        time.sleep(self.delay)
                    except Exception as e:
                        self.log(f"Ошибка при тестировании GET: {e}")
    
    def test_post_requests(self, forms):
        for form in forms:
            for vuln_type, payloads in self.payloads.items():
                for payload in payloads:
                    try:
                        data = {}
                        for field in form['fields']:
                            data[field] = payload
                        
                        self.log(f"Тестируем POST {self.target_url} с данными: {data}")
                        
                        response = self.session.post(
                            form['action'] if form['action'] else self.target_url,
                            data = data,
                            headers = self.headers,
                            timeout = 10,
                            allow_redirects = False
                        )
                        
                        if self.check_response(response, payload, vuln_type):
                            self.add_vulnerability(
                                vuln_type,
                                form['action'] if form['action'] else self.target_url,
                                payload,
                                "Ответ содержит признаки уязвимости"
                            )
                        
                        time.sleep(self.delay)
                    except Exception as e:
                        self.log(f"Ошибка при тестировании POST: {e}")
    
    def test_put_requests(self, paths):
        for path in paths:
            for vuln_type, payloads in self.payloads.items():
                for payload in payloads:
                    try:
                        url = urljoin(self.target_url, path)
                        self.log(f"Тестируем PUT {url}")
                        
                        response = self.session.put(
                            url,
                            data = payload,
                            headers = self.headers,
                            timeout = 10,
                            allow_redirects = False
                        )
                        
                        if response.status_code in [200, 201, 204]:
                            self.add_vulnerability(
                                'http_methods',
                                url,
                                'PUT',
                                "Сервер принимает PUT-запросы"
                            )
                        
                        time.sleep(self.delay)
                    except Exception as e:
                        self.log(f"Ошибка при тестировании PUT: {e}")
    
    def test_delete_requests(self, paths):
        for path in paths:
            try:
                url = urljoin(self.target_url, path)
                self.log(f"Тестируем DELETE {url}")
                
                response = self.session.delete(
                    url,
                    headers = self.headers,
                    timeout = 10,
                    allow_redirects = False
                )
                
                if response.status_code in [200, 202, 204]:
                    self.add_vulnerability(
                        'http_methods',
                        url,
                        'DELETE',
                        "Сервер принимает DELETE-запросы"
                    )
                
                time.sleep(self.delay)
            except Exception as e:
                self.log(f"Ошибка при тестировании DELETE: {e}")
    
    def scan(self):
        print(f"\n[+] Начинаем сканирование {self.target_url}\n")
        
        # Пример параметров для тестирования (в реальном сканере нужно парсить HTML)
        test_params = ['id', 'page', 'search', 'query', 'user', 'file']
        test_forms = [{'action': '', 'fields': ['username', 'password', 'email']}]
        test_paths = ['upload', 'files', 'data', 'api']
        
        self.test_get_requests(test_params)
        self.test_post_requests(test_forms)
        self.test_put_requests(test_paths)
        self.test_delete_requests(test_paths)
        
        print(f"\n[+] Сканирование завершено. Найдено {len(self.vulnerabilities)} уязвимостей.")
        return self.vulnerabilities

def main():
    parser = argparse.ArgumentParser(description = 'Web Vulnerability Scanner')
    parser.add_argument('-u', '--url', required = True, help = 'Target URL to scan')
    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Enable verbose output')
    parser.add_argument('-d', '--delay', type = float, default = 1, help = 'Delay between requests in seconds')
    parser.add_argument('-o', '--output', help = 'Output file to save results')
    
    args = parser.parse_args()
    
    scanner = VulnerabilityScanner(args.url, args.verbose, args.delay)
    vulnerabilities = scanner.scan()
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(vulnerabilities, f, indent = 2)
        print(f"\n[+] Результаты сохранены в {args.output}")

if __name__ == '__main__':
    main()

# ====================================================================================================================

# Парсер веб-страниц с GET-запросами и BeautifulSoup
# Вот Python-скрипт, который использует библиотеки requests и BeautifulSoup для парсинга веб-страниц и извлечения информации из HTML-кода:
# Установите необходимые библиотеки: pip install requests beautifulsoup4
# Запустите скрипт: python web_parser.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_page_content(url):
    """Получает содержимое веб-страницы"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers = headers, timeout = 10)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None

def parse_page(html, url):
    """Анализирует HTML-код страницы и извлекает информацию"""
    if not html:
        return
    
    soup = BeautifulSoup(html, 'html.parser')
    domain = urlparse(url).netloc
    
    print(f"\n{'=' * 50}")
    print(f"Анализ страницы: {url}")
    print(f"{'=' * 50}\n")
    
    # Извлекаем заголовок страницы
    title = soup.title.string if soup.title else "Нет заголовка"
    print(f"Заголовок страницы: {title}\n")
    
    # Извлекаем все ссылки
    print("Ссылки на странице:")
    links = []
    for link in soup.find_all('a', href = True):
        href = link['href']
        if href.startswith('http'):
            links.append(href)
        else:
            links.append(f"https://{domain}{href}")
    
    for i, link in enumerate(links[:10], 1):  # Выводим первые 10 ссылок
        print(f"{i}. {link}")
    print(f"... (всего {len(links)} ссылок)\n")
    
    # Извлекаем основной текст (упрощенный способ)
    print("Основной текст страницы (фрагмент):")
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    print(text[:500] + "..." if len(text) > 500 else text)
    print()
    
    # Извлекаем мета-описание
    meta_desc = soup.find('meta', attrs = {'name': 'description'})
    if meta_desc:
        print(f"Мета-описание: {meta_desc.get('content')}\n")
    
    # Извлекаем изображения
    images = soup.find_all('img')
    if images:
        print("Изображения на странице:")
        for i, img in enumerate(images[:5], 1):  # Выводим первые 5 изображений
            src = img.get('src', 'Нет ссылки')
            alt = img.get('alt', 'Нет описания')
            print(f"{i}. [src] {src} [alt] {alt}")
        print(f"... (всего {len(images)} изображений)\n")

def main():
    print("Веб-парсер с BeautifulSoup")
    print("Введите URL страницы для анализа (например: https://example.com)")
    
    while True:
        url = input("\nURL (или 'q' для выхода): ").strip()
        if url.lower() == 'q':
            break
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        html_content = get_page_content(url)
        parse_page(html_content, url)

if __name__ == "__main__":
    main()

# Парсинг таблиц:
tables = soup.find_all('table')
for table in tables:
    for row in table.find_all('tr'):
        cells = [cell.get_text(strip = True) for cell in row.find_all(['th', 'td'])]
        print(' | '.join(cells))

# Извлечение данных по CSS-классам:
articles = soup.find_all('div', class_ = 'article')
for article in articles:
    title = article.find('h2').get_text()
    print(f"Статья: {title}")

# Сохранение результатов в файл:
import json

data = {
    'title': title,
    'links': links,
    'text': text
}

with open('result.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii = False, indent = 2)

# Обработка динамических страниц (с использованием Selenium):
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# ==============================================================================================================================

# Инструмент для анализа производительности веб-сервера
# Установите необходимые зависимости: pip install requests matplotlib
# Запустите тестирование (примеры):
# Базовый тест (100 запросов, 10 параллельных соединений)
# python benchmark.py http://example.com

# Расширенный тест (500 запросов, 20 параллельных соединений)
# python benchmark.py http://example.com -n 500 -c 20

# Тест с увеличенным таймаутом
# python benchmark.py http://example.com -t 10

import requests
import time
import statistics
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import matplotlib.pyplot as plt

class WebServerBenchmark:
    def __init__(self, url, requests_count = 100, concurrency = 10, timeout = 5):
        self.url = url
        self.requests_count = requests_count
        self.concurrency = concurrency
        self.timeout = timeout
        self.results = []
        self.failed_requests = 0
        
        # Проверяем URL
        if not url.startswith(('http://', 'https://')):
            self.url = 'http://' + url

    def send_request(self, _):
        """Отправляет один GET-запрос и возвращает время ответа"""
        start_time = time.time()
        try:
            response = requests.get(
                self.url,
                timeout = self.timeout,
                headers = {'User-Agent': 'WebServerBenchmark/1.0'}
            )
            response_time = time.time() - start_time
            status_code = response.status_code
            
            if status_code != 200:
                self.failed_requests += 1
                return None
                
            return response_time
        except Exception as e:
            self.failed_requests += 1
            return None

    def run_benchmark(self):
        """Запускает нагрузочное тестирование"""
        print(f"\nЗапуск тестирования производительности для {self.url}")
        print(f"Всего запросов: {self.requests_count}, параллельных соединений: {self.concurrency}\n")
        
        start_test_time = time.time()
        
        with ThreadPoolExecutor(max_workers = self.concurrency) as executor:
            futures = [executor.submit(self.send_request, i) for i in range(self.requests_count)]
            
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    self.results.append(result)
        
        total_time = time.time() - start_test_time
        self.analyze_results(total_time)

    def analyze_results(self, total_time):
        """Анализирует результаты тестирования"""
        if not self.results:
            print("Все запросы завершились ошибкой!")
            return
            
        successful_requests = len(self.results)
        success_rate = (successful_requests / self.requests_count) * 100
        
        print("\nРезультаты тестирования:")
        print(f"  Успешных запросов: {successful_requests}/{self.requests_count} ({success_rate:.2f}%)")
        print(f"  Общее время теста: {total_time:.2f} сек")
        print(f"  Запросов в секунду: {successful_requests / total_time:.2f} req/sec")
        print("\nВремя ответа (в миллисекундах):")
        print(f"  Среднее: {statistics.mean(self.results) * 1000:.2f} мс")
        print(f"  Медиана: {statistics.median(self.results) * 1000:.2f} мс")
        print(f"  Минимальное: {min(self.results) * 1000:.2f} мс")
        print(f"  Максимальное: {max(self.results) * 1000:.2f} мс")
        print(f"  Стандартное отклонение: {statistics.stdev(self.results) * 1000:.2f} мс")
        
        # Построение графика
        self.plot_results()

    def plot_results(self):
        """Строит график времени ответа"""
        plt.figure(figsize = (10, 5))
        plt.plot([x * 1000 for x in self.results], 'b.', alpha = 0.5)
        plt.axhline(y = statistics.mean(self.results) * 1000, color = 'r', linestyle = '-', label = f'Среднее: {statistics.mean(self.results) * 1000:.2f} мс')
        plt.title('Время ответа сервера на GET-запросы')
        plt.xlabel('Номер запроса')
        plt.ylabel('Время ответа (мс)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('response_times.png')
        print("\nГрафик сохранен в файл 'response_times.png'")

def main():
    parser = argparse.ArgumentParser(description = 'Инструмент для анализа производительности веб-сервера')
    parser.add_argument('url', help = 'URL веб-сервера для тестирования')
    parser.add_argument('-n', '--requests', type = int, default = 100, help = 'Количество запросов (по умолчанию: 100)')
    parser.add_argument('-c', '--concurrency', type = int, default = 10, help = 'Количество параллельных соединений (по умолчанию: 10)')
    parser.add_argument('-t', '--timeout', type = int, default = 5, help = 'Таймаут запроса в секундах (по умолчанию: 5)')
    
    args = parser.parse_args()
    
    benchmark = WebServerBenchmark(
        url = args.url,
        requests_count = args.requests,
        concurrency = args.concurrency,
        timeout = args.timeout
    )
    
    benchmark.run_benchmark()

if __name__ == "__main__":
    main()

# Тестирование разных эндпоинтов:
endpoints = ['/', '/api', '/static/image.jpg']
for endpoint in endpoints:
    test_url = f"{args.url.rstrip('/')}/{endpoint.lstrip('/')}"
    benchmark = WebServerBenchmark(test_url, args.requests, args.concurrency)
    benchmark.run_benchmark()

# Генерация отчета в HTML:
def generate_html_report(results):
    with open('report.html', 'w') as f:
        f.write("<html><body>")
        f.write("<h1>Отчет о производительности</h1>")
        for url, stats in results.items():
            f.write(f"<h2>{url}</h2>")
            f.write(f"<p>Успешных запросов: {stats['success_rate']}%</p>")
            f.write(f"<img src='response_times_{url_hash}.png'>")
        f.write("</body></html>")

# Тестирование под нагрузкой с прогресс-баром:
from tqdm import tqdm

# В методе run_benchmark:
with tqdm(total = self.requests_count) as pbar:
    with ThreadPoolExecutor(max_workers = self.concurrency) as executor:
        futures = {executor.submit(self.send_request, i): i for i in range(self.requests_count)}
        for future in as_completed(futures):
            pbar.update(1)

# Поддержка различных типов запросов (POST, PUT и т.д.):
def send_post_request(self, data):
    start_time = time.time()
    try:
        response = requests.post(
            self.url,
            data = data,
            timeout = self.timeout
        )
        return time.time() - start_time
    except:
        return None
    
# ================================================= Анализ заголовков ==========================================================
# Анализ заголовков в контексте НТТР означает изучение и ин­терпретацию метаданных, содержащихся в НТТР-заголовках, 
# которые передаются вместе с НТТР-запросами и ответами меж­ду клиентом и сервером.

# Заголовки НТТР содержат информацию о запросе или ответе, которая помогает управлять и организовывать взаимодействие между клиентом и сервером.

# Существует множество инструментов и библиотек, которые упрощают анализ заголовков НТТР:

# cURL - утилита командной строки для оmравки запросов и получения ответов, которая позволяет легко просматривать заголовки.
# Postman - графический интерфейс для тестирования API, который отображает заголовки запросов и ответов.
# Wireshark - анализатор сетевого трафика, который может перехватывать и анализировать НТТР-запросы и ответы.
# Browser Developer Tools - встроенные инструменты разработчика в бра­узерах (например, Chrome DevTools), 
# которые позволяют просматривать заголовки запросов и ответов в реальном времени.
# Руthоо-библиотеки - requests, http.client, и urllib предоставляют возмож­ности для работы с НТТР-запросами и анализа заголовков.

# Получение заголовков с помощью библиотеки requests
import requests

# Отправляем GЕТ-запрос на указанный URL
response = requests.get("https://api.example.com/data")

# Получаем заголовки ответа
headers = response.headers

# Выводим заголовки на экран
print("Response Headers:")
for header in headers:
    print(header, ":", headers[header])

# ==========================================================================================================================================================

# Программа для отправки GET-запросов и вывода заголовков ответов
# Установите необходимую библиотеку: pip install requests
# Проверьте один URL: python headers_checker.py -u https://example.com
# Проверьте несколько URL из файла (по одному на строке): python headers_checker.py -f urls.txt
# Установите таймаут (по умолчанию 10 секунд): python headers_checker.py -u https://example.com -t 5

import requests
import argparse
from urllib.parse import urlparse
from datetime import datetime

def check_url(url):
    """Проверяет URL и добавляет схему при необходимости"""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'http://' + url
    return url

def get_headers(url, timeout = 10):
    """Отправляет GET-запрос и возвращает заголовки ответа"""
    try:
        response = requests.get(
            url,
            timeout = timeout,
            headers = {'User-Agent': 'HeaderChecker/1.0'}
        )
        return response.headers
    except requests.exceptions.RequestException as e:
        return {'Error': str(e)}

def print_headers(url, headers):
    """Выводит заголовки в удобном формате"""
    print(f"\n{'=' * 50}")
    print(f"Заголовки ответа для: {url}")
    print(f"Время проверки: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'=' * 50}\n")
    
    if 'Error' in headers:
        print(f"Ошибка: {headers['Error']}")
        return
    
    for header, value in headers.items():
        print(f"{header.ljust(25)}: {value}")

def main():
    parser = argparse.ArgumentParser(
        description = 'Инструмент для проверки HTTP-заголовков веб-серверов'
    )
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-u', '--url', help = 'Проверить один URL')
    group.add_argument('-f', '--file', help = 'Файл со списком URL (по одному на строку)')
    parser.add_argument('-t', '--timeout', type = int, default = 10, help = 'Таймаут запроса в секундах (по умолчанию: 10)')
    
    args = parser.parse_args()
    
    urls = []
    
    if args.url:
        urls.append(args.url)
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Ошибка: файл {args.file} не найден")
            return
    
    for raw_url in urls:
        url = check_url(raw_url)
        headers = get_headers(url, args.timeout)
        print_headers(url, headers)

if __name__ == "__main__":
    main()

# Фильтрация заголовков:
# Добавьте этот аргумент в парсер:
parser.add_argument('--filter', help = 'Фильтровать заголовки по ключевому слову')

# И измените функцию print_headers:
if args.filter:
    headers = {k: v for k, v in headers.items() if args.filter.lower() in k.lower()}

# Проверка безопасности:
security_headers = [
    'Strict-Transport-Security',
    'Content-Security-Policy',
    'X-Frame-Options',
    'X-Content-Type-Options',
    'Referrer-Policy'
]

missing_headers = [h for h in security_headers if h not in headers]
if missing_headers:
    print("\nОтсутствуют важные security-заголовки:")
    for h in missing_headers:
        print(f"  - {h}")

# Сохранение результатов в файл:
import json

with open('headers_results.json', 'w') as f:
    json.dump(all_results, f, indent = 2)

# Цветной вывод (с использованием colorama):
from colorama import Fore, init
init()

# В функции print_headers:
if 'Error' in headers:
    print(Fore.RED + f"Ошибка: {headers['Error']}" + Fore.RESET)
else:
    print(Fore.GREEN + "Успешный запрос!" + Fore.RESET)

# ===============================================================================================================================================

# Анализатор HTTP-заголовков на предмет уязвимостей
# Установите необходимые зависимости: pip install requests colorama
# Проверьте один URL: python header_analyzer.py -u https://example.com
# Проверьте несколько URL из файла: python header_analyzer.py -f urls.txt
# Установите таймаут (по умолчанию 10 секунд): python header_analyzer.py -u https://example.com -t 5

import requests
import argparse
from urllib.parse import urlparse
from colorama import Fore, Style, init

# Инициализация colorama для цветного вывода
init()

class HeaderAnalyzer:
    def __init__(self):
        # Определяем опасные заголовки и их безопасные значения
        self.vulnerability_patterns = {
            'Server': {
                'description': 'Раскрытие информации о сервере',
                'severity': 'medium',
                'recommendation': 'Удалите или измените заголовок Server'
            },
            'X-Powered-By': {
                'description': 'Раскрытие информации о технологиях',
                'severity': 'medium',
                'recommendation': 'Удалите заголовок X-Powered-By'
            },
            'Strict-Transport-Security': {
                'description': 'Отсутствие HSTS',
                'severity': 'high',
                'recommendation': 'Добавьте Strict-Transport-Security с max-age',
                'required': True
            },
            'X-XSS-Protection': {
                'description': 'Устаревшая или небезопасная защита XSS',
                'severity': 'high',
                'recommendation': 'Установите X-XSS-Protection: 0 (отключить устаревший фильтр)'
            },
            'X-Content-Type-Options': {
                'description': 'Отсутствие защиты от MIME-sniffing',
                'severity': 'medium',
                'recommendation': 'Добавьте X-Content-Type-Options: nosniff',
                'required': True
            },
            'Content-Security-Policy': {
                'description': 'Отсутствие политики безопасности контента',
                'severity': 'high',
                'recommendation': 'Реализуйте Content-Security-Policy',
                'required': True
            },
            'Access-Control-Allow-Origin': {
                'description': 'Небезопасные настройки CORS',
                'severity': 'high',
                'dangerous_values': ['*'],
                'recommendation': 'Не используйте Access-Control-Allow-Origin: * для конфиденциальных данных'
            },
            'Cache-Control': {
                'description': 'Небезопасное кэширование',
                'severity': 'medium',
                'dangerous_values': ['no-store', 'no-cache'],
                'recommendation': 'Проверьте настройки кэширования для конфиденциальных данных'
            }
        }

    def analyze_headers(self, headers, url):
        """Анализирует заголовки на предмет уязвимостей"""
        print(f"\n{Fore.CYAN}Анализ заголовков для: {url}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
        
        vulnerabilities_found = 0
        
        for header, value in headers.items():
            if header in self.vulnerability_patterns:
                pattern = self.vulnerability_patterns[header]
                
                # Проверяем опасные значения
                if 'dangerous_values' in pattern and value in pattern['dangerous_values']:
                    self._print_vulnerability(
                        header, 
                        f"Небезопасное значение: {value}",
                        pattern['severity'],
                        pattern['description'],
                        pattern['recommendation']
                    )
                    vulnerabilities_found += 1
                else:
                    self._print_safe(header, value)
            else:
                self._print_info(header, value)
        
        # Проверяем отсутствующие обязательные заголовки
        for header, pattern in self.vulnerability_patterns.items():
            if 'required' in pattern and header not in headers:
                self._print_vulnerability(
                    header,
                    "Отсутствует обязательный заголовок безопасности",
                    pattern['severity'],
                    pattern['description'],
                    pattern['recommendation']
                )
                vulnerabilities_found += 1
        
        if vulnerabilities_found == 0:
            print(f"\n{Fore.GREEN}Критических уязвимостей в заголовках не обнаружено!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Обнаружено уязвимостей: {vulnerabilities_found}{Style.RESET_ALL}")

    def _print_vulnerability(self, header, issue, severity, description, recommendation):
        """Выводит информацию об обнаруженной уязвимости"""
        color = Fore.RED if severity == 'high' else Fore.YELLOW
        print(f"\n{color}[!] Уязвимость в заголовке: {header}{Style.RESET_ALL}")
        print(f"{color}    Уровень опасности: {severity.upper()}{Style.RESET_ALL}")
        print(f"    Проблема: {issue}")
        print(f"    Описание: {description}")
        print(f"    Рекомендация: {recommendation}")

    def _print_safe(self, header, value):
        """Выводит информацию о безопасном заголовке"""
        print(f"{Fore.GREEN}[+] {header}: {value}{Style.RESET_ALL}")

    def _print_info(self, header, value):
        """Выводит информацию о стандартном заголовке"""
        print(f"{Fore.BLUE}[*] {header}: {value}{Style.RESET_ALL}")

def get_response_headers(url, timeout = 10):
    """Получает заголовки HTTP-ответа"""
    try:
        # Добавляем схему, если отсутствует
        if not urlparse(url).scheme:
            url = 'http://' + url
        
        response = requests.get(
            url,
            timeout = timeout,
            headers = {'User-Agent': 'SecurityHeaderAnalyzer/1.0'}
        )
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Ошибка при запросе к {url}: {e}{Style.RESET_ALL}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description = 'Анализатор HTTP-заголовков на предмет уязвимостей'
    )
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-u', '--url', help = 'URL для анализа')
    group.add_argument('-f', '--file', help = 'Файл со списком URL (по одному на строке)')
    parser.add_argument('-t', '--timeout', type = int, default = 10, help = 'Таймаут запроса в секундах (по умолчанию: 10)')
    
    args = parser.parse_args()
    
    analyzer = HeaderAnalyzer()
    urls = []
    
    if args.url:
        urls.append(args.url)
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.RED}Ошибка: файл {args.file} не найден{Style.RESET_ALL}")
            return
    
    for url in urls:
        headers = get_response_headers(url, args.timeout)
        if headers:
            analyzer.analyze_headers(headers, url)

if __name__ == "__main__":
    main()

# Проверка cookies на флаги Secure и HttpOnly:
if 'set-cookie' in headers:
    cookies = headers['set-cookie'].split(',')
    for cookie in cookies:
        if 'secure' not in cookie.lower():
            print(f"{Fore.YELLOW}[!] Cookie без флага Secure: {cookie}{Style.RESET_ALL}")
        if 'httponly' not in cookie.lower():
            print(f"{Fore.YELLOW}[!] Cookie без флага HttpOnly: {cookie}{Style.RESET_ALL}")

# Проверка заголовков для API:
api_specific_checks = {
    'X-API-Version': {
        'description': 'Раскрытие версии API',
        'severity': 'low',
        'recommendation': 'Не раскрывайте версию API в заголовках'
    }
}

# Экспорт результатов в JSON:
import json

def save_results(url, vulnerabilities):
    with open('security_report.json', 'w') as f:
        json.dump({
            'url': url,
            'vulnerabilities': vulnerabilities,
            'timestamp': datetime.now().isoformat()
        }, f, indent = 2)

# Поддержка различных методов запросов:
def check_post_headers(url):
    response = requests.post(url, data = {'test': 'value'})
    return response.headers

# ==================================================================================================================================================

# Код: Утилита анализа HTTP-заголовков безопасности
# Для работы потребуется библиотека requests. pip install requests

import requests

# Ключевые заголовки и их значение
RECOMMENDED_HEADERS = {
    "Content-Security-Policy": "Защита от XSS и внедрений",
    "X-Frame-Options": "Защита от clickjacking",
    "X-Content-Type-Options": "Предотвращает MIME-sniffing",
    "Strict-Transport-Security": "Обязательное использование HTTPS",
    "Referrer-Policy": "Ограничение утечки информации реферера",
    "Permissions-Policy": "Ограничение доступа к API браузера",
    "Cache-Control": "Управление кешированием (важно для конфиденциальности)",
    "Cross-Origin-Embedder-Policy": "Управление внедрением ресурсов (COEP)",
    "Cross-Origin-Opener-Policy": "Изоляция контекста (COOP)",
    "Cross-Origin-Resource-Policy": "Контроль доступа к ресурсам (CORP)",
}

def analyze_security_headers(url):
    try:
        response = requests.get(url, timeout = 10)
        headers = response.headers

        print(f"\n🔍 Анализ безопасности заголовков для: {url}\n")
        print("Полученные заголовки:\n")
        for key, value in headers.items():
            print(f"{key}: {value}")
        
        print("\n📋 Результаты анализа:\n")
        missing = []
        for header, description in RECOMMENDED_HEADERS.items():
            if header not in headers:
                print(f"❌ Отсутствует заголовок: {header} — {description}")
                missing.append(header)
            else:
                print(f"✅ Присутствует: {header}")

        if "Set-Cookie" in headers:
            cookie = headers["Set-Cookie"]
            if "HttpOnly" not in cookie or "Secure" not in cookie:
                print("⚠️ Заголовок Set-Cookie не содержит флагов Secure и/или HttpOnly")
        
        if not missing:
            print("\n🎉 Все рекомендуемые заголовки безопасности присутствуют.")
        else:
            print(f"\n⚠️ Обнаружено {len(missing)} проблем(ы). Рекомендуется настроить отсутствующие заголовки.")
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при подключении к сайту: {e}")

# Пример запуска
if __name__ == "__main__":
    target_url = input("Введите URL сайта (например, https://example.com): ").strip()
    analyze_security_headers(target_url)

# ======================================================================================================================================================

# HTTP Server Performance Analyzer
# Установите необходимые зависимости: pip install requests
# Запустите скрипт, указав URL для тестирования: python server_performance.py https://example.com
# Для изменения количества запросов (по умолчанию 10): python server_performance.py https://example.com -n 20

import requests
import time
import statistics
from urllib.parse import urlparse
import argparse

def analyze_server_performance(url, requests_count = 10):
    """
    Анализирует производительность веб-сервера по указанному URL.
    
    Параметры:
        url (str): URL для тестирования
        requests_count (int): Количество запросов для анализа (по умолчанию 10)
    
    Возвращает:
        dict: Словарь с метриками производительности
    """
    response_times = []
    content_sizes = []
    status_codes = []
    server_versions = []
    other_metrics = {
        'keep-alive': [],
        'compression': [],
        'cache': []
    }
    
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    print(f"Testing server performance for: {base_url}")
    print(f"Making {requests_count} requests...\n")
    
    for i in range(requests_count):
        try:
            start_time = time.time()
            response = requests.get(url, headers = {'Accept-Encoding': 'gzip'})
            end_time = time.time()
            
            # Основные метрики
            response_time = (end_time - start_time) * 1000  # в миллисекундах
            response_times.append(response_time)
            content_sizes.append(len(response.content))
            status_codes.append(response.status_code)
            
            # Анализ заголовков
            headers = response.headers
            
            # Server version
            server = headers.get('Server', 'Unknown')
            server_versions.append(server)
            
            # Keep-Alive
            keep_alive = 'keep-alive' in headers.get('Connection', '').lower()
            other_metrics['keep-alive'].append(keep_alive)
            
            # Compression
            encoding = headers.get('Content-Encoding', '').lower()
            compressed = 'gzip' in encoding or 'deflate' in encoding or 'br' in encoding
            other_metrics['compression'].append(compressed)
            
            # Caching
            cache_control = headers.get('Cache-Control', '').lower()
            caching = any(x in cache_control for x in ['max-age', 'public', 'private'])
            other_metrics['cache'].append(caching)
            
            print(f"Request {i + 1}: {response_time:.2f} ms, Size: {len(response.content)} bytes, Status: {response.status_code}")
            
        except requests.exceptions.RequestException as e:
            print(f"Request {i + 1} failed: {str(e)}")
    
    # Статистическая обработка результатов
    if not response_times:
        return None
    
    results = {
        'url': base_url,
        'requests_made': requests_count,
        'successful_requests': len(response_times),
        'response_time': {
            'min': min(response_times),
            'max': max(response_times),
            'avg': statistics.mean(response_times),
            'median': statistics.median(response_times),
            'stdev': statistics.stdev(response_times) if len(response_times) > 1 else 0
        },
        'content_size': {
            'min': min(content_sizes),
            'max': max(content_sizes),
            'avg': statistics.mean(content_sizes),
            'median': statistics.median(content_sizes),
            'total': sum(content_sizes)
        },
        'status_codes': {
            'distribution': {code: status_codes.count(code) for code in set(status_codes)}
        },
        'server': {
            'versions': list(set(server_versions)),
            'most_common': max(set(server_versions), key = server_versions.count)
        },
        'features': {
            'keep_alive_enabled': sum(other_metrics['keep-alive']) / len(other_metrics['keep-alive']),
            'compression_enabled': sum(other_metrics['compression']) / len(other_metrics['compression']),
            'caching_enabled': sum(other_metrics['cache']) / len(other_metrics['cache'])
        }
    }
    
    return results

def print_results(results):
    """Выводит результаты анализа в читаемом формате."""
    if not results:
        print("No results to display.")
        return
    
    print("\n=== Performance Analysis Results ===")
    print(f"Server: {results['url']}")
    print(f"Requests: {results['successful_requests']} successful, {results['requests_made']} total")
    
    print("\nResponse Times (ms):")
    rt = results['response_time']
    print(f"  Min: {rt['min']:.2f}, Max: {rt['max']:.2f}, Avg: {rt['avg']:.2f}")
    print(f"  Median: {rt['median']:.2f}, Std Dev: {rt['stdev']:.2f}")
    
    print("\nContent Size (bytes):")
    cs = results['content_size']
    print(f"  Min: {cs['min']}, Max: {cs['max']}, Avg: {cs['avg']:.1f}")
    print(f"  Median: {cs['median']}, Total: {cs['total']}")
    
    print("\nStatus Codes:")
    for code, count in results['status_codes']['distribution'].items():
        print(f"  {code}: {count} times")
    
    print("\nServer Information:")
    print(f"  Versions detected: {', '.join(results['server']['versions'])}")
    print(f"  Most common: {results['server']['most_common']}")
    
    print("\nFeature Analysis:")
    feats = results['features']
    print(f"  Keep-Alive: {feats['keep_alive_enabled'] * 100:.1f}% of responses")
    print(f"  Compression: {feats['compression_enabled'] * 100:.1f}% of responses")
    print(f"  Caching: {feats['caching_enabled'] * 100:.1f}% of responses")

def main():
    parser = argparse.ArgumentParser(description = 'HTTP Server Performance Analyzer')
    parser.add_argument('url', help = 'URL to test')
    parser.add_argument('-n', '--requests', type = int, default = 10, help = 'Number of requests to make (default: 10)')
    
    args = parser.parse_args()
    
    results = analyze_server_performance(args.url, args.requests)
    print_results(results)

if __name__ == "__main__":
    main()

# ==================================================================================================================================================

# Инструмент для анализа цепочек перенаправлений (HTTP Redirect Analyzer)
# Установите зависимости: pip install requests
# Запустите анализ для конкретного URL: python redirect_analyzer.py https://example.com
# Дополнительные параметры:
# С ограничением количества редиректов
# python redirect_analyzer.py https://example.com --max-redirects 10

# С указанием таймаута
# python redirect_analyzer.py https://example.com --timeout 5

# С пользовательским User-Agent
# python redirect_analyzer.py https://example.com --user-agent "MyBot/1.0"

import requests
from urllib.parse import urlparse
import argparse
from collections import defaultdict

class RedirectAnalyzer:
    def __init__(self, max_redirects = 20, timeout = 10, user_agent = None):
        self.max_redirects = max_redirects
        self.timeout = timeout
        self.user_agent = user_agent or "RedirectAnalyzer/1.0"
        self.visited_urls = defaultdict(int)
        self.redirect_chains = []
        self.problems = []

    def analyze_redirects(self, url):
        """Анализирует цепочку перенаправлений для указанного URL"""
        self.visited_urls.clear()
        self.redirect_chains.clear()
        self.problems.clear()
        
        current_url = url
        session = requests.Session()
        session.max_redirects = 0  # Отключаем автоматические редиректы
        headers = {'User-Agent': self.user_agent}

        try:
            for step in range(self.max_redirects + 1):
                if step == self.max_redirects:
                    self.problems.append(f"Превышено максимальное количество перенаправлений ({self.max_redirects})")
                    break

                # Проверяем, не посещали ли мы этот URL ранее
                self.visited_urls[current_url] += 1
                if self.visited_urls[current_url] > 1:
                    self.problems.append(f"Обнаружен цикл: URL {current_url} встречается {self.visited_urls[current_url]} раз")
                    break

                # Отправляем запрос
                try:
                    response = session.head(
                        current_url,
                        allow_redirects = False,
                        timeout = self.timeout,
                        headers = headers
                    )
                except requests.exceptions.RequestException as e:
                    self.problems.append(f"Ошибка при запросе {current_url}: {str(e)}")
                    break

                # Сохраняем информацию о текущем ответе
                redirect_info = {
                    'url': current_url,
                    'status': response.status_code,
                    'headers': dict(response.headers),
                    'target': None
                }

                # Проверяем, является ли ответ перенаправлением
                if response.is_redirect and 'Location' in response.headers:
                    redirect_info['target'] = response.headers['Location']
                    next_url = self._resolve_relative_url(current_url, redirect_info['target'])
                    
                    # Проверяем потенциальные проблемы
                    self._check_redirect_problems(response.status_code, current_url, next_url)
                    
                    current_url = next_url
                else:
                    # Конец цепочки перенаправлений
                    break

                self.redirect_chains.append(redirect_info)

        except Exception as e:
            self.problems.append(f"Критическая ошибка: {str(e)}")

        return {
            'start_url': url,
            'final_url': current_url,
            'redirect_chain': self.redirect_chains,
            'problems': self.problems,
            'is_cyclic': any("Обнаружен цикл" in p for p in self.problems)
        }

    def _resolve_relative_url(self, base_url, target_url):
        """Преобразует относительный URL в абсолютный"""
        if target_url.startswith(('http://', 'https://')):
            return target_url
        
        base = urlparse(base_url)
        if target_url.startswith('/'):
            return f"{base.scheme}://{base.netloc}{target_url}"
        else:
            path = base.path.rsplit('/', 1)[0] if '/' in base.path else ''
            return f"{base.scheme}://{base.netloc}{path}/{target_url}"

    def _check_redirect_problems(self, status_code, from_url, to_url):
        """Проверяет потенциальные проблемы с перенаправлением"""
        # Проверка на редирект с одинаковыми URL
        if from_url == to_url:
            self.problems.append(f"Редирект на тот же URL: {from_url} -> {to_url}")

        # Проверка нежелательных кодов статуса
        if status_code not in (301, 302, 303, 307, 308):
            self.problems.append(f"Нестандартный код статуса для редиректа: {status_code}")

        # Проверка на редирект с HTTP на HTTPS (это нормально, но отмечаем)
        from_https = from_url.startswith('https://')
        to_https = to_url.startswith('https://')
        if from_https and not to_https:
            self.problems.append(f"Опасный редирект: с HTTPS на HTTP ({from_url} -> {to_url})")

def print_analysis_result(result):
    """Выводит результаты анализа в читаемом формате"""
    print("\n=== Анализ цепочки перенаправлений ===")
    print(f"Начальный URL: {result['start_url']}")
    print(f"Конечный URL: {result['final_url']}")
    print(f"Количество перенаправлений: {len(result['redirect_chain'])}")
    
    if result['is_cyclic']:
        print("\n⚠️ Обнаружена циклическая цепочка перенаправлений!")
    
    if result['problems']:
        print("\n=== Потенциальные проблемы ===")
        for problem in result['problems']:
            print(f"• {problem}")
    
    if result['redirect_chain']:
        print("\n=== Детали перенаправлений ===")
        for i, redirect in enumerate(result['redirect_chain'], 1):
            print(f"\nШаг {i}:")
            print(f"  URL: {redirect['url']}")
            print(f"  Код статуса: {redirect['status']}")
            print(f"  Целевой URL: {redirect['target']}")
            
            # Выводим важные заголовки
            headers = redirect['headers']
            print("  Заголовки:")
            for h in ['Server', 'Date', 'Cache-Control', 'Content-Type']:
                if h in headers:
                    print(f"    {h}: {headers[h]}")
    
    print("\nАнализ завершен.")

def main():
    parser = argparse.ArgumentParser(description = 'Анализатор цепочек HTTP-перенаправлений')
    parser.add_argument('url', help = 'URL для анализа')
    parser.add_argument('--max-redirects', type = int, default = 20, help = 'Максимальное количество перенаправлений для проверки')
    parser.add_argument('--timeout', type = int, default = 10, help = 'Таймаут запроса в секундах')
    parser.add_argument('--user-agent', default = None, help = 'Пользовательский User-Agent для запросов')
    
    args = parser.parse_args()
    
    analyzer = RedirectAnalyzer(
        max_redirects = args.max_redirects,
        timeout = args.timeout,
        user_agent = args.user_agent
    )
    
    result = analyzer.analyze_redirects(args.url)
    print_analysis_result(result)

if __name__ == "__main__":
    main()

# Скрипт: Анализ цепочки перенаправлений
import requests

def analyze_redirects(url):
    try:
        print(f"\n🔍 Анализ перенаправлений для: {url}\n")
        response = requests.get(url, allow_redirects = True, timeout = 10)

        history = response.history
        visited_urls = set()
        has_cycle = False

        if not history:
            print("✅ Нет перенаправлений. Конечный URL:", response.url)
            return

        print("🔗 Обнаружена цепочка редиректов:")
        for i, resp in enumerate(history):
            location = resp.headers.get("Location", "Не указан")
            code = resp.status_code

            if resp.url in visited_urls:
                has_cycle = True
                print(f"🔁 Цикл обнаружен на шаге {i + 1}: {resp.url}")
                break

            visited_urls.add(resp.url)
            print(f"{i + 1}. [{code}] {resp.url} ➡ {location}")

        # Финальный ответ
        final_url = response.url
        print(f"\n🏁 Конечный URL: {final_url}")
        print(f"📦 Статус: {response.status_code}")

        # Доп. проверка: если начальный был https, а в цепочке http — это может быть уязвимость
        initial_scheme = history[0].url.split("://")[0] if history else url.split("://")[0]
        if initial_scheme == "https":
            for hop in history:
                if hop.url.startswith("http://"):
                    print("⚠️ Перенаправление с HTTPS на HTTP! Это может быть небезопасно.")
                    break

        if has_cycle:
            print("❌ Цикл в редиректах обнаружен.")
        else:
            print("✅ Циклов в редиректах не обнаружено.")
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Ошибка при подключении: {e}")

# Точка входа
if __name__ == "__main__":
    target = input("Введите URL сайта (например, https://example.com): ").strip()
    analyze_redirects(target)
