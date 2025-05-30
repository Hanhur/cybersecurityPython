# ================================================================================================================================
# Библиотека requests, с которой мы уже знакомы, в Python предостав­ляет простой и удобный способ отправки НТТР-запросов и работы с веб­-ресурсами. 
# Чаще всего она используется для отправки или принятия данных на сервер и с сервера.
# ======================================================================================================================================

# Для отправки GЕТ-запроса к веб-ресурсу используйте функцию get
# GET
response = requests.get('https://example.com')

# Для отправки РОSТ-запроса с данными используйте функцию post.
# POST
data = { 'key': 'value'}
response = requests.post('https://example.com/post', data = data)

# Пример для получения содержимого ответа
print(response.text)

# В случае возникновения ошибок при отправке запроса, библиотека requests автоматически сгенерирует исключение. 
# Вы можете использовать блок try-except для обработки исключений:

# Обработка ошибок
try:
    response = requests.get('https://example.com')
    response.raise_for_status() # Генерирует исключение, если ответ содержит ошибку
except requests.HTTPError as e:
    print(f' НТТР error occurred: {e} ')
except requests.RequestException as e:
    print(f'Request error occurred: {e} ')

# User Agent
headers = {'User-Agent': 'Mozilla/ 5. О'}
params = {'key': 'value'}
response = requests.get('https://example.com', headers = headers, params = params)


# Сессии
with requests.Session() as session:
    session.auth = ('user', 'pass')
    response = session.get('https://example.com')

# ==============================================================================================================================

# Программа для отправки GET-запросов к открытым API
# становите зависимости: pip install requests

import requests
import json
from pprint import pp

def fetch_api_data(url, params = None, headers = None):
    """
    Отправляет GET-запрос к API и возвращает данные
    
    :param url: URL API-эндпоинта
    :param params: Параметры запроса (словарь)
    :param headers: Заголовки запроса (словарь)
    :return: Ответ от API в формате словаря
    """
    try:
        response = requests.get(
            url,
            params = params or {},
            headers = headers or {'User-Agent': 'API Data Fetcher/1.0'}
        )
        response.raise_for_status()  # Проверка на ошибки HTTP
        
        # Пытаемся распарсить JSON ответ
        try:
            return response.json()
        except json.JSONDecodeError:
            return {'raw_response': response.text}
            
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def display_api_data(data):
    """Выводит данные API в удобном формате"""
    if not data:
        print("Нет данных для отображения")
        return
    
    if 'error' in data:
        print(f"Ошибка: {data['error']}")
        return
    
    print("\nПолученные данные от API:")
    pp(data, indent = 2, width = 80, depth = 3, compact = False, sort_dicts = False)

def get_user_input():
    """Получает параметры API от пользователя"""
    print("Введите данные для запроса к API")
    url = input("URL API (например, https://api.github.com/users/octocat): ").strip()
    
    params = {}
    print("\nВведите параметры запроса (оставьте пустым для завершения):")
    while True:
        key = input("Ключ параметра: ").strip()
        if not key:
            break
        value = input(f"Значение для '{key}': ").strip()
        params[key] = value
    
    headers = {}
    print("\nВведите заголовки запроса (оставьте пустым для завершения):")
    while True:
        key = input("Ключ заголовка: ").strip()
        if not key:
            break
        value = input(f"Значение для '{key}': ").strip()
        headers[key] = value
    
    return url, params, headers

