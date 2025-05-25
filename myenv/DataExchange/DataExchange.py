# ==================================================================================================================
# В Python для отправки и приема данных используются методы send() и recv(). В случае ТСР-соединения (SOCK_STREAM),
# данные отправляются и получаются в виде последовательности байтов.
# ==================================================================================================================

# Для отправки данных с клиента на сервер используется метод send() клиентского сокета. 
# Этот метод принимает в качестве аргумента байтовую строку данных и отправляет её по сети.

client_socket.send(b'Hello, server!')

# В этом примере строка 'Hello, server!' преобразуется в байтовую строку (b'Hello, seгver!') и отправляется на сервер.

# Для приема данных от сервера на клиент используется метод recv() клиентского сокета. 
# Этот метод принимает количество байтов для чтения и возвращает полученные данные в виде байтовой строки.

data = client_socket.recv(1024)

# Процесс отправки ответа аналогичен отправке данных от клиента к серверу с исполь­ зованием метода seнd() серверного сокета.

server_socket.send(b'Hello, client!')

#Простой сервер для обмена сообщениями
import socket

#Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Привязываем сокет к адресу и порту
server_socket.bind(('localhost', 12345))

#Начинаем прослушивание входящих подключений
server_socket.listen()
print("Cepвep запущен и ожидает подключений...")

# while True:
#     #Принимаем входящее подключение
#     client_socket, client_address = server_socket.accept()
#     print(f"Подключился клиент {client_address}")

#     #Принимаем сообщение от клиента
#     message = client_socket.recv(1024)
#     print("Получено сообщение от клиента:", message.decode())

#     #Отправляем ответ клиенту
#     response = "Сообщение получено!"
#     client_socket.send(response.encode())

#     # Закрываем соединение с клиентом
#     client_socket.close()

#Простой клиент для отправки сообщений
import socket

#Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Подключаемся к серверу
client_socket.connect(('localhost', 12345))

#Отправляем сообщение серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024)
print("Oтвeт от сервера:", response.decode())

# Закрываем соединение
client_socket.close()

# =================================================================================================================

# Программа для отправки и получения файлов между клиентом и сервером.
# Серверная часть (file_server.py)
import socket
import os
import hashlib
from threading import Thread

class FileServer:
    def __init__(self, host = '0.0.0.0', port = 5555, storage_dir = 'received_files'):
        self.host = host
        self.port = port
        self.storage_dir = storage_dir
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Создаем директорию для хранения файлов
        os.makedirs(self.storage_dir, exist_ok = True)
    
    def handle_client(self, conn, addr):
        """Обработка подключения клиента"""
        print(f"[+] Подключен клиент: {addr}")
        
        try:
            # Получаем информацию о файле (имя и размер)
            file_info = conn.recv(1024).decode('utf-8')
            if not file_info:
                return
            
            filename, filesize = file_info.split('|')
            filesize = int(filesize)
            
            # Генерируем уникальное имя файла, если такой уже существует
            save_path = self.get_unique_filename(filename)
            
            # Получаем файл по частям и сохраняем
            received_bytes = 0
            file_hash = hashlib.md5()
            
            with open(save_path, 'wb') as f:
                while received_bytes < filesize:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
                    file_hash.update(data)
                    received_bytes += len(data)
            
            # Проверяем целостность файла
            if received_bytes == filesize:
                response = f"SUCCESS|Файл успешно сохранен как {os.path.basename(save_path)}|{file_hash.hexdigest()}"
                print(f"[+] Файл сохранен: {save_path} ({filesize} bytes, MD5: {file_hash.hexdigest()})")
            else:
                response = "ERROR|Не удалось получить полный файл"
                os.remove(save_path)
                print(f"[-] Ошибка передачи файла {filename}. Получено {received_bytes} из {filesize} байт")
            
            # Отправляем подтверждение клиенту
            conn.sendall(response.encode('utf-8'))
            
        except Exception as e:
            print(f"[-] Ошибка с клиентом {addr}: {e}")
            conn.sendall(f"ERROR|{str(e)}".encode('utf-8'))
        finally:
            conn.close()
            print(f"[+] Соединение с {addr} закрыто")
    
    def get_unique_filename(self, filename):
        """Генерация уникального имени файла"""
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        save_path = os.path.join(self.storage_dir, new_filename)
        
        while os.path.exists(save_path):
            new_filename = f"{base}_{counter}{ext}"
            save_path = os.path.join(self.storage_dir, new_filename)
            counter += 1
            
        return save_path
    
    def start(self):
        """Запуск сервера"""
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"[*] Сервер запущен на {self.host}:{self.port}")
            print(f"[*] Файлы сохраняются в: {os.path.abspath(self.storage_dir)}")
            
            while True:
                conn, addr = self.server_socket.accept()
                client_thread = Thread(target = self.handle_client, args = (conn, addr))
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\n[*] Остановка сервера...")
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server = FileServer()
    server.start()

