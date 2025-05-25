# ===============================================================================
# Для создания сокета вызывается функция socket() из модуля socket. 
# Эта функция принимает два основных аргумента: семейство адресов и тип сокета.
# ===============================================================================

# Семейство адресов (Address Family)
# socket.AF lNET - используется для создания сокета для сетевого (IPv4) соединения.
# socket.AF_ lNETб- используется для создания сокета для IРvб-соединения.

# Тип сокета (Socket Туре)
# socket.SOCK_STREAM - используется для создания ТСР-сокетов, кото­рые обеспечивают надежное соединение, 
# где данные передаются в пра­вильном порядке.

# socket.SOCK_DGRAM - используется для создания UDР-сокетов, кото­рые отправляют данные без установки 
# соединения и не гарантируют их порядок, но обеспечивают более быструю передачу.

# Для создания серверного сокета для ТСР-соединения, используйте socket.socket с аргументами socket.AF_INET и socket.SOCK_STREAM. 
# Это создаст сокет, который будет ожидать подключения клиентов через протокол ТСР:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Для создания клиентского сокета для UDР-соединения используйте socket.socket с аргументами socket.AF_INET и socket.SOCK_DGRAM. 
# Это создаст сокет, который будет отправлять и получать данные через протокол UDP:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Если вы создаете серверный сокет, следующим шагом будет привязка со­кета к конкретному адресу и порту на вашем компьютере.
server_socket.bind(('localhost', 8080))

# В этом примере сокет привязывается к локальному адресу 'locaihost' и порту 8080.
# Если вы создаете клиентский сокет, следующим шагом будет установка соединения с сервером с указанием его адреса и порта.
client_socket.connect(('localhost', 8080))

# Это можно сделать с помощью метода setsockopt(). Пример установки тай­маута для сокета:
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_TIMEOUT, 5)

# По завершении работы с сокетами они должны быть закрыты с помощью метода close(). 
# Это освободит ресурсы, занятые сокетом, и закроет соединение.
server_socket.close()
client_socket.close()

#Пример.простого серверного приложения
import socket

#Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Связываем сокет с адресом и портом
server_socket.bind( ('localhost', 12345))

# Начинаем прослушивание входящих подключений
server_socket.listen()

print("Cepвep запущен и ожидает подключений...")

# while True:
#     #Принимаем входящее подключение
#     client_socket, client_address = server_socket.accept()
#     print(f"Подключился клиент {client_address}")

#     #Принимаем данные от клиента
#     data = client_socket.recv(1024)
#     print("Получены данные от клиента:", data.decode())

#     # Отправляем ответ клиенту
#     response = "Сообщение получено!"
#     client_socket.send(response.encode())

#     # Закрываем соединение с клиентом
#     client_socket.close()


#Пример простого клиентского приложения
import socket

#Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Подключаемся к серверу
client_socket.connect(('localhost', 12345))

# Отправляем данные серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024)
print("Oтвeт от сервера:", response.decode())

# Закрываем соединение
client_socket.close()

# =============================================================================================================================

# Простой клиент-серверный чат на Python
# Серверная часть (chat_server.py)
import socket
import threading

clients = []  # Список подключенных клиентов

def broadcast(message, sender = None):
    """Отправка сообщения всем клиентам"""
    for client in clients:
        if client != sender:  # Не отправляем отправителю его же сообщение
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