if __name__ == "__main__":
    # Примеры популярных открытых API
    example_apis = {
        '1': {
            'name': 'GitHub User Data',
            'url': 'https://api.github.com/users/{username}',
            'params': {'username': 'octocat'}
        },
        '2': {
            'name': 'Random User Generator',
            'url': 'https://randomuser.me/api/',
            'params': {'results': '3', 'nat': 'us'}
        },
        '3': {
            'name': 'Dog Facts',
            'url': 'https://dog-api.kinduff.com/api/facts',
            'params': {'number': '5'}
        },
        '4': {
            'name': 'NASA APOD',
            'url': 'https://api.nasa.gov/planetary/apod',
            'params': {'api_key': 'DEMO_KEY'}
        },
        '5': {
            'name': 'Custom API',
            'url': '',
            'params': {}
        }
    }
    
    print("Доступные примеры API:")
    for key, api in example_apis.items():
        print(f"{key}. {api['name']}: {api['url']}")
    
    choice = input("\nВыберите API (1-5) или нажмите Enter для ручного ввода: ").strip()
    
    if choice in example_apis:
        api = example_apis[choice]
        if choice == '5':  # Custom API
            url, params, headers = get_user_input()
        else:
            url = api['url']
            params = api['params']
            headers = {}
            
            # Заменяем плейсхолдеры в URL
            if '{username}' in url and 'username' in params:
                url = url.format(username = params.pop('username'))
    else:
        url, params, headers = get_user_input()
    
    print(f"\nОтправляем GET-запрос к: {url}")
    if params:
        print("Параметры:", params)
    if headers:
        print("Заголовки:", headers)
    
    # Отправляем запрос и выводим результат
    api_data = fetch_api_data(url, params, headers)
    display_api_data(api_data)
    
    # Сохраняем результат в файл
    save = input("\nСохранить результат в файл? (y/n): ").lower()
    if save == 'y':
        filename = input("Введите имя файла (без расширения): ").strip() or 'api_response'
        filename = f"{filename}.json"
        
        try:
            with open(filename, 'w', encoding = 'utf-8') as f:
                json.dump(api_data, f, indent = 2, ensure_ascii = False)
            print(f"Результат сохранен в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")


# Поддержку POST-запросов:
response = requests.post(url, json = data)

# Авторизацию:
auth = ('username', 'password')
response = requests.get(url, auth = auth)

# Кэширование запросов:
from cachetools import cached, TTLCache
cache = TTLCache(maxsize = 100, ttl = 300)

@cached(cache)
def fetch_api_data(url):
    # fgbghbtyhetyh

# Асинхронные запросы:
import aiohttp
import asyncio

async def fetch_api_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        
# ===========================================================================================================================================

# Скрипт для отправки POST-запроса с авторизацией
# Установите зависимости: pip install requests

import requests
import json
from getpass import getpass

def send_post_request(url, auth_data, payload = None, headers = None):
    """
    Отправляет POST-запрос с авторизационными данными
    
    :param url: URL сервера
    :param auth_data: словарь с учетными данными
    :param payload: данные для отправки (словарь)
    :param headers: заголовки запроса (словарь)
    :return: ответ сервера в виде словаря
    """
    try:
        # Отправляем POST-запрос
        response = requests.post(
            url,
            data = payload or {},
            headers = headers or {'Content-Type': 'application/x-www-form-urlencoded'},
            auth = (auth_data['username'], auth_data['password']),
            timeout = 10
        )
        
        # Проверяем статус ответа
        response.raise_for_status()
        
        # Пытаемся распарсить JSON ответ
        try:
            return {
                'status': 'success',
                'status_code': response.status_code,
                'data': response.json(),
                'headers': dict(response.headers)
            }
        except json.JSONDecodeError:
            return {
                'status': 'success',
                'status_code': response.status_code,
                'data': response.text,
                'headers': dict(response.headers)
            }
            
    except requests.exceptions.RequestException as e:
        return {
            'status': 'error',
            'message': str(e),
            'status_code': getattr(e.response, 'status_code', None)
        }

def display_response(response):
    """Выводит ответ сервера в читаемом формате"""
    print("\nОтвет сервера:")
    print(f"Статус: {response.get('status')}")
    print(f"Код статуса: {response.get('status_code')}")
    
    if response['status'] == 'success':
        print("\nЗаголовки ответа:")
        for key, value in response.get('headers', {}).items():
            print(f"{key}: {value}")
        
        print("\nТело ответа:")
        if isinstance(response['data'], dict):
            print(json.dumps(response['data'], indent = 2, ensure_ascii = False))
        else:
            print(response['data'])
    else:
        print(f"\nОшибка: {response.get('message')}")