# Клиентская часть (file_client.py)
import socket
import os
import hashlib

class FileClient:
    def __init__(self, server_host = 'localhost', server_port = 5555):
        self.server_host = server_host
        self.server_port = server_port
    
    def send_file(self, file_path):
        """Отправка файла на сервер"""
        try:
            # Проверяем существование файла
            if not os.path.exists(file_path):
                print(f"[-] Файл не найден: {file_path}")
                return False
            
            # Подключаемся к серверу
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.server_host, self.server_port))
                
                # Получаем информацию о файле
                filename = os.path.basename(file_path)
                filesize = os.path.getsize(file_path)
                
                # Отправляем информацию о файле
                file_info = f"{filename}|{filesize}"
                sock.sendall(file_info.encode('utf-8'))
                
                # Отправляем файл по частям
                file_hash = hashlib.md5()
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(4096)
                        if not data:
                            break
                        sock.sendall(data)
                        file_hash.update(data)
                
                # Получаем ответ от сервера
                response = sock.recv(1024).decode('utf-8')
                
                if response.startswith("SUCCESS"):
                    _, message, server_hash = response.split('|')
                    print(f"[+] {message}")
                    
                    # Проверяем хеш файла
                    if file_hash.hexdigest() == server_hash:
                        print(f"[+] Контрольная сумма MD5 совпадает: {server_hash}")
                        return True
                    else:
                        print("[-] Ошибка: контрольные суммы не совпадают!")
                else:
                    print(f"[-] Ошибка сервера: {response.split('|')[1]}")
                
                return False
                
        except Exception as e:
            print(f"[-] Ошибка при отправке файла: {e}")
            return False

def main():
    print("=== Клиент для отправки файлов ===")
    server_host = input("Введите адрес сервера [localhost]: ") or 'localhost'
    server_port = int(input("Введите порт сервера [5555]: ") or 5555)
    file_path = input("Введите путь к файлу для отправки: ")
    
    client = FileClient(server_host, server_port)
    if client.send_file(file_path):
        print("[+] Файл успешно отправлен и сохранен на сервере!")
    else:
        print("[-] Не удалось отправить файл")

if __name__ == "__main__":
    main()

# ===========================================================================================================================

# Чат-сервер с поддержкой множества клиентов
# Серверная часть (chat_server.py)
import socket
import threading
import time
from datetime import datetime

