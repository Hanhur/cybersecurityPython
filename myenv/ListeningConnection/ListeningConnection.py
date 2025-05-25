# =================================================================================================================================
# Прослушивание - это когда сервер начинает "слушать" входя­щие подключения на своем сокете. 
# После того как сервер соз­дал сокет и привязал его к нужному адресу и порту, он начинает ожидать подключений, используя метод listen(). 
# Это похоже на то , как вы ждете звонка по телефону, только в данном случае ваш телефон - это сервер.
# ==================================================================================================================================

server_socket.listen(5) # прослушивать до 5 входящих соединений

# ===================================================================================================================================
# Подключение - это процесс установления связи между клиентским и серверным сокетами. Когда клиент пытается подключиться к серверу, 
# он создает новый сокет для этого соединения. Затем сервер принимает входящее соединение с помощью метода accept(), 
# который возвращает новый сокет и адрес клиента.
# ===================================================================================================================================

client_socket, client_address = server_socket.accept()

#Простой сервер для приема сообщений
import socket

#Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Привязываем сокет к адресу и порту
server_socket.bind(('localhost', 12345))

##Начинаем прослушивание входящих подключений
server_socket.listen()
print("Cepвep запущен и ожидает подключений... ")

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

#     #Закрываем соединение с клиентом
#     client_socket.close()

#Простой клиент для отправки сообщений
import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client_socket.connect(('localhost', 12345))

# Отправляем сообщение серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024)
print("Oтвeт от сервера:", response.decode())

# Закрываем соединение
client_socket.close()

# =============================================================================================================================

# Сервер для приема файлов от клиентов
# Серверная часть (file_server.py)
import socket
import os
import hashlib
from threading import Thread