def get_user_credentials():
    """Запрашивает учетные данные у пользователя"""
    print("Введите учетные данные для авторизации")
    username = input("Имя пользователя: ").strip()
    password = getpass("Пароль: ").strip()
    return {'username': username, 'password': password}

def get_request_data():
    """Запрашивает данные для POST-запроса"""
    print("\nВведите данные для отправки (оставьте пустым для завершения):")
    payload = {}
    while True:
        key = input("Ключ: ").strip()
        if not key:
            break
        value = input(f"Значение для '{key}': ").strip()
        payload[key] = value
    return payload

if __name__ == "__main__":
    # Примеры API для тестирования
    example_apis = {
        '1': {
            'name': 'JSONPlaceholder Auth',
            'url': 'https://jsonplaceholder.typicode.com/posts',
            'description': 'Тестовое API (на самом деле не требует авторизации)'
        },
        '2': {
            'name': 'ReqRes.in Login',
            'url': 'https://reqres.in/api/login',
            'description': 'Тестовое API для авторизации (используйте email: "eve.holt@reqres.in", пароль: любой)'
        },
        '3': {
            'name': 'Custom API',
            'url': '',
            'description': 'Введите свой URL API'
        }
    }
    
    print("Доступные примеры API:")
    for key, api in example_apis.items():
        print(f"{key}. {api['name']}: {api['description']}")
    
    choice = input("\nВыберите API (1-3) или нажмите Enter для ручного ввода: ").strip()
    
    if choice in example_apis:
        url = example_apis[choice]['url']
        if choice == '3':
            url = input("Введите URL API: ").strip()
    else:
        url = input("Введите URL API: ").strip()
    
    # Получаем учетные данные
    auth_data = get_user_credentials()
    
    # Получаем данные для отправки
    payload = get_request_data()
    
    # Опциональные заголовки
    headers = {}
    if input("\nДобавить кастомные заголовки? (y/n): ").lower() == 'y':
        print("Введите заголовки (оставьте пустым для завершения):")
        while True:
            key = input("Имя заголовка: ").strip()
            if not key:
                break
            value = input(f"Значение для '{key}': ").strip()
            headers[key] = value
    
    print(f"\nОтправляем POST-запрос на {url}")
    print(f"Используемые данные: {payload}")
    
    # Отправляем запрос и выводим результат
    response = send_post_request(url, auth_data, payload, headers)
    display_response(response)
    
    # Сохраняем результат в файл
    if input("\nСохранить результат в файл? (y/n): ").lower() == 'y':
        filename = input("Введите имя файла (без расширения): ").strip() or 'api_response'
        filename = f"{filename}.json"
        
        try:
            with open(filename, 'w', encoding = 'utf-8') as f:
                json.dump(response, f, indent = 2, ensure_ascii = False)
            print(f"Результат сохранен в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

# Поддержку разных типов авторизации:
# OAuth2
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

# API Key
params = {'api_key': 'YOUR_API_KEY'}

# Поддержку JSON-данных:
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json = payload, headers = headers)

# Повторные попытки при ошибках:
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total = 3, backoff_factor = 1)
session.mount('https://', HTTPAdapter(max_retries = retries))

# Валидацию входных данных:
if not url.startswith(('http://', 'https://')):
    print("URL должен начинаться с http:// или https://")
    exit()

# ===========================================================================================================================================

# Утилита для проверки доступности веб-ресурсов
# Установите зависимости: pip install requests

import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

def check_website(url, timeout = 10):
    """
    Проверяет доступность веб-сайта
    :param url: URL сайта для проверки
    :param timeout: таймаут запроса в секундах
    :return: словарь с результатами проверки
    """
    # Добавляем схему, если отсутствует
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    result = {
        'url': url,
        'status': None,
        'status_code': None,
        'response_time': None,
        'error': None
    }

    try:
        start_time = time.time()
        response = requests.get(
            url,
            timeout = timeout,
            headers = {'User-Agent': 'Website Availability Checker/1.0'},
            allow_redirects = True
        )
        end_time = time.time()

        result['status'] = 'UP' if response.status_code < 400 else 'DOWN'
        result['status_code'] = response.status_code
        result['response_time'] = round((end_time - start_time) * 1000, 2)  # мс
        result['final_url'] = response.url  # после редиректов

    except requests.exceptions.RequestException as e:
        result['status'] = 'DOWN'
        result['error'] = str(e)
    
    return result