def handle_client(client_socket, address):
    """Обработка подключения клиента"""
    try:
        print(f"Новое подключение: {address}")
        clients.append(client_socket)
        
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
                
            print(f"{address}: {message}")
            broadcast(f"{address}: {message}", client_socket)
            
    except Exception as e:
        print(f"Ошибка с клиентом {address}: {e}")
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()
        print(f"Клиент {address} отключен")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Сервер чата запущен на порту 12345...")
    
    try:
        while True:
            client_socket, address = server.accept()
            client_thread = threading.Thread(
                target = handle_client, 
                args = (client_socket, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Остановка сервера...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()

# Клиентская часть (chat_client.py)
import socket
import threading

def receive_messages(client_socket):
    """Получение сообщений от сервера"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Соединение с сервером потеряно!")
            client_socket.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    
    # Поток для получения сообщений
    receive_thread = threading.Thread(
        target=receive_messages, 
        args=(client,))
    receive_thread.start()
    
    print("Подключение к чату установлено. Вводите сообщения:")
    
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            client.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        client.close()
        print("Отключение от чата...")

if __name__ == "__main__":
    start_client()

# =========================================================================================================

# Файловый сервер и клиент для передачи файлов
# Серверная часть (file_server.py)
import socket
import os
import hashlib

def save_file(connection, file_info):
    try:
        filename, filesize = file_info.split('|')
        filesize = int(filesize)
        
        # Создаем папку для сохранения файлов, если ее нет
        if not os.path.exists('received_files'):
            os.makedirs('received_files')
        
        # Генерируем уникальное имя файла, если он уже существует
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(f'received_files/{new_filename}'):
            new_filename = f"{base}_{counter}{ext}"
            counter += 1
        
        filepath = os.path.join('received_files', new_filename)
        
        # Получаем файл по частям и сохраняем
        received = 0
        with open(filepath, 'wb') as file:
            while received < filesize:
                data = connection.recv(4096)
                if not data:
                    break
                file.write(data)
                received += len(data)
        
        # Проверяем целостность файла
        if received == filesize:
            # Вычисляем хеш полученного файла
            with open(filepath, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()
            
            connection.sendall(f"SUCCESS|{new_filename}|{file_hash}".encode())
            print(f"Файл {new_filename} ({filesize} bytes) успешно сохранен. MD5: {file_hash}")
        else:
            os.remove(filepath)
            connection.sendall(b"ERROR|File transfer incomplete")
            print(f"Ошибка передачи файла {filename}. Получено {received} из {filesize} байт")
            
    except Exception as e:
        connection.sendall(f"ERROR|{str(e)}".encode())
        print(f"Ошибка при сохранении файла: {e}")

def start_file_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Файловый сервер запущен. Ожидание подключений...")
    
    try:
        while True:
            connection, address = server_socket.accept()
            print(f"\nПодключен клиент: {address}")
            
            try:
                # Получаем информацию о файле (имя и размер)
                file_info = connection.recv(1024).decode()
                if not file_info:
                    continue
                
                print(f"Получение файла: {file_info.split('|')[0]}")
                save_file(connection, file_info)
                
            except Exception as e:
                print(f"Ошибка при работе с клиентом {address}: {e}")
            finally:
                connection.close()
                print(f"Соединение с {address} закрыто")
                
    except KeyboardInterrupt:
        print("\nОстановка сервера...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_file_server()

# Клиентская часть (file_client.py)
import socket
import os
import hashlib

def send_file(client_socket, filepath):
    try:
        # Получаем информацию о файле
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        
        # Отправляем информацию о файле (имя и размер)
        file_info = f"{filename}|{filesize}"
        client_socket.send(file_info.encode())
        
        # Отправляем файл по частям
        with open(filepath, 'rb') as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                client_socket.sendall(data)
        
        # Получаем ответ от сервера
        response = client_socket.recv(1024).decode()
        if response.startswith("SUCCESS"):
            _, saved_name, file_hash = response.split('|')
            
            # Проверяем хеш отправленного файла
            with open(filepath, 'rb') as file:
                local_hash = hashlib.md5(file.read()).hexdigest()
            
            if local_hash == file_hash:
                print(f"Файл успешно сохранен на сервере как: {saved_name}")
                print(f"MD5 хеш совпадает: {file_hash}")
            else:
                print("Ошибка: хеш файла не совпадает!")
        else:
            print(f"Ошибка сервера: {response}")
            
    except Exception as e:
        print(f"Ошибка при отправке файла: {e}")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    try:
        filepath = input("Введите путь к файлу для отправки: ")
        if not os.path.exists(filepath):
            print("Файл не найден!")
            return
        
        print(f"Отправка файла: {filepath}")
        send_file(client_socket, filepath)
        
    except KeyboardInterrupt:
        print("\nОтмена передачи...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()

# ================================================================================================================================

# Программа для сканирования портов на удаленном хосте
import socket
import concurrent.futures
from datetime import datetime

def scan_port(ip, port, timeout=1):
    """Проверяет, открыт ли указанный порт"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                return port
    except:
        pass
    return None

def port_scanner():
    print("=== Сканер портов ===")
    target = input("Введите IP-адрес или доменное имя: ")
    start_port = int(input("Введите начальный порт: "))
    end_port = int(input("Введите конечный порт: "))
    
    # Проверка корректности диапазона портов
    if start_port > end_port:
        start_port, end_port = end_port, start_port
    
    # Проверка допустимости значений портов
    if start_port < 1 or end_port > 65535:
        print("Ошибка: порты должны быть в диапазоне 1-65535")
        return
    
    print(f"\nСканирование {target} с порта {start_port} до {end_port}...")
    start_time = datetime.now()
    open_ports = []
    
    # Используем ThreadPoolExecutor для параллельного сканирования
    with concurrent.futures.ThreadPoolExecutor(max_workers = 100) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in range(start_port, end_port + 1)}
        
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                result = future.result()
                if result is not None:
                    open_ports.append(result)
                    print(f"Порт {result} открыт")
            except Exception as e:
                print(f"Ошибка при сканировании порта {port}: {e}")
    
    # Выводим результаты
    duration = datetime.now() - start_time
    print(f"\nСканирование завершено за {duration.total_seconds():.2f} секунд")
    print(f"Открытые порты: {sorted(open_ports)}")

if __name__ == "__main__":
    port_scanner()

# ======================================================================================================================================

# Простой HTTP-сервер на Python
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class SimpleWebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка GET-запросов"""
        # Определяем путь запроса
        if self.path == "/":
            self.path = "/index.html"
        
        try:
            # Отправляем ответ 200 OK
            self.send_response(200)
            
            # Устанавливаем заголовки
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Формируем содержимое страницы
            content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Simple Python Web Server</title>
            </head>
            <body>
                <h1>Welcome to Simple Web Server</h1>
                <p>Current time: {time.strftime("%Y-%m-%d %H:%M:%S")}</p>
                <p>Request path: {self.path}</p>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </body>
            </html>
            """.encode("utf-8")
            
            # Отправляем содержимое
            self.wfile.write(content)
            
        except Exception as e:
            self.send_error(404, f"Error: {str(e)}")

def run_server():
    """Запуск сервера"""
    host = "localhost"
    port = 8080
    server = HTTPServer((host, port), SimpleWebServer)
    
    print(f"Server started at http://{host}:{port}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    print("Server stopped")

if __name__ == "__main__":
    run_server()

# Пример ответа сервера:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Simple Python Web Server</title>
# </head>
# <body>
#     <h1>Welcome to Simple Web Server</h1>
#     <p>Current time: 2023-05-15 14:30:45</p>
#     <p>Request path: /about</p>
#     <ul>
#         <li><a href="/">Home</a></li>
#         <li><a href="/about">About</a></li>
#         <li><a href="/contact">Contact</a></li>
#     </ul>
# </body>
# </html>

# ==========================================================================================================================

# SMTP-клиент для отправки электронной почты с использованием сокетов
import socket
import base64
import ssl
from getpass import getpass

class SMTPClient:
    def __init__(self, server, port, use_tls = True):
        self.server = server
        self.port = port
        self.use_tls = use_tls
        self.socket = None
        self.connection = None

    def connect(self):
        """Установка соединения с SMTP-сервером"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))
        self.connection = self.socket.makefile('rb')
        
        # Получаем приветственное сообщение от сервера
        response = self._get_response()
        print(f"Сервер: {response}")
        
        # Отправляем EHLO
        self._send_command(f"EHLO {socket.gethostname()}")
        
        if self.use_tls:
            # Запускаем TLS
            self._send_command("STARTTLS")
            context = ssl.create_default_context()
            self.socket = context.wrap_socket(self.socket, server_hostname = self.server)
            self.connection = self.socket.makefile('rb')
            
            # Повторно отправляем EHLO после STARTTLS
            self._send_command(f"EHLO {socket.gethostname()}")

    def login(self, username, password):
        """Аутентификация на SMTP-сервере"""
        self._send_command("AUTH LOGIN")
        self._send_command(base64.b64encode(username.encode()).decode())
        self._send_command(base64.b64encode(password.encode()).decode())

    def send_email(self, from_addr, to_addrs, subject, body):
        """Отправка письма"""
        # Начинаем транзакцию
        self._send_command(f"MAIL FROM: <{from_addr}>")
        
        # Указываем получателей
        if isinstance(to_addrs, str):
            to_addrs = [to_addrs]
        for addr in to_addrs:
            self._send_command(f"RCPT TO: <{addr}>")
        
        # Отправляем данные письма
        self._send_command("DATA")
        
        # Формируем заголовки письма
        message = f"From: {from_addr}\r\n"
        message += f"To: {', '.join(to_addrs)}\r\n"
        message += f"Subject: {subject}\r\n"
        message += "MIME-Version: 1.0\r\n"
        message += "Content-Type: text/plain; charset=utf-8\r\n"
        message += "\r\n" + body + "\r\n.\r\n"
        
        self._send_command(message)
        
        # Завершаем транзакцию
        self._send_command("QUIT")

    def _send_command(self, command):
        """Отправка команды серверу и получение ответа"""
        print(f"Клиент: {command}")
        self.socket.sendall((command + "\r\n").encode())
        response = self._get_response()
        print(f"Сервер: {response}")
        return response

    def _get_response(self):
        """Получение ответа от сервера"""
        response = []
        while True:
            line = self.connection.readline().decode().strip()
            response.append(line)
            if line[3:4] != "-":  # Проверяем последнюю строку ответа
                break
        return "\n".join(response)

    def close(self):
        """Закрытие соединения"""
        if self.connection:
            self.connection.close()
        if self.socket:
            self.socket.close()

def main():
    print("=== SMTP Email Client ===")
    
    # Настройки SMTP-сервера (пример для Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Данные отправителя
    username = input("Введите ваш email: ")
    password = getpass("Введите пароль: ")
    
    # Данные письма
    from_addr = username
    to_addrs = input("Введите email получателя (через запятую для нескольких): ").split(',')
    subject = input("Введите тему письма: ")
    body = input("Введите текст письма: ")
    
    # Создаем и настраиваем клиент
    client = SMTPClient(smtp_server, smtp_port)
    
    try:
        # Устанавливаем соединение и отправляем письмо
        client.connect()
        client.login(username, password)
        client.send_email(from_addr, to_addrs, subject, body)
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()