class FileServer:
    def __init__(self, host = '0.0.0.0', port = 12345, save_dir = 'received_files'):
        self.host = host
        self.port = port
        self.save_dir = save_dir
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Создаем директорию для сохранения файлов
        os.makedirs(self.save_dir, exist_ok = True)
    
    def _handle_client(self, conn, addr):
        try:
            print(f"[+] Подключен клиент: {addr}")
            
            # Получаем информацию о файле (имя и размер)
            file_info = conn.recv(1024).decode()
            if not file_info:
                return
            
            filename, filesize = file_info.split('|')
            filesize = int(filesize)
            filepath = os.path.join(self.save_dir, filename)
            
            # Проверяем, не существует ли файл
            counter = 1
            base, ext = os.path.splitext(filename)
            while os.path.exists(filepath):
                filepath = os.path.join(self.save_dir, f"{base}_{counter}{ext}")
                counter += 1
            
            # Получаем файл по частям
            received = 0
            file_hash = hashlib.md5()
            with open(filepath, 'wb') as f:
                while received < filesize:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
                    file_hash.update(data)
                    received += len(data)
            
            # Проверяем целостность файла
            if received == filesize:
                response = f"SUCCESS|{os.path.basename(filepath)}|{file_hash.hexdigest()}"
                print(f"[+] Файл сохранен: {filepath} ({filesize} bytes, MD5: {file_hash.hexdigest()})")
            else:
                response = "ERROR|Неполная передача файла"
                print(f"[-] Ошибка передачи файла {filename}. Получено {received} из {filesize} байт")
            
            # Отправляем ответ клиенту
            conn.sendall(response.encode())
            
        except Exception as e:
            print(f"[-] Ошибка с клиентом {addr}: {e}")
            conn.sendall(f"ERROR|{str(e)}".encode())
        finally:
            conn.close()
            print(f"[+] Соединение с {addr} закрыто")
    
    def start(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            print(f"[*] Сервер запущен на {self.host}:{self.port}")
            print(f"[*] Файлы сохраняются в: {os.path.abspath(self.save_dir)}")
            
            while True:
                conn, addr = self.socket.accept()
                client_thread = Thread(target = self._handle_client, args = (conn, addr))
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\n[*] Остановка сервера...")
        finally:
            self.socket.close()

if __name__ == "__main__":
    server = FileServer()
    server.start()

# Клиентская часть (file_client.py)
import socket
import os
import hashlib

class FileClient:
    def __init__(self, host = 'localhost', port = 12345):
        self.host = host
        self.port = port
    
    def send_file(self, filepath):
        try:
            # Проверяем существование файла
            if not os.path.exists(filepath):
                print(f"[-] Файл не найден: {filepath}")
                return
            
            # Подключаемся к серверу
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                filename = os.path.basename(filepath)
                filesize = os.path.getsize(filepath)
                
                # Отправляем информацию о файле
                file_info = f"{filename}|{filesize}"
                s.sendall(file_info.encode())
                
                # Отправляем файл по частям
                file_hash = hashlib.md5()
                with open(filepath, 'rb') as f:
                    while True:
                        data = f.read(4096)
                        if not data:
                            break
                        s.sendall(data)
                        file_hash.update(data)
                
                # Получаем ответ от сервера
                response = s.recv(1024).decode()
                
                if response.startswith("SUCCESS"):
                    _, saved_name, server_hash = response.split('|')
                    if file_hash.hexdigest() == server_hash:
                        print(f"[+] Файл успешно передан и сохранен как: {saved_name}")
                        print(f"[+] Контрольная сумма MD5 совпадает: {server_hash}")
                    else:
                        print("[-] Ошибка: контрольные суммы не совпадают!")
                else:
                    print(f"[-] Ошибка сервера: {response}")
                    
        except Exception as e:
            print(f"[-] Ошибка при отправке файла: {e}")

if __name__ == "__main__":
    print("=== Клиент для отправки файлов ===")
    host = input("Введите адрес сервера [localhost]: ") or 'localhost'
    port = int(input("Введите порт сервера [12345]: ") or 12345)
    filepath = input("Введите путь к файлу для отправки: ")
    
    client = FileClient(host, port)
    client.send_file(filepath)

# ======================================================================================================================================

# Многопользовательский чат-сервер с поддержкой реального времени
# Серверная часть (chat_server.py)
import socket
import threading
import time

class ChatServer:
    def __init__(self, host = '0.0.0.0', port = 5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.nicknames = []
        
    def broadcast(self, message, sender = None):
        """Отправка сообщения всем клиентам, кроме отправителя"""
        for client in self.clients:
            if client != sender:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    self.remove_client(client)
    
    def handle_client(self, client):
        """Обработка подключения клиента"""
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    self.broadcast(message, client)
                    print(f"Пересылка сообщения: {message}")
                else:
                    raise Exception("Пустое сообщение")
            except:
                self.remove_client(client)
                break
    
    def remove_client(self, client):
        """Удаление клиента при отключении"""
        if client in self.clients:
            index = self.clients.index(client)
            nickname = self.nicknames[index]
            self.broadcast(f'{nickname} покинул чат!'.encode('utf-8'))
            self.clients.remove(client)
            self.nicknames.remove(nickname)
            client.close()
            print(f"{nickname} отключился")
    
    def receive(self):
        """Прием новых подключений"""
        print(f"Сервер чата запущен на {self.host}:{self.port}")
        while True:
            client, address = self.server.accept()
            print(f"Новое подключение от {str(address)}")
            
            # Запрос ника у клиента
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            
            self.nicknames.append(nickname)
            self.clients.append(client)
            
            print(f"Ник клиента: {nickname}")
            self.broadcast(f"{nickname} присоединился к чату!", client)
            client.send('Подключение к серверу успешно!'.encode('utf-8'))
            
            # Запуск потока для обработки сообщений клиента
            thread = threading.Thread(target = self.handle_client, args = (client,))
            thread.start()
    
    def start(self):
        """Запуск сервера"""
        try:
            self.receive()
        except KeyboardInterrupt:
            print("\nОстановка сервера...")
            self.server.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()

# Клиентская часть (chat_client.py)
import socket
import threading

class ChatClient:
    def __init__(self, host = 'localhost', port = 5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def receive(self):
        """Получение сообщений от сервера"""
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("Ошибка соединения!")
                self.client.close()
                break
    
    def write(self):
        """Отправка сообщений на сервер"""
        while True:
            message = input('')
            if message.lower() == 'exit':
                self.client.close()
                break
            self.client.send(f'{self.nickname}: {message}'.encode('utf-8'))
    
    def start(self):
        """Запуск клиента"""
        self.nickname = input("Введите ваш ник: ")
        try:
            self.client.connect((self.host, self.port))
            print(f"Подключение к {self.host}:{self.port} установлено")
            
            # Запуск потоков для получения и отправки сообщений
            receive_thread = threading.Thread(target = self.receive)
            receive_thread.start()
            
            write_thread = threading.Thread(target = self.write)
            write_thread.start()
            
        except Exception as e:
            print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    print("=== Чат-клиент ===")
    host = input("Введите адрес сервера [localhost]: ") or 'localhost'
    port = int(input("Введите порт сервера [5555]: ") or 5555)
    
    client = ChatClient(host, port)
    client.start()

# ================================================================================================================================

# Простой HTTP-сервер с обработкой GET-запросов
# Серверная часть (http_server.py)
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import mimetypes

class SimpleHTTPServer(BaseHTTPRequestHandler):
    # Директория с файлами для сервера
    WEB_DIR = "www"
    
    def do_GET(self):
        """Обработка GET-запросов"""
        try:
            # Определяем путь к запрашиваемому файлу
            path = self.path.split('?')[0]  # Игнорируем параметры запроса
            if path == '/':
                path = '/index.html'
            
            filepath = os.path.join(self.WEB_DIR, path.lstrip('/'))
            
            # Проверяем существование файла
            if os.path.exists(filepath) and os.path.isfile(filepath):
                self.send_response(200)
                
                # Определяем MIME-тип файла
                mime_type, _ = mimetypes.guess_type(filepath)
                if mime_type:
                    self.send_header('Content-type', mime_type)
                else:
                    self.send_header('Content-type', 'application/octet-stream')
                
                self.end_headers()
                
                # Отправляем содержимое файла
                with open(filepath, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                # Файл не найден - 404
                self.send_error(404, "File Not Found")
                
        except Exception as e:
            self.send_error(500, f"Server Error: {str(e)}")

def run(server_class = HTTPServer, handler_class = SimpleHTTPServer, port = 8000):
    """Запуск сервера"""
    # Создаем директорию для файлов, если ее нет
    os.makedirs(handler_class.WEB_DIR, exist_ok = True)
    
    # Создаем индексный файл, если его нет
    index_file = os.path.join(handler_class.WEB_DIR, 'index.html')
    if not os.path.exists(index_file):
        with open(index_file, 'w') as f:
            f.write("""<!DOCTYPE html>
                <html>
                <head>
                    <title>Simple HTTP Server</title>
                </head>
                <body>
                    <h1>Welcome to Simple HTTP Server</h1>
                    <p>This is the default index page.</p>
                    <p>Try accessing <a href="/test.html">test.html</a></p>
                </body>
                </html>""")
    
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    print(f"Serving files from directory: {os.path.abspath(handler_class.WEB_DIR)}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

# Использование с библиотекой requests (client.py)
import requests

def test_http_server():
    # Базовый URL сервера
    base_url = "http://localhost:8000"
    
    # Делаем GET-запросы
    try:
        # Запрос главной страницы
        print("\nRequesting index page:")
        response = requests.get(base_url + "/")
        print(f"Status Code: {response.status_code}")
        print(f"Content:\n{response.text[:200]}...")  # Печатаем первые 200 символов
        
        # Запрос несуществующей страницы
        print("\nRequesting non-existent page:")
        response = requests.get(base_url + "/nonexistent.html")
        print(f"Status Code: {response.status_code}")
        
        # Можно создать тестовый файл и запросить его
        with open("www/test.html", "w") as f:
            f.write("<h1>Test Page</h1><p>This is a test page.</p>")
        
        print("\nRequesting test page:")
        response = requests.get(base_url + "/test.html")
        print(f"Status Code: {response.status_code}")
        print(f"Content:\n{response.text}")
        
    except requests.ConnectionError:
        print("Error: Could not connect to the server. Is it running?")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_http_server()

# ===================================================================================================================

# SMTP-сервер для обработки запросов на отправку email
# Серверная часть (smtp_gateway.py)
import socket
import smtplib
from email.mime.text import MIMEText
from threading import Thread
import json
import ssl

class SMTPServer:
    def __init__(self, host = 'localhost', port = 5555, 
                 smtp_host = 'smtp.gmail.com', smtp_port = 587):
        self.host = host
        self.port = port
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # SMTP credentials (лучше хранить в защищенном хранилище)
        self.smtp_username = 'your_email@gmail.com'
        self.smtp_password = 'your_password'
    
    def handle_client(self, conn, addr):
        """Обработка клиентского соединения"""
        print(f"[+] Подключен клиент: {addr}")
        
        try:
            # Получаем данные от клиента
            data = conn.recv(1024).decode('utf-8')
            if not data:
                return
            
            # Парсим JSON с параметрами письма
            email_data = json.loads(data)
            to_email = email_data['to']
            subject = email_data['subject']
            body = email_data['body']
            
            # Отправляем письмо через SMTP
            result = self.send_email(to_email, subject, body)
            
            # Отправляем результат клиенту
            conn.sendall(result.encode('utf-8'))
            
        except json.JSONDecodeError:
            conn.sendall(b'ERROR: Invalid JSON format')
        except KeyError as e:
            conn.sendall(f'ERROR: Missing required field {str(e)}'.encode())
        except Exception as e:
            conn.sendall(f'ERROR: {str(e)}'.encode())
        finally:
            conn.close()
            print(f"[+] Соединение с {addr} закрыто")
    
    def send_email(self, to_email, subject, body):
        """Отправка email через SMTP"""
        try:
            # Создаем MIME сообщение
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.smtp_username
            msg['To'] = to_email
            
            # Устанавливаем соединение с SMTP сервером
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls(context=ssl.create_default_context())
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            return f"SUCCESS: Email sent to {to_email}"
        except Exception as e:
            return f"ERROR: Failed to send email - {str(e)}"
    
    def start(self):
        """Запуск сервера"""
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"[*] SMTP Gateway запущен на {self.host}:{self.port}")
        
        try:
            while True:
                conn, addr = self.socket.accept()
                client_thread = Thread(target = self.handle_client, args = (conn, addr))
                client_thread.start()
        except KeyboardInterrupt:
            print("\n[*] Остановка сервера...")
        finally:
            self.socket.close()

if __name__ == "__main__":
    # Настройки (лучше вынести в конфиг)
    server = SMTPServer(
        host ='0.0.0.0', 
        port = 5555,
        smtp_host = 'smtp.gmail.com',
        smtp_port = 587
    )
    server.start()

# Клиентская часть (email_client.py)
import socket
import json

class EmailClient:
    def __init__(self, host = 'localhost', port = 5555):
        self.host = host
        self.port = port
    
    def send_email_request(self, to_email, subject, body):
        """Отправка запроса на сервер"""
        try:
            # Создаем сокет и подключаемся к серверу
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                
                # Формируем JSON с данными письма
                email_data = {
                    'to': to_email,
                    'subject': subject,
                    'body': body
                }
                
                # Отправляем данные на сервер
                s.sendall(json.dumps(email_data).encode('utf-8'))
                
                # Получаем ответ от сервера
                response = s.recv(1024).decode('utf-8')
                return response
                
        except Exception as e:
            return f"Connection error: {str(e)}"

def main():
    print("=== Email Client ===")
    host = input("Введите адрес сервера [localhost]: ") or 'localhost'
    port = int(input("Введите порт сервера [5555]: ") or 5555)
    
    client = EmailClient(host, port)
    
    while True:
        print("\nВведите данные письма:")
        to_email = input("Кому: ")
        if not to_email:
            break
            
        subject = input("Тема: ")
        body = input("Текст письма: ")
        
        response = client.send_email_request(to_email, subject, body)
        print(f"\nОтвет сервера: {response}")
        
        if input("\nОтправить еще одно письмо? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()

# ============================================================================================================================

# Сервер для игры "Крестики-нолики" с сетевым взаимодействием
# Серверная часть (tictactoe_server.py)
import socket
import threading
import json
from enum import Enum

class GameStatus(Enum):
    WAITING = "Ожидание второго игрока"
    PLAYING = "Игра идет"
    X_WON = "Победили крестики!"
    O_WON = "Победили нолики!"
    DRAW = "Ничья!"

class TicTacToeServer:
    def __init__(self, host = '0.0.0.0', port = 5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.games = {}
        self.player_symbols = {}
        print(f"Сервер запущен на {host}:{port}")

    def broadcast(self, game_id, message):
        """Отправка сообщения всем игрокам в игре"""
        for player in self.games[game_id]['players']:
            try:
                player.send(json.dumps(message).encode('utf-8'))
            except:
                self.handle_disconnect(player)

    def handle_disconnect(self, client):
        """Обработка отключения клиента"""
        for game_id, game in list(self.games.items()):
            if client in game['players']:
                opponent = game['players'][0] if game['players'][1] == client else game['players'][1]
                if opponent:
                    try:
                        opponent.send(json.dumps({"type": "opponent_disconnected"}).encode('utf-8'))
                    except:
                        pass
                del self.games[game_id]
                break
        if client in self.clients:
            self.clients.remove(client)
        client.close()

    def handle_client(self, client):
        """Обработка клиентского соединения"""
        self.clients.append(client)
        print(f"Новое подключение: {client.getpeername()}")

        try:
            while True:
                data = client.recv(1024).decode('utf-8')
                if not data:
                    break

                message = json.loads(data)
                if message['type'] == 'create_game':
                    self.create_game(client)
                elif message['type'] == 'join_game':
                    self.join_game(client, message['game_id'])
                elif message['type'] == 'make_move':
                    self.process_move(client, message['game_id'], message['position'])

        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            self.handle_disconnect(client)
            print(f"Клиент отключен: {client.getpeername()}")

    def create_game(self, client):
        """Создание новой игры"""
        game_id = len(self.games) + 1
        self.games[game_id] = {
            'board': [' ' for _ in range(9)],
            'players': [client],
            'current_player': 'X',
            'status': GameStatus.WAITING.value
        }
        self.player_symbols[client] = 'X'
        client.send(json.dumps({
            'type': 'game_created',
            'game_id': game_id,
            'symbol': 'X',
            'status': GameStatus.WAITING.value
        }).encode('utf-8'))
        print(f"Создана игра #{game_id}")

    def join_game(self, client, game_id):
        """Подключение к существующей игре"""
        if game_id in self.games and len(self.games[game_id]['players']) < 2:
            game = self.games[game_id]
            game['players'].append(client)
            game['status'] = GameStatus.PLAYING.value
            self.player_symbols[client] = 'O'

            # Отправка уведомлений обоим игрокам
            for i, player in enumerate(game['players']):
                player.send(json.dumps({
                    'type': 'game_started',
                    'game_id': game_id,
                    'symbol': 'X' if i == 0 else 'O',
                    'current_player': game['current_player'],
                    'board': game['board'],
                    'status': game['status']
                }).encode('utf-8'))
            
            print(f"Игра #{game_id} началась")
        else:
            client.send(json.dumps({
                'type': 'error',
                'message': 'Не удалось подключиться к игре'
            }).encode('utf-8'))

    def process_move(self, client, game_id, position):
        """Обработка хода игрока"""
        if game_id not in self.games:
            return

        game = self.games[game_id]
        symbol = self.player_symbols[client]

        # Проверка валидности хода
        if (game['current_player'] != symbol or 
            game['board'][position] != ' ' or 
            game['status'] != GameStatus.PLAYING.value):
            return

        # Обновление доски
        game['board'][position] = symbol
        game['current_player'] = 'O' if symbol == 'X' else 'X'

        # Проверка условий победы
        winner = self.check_winner(game['board'])
        if winner:
            game['status'] = GameStatus.X_WON.value if winner == 'X' else GameStatus.O_WON.value
        elif ' ' not in game['board']:
            game['status'] = GameStatus.DRAW.value

        # Отправка обновления обоим игрокам
        self.broadcast(game_id, {
            'type': 'game_update',
            'board': game['board'],
            'current_player': game['current_player'],
            'status': game['status']
        })

    def check_winner(self, board):
        """Проверка победных комбинаций"""
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
            [0, 4, 8], [2, 4, 6]              # Диагонали
        ]
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
                return board[line[0]]
        return None

    def start(self):
        """Запуск сервера"""
        try:
            while True:
                client, addr = self.server.accept()
                thread = threading.Thread(target = self.handle_client, args = (client,))
                thread.start()
        except KeyboardInterrupt:
            print("Остановка сервера...")
        finally:
            self.server.close()

if __name__ == "__main__":
    server = TicTacToeServer()
    server.start()

# Клиентская часть (tictactoe_client.py)
import socket
import json
import threading

class TicTacToeClient:
    def __init__(self, host = 'localhost', port = 5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.symbol = None
        self.game_id = None
        self.current_player = None
        self.board = [' ' for _ in range(9)]
        self.status = None

    def connect(self):
        """Подключение к серверу"""
        self.client.connect((self.host, self.port))
        print(f"Подключено к серверу {self.host}:{self.port}")

        # Запуск потока для получения сообщений
        receive_thread = threading.Thread(target = self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def receive_messages(self):
        """Получение сообщений от сервера"""
        while True:
            try:
                data = self.client.recv(1024).decode('utf-8')
                if not data:
                    break

                message = json.loads(data)
                self.handle_server_message(message)

            except Exception as e:
                print(f"Ошибка соединения: {e}")
                break

    def handle_server_message(self, message):
        """Обработка сообщений от сервера"""
        if message['type'] == 'game_created':
            self.game_id = message['game_id']
            self.symbol = message['symbol']
            self.status = message['status']
            print(f"Создана игра #{self.game_id}. Ваш символ: {self.symbol}")
            print(f"Статус: {self.status}")

        elif message['type'] == 'game_started':
            self.game_id = message['game_id']
            self.symbol = message['symbol']
            self.current_player = message['current_player']
            self.board = message['board']
            self.status = message['status']
            self.print_game_state()

        elif message['type'] == 'game_update':
            self.board = message['board']
            self.current_player = message['current_player']
            self.status = message['status']
            self.print_game_state()

        elif message['type'] == 'opponent_disconnected':
            print("\nПротивник отключился. Игра завершена.")
            self.reset_game()

        elif message['type'] == 'error':
            print(f"Ошибка: {message['message']}")

    def print_game_state(self):
        """Отображение текущего состояния игры"""
        print("\nТекущее состояние игры:")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} ")
            if i < 6:
                print("-----------")
        print(f"\nСтатус: {self.status}")
        if self.current_player == self.symbol and self.status == "Игра идет":
            print("Ваш ход! Введите номер клетки (0-8):")

    def make_move(self, position):
        """Отправка хода на сервер"""
        try:
            position = int(position)
            if 0 <= position <= 8:
                self.client.send(json.dumps({
                    'type': 'make_move',
                    'game_id': self.game_id,
                    'position': position
                }).encode('utf-8'))
            else:
                print("Некорректный номер клетки. Введите число от 0 до 8.")
        except ValueError:
            print("Пожалуйста, введите число от 0 до 8.")

    def create_game(self):
        """Создание новой игры"""
        self.client.send(json.dumps({'type': 'create_game'}).encode('utf-8'))

    def join_game(self, game_id):
        """Подключение к существующей игре"""
        self.client.send(json.dumps({
            'type': 'join_game',
            'game_id': int(game_id)
        }).encode('utf-8'))

    def reset_game(self):
        """Сброс состояния игры"""
        self.symbol = None
        self.game_id = None
        self.current_player = None
        self.board = [' ' for _ in range(9)]
        self.status = None

def main():
    print("=== Клиент для игры в Крестики-нолики ===")
    host = input("Введите адрес сервера [localhost]: ") or 'localhost'
    port = int(input("Введите порт сервера [5555]: ")) or 5555

    client = TicTacToeClient(host, port)
    client.connect()

    while True:
        print("\nМеню:")
        print("1. Создать новую игру")
        print("2. Присоединиться к существующей игре")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            client.create_game()
            break
        elif choice == '2':
            game_id = input("Введите ID игры: ")
            client.join_game(game_id)
            break
        elif choice == '3':
            client.client.close()
            return
        else:
            print("Некорректный ввод. Попробуйте снова.")

    # Основной игровой цикл
    try:
        while True:
            if client.current_player == client.symbol and client.status == "Игра идет":
                move = input()
                client.make_move(move)
    except KeyboardInterrupt:
        print("\nВыход из игры...")
    finally:
        client.client.close()

if __name__ == "__main__":
    main()