def display_results(results):
    """Выводит результаты проверки в табличном формате"""
    print("\nРезультаты проверки:")
    print("{:<40} {:<10} {:<10} {:<10} {:<30}".format(
        "URL", "Статус", "Код", "Время(мс)", "Ошибка/Финальный URL"))
    print("-" * 100)
    
    for result in results:
        error_or_url = result.get('error', result.get('final_url', ''))
        print("{:<40} {:<10} {:<10} {:<10} {:<30}".format(
            result['url'],
            result['status'],
            str(result.get('status_code', 'N/A')),
            str(result.get('response_time', 'N/A')),
            error_or_url[:30] + '...' if len(str(error_or_url)) > 30 else error_or_url
        ))

def save_to_csv(results, filename = "website_status.csv"):
    """Сохраняет результаты в CSV файл"""
    import csv
    
    with open(filename, 'w', newline = '', encoding = 'utf-8') as csvfile:
        fieldnames = ['url', 'status', 'status_code', 'response_time', 'final_url', 'error']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"\nРезультаты сохранены в {filename}")

def get_websites_to_check():
    """Получает список сайтов для проверки"""
    print("Введите сайты для проверки (по одному в строке, пустая строка для завершения):")
    websites = []
    while True:
        url = input().strip()
        if not url:
            break
        websites.append(url)
    
    # Если ничего не введено, используем список по умолчанию
    if not websites:
        websites = [
            'google.com',
            'youtube.com',
            'facebook.com',
            'baidu.com',
            'wikipedia.org',
            'yahoo.com',
            'amazon.com',
            'twitter.com'
        ]
        print(f"\nИспользуем список по умолчанию: {', '.join(websites)}")
    
    return websites

def check_websites_concurrently(websites, max_workers = 5):
    """Проверяет сайты параллельно"""
    results = []
    with ThreadPoolExecutor(max_workers = max_workers) as executor:
        futures = {executor.submit(check_website, url): url for url in websites}
        
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Ошибка при проверке сайта: {e}")
    
    return sorted(results, key = lambda x: x['url'])

if __name__ == "__main__":
    print("=== Утилита проверки доступности веб-ресурсов ===")
    
    # Получаем список сайтов для проверки
    websites = get_websites_to_check()
    
    # Проверяем сайты
    print(f"\nПроверяем {len(websites)} сайтов...")
    results = check_websites_concurrently(websites)
    
    # Выводим результаты
    display_results(results)
    
    # Сохраняем в CSV
    if input("\nСохранить результаты в CSV файл? (y/n): ").lower() == 'y':
        filename = input("Введите имя файла (по умолчанию website_status.csv): ").strip()
        save_to_csv(results, filename or "website_status.csv")
    
    print("\nПроверка завершена.")

# Проверку по расписанию:
import schedule
import time

def job():
    print("Проверка сайтов...")
    results = check_websites_concurrently(websites)
    display_results(results)

schedule.every(1).hour.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# Telegram-уведомления:
import telegram

def send_telegram_alert(message):
    bot = telegram.Bot(token = 'YOUR_BOT_TOKEN')
    bot.send_message(chat_id = 'YOUR_CHAT_ID', text = message)

# Проверку содержимого страницы:
def check_content(response, expected_text):
    return expected_text in response.text

# Цветной вывод:
from colorama import Fore, Style

def colored_status(status):
    return Fore.GREEN + status + Style.RESET_ALL if status == 'UP' else Fore.RED + status + Style.RESET_ALL

# =======================================================================================================================================

# Скрипт для загрузки файлов с веб-сервера
# Установите зависимости: pip install requests

import requests
import os
from urllib.parse import urlparse