class ChatServer:
    def __init__(self, host = '0.0.0.0', port = 5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.nicknames = {}
        print(f"🎉 Сервер чата запущен на {host}:{port}")

    def broadcast(self, message, sender = None):
        """Отправка сообщения всем клиентам, кроме отправителя"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_msg = f"[{timestamp}] {message}"
        
        for client in list(self.clients):
            if client != sender:
                try:
                    client.send(formatted_msg.encode('utf-8'))
                except:
                    self.remove_client(client)

    def handle_client(self, client):
        """Обработка подключения клиента"""
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                
                if message.startswith("/nick "):
                    # Смена ника
                    new_nick = message[6:]
                    old_nick = self.nicknames.get(client, "Аноним")
                    self.nicknames[client] = new_nick
                    self.broadcast(f"🌟 {old_nick} сменил ник на {new_nick}")
                    
                elif message == "/quit":
                    # Выход из чата
                    raise Exception("Клиент вышел")
                    
                elif message:
                    # Обычное сообщение
                    nick = self.nicknames.get(client, "Аноним")
                    self.broadcast(f"{nick}: {message}", client)
                    
            except Exception as e:
                print(f"⚠️ Ошибка: {e}")
                self.remove_client(client)
                break

    def remove_client(self, client):
        """Удаление клиента при отключении"""
        if client in self.clients:
            nick = self.nicknames.get(client, "Аноним")
            self.clients.remove(client)
            if client in self.nicknames:
                del self.nicknames[client]
            self.broadcast(f"🚪 {nick} покинул чат")
            client.close()
            print(f"🔌 {nick} отключился")

    def accept_connections(self):
        """Прием новых подключений"""
        while True:
            try:
                client, address = self.server.accept()
                print(f"🔗 Новое подключение от {address}")
                
                # Запрашиваем никнейм
                client.send("Добро пожаловать! Введите ваш ник: ".encode('utf-8'))
                nickname = client.recv(1024).decode('utf-8').strip()
                
                self.clients.append(client)
                self.nicknames[client] = nickname
                
                # Приветствуем нового участника
                welcome_msg = f"🎊 {nickname} присоединился к чату!"
                self.broadcast(welcome_msg)
                client.send(f"Вы подключены как {nickname}".encode('utf-8'))
                
                # Запускаем обработчик клиента
                thread = threading.Thread(target = self.handle_client, args = (client,))
                thread.start()
                
            except Exception as e:
                print(f"⚠️ Ошибка при подключении: {e}")
                break

    def start(self):
        """Запуск сервера"""
        print("Сервер запущен. Ожидание подключений...")
        try:
            self.accept_connections()
        except KeyboardInterrupt:
            print("\n⏹️ Остановка сервера...")
        finally:
            for client in self.clients:
                client.close()
            self.server.close()
            print("Сервер остановлен")

if __name__ == "__main__":
    server = ChatServer()
    server.start()

# Клиентская часть (chat_client.py)
import socket
import threading
import sys

class ChatClient:
    def __init__(self, host = 'localhost', port = 5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = None

    def receive_messages(self):
        """Получение сообщений от сервера"""
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message:
                    print(message)
                else:
                    raise Exception("Соединение разорвано")
            except:
                print("❌ Соединение с сервером потеряно")
                self.client.close()
                break

    def send_messages(self):
        """Отправка сообщений на сервер"""
        try:
            while True:
                message = input()
                if message.lower() == '/quit':
                    self.client.send(message.encode('utf-8'))
                    break
                self.client.send(message.encode('utf-8'))
        except:
            pass
        finally:
            self.client.close()
            print("Выход из чата...")
            sys.exit(0)

    def start(self):
        """Запуск клиента"""
        try:
            self.client.connect((self.host, self.port))
            
            # Получаем приглашение ввести ник
            nickname_prompt = self.client.recv(1024).decode('utf-8')
            print(nickname_prompt, end = '')
            
            self.nickname = input()
            self.client.send(self.nickname.encode('utf-8'))
            
            # Получаем подтверждение подключения
            welcome_msg = self.client.recv(1024).decode('utf-8')
            print(welcome_msg)
            
            print("\nДоступные команды:")
            print("/nick <новый_ник> - сменить никнейм")
            print("/quit - выйти из чата\n")
            
            # Запускаем потоки для получения и отправки сообщений
            receive_thread = threading.Thread(target = self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            send_thread = threading.Thread(target = self.send_messages)
            send_thread.start()
            
            send_thread.join()
            
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            self.client.close()

if __name__ == "__main__":
    print("=== Чат-клиент ===")
    host = input("Введите адрес сервера [localhost]: ") or 'localhost'
    port = int(input("Введите порт сервера [5555]: ") or 5555)
    
    client = ChatClient(host, port)
    client.start()

# ================================================================================================================================

# Программа-сервер для приема НТТР-запросов.
# Серверная часть (http_server.py)
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import mimetypes
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Директория с файлами для сервера
    WEB_ROOT = "www"
    
    def do_GET(self):
        """Обработка GET-запросов"""
        try:
            parsed_path = urlparse(self.path)
            path = parsed_path.path
            query_params = parse_qs(parsed_path.query)
            
            # Логирование запроса
            self.log_request(path, query_params)
            
            # Обработка разных маршрутов
            if path == '/':
                self.serve_homepage()
            elif path == '/time':
                self.serve_current_time()
            elif path == '/echo':
                self.serve_echo(query_params)
            elif os.path.exists(self.get_file_path(path)):
                self.serve_static_file(path)
            else:
                self.send_error(404, "File Not Found")
                
        except Exception as e:
            self.send_error(500, f"Server Error: {str(e)}")
    
    def do_POST(self):
        """Обработка POST-запросов"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            self.log_request(self.path, post_data)
            
            if self.path == '/submit':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success', 'received': post_data}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                self.send_error(404, "Not Found")
                
        except Exception as e:
            self.send_error(500, f"Server Error: {str(e)}")
    
    def serve_homepage(self):
        """Главная страница"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Simple HTTP Server</title>
            </head>
            <body>
                <h1>Welcome to Simple HTTP Server</h1>
                <p>Available endpoints:</p>
                <ul>
                    <li><a href="/time">/time</a> - Current server time</li>
                    <li><a href="/echo?message=hello">/echo?message=hello</a> - Echo service</li>
                    <li><a href="/sample.txt">/sample.txt</a> - Sample text file</li>
                </ul>
                <form action="/submit" method="post">
                    <input type="text" name="data" placeholder="Enter something">
                    <button type="submit">Submit</button>
                </form>
            </body>
            </html>
        """
        self.wfile.write(html.encode('utf-8'))
    
    def serve_current_time(self):
        """Текущее время сервера"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timezone': 'UTC'
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def serve_echo(self, params):
        """Эхо-сервис"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        message = params.get('message', [''])[0]
        response = {
            'echo': message,
            'length': len(message),
            'reversed': message[::-1]
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def serve_static_file(self, path):
        """Обслуживание статических файлов"""
        filepath = self.get_file_path(path)
        mime_type, _ = mimetypes.guess_type(filepath)
        
        self.send_response(200)
        self.send_header('Content-type', mime_type or 'application/octet-stream')
        self.end_headers()
        
        with open(filepath, 'rb') as file:
            self.wfile.write(file.read())
    
    def get_file_path(self, path):
        """Получение полного пути к файлу"""
        return os.path.join(self.WEB_ROOT, path.lstrip('/'))
    
    def log_request(self, path, data = None):
        """Логирование запросов"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_ip = self.client_address[0]
        method = self.command
        
        log_msg = f"[{timestamp}] {client_ip} {method} {path}"
        if data:
            log_msg += f" {data}"
        
        print(log_msg)

def run(server_class = HTTPServer, handler_class = SimpleHTTPRequestHandler, port = 8000):
    """Запуск сервера"""
    # Создаем директорию для файлов, если ее нет
    os.makedirs(handler_class.WEB_ROOT, exist_ok = True)
    
    # Создаем тестовые файлы
    with open(os.path.join(handler_class.WEB_ROOT, 'sample.txt'), 'w') as f:
        f.write("This is a sample text file served by our HTTP server.")
    
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    print(f"Serving files from: {os.path.abspath(handler_class.WEB_ROOT)}")
    print("Available endpoints:")
    print("  /         - Homepage")
    print("  /time     - Current server time")
    print("  /echo     - Echo service (try /echo?message=hello)")
    print("  /sample.txt - Sample text file")
    print("  POST /submit - Form submission endpoint")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

# Использование с библиотекой requests (http_client.py)
import requests

def test_http_server():
    base_url = "http://localhost:8000"
    
    print("Testing HTTP server endpoints:")
    
    try:
        # Главная страница
        print("\n1. Homepage:")
        response = requests.get(base_url)
        print(f"Status: {response.status_code}")
        print(f"Content (first 200 chars):\n{response.text[:200]}...")
        
        # Текущее время
        print("\n2. Current time:")
        response = requests.get(base_url + "/time")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Эхо-сервис
        print("\n3. Echo service:")
        response = requests.get(base_url + "/echo?message=hello")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Статический файл
        print("\n4. Static file:")
        response = requests.get(base_url + "/sample.txt")
        print(f"Status: {response.status_code}")
        print(f"Content: {response.text}")
        
        # POST запрос
        print("\n5. POST request:")
        response = requests.post(base_url + "/submit", data = {"data": "test data"})
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
    except requests.ConnectionError:
        print("Error: Could not connect to the server. Is it running?")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_http_server()

# ==============================================================================================================================

# Клиентская программа для отправки электронной почты с использовани­ем SMTP.
# pip install secure-smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import ssl

def send_email(smtp_server, smtp_port, sender_email, sender_password):
    """Функция для отправки email через SMTP"""
    
    # Запрашиваем данные письма у пользователя
    print("\nВведите данные письма:")
    recipient_email = input("Кому (email получателя): ").strip()
    subject = input("Тема письма: ").strip()
    message_body = input("Текст письма: ").strip()
    
    try:
        # Создаем MIME сообщение
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        
        # Добавляем текст письма
        message.attach(MIMEText(message_body, "plain"))
        
        # Создаем безопасное соединение с SMTP сервером
        context = ssl.create_default_context()
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context = context)  # Включаем шифрование
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        print("\n✅ Письмо успешно отправлено!")
    
    except smtplib.SMTPAuthenticationError:
        print("\n❌ Ошибка аутентификации. Проверьте логин и пароль.")
    except smtplib.SMTPException as e:
        print(f"\n❌ Ошибка при отправке письма: {e}")
    except Exception as e:
        print(f"\n❌ Произошла непредвиденная ошибка: {e}")

def main():
    print("=== SMTP Email Client ===")
    print("Настройки SMTP сервера (пример для Gmail):")
    
    # Настройки SMTP (можно изменить для других почтовых сервисов)
    smtp_server = input("SMTP сервер [smtp.gmail.com]: ") or "smtp.gmail.com"
    smtp_port = int(input("SMTP порт [587]: ") or 587)
    
    # Данные отправителя
    sender_email = input("Ваш email: ").strip()
    sender_password = getpass.getpass("Пароль (не отображается): ")
    
    while True:
        send_email(smtp_server, smtp_port, sender_email, sender_password)
        
        if input("\nОтправить еще одно письмо? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()

# ==============================================================================================================================

# Сервер для игры "Морской бой"
import socket
import threading
import random
import json
from time import sleep

class BattleshipServer:
    def __init__(self, host = '0.0.0.0', port = 5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.players = {}
        self.games = {}
        self.player_queue = []
        print(f"⚓ Сервер Морского боя запущен на {host}:{port}")

    def handle_client(self, conn, addr):
        """Обработка подключения клиента"""
        try:
            # Регистрация игрока
            player_id = len(self.players) + 1
            self.players[player_id] = {
                'conn': conn,
                'addr': addr,
                'ready': False,
                'board': None,
                'game_id': None
            }
            print(f"🎮 Подключен игрок {player_id} с адреса {addr}")

            conn.send(f"PLAYER_ID|{player_id}".encode('utf-8'))

            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                self.process_message(player_id, data)

        except Exception as e:
            print(f"⚠️ Ошибка с игроком {player_id}: {e}")
        finally:
            self.remove_player(player_id)
            conn.close()

    def process_message(self, player_id, message):
        """Обработка сообщений от клиента"""
        parts = message.split('|')
        cmd = parts[0]

        if cmd == 'READY':
            # Игрок готов к игре (отправил свою расстановку кораблей)
            board = json.loads(parts[1])
            self.players[player_id]['board'] = board
            self.players[player_id]['ready'] = True
            print(f"🛟 Игрок {player_id} готов к игре")
            self.add_to_queue(player_id)

        elif cmd == 'FIRE':
            # Игрок сделал выстрел
            if self.players[player_id]['game_id'] is None:
                return

            game_id = self.players[player_id]['game_id']
            x, y = map(int, parts[1:])
            self.process_shot(game_id, player_id, x, y)

    def add_to_queue(self, player_id):
        """Добавление игрока в очередь для поиска соперника"""
        if player_id not in self.player_queue:
            self.player_queue.append(player_id)

        # Если в очереди есть хотя бы 2 игрока, создаем игру
        if len(self.player_queue) >= 2:
            player1 = self.player_queue.pop(0)
            player2 = self.player_queue.pop(0)
            self.create_game(player1, player2)

    def create_game(self, player1_id, player2_id):
        """Создание новой игры"""
        game_id = len(self.games) + 1
        self.games[game_id] = {
            'players': [player1_id, player2_id],
            'current_turn': random.choice([player1_id, player2_id]),
            'boards': {
                player1_id: self.players[player1_id]['board'],
                player2_id: self.players[player2_id]['board']
            },
            'hits': {
                player1_id: set(),
                player2_id: set()
            },
            'sunk_ships': {
                player1_id: 0,
                player2_id: 0
            }
        }

        # Назначаем игру игрокам
        self.players[player1_id]['game_id'] = game_id
        self.players[player2_id]['game_id'] = game_id

        # Уведомляем игроков о начале игры
        self.send_message(player1_id, f"GAME_START|{player2_id}|SECOND")
        self.send_message(player2_id, f"GAME_START|{player1_id}|FIRST")

        # Сообщаем, чей первый ход
        current_player = self.games[game_id]['current_turn']
        self.send_message(current_player, "YOUR_TURN")
        print(f"🎲 Начата игра #{game_id} между игроками {player1_id} и {player2_id}")

    def process_shot(self, game_id, shooter_id, x, y):
        """Обработка выстрела игрока"""
        game = self.games.get(game_id)
        if not game:
            return

        # Проверяем, чей сейчас ход
        if shooter_id != game['current_turn']:
            self.send_message(shooter_id, "NOT_YOUR_TURN")
            return

        # Определяем соперника
        opponent_id = game['players'][0] if shooter_id == game['players'][1] else game['players'][1]
        opponent_board = game['boards'][opponent_id]

        # Проверяем попадание
        hit = opponent_board[y][x] == 1
        game['hits'][shooter_id].add((x, y))

        # Проверяем потопление корабля
        sunk = False
        if hit:
            sunk = self.check_sunk_ship(opponent_board, x, y, game['hits'][shooter_id])
            if sunk:
                game['sunk_ships'][shooter_id] += 1

        # Отправляем результат выстрела стрелявшему
        self.send_message(shooter_id, f"SHOT_RESULT|{x}|{y}|{'HIT' if hit else 'MISS'}|{'SUNK' if sunk else ''}")

        # Отправляем результат выстрела сопернику
        self.send_message(opponent_id, f"OPPONENT_SHOT|{x}|{y}|{'HIT' if hit else 'MISS'}|{'SUNK' if sunk else ''}")

        # Проверяем условие победы
        if self.check_win_condition(game_id, shooter_id):
            self.send_message(shooter_id, "YOU_WIN")
            self.send_message(opponent_id, "YOU_LOSE")
            print(f"🏆 Игра #{game_id} завершена. Победитель: {shooter_id}")
            self.end_game(game_id)
            return

        # Передаем ход другому игроку
        game['current_turn'] = opponent_id
        self.send_message(opponent_id, "YOUR_TURN")

    def check_sunk_ship(self, board, x, y, hits):
        """Проверка, был ли потоплен корабль"""
        # Простая реализация - проверяем все клетки вокруг
        # В реальной игре нужно анализировать весь корабль
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if board[ny][nx] == 1 and (nx, ny) not in hits:
                    return False
        return True

    def check_win_condition(self, game_id, player_id):
        """Проверка условия победы"""
        game = self.games[game_id]
        opponent_id = game['players'][0] if player_id == game['players'][1] else game['players'][1]
        
        # Подсчитываем количество попаданий по кораблям противника
        hits_on_opponent = sum(1 for y in range(10) for x in range(10) 
                             if game['boards'][opponent_id][y][x] == 1 and (x, y) in game['hits'][player_id])
        
        # Все корабли противника потоплены (17 клеток - сумма всех кораблей)
        return hits_on_opponent == 17

    def send_message(self, player_id, message):
        """Отправка сообщения игроку"""
        try:
            self.players[player_id]['conn'].send(message.encode('utf-8'))
        except:
            self.remove_player(player_id)

    def remove_player(self, player_id):
        """Удаление игрока"""
        if player_id in self.players:
            game_id = self.players[player_id]['game_id']
            if game_id and game_id in self.games:
                # Уведомляем соперника о дисконнекте
                players = self.games[game_id]['players']
                opponent_id = players[0] if player_id == players[1] else players[1]
                if opponent_id in self.players:
                    self.send_message(opponent_id, "OPPONENT_DISCONNECTED")
                del self.games[game_id]
            
            if player_id in self.player_queue:
                self.player_queue.remove(player_id)
            
            print(f"🚪 Игрок {player_id} отключился")
            del self.players[player_id]

    def start(self):
        """Запуск сервера"""
        try:
            while True:
                conn, addr = self.server.accept()
                thread = threading.Thread(target = self.handle_client, args = (conn, addr))
                thread.start()
        except KeyboardInterrupt:
            print("\n🛑 Остановка сервера...")
        finally:
            self.server.close()

if __name__ == "__main__":
    server = BattleshipServer()
    server.start()

# Клиентская часть (battleship_client.py)
import socket
import json
import random
from threading import Thread

class BattleshipClient:
    def __init__(self, host = 'localhost', port = 5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player_id = None
        self.opponent_id = None
        self.my_turn = False
        self.my_board = [[0 for _ in range(10)] for _ in range(10)]
        self.opponent_board = [[0 for _ in range(10)] for _ in range(10)]
        self.ships = [
            (4, 1),  # 1 корабль на 4 клетки
            (3, 2),  # 2 корабля на 3 клетки
            (2, 3),  # 3 корабля на 2 клетки
            (1, 4)   # 4 корабля на 1 клетку
        ]

    def connect(self):
        """Подключение к серверу"""
        self.client.connect((self.host, self.port))
        
        # Получаем ID игрока
        data = self.client.recv(1024).decode('utf-8')
        if data.startswith('PLAYER_ID'):
            self.player_id = int(data.split('|')[1])
            print(f"Вы подключены как игрок {self.player_id}")
        
        # Запускаем поток для получения сообщений
        receive_thread = Thread(target = self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def receive_messages(self):
        """Получение сообщений от сервера"""
        while True:
            try:
                data = self.client.recv(1024).decode('utf-8')
                if not data:
                    break

                self.process_server_message(data)
            except:
                print("Соединение с сервером потеряно")
                break

    def process_server_message(self, message):
        """Обработка сообщений от сервера"""
        parts = message.split('|')
        cmd = parts[0]

        if cmd == 'GAME_START':
            self.opponent_id = int(parts[1])
            print(f"\n🎮 Начинаем игру против игрока {self.opponent_id}!")
            if parts[2] == 'FIRST':
                self.my_turn = True
                print("Ваш ход первый!")

        elif cmd == 'YOUR_TURN':
            self.my_turn = True
            print("\nВаш ход! Введите координаты выстрела (x y):")

        elif cmd == 'NOT_YOUR_TURN':
            print("Сейчас не ваш ход!")

        elif cmd == 'SHOT_RESULT':
            x, y = int(parts[1]), int(parts[2])
            result = parts[3]
            sunk = len(parts) > 4 and parts[4] == 'SUNK'
            
            if result == 'HIT':
                self.opponent_board[y][x] = 2  # 2 - попадание
                print(f"\nВы попали в ({x}, {y})!")
                if sunk:
                    print("Вы потопили корабль противника!")
            else:
                self.opponent_board[y][x] = 3  # 3 - промах
                print(f"\nВы промахнулись в ({x}, {y})")

        elif cmd == 'OPPONENT_SHOT':
            x, y = int(parts[1]), int(parts[2])
            result = parts[3]
            sunk = len(parts) > 4 and parts[4] == 'SUNK'
            
            if result == 'HIT':
                self.my_board[y][x] = 2  # 2 - попадание
                print(f"\nПротивник попал в ({x}, {y})!")
                if sunk:
                    print("Противник потопил ваш корабль!")
            else:
                print(f"\nПротивник промахнулся в ({x}, {y})")

        elif cmd == 'YOU_WIN':
            print("\n🎉 Поздравляем! Вы выиграли!")
            self.my_turn = False

        elif cmd == 'YOU_LOSE':
            print("\n😢 К сожалению, вы проиграли.")
            self.my_turn = False

        elif cmd == 'OPPONENT_DISCONNECTED':
            print("\nПротивник отключился. Игра завершена.")
            self.my_turn = False

    def send_ready(self):
        """Отправка серверу готовности к игре"""
        self.setup_ships()
        board_json = json.dumps(self.my_board)
        self.client.send(f"READY|{board_json}".encode('utf-8'))
        print("Расстановка кораблей завершена. Ожидаем соперника...")

    def setup_ships(self):
        """Автоматическая расстановка кораблей"""
        for ship_size, ship_count in self.ships:
            for _ in range(ship_count):
                placed = False
                while not placed:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    direction = random.choice(['horizontal', 'vertical'])
                    
                    if self.can_place_ship(x, y, ship_size, direction):
                        self.place_ship(x, y, ship_size, direction)
                        placed = True

    def can_place_ship(self, x, y, size, direction):
        """Проверка возможности размещения корабля"""
        if direction == 'horizontal':
            if x + size > 10:
                return False
            for i in range(size):
                if self.my_board[y][x + i] != 0:
                    return False
        else:  # vertical
            if y + size > 10:
                return False
            for i in range(size):
                if self.my_board[y + i][x] != 0:
                    return False
        return True

    def place_ship(self, x, y, size, direction):
        """Размещение корабля на доске"""
        if direction == 'horizontal':
            for i in range(size):
                self.my_board[y][x + i] = 1
        else:  # vertical
            for i in range(size):
                self.my_board[y + i][x] = 1

    def fire(self, x, y):
        """Отправка выстрела на сервер"""
        if not self.my_turn:
            print("Сейчас не ваш ход!")
            return False

        if not (0 <= x < 10 and 0 <= y < 10):
            print("Координаты должны быть от 0 до 9")
            return False

        if self.opponent_board[y][x] in [2, 3]:
            print("Вы уже стреляли в эту клетку")
            return False

        self.client.send(f"FIRE|{x}|{y}".encode('utf-8'))
        self.my_turn = False
        return True

    def start(self):
        """Запуск клиента"""
        print("=== Морской бой ===")
        host = input("Введите адрес сервера [localhost]: ") or 'localhost'
        port = int(input("Введите порт сервера [5555]: ") or 5555)

        self.host = host
        self.port = port

        try:
            self.connect()
            input("Нажмите Enter для автоматической расстановки кораблей...")
            self.send_ready()

            while True:
                if self.my_turn:
                    try:
                        coords = input("Введите координаты (x y): ").split()
                        if len(coords) == 2:
                            x, y = map(int, coords)
                            self.fire(x, y)
                    except ValueError:
                        print("Пожалуйста, введите два числа от 0 до 9")
                else:
                    sleep(0.5)  # Небольшая задержка для экономии CPU

        except KeyboardInterrupt:
            print("\nВыход из игры...")
        finally:
            self.client.close()

if __name__ == "__main__":
    client = BattleshipClient()
    client.start()