def download_file(url, save_path = None, chunk_size = 8192):
    """
    Загружает файл с указанного URL и сохраняет его на диск
    
    :param url: URL файла для загрузки
    :param save_path: Путь для сохранения (None для автоматического определения)
    :param chunk_size: Размер чанков для потоковой загрузки
    :return: Путь к сохраненному файлу
    """
    try:
        # Отправляем GET-запрос с потоковой загрузкой
        with requests.get(url, stream = True) as response:
            response.raise_for_status()  # Проверяем на ошибки
            
            # Определяем имя файла, если не указано
            if save_path is None:
                # Пробуем получить имя файла из URL
                filename = os.path.basename(urlparse(url).path)
                if not filename:
                    # Если не получилось, используем имя из заголовков
                    content_disposition = response.headers.get('content-disposition')
                    if content_disposition:
                        filename = content_disposition.split('filename=')[-1].strip('"\'')
                    else:
                        filename = 'downloaded_file'
                
                save_path = filename
            
            # Создаем директорию, если нужно
            os.makedirs(os.path.dirname(save_path), exist_ok = True)
            
            # Загружаем файл по частям
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size = chunk_size):
                    if chunk:  # фильтруем keep-alive chunks
                        file.write(chunk)
            
            print(f"Файл успешно загружен и сохранен как: {save_path}")
            print(f"Размер файла: {os.path.getsize(save_path) / 1024:.2f} KB")
            return save_path
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def get_user_input():
    """Получает данные от пользователя"""
    print("=== Утилита загрузки файлов ===")
    url = input("Введите URL файла для загрузки: ").strip()
    
    save_path = input("Введите путь для сохранения (оставьте пустым для автоматического определения): ").strip()
    if not save_path:
        save_path = None
    
    return url, save_path

if __name__ == "__main__":
    # Примеры URL для тестирования
    example_files = {
        '1': {
            'url': 'https://speed.hetzner.de/100MB.bin',
            'description': 'Тестовый файл 100MB'
        },
        '2': {
            'url': 'https://www.python.org/static/img/python-logo.png',
            'description': 'Логотип Python'
        },
        '3': {
            'url': '',
            'description': 'Свой URL'
        }
    }
    
    print("Доступные примеры файлов:")
    for key, file in example_files.items():
        print(f"{key}. {file['description']}: {file['url']}")
    
    choice = input("\nВыберите файл (1-3) или нажмите Enter для ручного ввода: ").strip()
    
    if choice in example_files:
        url = example_files[choice]['url']
        if choice == '3':
            url = input("Введите URL файла: ").strip()
    else:
        url, save_path = get_user_input()
    
    if not url:
        print("URL не указан. Завершение работы.")
        exit()
    
    # Загружаем файл
    downloaded_file = download_file(url, save_path)
    
    if downloaded_file:
        print("\nЗагрузка завершена успешно!")
    else:
        print("\nНе удалось загрузить файл.")

# Загрузка с автоматическим именем:
download_file('https://example.com/image.jpg')
# Сохранит как image.jpg в текущей директории

# Загрузка с указанием пути:
download_file('https://example.com/data.zip', 'downloads/data.zip')
# Сохранит как downloads/data.zip

# Загрузка большого файла:
download_file('https://example.com/large_video.mp4', chunk_size = 65536)
# Использует большие чанки для более эффективной загрузки

# Прогресс-бар:
from tqdm import tqdm

# В функции download_file:
total_size = int(response.headers.get('content-length', 0))
progress_bar = tqdm(total = total_size, unit = 'iB', unit_scale = True)

for chunk in response.iter_content(chunk_size = chunk_size):
    if chunk:
        file.write(chunk)
        progress_bar.update(len(chunk))
progress_bar.close()

# Проверку контрольной суммы:
import hashlib

def calculate_checksum(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Многопоточную загрузку:
import threading

def download_chunk(url, start_byte, end_byte, filename):
    headers = {'Range': f'bytes={start_byte}-{end_byte}'}
    response = requests.get(url, headers = headers, stream = True)
    with open(filename, 'r+b') as f:
        f.seek(start_byte)
        f.write(response.content)

# Возобновление загрузки:
if os.path.exists(save_path):
    file_size = os.path.getsize(save_path)
    headers = {'Range': f'bytes={file_size}-'}
else:
    file_size = 0

with requests.get(url, headers = headers, stream = True) as response:
    with open(save_path, 'ab') as file:
        for chunk in response.iter_content(chunk_size = chunk_size):
            if chunk:
                file.write(chunk)

# ==============================================================================================================================

# Приложение для отправки электронной почты через SMTP с использованием Requests

import requests
import json
from getpass import getpass

def send_email_via_api(api_url, api_key, email_data):
    """
    Отправляет email через API почтового сервиса
    
    :param api_url: URL API SMTP-шлюза
    :param api_key: API ключ для аутентификации
    :param email_data: данные письма
    :return: результат отправки
    """
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(
            api_url,
            headers = headers,
            data = json.dumps(email_data),
            timeout = 10
        )
        response.raise_for_status()
        return {'status': 'success', 'response': response.json()}
    except requests.exceptions.RequestException as e:
        return {'status': 'error', 'message': str(e)}

def get_email_data():
    """Запрашивает данные письма у пользователя"""
    print("Введите данные письма:")
    from_email = input("От кого (email): ").strip()
    to_email = input("Кому (email, через запятую если несколько): ").strip()
    subject = input("Тема: ").strip()
    print("Текст письма (введите 'END' на новой строке для завершения):")
    
    body_lines = []
    while True:
        line = input()
        if line == 'END':
            break
        body_lines.append(line)
    
    return {
        'from': from_email,
        'to': [email.strip() for email in to_email.split(',')],
        'subject': subject,
        'body': '\n'.join(body_lines)
    }

if __name__ == "__main__":
    # Пример API URL (замените на реальный)
    API_URL = "https://api.mailservice.example/send"
    
    print("=== Отправка email через SMTP API ===")
    api_key = getpass("Введите ваш API ключ: ")
    
    email_data = get_email_data()
    
    print("\nОтправляем письмо...")
    result = send_email_via_api(API_URL, api_key, email_data)
    
    if result['status'] == 'success':
        print("Письмо успешно отправлено!")
        print("Ответ сервера:", result['response'])
    else:
        print("Ошибка при отправке:", result['message'])

# Вариант 2: Классический способ через smtplib (рекомендуемый)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def send_email_smtp(smtp_server, port, username, password, email_data):
    """
    Отправляет email через SMTP сервер
    
    :param smtp_server: адрес SMTP сервера
    :param port: порт SMTP сервера
    :param username: логин SMTP
    :param password: пароль SMTP
    :param email_data: данные письма
    :return: статус отправки
    """
    try:
        # Создаем сообщение
        msg = MIMEMultipart()
        msg['From'] = email_data['from']
        msg['To'] = ', '.join(email_data['to'])
        msg['Subject'] = email_data['subject']
        
        # Добавляем текст письма
        msg.attach(MIMEText(email_data['body'], 'plain'))
        
        # Подключаемся к серверу и отправляем
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Используем шифрование
            server.login(username, password)
            server.send_message(msg)
        
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def get_smtp_credentials():
    """Запрашивает SMTP-данные у пользователя"""
    print("Введите SMTP данные:")
    smtp_server = input("SMTP сервер (например: smtp.gmail.com): ").strip()
    port = int(input("Порт (например 587 для TLS): ").strip())
    username = input("Логин (email): ").strip()
    password = getpass("Пароль: ")
    return smtp_server, port, username, password

if __name__ == "__main__":
    print("=== Отправка email через SMTP ===")
    
    smtp_server, port, username, password = get_smtp_credentials()
    email_data = get_email_data()  # Используем функцию из первого варианта
    
    print("\nОтправляем письмо...")
    result = send_email_smtp(smtp_server, port, username, password, email_data)
    
    if result['status'] == 'success':
        print("Письмо успешно отправлено!")
    else:
        print("Ошибка при отправке:", result['message'])