# ====================================================================================================================================
# Защита от взлома - это важный аспект кибербезопасности, который включает в себя применение различных практик и методов для защиты 
# компьютерных систем, сетей, данных и приложений от несанкционированного доступа и злонамеренных атак.
# =====================================================================================================================================

# Пример скрипта для мониторинга логов:
import os
def monitor_logs (log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "FAILED LOGIN" in line or "UNAUTHORIZED ACCESS":
                print(f"Suspicious activity detected: {line}")

log_file = '/var/log/auth.log'
monitor_logs(log_file)

# Проверка на уязвимости и сканирование сети
import nmap
def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts = network, arguments = '-sP')
    for host in nm.all_hosts():
        print(f'Host: {host}, State: {nm[host].state()} ')

network = '192.168.1.0/24'
scan_network(network)

# Разработка собственных инструментов обнаружения вторжений
from sklearn.ensemble import IsolationForest
import numpy as np

# Пример данных (замените на реальные данные сетевого трафика)
data = np.array([[1, 2], [1, 2.5], [1.5, 1.8], [8, 9], [8.5, 9.5]])

# Модель обнаружения аномалий
model = IsolationForest(contamiцation = 0.2)
model.fit(data)

# Прогноз аномалий
predictions = model.predict(data)
print(predictions)

# Разработка системы мониторинга безопасности
import hashlib
import os

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def monitor_files(files):
    hashes = {}
    for file in files:
        hashes [file] = hash_file(file)

    while True:
        for file in files:
            current_hash = hash_file(file)
            if current_hash != hashes[file]:
                print(f"File changed: {file}")
                hashes[file] = current_hash

files_to_monitor = ['/etc/passwd', '/etc/hosts']
monitor_files(files_to_monitor)

# Реализация системы резервного копирования данных
import shutil
import os
import time
def backup_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for filename in os.listdir(source):
        full_file_name = os.path.join(source, filename)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination)

source_dir = '/path/to/source'
backup_dir = '/path/to/backup'
backup_files(source_dir, backup_dir)

# Автоматизация процесса обновления и установки патчей
# Пример скрипта для автома­ тического обновления на Linux:
import os

def update_system():
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade -y')

update_system()

# Пример использования библиотеки pyotp для создания ОТР:
import pyotp
import time

def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

# Секретный'ключ для генерации ОТР
secret = 'JBSWY3DPEHPK3PXP'
print("Current OTP:", generate_otp(secret))

# Проверка ОТР
time.sleep(30)
print("New OTP:", generate_otp(secret))

# Использование библиотеки cryptography для шифрования и расшифрования конфиденциальных данных:
from cryptography.fernet import Fernet

# Генерация ключа шифрования
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифрование данных
# message = b"Секретные данные"
encrypted_message = cipher.encrypt(message)

# Расшифрование данных
decrypted_message = cipher.decrypt(encrypted_message)
print("Исходные данные:", message)
print("Зашифрованные данные:", encrypted_message)
print("Расшифрованные данные:", decrypted_message)

# ===================== Развитие навыков: создание собственных инструментов безопасности ======================================
# Разработка собственных инструментов для анализа Wi-Fi безопасности
# Преимущества создания собственных инструментов безопасности
# Понимание принципов работы.
# Псевдокод WPS-атаки
def wps_attack(target_bssid):
    for pin in generate_pins():  # Генерация 8-значных PIN
        response = send_wps_request(target_bssid, pin)
        if response == "SUCCESS":
            return pin  # Уязвимый PIN найден
        
# Пример: создание простого сканера Wi-Fi на Python
# Используем Scapy для анализа 802.11-фреймов
from scapy.all import *
from scapy.layers.dot11 import Dot11ProbeReq

def packet_handler(pkt):
    if pkt.haslayer(Dot11ProbeReq):  # Анализ пробных запросов
        print(f"Устройство {pkt.addr2} ищет сеть {pkt.info.decode()}")

sniff(iface = "wlan0mon", prn = packet_handler, store = 0)

# Анализ 4-way handshake
def detect_krack(packets):
    handshakes = 0
    for pkt in packets:
        if is_handshake_packet(pkt):  # Проверка на рукопожатие
            handshakes += 1
            if handshakes > 3:  # Повторное рукопожатие
                alert("Возможна KRACK-атака!")

# Детектор поддельных MAC
import scapy.all as scapy

known_macs = {"00:11:22:33:44:55"}

def detect_mac_spoofing(pkt):
    if pkt.addr2 in known_macs and pkt.addr2 != get_vendor_mac(pkt.addr2):
        alert(f"Поддельный MAC: {pkt.addr2}")

# Умный генератор паролей
import itertools

def generate_passwords(base_words, years, special_chars):
    for word, year, char in itertools.product(base_words, years, special_chars):
        yield f"{word.capitalize()}{year}{char}"

# Пример практического применения
def detect_rogue_ap(beacons, known_aps):
    for bssid, ssid in beacons:
        if ssid in known_aps.values() and bssid not in known_aps:
            alert(f"Фальшивая точка доступа: {ssid} ({bssid})")

# ======================================================================================================================================

# Адаптация инструментов под специфические задачи Wi-Fi безопасности.
# Адаптация под конкретные задачи.
# Специфические требования к анализу.
# Пример: детектирование кастомных фреймов
if pkt.haslayer(Dot11) and pkt.type == 2 and pkt.subtype == 15:
    analyze_custom_frame(pkt)  # Нет в стандартных анализаторах

# Пример для GPU-ускорения:
# Специальная оптимизация под архитектуру NVIDIA
@cuda.jit
def bruteforce_kernel(hashes, alphabet, max_length):
    # ... CUDA-оптимизированный перебор

#  Практические примеры адаптации
from scapy.all import *

hidden_nets = set()

def packet_handler(pkt):
    if pkt.haslayer(Dot11ProbeResp) and not pkt.info:
        if pkt.addr3 not in hidden_nets:
            print(f"Обнаружена скрытая сеть BSSID: {pkt.addr3}")
            hidden_nets.add(pkt.addr3)

sniff(iface = "wlan0mon", prn = packet_handler, store = 0)

# Анализатор энергопотребления IoT
import time
from collections import defaultdict

traffic_stats = defaultdict(lambda: {'bytes': 0, 'last_seen': 0})

def analyze_energy(pkt):
    dev = pkt.addr2
    traffic_stats[dev]['bytes'] += len(pkt)
    traffic_stats[dev]['last_seen'] = time.time()
    
    # Вычисляем "агрессивность" устройства
    traffic_rate = traffic_stats[dev]['bytes'] / (time.time() - first_seen[dev])
    if traffic_rate > THRESHOLD:
        alert(f"Устройство {dev} потенциально заражено")

# Пример: быстрый сниффер на Scapy
from scapy.all import *

def channel_hopper():
    while True:
        for channel in range(1,14):
            os.system(f"iwconfig wlan0mon channel {channel}")
            time.sleep(0.5)

Thread(target = channel_hopper).start()

sniff(iface = "wlan0mon", prn = lambda x: x.summary())

# Анализируем структуру пакетов:
if pkt[TCP].dport == 9542 and len(pkt.load) == 128:
    decrypt_proprietary(pkt.load)  # Наша кастомная функция

# Оптимизированный генератор:
def company_passwords():
    prefixes = ["C0mpAny", "Corp", "Office"]
    years = [2020, 2021, 2022, 2023, 2024]
    for p, y in itertools.product(prefixes, years):
        yield f"{p}_{y}"  # Только релевантные комбинации

# Используйте модульную архитектуру:
class WiFiScanner:
    def __init__(self, interface):
        self.iface = interface
    
    def start_scan(self):
        # ... отдельный метод для сканирования

    def analyze(self):
        # ... отдельный метод для анализа

# Анализ временных характеристик
timings = []
for i in range(100):
    start = time.time()
    send_wps_probe(target)
    timings.append(time.time() - start)

if statistics.stdev(timings) > 0.5:
    print("Обнаружены аномалии времени ответа")

# Машинное обучение для детектирования атак
from sklearn.ensemble import IsolationForest

clf = IsolationForest()
clf.fit(training_data)  # Данные нормального трафика
anomalies = clf.predict(live_traffic)

# =========================================================================================================================================

# Развитие навыков Python через разработку инструментов Wi-Fi безопасности
# Развитие навыков программирования.
# Работа с сетевыми протоколами
from scapy.all import *
# Анализ 802.11 фреймов
pkts = sniff(iface = "wlan0mon", count = 100, lfilter = lambda x: x.haslayer(Dot11Beacon))

# Обработка больших объемов данных
import pandas as pd
# Анализ собранных handshake'ов
df = pd.DataFrame([parse_packet(p) for p in packets])
df.groupby('bssid')['signal'].plot.hist()

# Пример 1: Улучшенный сниффер Wi-Fi
from collections import defaultdict
import matplotlib.pyplot as plt

class WiFiScanner:
    def __init__(self):
        self.devices = defaultdict(int)
    
    def packet_handler(self, pkt):
        if pkt.haslayer(Dot11):
            self.devices[pkt.addr2] += 1
    
    def show_stats(self):
        plt.bar(self.devices.keys(), self.devices.values())
        plt.xticks(rotation = 90)
        plt.show()

scanner = WiFiScanner()
sniff(prn = scanner.packet_handler, timeout = 60)
scanner.show_stats()

# Пример 2: Оптимизированный брутфорс WPS
import concurrent.futures

def check_pin(pin):
    response = send_wps_request(pin)
    return pin if response.success else None

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(check_pin, generate_pins())
    for valid_pin in filter(None, results):
        print(f"Found PIN: {valid_pin}")
        break

# Интеграция с аппаратным ускорением
from numba import cuda

@cuda.jit
def gpu_bruteforce(hashes, alphabet, result):
    # Реализация перебора на GPU
    pass

# Машинное обучение для детектирования атак
from sklearn.ensemble import IsolationForest

clf = IsolationForest()
clf.fit(normal_traffic)
anomalies = clf.predict(current_traffic)

# ================================================================================================================================

# Разработка сканера уязвимостей:
# Вот скрипт на Python, который сканирует веб-приложения на наличие распространенных уязвимостей, таких как SQL-инъекции, XSS и другие:
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse
import re

class VulnerabilityScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.links_to_scan = set()
        self.vulnerabilities = []
        
    def scan(self):
        print(f"[*] Начинаем сканирование: {self.target_url}")
        self.crawl()
        self.test_xss()
        self.test_sql_injection()
        self.test_csrf()
        self.display_results()
        
    def crawl(self):
        print("[*] Поиск ссылок на странице...")
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href = True):
                url = urljoin(self.target_url, link['href'])
                if self.target_url in url and url not in self.links_to_scan:
                    self.links_to_scan.add(url)
                    print(f"[+] Найдена ссылка: {url}")
                    
        except Exception as e:
            print(f"[-] Ошибка при поиске ссылок: {e}")
    
    def test_xss(self):
        print("\n[*] Тестирование на XSS уязвимости...")
        test_script = "<script>alert('XSS')</script>"
        
        for url in list(self.links_to_scan):
            try:
                # Проверка отраженного XSS в URL параметрах
                if '=' in url:
                    vulnerable_url = self.inject_payload(url, test_script)
                    response = self.session.get(vulnerable_url)
                    if test_script in response.text:
                        self.vulnerabilities.append((
                            "Отраженная XSS", 
                            url, 
                            "Параметры URL могут отражать JavaScript код"
                        ))
                        print(f"[!] Обнаружена XSS уязвимость: {url}")
                
                # Проверка форм на странице
                response = self.session.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for form in soup.find_all('form'):
                    form_action = form.get('action')
                    if form_action:
                        form_url = urljoin(url, form_action)
                    else:
                        form_url = url
                    
                    form_method = form.get('method', 'get').lower()
                    
                    inputs = form.find_all('input')
                    form_data = {}
                    for input_tag in inputs:
                        input_name = input_tag.get('name')
                        input_type = input_tag.get('type', 'text')
                        if input_name and input_type != 'submit':
                            form_data[input_name] = test_script
                    
                    if form_method == 'post':
                        response = self.session.post(form_url, data = form_data)
                    else:
                        response = self.session.get(form_url, params = form_data)
                    
                    if test_script in response.text:
                        self.vulnerabilities.append((
                            "Хранимая XSS", 
                            form_url, 
                            f"Форма может сохранять JavaScript код (метод {form_method})"
                        ))
                        print(f"[!] Обнаружена XSS уязвимость в форме: {form_url}")
                        
            except Exception as e:
                print(f"[-] Ошибка при тестировании XSS для {url}: {e}")
    
    def test_sql_injection(self):
        print("\n[*] Тестирование на SQL-инъекции...")
        sql_errors = {
            "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*"),
            "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*"),
            "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"Warning.*mssql_.*"),
            "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Warning.*oci_.*"),
            "SQLite": (r"SQLite/JDBCDriver", r"System.Data.SQLite.SQLiteException"),
            "General": (r"SQL syntax.*", r"Warning.*sql_.*", r"Unclosed quotation mark.*")
        }
        
        test_payloads = [
            "'", 
            "\"", 
            "' OR '1'='1", 
            "\" OR \"1\"=\"1", 
            "' OR 1=1 --", 
            "' UNION SELECT null, username, password FROM users--"
        ]
        
        for url in list(self.links_to_scan):
            try:
                if '=' in url:
                    for payload in test_payloads:
                        vulnerable_url = self.inject_payload(url, payload)
                        response = self.session.get(vulnerable_url)
                        
                        for db, errors in sql_errors.items():
                            for error in errors:
                                if re.search(error, response.text, re.I):
                                    self.vulnerabilities.append((
                                        "SQL-инъекция", 
                                        url, 
                                        f"Возможна SQL-инъекция для {db} с payload: {payload}"
                                    ))
                                    print(f"[!] Обнаружена SQL-инъекция: {url}")
                                    break
                
                # Проверка форм на SQL-инъекции
                response = self.session.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for form in soup.find_all('form'):
                    form_action = form.get('action')
                    if form_action:
                        form_url = urljoin(url, form_action)
                    else:
                        form_url = url
                    
                    form_method = form.get('method', 'get').lower()
                    inputs = form.find_all('input')
                    form_data = {}
                    
                    for input_tag in inputs:
                        input_name = input_tag.get('name')
                        input_type = input_tag.get('type', 'text')
                        if input_name and input_type != 'submit':
                            form_data[input_name] = test_payloads[0]  # Используем первый payload для теста
                    
                    if form_method == 'post':
                        response = self.session.post(form_url, data = form_data)
                    else:
                        response = self.session.get(form_url, params = form_data)
                    
                    for db, errors in sql_errors.items():
                        for error in errors:
                            if re.search(error, response.text, re.I):
                                self.vulnerabilities.append((
                                    "SQL-инъекция", 
                                    form_url, 
                                    f"Возможна SQL-инъекция для {db} в форме (метод {form_method})"
                                ))
                                print(f"[!] Обнаружена SQL-инъекция в форме: {form_url}")
                                break
                            
            except Exception as e:
                print(f"[-] Ошибка при тестировании SQL-инъекции для {url}: {e}")
    
    def test_csrf(self):
        print("\n[*] Проверка на отсутствие CSRF-токенов...")
        for url in list(self.links_to_scan):
            try:
                response = self.session.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for form in soup.find_all('form'):
                    if form.get('method', 'get').lower() == 'post':
                        csrf_token = form.find('input', {'name': 'csrf_token'}) or \
                                     form.find('input', {'name': 'csrfmiddlewaretoken'}) or \
                                     form.find('input', {'name': 'authenticity_token'})
                        
                        if not csrf_token:
                            form_action = form.get('action')
                            if form_action:
                                form_url = urljoin(url, form_action)
                            else:
                                form_url = url
                            
                            self.vulnerabilities.append((
                                "CSRF", 
                                form_url, 
                                "Форма не содержит CSRF-токен и уязвима к CSRF-атакам"
                            ))
                            print(f"[!] Обнаружена форма без CSRF-токена: {form_url}")
                            
            except Exception as e:
                print(f"[-] Ошибка при проверке CSRF для {url}: {e}")
    
    def inject_payload(self, url, payload):
        parts = url.split('?')
        if len(parts) == 2:
            base_url = parts[0]
            params = parts[1].split('&')
            new_params = []
            
            for param in params:
                if '=' in param:
                    key, value = param.split('=', 1)
                    new_params.append(f"{key}={payload}")
                else:
                    new_params.append(param)
            
            return f"{base_url}?{'&'.join(new_params)}"
        return url
    
    def display_results(self):
        print("\n[+] Результаты сканирования:")
        if not self.vulnerabilities:
            print("[+] Уязвимостей не обнаружено")
            return
            
        print(f"Обнаружено {len(self.vulnerabilities)} уязвимостей:")
        print("-" * 80)
        for i, (vuln_type, url, desc) in enumerate(self.vulnerabilities, 1):
            print(f"{i}. Тип: {vuln_type}")
            print(f"   URL: {url}")
            print(f"   Описание: {desc}")
            print("-" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Сканер уязвимостей веб-приложений")
    parser.add_argument("-u", "--url", required = True, help = "Целевой URL для сканирования")
    args = parser.parse_args()
    
    scanner = VulnerabilityScanner(args.url)
    scanner.scan()

# ==========================================================================================================================================

# Создание инструмента для обнаружения АRР-отравления:
# Установите необходимые зависимости: pip install scapy
# Запустите скрипт с правами root (для работы с сетевыми интерфейсами): sudo python3 arp_spoof_detector.py -i eth0
# Для отправки email уведомлений укажите email адрес: sudo python3 arp_spoof_detector.py -i eth0 -e admin@example.com

# Инструмент для обнаружения ARP-отравления на Python
#!/usr/bin/env python3
import scapy.all as scapy
import time
import smtplib
from email.mime.text import MIMEText
import argparse
import threading
import sys
from collections import defaultdict

class ARPSpoofDetector:
    def __init__(self, interface, alert_email = None, alert_threshold = 5, check_interval = 10):
        self.interface = interface
        self.alert_email = alert_email
        self.alert_threshold = alert_threshold
        self.check_interval = check_interval
        self.arp_table = defaultdict(dict)
        self.suspicious_activity = defaultdict(int)
        self.running = False
        self.lock = threading.Lock()

    def start(self):
        """Запуск мониторинга сети"""
        print(f"[*] Запуск ARP мониторинга на интерфейсе {self.interface}")
        print("[*] Нажмите Ctrl+C для остановки\n")
        
        self.running = True
        # Запуск потока для периодической проверки ARP таблицы
        checker_thread = threading.Thread(target = self.check_arp_table)
        checker_thread.daemon = True
        checker_thread.start()
        
        # Запуск сниффера ARP пакетов
        try:
            scapy.sniff(iface = self.interface, store = False, prn = self.process_packet)
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            print(f"[-] Ошибка: {e}")
            self.stop()

    def stop(self):
        """Остановка мониторинга"""
        self.running = False
        print("\n[*] Остановка ARP мониторинга")
        sys.exit(0)

    def process_packet(self, packet):
        """Обработка ARP пакетов"""
        if packet.haslayer(scapy.ARP):
            arp_packet = packet[scapy.ARP]
            
            # Игнорируем ARP-запросы (op=1), интересуют только ответы (op=2)
            if arp_packet.op == 2:
                ip = arp_packet.psrc
                mac = arp_packet.hwsrc
                
                with self.lock:
                    # Проверяем, есть ли уже запись для этого IP
                    if ip in self.arp_table:
                        # Если MAC изменился - возможна ARP-атака
                        if self.arp_table[ip] != mac:
                            old_mac = self.arp_table[ip]
                            self.suspicious_activity[ip] += 1
                            print(f"[!] Подозрительное изменение ARP: IP {ip} изменил MAC с {old_mac} на {mac}")
                            
                            # Если превышен порог подозрительной активности - отправляем предупреждение
                            if self.suspicious_activity[ip] >= self.alert_threshold:
                                self.send_alert(ip, old_mac, mac)
                    else:
                        # Добавляем новую запись в ARP таблицу
                        self.arp_table[ip] = mac

    def check_arp_table(self):
        """Периодическая проверка ARP таблицы на несоответствия"""
        while self.running:
            time.sleep(self.check_interval)
            with self.lock:
                current_arp = self.get_system_arp_table()
                
                for ip, mac in current_arp.items():
                    if ip in self.arp_table and self.arp_table[ip] != mac:
                        old_mac = self.arp_table[ip]
                        self.suspicious_activity[ip] += 1
                        print(f"[!] Несоответствие в ARP таблице: IP {ip} изменил MAC с {old_mac} на {mac}")
                        
                        if self.suspicious_activity[ip] >= self.alert_threshold:
                            self.send_alert(ip, old_mac, mac)
                    
                    # Обновляем нашу ARP таблицу
                    self.arp_table[ip] = mac

    def get_system_arp_table(self):
        """Получение текущей ARP таблицы системы"""
        result = {}
        try:
            # Используем команду arp для получения таблицы
            output = scapy.get_working_if().arp_cache
            for entry in output:
                ip = entry[0]
                mac = entry[1]
                if ip and mac:
                    result[ip] = mac
        except Exception as e:
            print(f"[-] Ошибка при получении ARP таблицы: {e}")
        return result

    def send_alert(self, ip, old_mac, new_mac):
        """Отправка предупреждения об ARP-отравлении"""
        message = f"""Обнаружена возможная ARP-атака (ARP spoofing)!
        
Детали:
- IP адрес: {ip}
- Старый MAC: {old_mac}
- Новый MAC: {new_mac}
- Количество изменений: {self.suspicious_activity[ip]}

Время обнаружения: {time.strftime('%Y-%m-%d %H:%M:%S')}

Рекомендуемые действия:
1. Проверить устройство с MAC {new_mac}
2. Проверить журналы сети на предмет подозрительной активности
3. При необходимости изолировать подозрительное устройство
"""
        print(f"[ALERT] {message}")
        
        # Отправка email уведомления
        if self.alert_email:
            try:
                msg = MIMEText(message)
                msg['Subject'] = f'[ALERT] Обнаружена ARP-атака в сети (IP: {ip})'
                msg['From'] = 'arp_monitor@yourdomain.com'
                msg['To'] = self.alert_email
                
                # Настройте SMTP сервер согласно вашей конфигурации
                with smtplib.SMTP('localhost') as server:
                    server.send_message(msg)
                print(f"[+] Email предупреждение отправлено на {self.alert_email}")
            except Exception as e:
                print(f"[-] Ошибка при отправке email: {e}")

def get_arguments():
    parser = argparse.ArgumentParser(description = 'ARP Spoofing Detector')
    parser.add_argument('-i', '--interface', dest = 'interface', help = 'Сетевой интерфейс для мониторинга', required = True)
    parser.add_argument('-e', '--email', dest = 'email', help = 'Email для отправки предупреждений (необязательно)')
    parser.add_argument('-t', '--threshold', dest = 'threshold', type = int, default = 5,help = 'Порог подозрительной активности перед отправкой предупреждения (по умолчанию: 5)')
    parser.add_argument('-c', '--check-interval', dest = 'interval', type = int, default = 10,help = 'Интервал проверки ARP таблицы в секундах (по умолчанию: 10)')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()
    detector = ARPSpoofDetector(
        interface = args.interface,
        alert_email = args.email,
        alert_threshold = args.threshold,
        check_interval = args.interval
    )
    detector.start()

# =========================================================================================================================================

# Реализация инструмента для обнаружения сетевого сниффинга:
# Установите необходимые зависимости: pip install scapy netifaces
# Запустите скрипт с правами root (для работы с сетевыми интерфейсами): sudo python3 sniffing_detector.py -i eth0
# Для отправки email уведомлений укажите email адрес: sudo python3 sniffing_detector.py -i eth0 -e admin@example.com

# Инструмент для обнаружения сетевого сниффинга на Python
#!/usr/bin/env python3
import scapy.all as scapy
import time
import argparse
import threading
import sys
from collections import defaultdict
import socket
import netifaces
import smtplib
from email.mime.text import MIMEText

class SniffingDetector:
    def __init__(self, interface, alert_email = None, check_interval = 30):
        self.interface = interface
        self.alert_email = alert_email
        self.check_interval = check_interval
        self.running = False
        self.suspicious_devices = defaultdict(int)
        self.local_ip = self.get_local_ip()
        self.local_mac = self.get_local_mac()
        self.gateway_ip, self.gateway_mac = self.get_gateway_info()
        self.promiscuous_mode_warned = False

    def start(self):
        """Запуск мониторинга сети"""
        print(f"[*] Запуск детектора сниффинга на интерфейсе {self.interface}")
        print(f"[*] Локальный IP: {self.local_ip}, MAC: {self.local_mac}")
        print(f"[*] Шлюз: IP {self.gateway_ip}, MAC: {self.gateway_mac}")
        print("[*] Нажмите Ctrl+C для остановки\n")
        
        self.running = True
        
        # Запуск проверки сетевого интерфейса на promiscuous mode
        promisc_checker = threading.Thread(target = self.check_promiscuous_mode)
        promisc_checker.daemon = True
        promisc_checker.start()
        
        # Запуск сниффера для обнаружения подозрительного трафика
        try:
            scapy.sniff(iface = self.interface, store = False, prn = self.process_packet)
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            print(f"[-] Ошибка: {e}")
            self.stop()

    def stop(self):
        """Остановка мониторинга"""
        self.running = False
        print("\n[*] Остановка детектора сниффинга")
        sys.exit(0)

    def get_local_ip(self):
        """Получение локального IP адреса"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]['addr']

    def get_local_mac(self):
        """Получение локального MAC адреса"""
        try:
            return netifaces.ifaddresses(self.interface)[netifaces.AF_LINK][0]['addr']
        except Exception as e:
            print(f"[-] Ошибка получения MAC адреса: {e}")
            return "unknown"

    def get_gateway_info(self):
        """Получение информации о шлюзе по умолчанию"""
        try:
            gateways = netifaces.gateways()
            default_gateway = gateways['default'][netifaces.AF_INET]
            gateway_ip = default_gateway[0]
            
            # Получаем MAC шлюза с помощью ARP запроса
            ans, _ = scapy.arping(gateway_ip, timeout = 2, verbose = False, iface = self.interface)
            if ans:
                gateway_mac = ans[0][1].hwsrc
                return gateway_ip, gateway_mac
        except Exception as e:
            print(f"[-] Ошибка получения информации о шлюзе: {e}")
        
        return "unknown", "unknown"

    def check_promiscuous_mode(self):
        """Проверка, находится ли интерфейс в promiscuous mode"""
        while self.running:
            try:
                with open(f"/sys/class/net/{self.interface}/flags") as f:
                    flags = int(f.read().strip(), 16)
                    promisc_mode = bool(flags & 0x100)  # Проверяем бит PROMISC
                    
                    if promisc_mode and not self.promiscuous_mode_warned:
                        self.send_alert(
                            "Обнаружен сетевой интерфейс в promiscuous mode",
                            f"Интерфейс {self.interface} находится в promiscuous mode, "
                            "что может указывать на активный сниффинг трафика."
                        )
                        self.promiscuous_mode_warned = True
                        print("[!] ВНИМАНИЕ: Сетевой интерфейс в promiscuous mode!")
                        
            except Exception as e:
                print(f"[-] Ошибка проверки promiscuous mode: {e}")
            
            time.sleep(self.check_interval)

    def process_packet(self, packet):
        """Анализ сетевых пакетов на признаки сниффинга"""
        # 1. Обнаружение ARP-запросов в большом количестве (может указывать на ARP-сканирование)
        if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 1:  # ARP-запрос
            src_mac = packet[scapy.ARP].hwsrc
            self.suspicious_devices[src_mac] += 1
            
            if self.suspicious_devices[src_mac] == 50:  # Порог для предупреждения
                self.send_alert(
                    "Подозрительная ARP активность",
                    f"Устройство с MAC {src_mac} отправило 50+ ARP-запросов, "
                    "что может указывать на ARP-сканирование сети."
                )
                print(f"[!] Подозрительная ARP активность от {src_mac}")
        
        # 2. Обнаружение необычно большого количества ICMP-запросов (может быть ping-сканирование)
        elif packet.haslayer(scapy.ICMP):
            src_ip = packet[scapy.IP].src
            src_mac = packet.src
            
            if src_ip != self.local_ip and src_mac != self.local_mac:
                self.suspicious_devices[src_mac] += 1
                
                if self.suspicious_devices[src_mac] == 100:  # Порог для предупреждения
                    self.send_alert(
                        "Подозрительная ICMP активность",
                        f"Устройство {src_ip} ({src_mac}) отправило 100+ ICMP-пакетов, "
                        "что может указывать на ping-сканирование сети."
                    )
                    print(f"[!] Подозрительная ICMP активность от {src_ip} ({src_mac})")
        
        # 3. Обнаружение DNS-запросов к подозрительным доменам (может быть DNS-туннелирование)
        elif packet.haslayer(scapy.DNSQR):
            dns_query = packet[scapy.DNSQR].qname.decode('utf-8', errors = 'ignore')
            suspicious_domains = ['exfiltration', 'tunnel', 'malicious', 'data.leak']
            
            if any(domain in dns_query.lower() for domain in suspicious_domains):
                src_ip = packet[scapy.IP].src
                self.send_alert(
                    "Подозрительный DNS-запрос",
                    f"Обнаружен DNS-запрос к подозрительному домену: {dns_query}\n"
                    f"Источник: {src_ip}"
                )
                print(f"[!] Подозрительный DNS-запрос: {dns_query} от {src_ip}")
        
        # 4. Обнаружение аномально больших объемов исходящего трафика (может быть утечка данных)
        if packet.haslayer(scapy.IP):
            if packet[scapy.IP].src == self.local_ip:
                size = len(packet)
                if size > 1500:  # Большие пакеты
                    dst_ip = packet[scapy.IP].dst
                    self.send_alert(
                        "Большой исходящий пакет",
                        f"Обнаружен большой исходящий пакет ({size} байт) "
                        f"на адрес {dst_ip}, что может указывать на утечку данных."
                    )
                    print(f"[!] Большой исходящий пакет ({size} байт) на {dst_ip}")

    def send_alert(self, subject, message):
        """Отправка предупреждения"""
        print(f"[ALERT] {subject}\n{message}")
        
        # Отправка email уведомления
        if self.alert_email:
            try:
                msg = MIMEText(message)
                msg['Subject'] = f'[ALERT] {subject}'
                msg['From'] = 'sniffing_detector@yourdomain.com'
                msg['To'] = self.alert_email
                
                # Настройте SMTP сервер согласно вашей конфигурации
                with smtplib.SMTP('localhost') as server:
                    server.send_message(msg)
                print(f"[+] Email предупреждение отправлено на {self.alert_email}")
            except Exception as e:
                print(f"[-] Ошибка при отправке email: {e}")

def get_arguments():
    parser = argparse.ArgumentParser(description = 'Детектор сетевого сниффинга')
    parser.add_argument('-i', '--interface', dest = 'interface', help = 'Сетевой интерфейс для мониторинга', required = True)
    parser.add_argument('-e', '--email', dest = 'email', help = 'Email для отправки предупреждений (необязательно)')
    parser.add_argument('-c', '--check-interval', dest = 'interval', type = int, default = 30, help = 'Интервал проверки в секундах (по умолчанию: 30)')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()
    detector = SniffingDetector(
        interface = args.interface,
        alert_email = args.email,
        check_interval = args.interval
    )
    detector.start()

# ===================================================================================================================================

# Разработка простого фаервола:

# Установите необходимые зависимости: sudo apt-get install iptables
# Дайте скрипту права на выполнение: chmod +x simple_firewall.py
# Загрузить правила из файла: sudo ./simple_firewall.py -c firewall_rules.json load
# Применить все правила: sudo ./simple_firewall.py apply
# Добавить правило: sudo ./simple_firewall.py add -p tcp --dst-port 80 -a ACCEPT -m "Allow HTTP"
# Блокировать IP: sudo ./simple_firewall.py block-ip 192.168.1.100 -m "Block attacker"
# Разрешить порт: sudo ./simple_firewall.py allow-port 22 -p tcp -m "Allow SSH"
# Блокировать порт: sudo ./simple_firewall.py block-port 23 -p tcp -m "Block Telnet"
# Показать все правила: sudo ./simple_firewall.py list
# Удалить правило по индексу: sudo ./simple_firewall.py delete 0
# Сбросить все правила: sudo ./simple_firewall.py reset

# Простой фаервол на Python с использованием iptables
#!/usr/bin/env python3
import subprocess
import argparse
import sys
import json
import os
from datetime import datetime

class SimpleFirewall:
    def __init__(self, config_file = None):
        self.config_file = config_file or "firewall_rules.json"
        self.rules = []
        self.chain_name = "PYTHON_FIREWALL"
        self.setup_firewall_chain()

    def setup_firewall_chain(self):
        """Создание специальной цепочки для нашего фаервола"""
        # Проверяем существует ли уже наша цепочка
        result = subprocess.run(
            ["sudo", "iptables", "-nL", self.chain_name],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        
        # Если цепочка не существует - создаем
        if result.returncode != 0:
            subprocess.run(["sudo", "iptables", "-N", self.chain_name])
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-j", self.chain_name])
            subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-j", self.chain_name])
            print(f"[+] Создана новая цепочка {self.chain_name}")

    def load_rules(self):
        """Загрузка правил из конфигурационного файла"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, "r") as f:
                    self.rules = json.load(f)
                print(f"[+] Загружено {len(self.rules)} правил из {self.config_file}")
            else:
                print(f"[-] Файл конфигурации {self.config_file} не найден")
        except Exception as e:
            print(f"[-] Ошибка загрузки правил: {e}")

    def save_rules(self):
        """Сохранение правил в конфигурационный файл"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.rules, f, indent = 4)
            print(f"[+] Правила сохранены в {self.config_file}")
        except Exception as e:
            print(f"[-] Ошибка сохранения правил: {e}")

    def apply_rules(self):
        """Применение всех правил"""
        # Сначала очищаем цепочку
        subprocess.run(["sudo", "iptables", "-F", self.chain_name])
        
        # Применяем каждое правило
        for rule in self.rules:
            self.add_rule(rule, save_to_config = False)
        
        print(f"[+] Применено {len(self.rules)} правил")

    def add_rule(self, rule, save_to_config = True):
        """Добавление нового правила"""
        try:
            # Формируем команду iptables
            cmd = ["sudo", "iptables", "-A", self.chain_name]
            
            # Указываем протокол если есть
            if rule.get("protocol"):
                cmd.extend(["-p", rule["protocol"]])
            
            # Указываем исходный адрес если есть
            if rule.get("src_ip"):
                cmd.extend(["-s", rule["src_ip"]])
            
            # Указываем порт назначения если есть
            if rule.get("dst_port"):
                cmd.extend(["--dport", str(rule["dst_port"])])
            
            # Указываем исходный порт если есть
            if rule.get("src_port"):
                cmd.extend(["--sport", str(rule["src_port"])])
            
            # Указываем интерфейс если есть
            if rule.get("interface"):
                cmd.extend(["-i", rule["interface"]])
            
            # Указываем действие
            cmd.extend(["-j", rule["action"].upper()])
            
            # Добавляем комментарий
            comment = rule.get("comment", "").replace(" ", "_")
            cmd.extend(["-m", "comment", "--comment", f"PYFW_{comment}"])
            
            # Выполняем команду
            subprocess.run(cmd, check=True)
            
            # Добавляем правило в конфиг
            if save_to_config:
                rule["timestamp"] = datetime.now().isoformat()
                self.rules.append(rule)
                self.save_rules()
            
            print(f"[+] Добавлено правило: {rule.get('comment')}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[-] Ошибка добавления правила: {e}")
            return False
        except Exception as e:
            print(f"[-] Ошибка: {e}")
            return False

    def delete_rule(self, rule_index):
        """Удаление правила по индексу"""
        try:
            if 0 <= rule_index < len(self.rules):
                # Находим правило в iptables по комментарию
                comment = self.rules[rule_index].get("comment", "").replace(" ", "_")
                result = subprocess.run(
                    ["sudo", "iptables", "-L", self.chain_name, "--line-numbers"],
                    stdout = subprocess.PIPE,
                    text = True
                )
                
                # Ищем правило с нашим комментарием
                for line in result.stdout.splitlines():
                    if f"PYFW_{comment}" in line:
                        line_num = line.split()[0]
                        subprocess.run(
                            ["sudo", "iptables", "-D", self.chain_name, line_num],
                            check = True
                        )
                        break
                
                # Удаляем правило из конфига
                del self.rules[rule_index]
                self.save_rules()
                print(f"[+] Правило {rule_index} удалено")
                return True
            else:
                print(f"[-] Неверный индекс правила: {rule_index}")
                return False
        except Exception as e:
            print(f"[-] Ошибка удаления правила: {e}")
            return False

    def list_rules(self):
        """Вывод списка всех правил"""
        print("\nТекущие правила фаервола:")
        print("-" * 80)
        for i, rule in enumerate(self.rules):
            print(f"{i}: {rule}")
        print("-" * 80)
        
        # Показываем также правила iptables
        print("\nАктивные правила в iptables:")
        subprocess.run(["sudo", "iptables", "-L", self.chain_name, "-n", "-v"])

    def block_ip(self, ip, comment = ""):
        """Блокировка IP адреса"""
        rule = {
            "src_ip": ip,
            "action": "DROP",
            "comment": f"Block {ip} {comment}".strip(),
            "timestamp": datetime.now().isoformat()
        }
        return self.add_rule(rule)

    def allow_port(self, port, protocol = "tcp", comment = ""):
        """Разрешение доступа к порту"""
        rule = {
            "dst_port": port,
            "protocol": protocol,
            "action": "ACCEPT",
            "comment": f"Allow {protocol.upper()} port {port} {comment}".strip(),
            "timestamp": datetime.now().isoftime()
        }
        return self.add_rule(rule)

    def block_port(self, port, protocol = "tcp", comment = ""):
        """Блокировка доступа к порту"""
        rule = {
            "dst_port": port,
            "protocol": protocol,
            "action": "DROP",
            "comment": f"Block {protocol.upper()} port {port} {comment}".strip(),
            "timestamp": datetime.now().isoformat()
        }
        return self.add_rule(rule)

    def reset_firewall(self):
        """Сброс всех правил фаервола"""
        subprocess.run(["sudo", "iptables", "-F", self.chain_name])
        self.rules = []
        self.save_rules()
        print("[+] Все правила фаервола сброшены")

def main():
    parser = argparse.ArgumentParser(description = "Простой фаервол на Python")
    parser.add_argument("-c", "--config", help = "Файл конфигурации правил", default = "firewall_rules.json")
    
    subparsers = parser.add_subparsers(dest = "command", help = "Команды")
    
    # Команда загрузки правил
    load_parser = subparsers.add_parser("load", help = "Загрузить правила из файла")
    
    # Команда применения правил
    apply_parser = subparsers.add_parser("apply", help = "Применить все правила")
    
    # Команда добавления правила
    add_parser = subparsers.add_parser("add", help = "Добавить новое правило")
    add_parser.add_argument("-p", "--protocol", help = "Протокол (tcp, udp, icmp и др.)")
    add_parser.add_argument("-s", "--src-ip", help = "Исходный IP адрес")
    add_parser.add_argument("--src-port", type = int, help = "Исходный порт")
    add_parser.add_argument("--dst-port", type = int, help = "Порт назначения")
    add_parser.add_argument("-i", "--interface", help = "Сетевой интерфейс")
    add_parser.add_argument("-a", "--action", required = True, choices = ["ACCEPT", "DROP", "REJECT"], help = "Действие для правила")
    add_parser.add_argument("-m", "--comment", default = "", help = "Комментарий к правилу")
    
    # Команда блокировки IP
    block_ip_parser = subparsers.add_parser("block-ip", help = "Блокировать IP адрес")
    block_ip_parser.add_argument("ip", help = "IP адрес для блокировки")
    block_ip_parser.add_argument("-m", "--comment", default = "", help = "Комментарий")
    
    # Команда разрешения порта
    allow_port_parser = subparsers.add_parser("allow-port", help = "Разрешить доступ к порту")
    allow_port_parser.add_argument("port", type = int, help = "Номер порта")
    allow_port_parser.add_argument("-p", "--protocol", default = "tcp", help = "Протокол (по умолчанию tcp)")
    allow_port_parser.add_argument("-m", "--comment", default = "", help = "Комментарий")
    
    # Команда блокировки порта
    block_port_parser = subparsers.add_parser("block-port", help = "Блокировать доступ к порту")
    block_port_parser.add_argument("port", type = int, help = "Номер порта")
    block_port_parser.add_argument("-p", "--protocol", default = "tcp", help = "Протокол (по умолчанию tcp)")
    block_port_parser.add_argument("-m", "--comment", default = "", help = "Комментарий")
    
    # Команда удаления правила
    delete_parser = subparsers.add_parser("delete", help = "Удалить правило по индексу")
    delete_parser.add_argument("index", type = int, help = "Индекс правила для удаления")
    
    # Команда списка правил
    list_parser = subparsers.add_parser("list", help = "Показать все правила")
    
    # Команда сброса
    reset_parser = subparsers.add_parser("reset", help = "Сбросить все правила фаервола")
    
    args = parser.parse_args()
    
    firewall = SimpleFirewall(args.config)
    firewall.load_rules()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "load":
        firewall.load_rules()
    elif args.command == "apply":
        firewall.apply_rules()
    elif args.command == "add":
        rule = {
            "protocol": args.protocol,
            "src_ip": args.src_ip,
            "src_port": args.src_port,
            "dst_port": args.dst_port,
            "interface": args.interface,
            "action": args.action,
            "comment": args.comment
        }
        firewall.add_rule(rule)
    elif args.command == "block-ip":
        firewall.block_ip(args.ip, args.comment)
    elif args.command == "allow-port":
        firewall.allow_port(args.port, args.protocol, args.comment)
    elif args.command == "block-port":
        firewall.block_port(args.port, args.protocol, args.comment)
    elif args.command == "delete":
        firewall.delete_rule(args.index)
    elif args.command == "list":
        firewall.list_rules()
    elif args.command == "reset":
        firewall.reset_firewall()

if __name__ == "__main__":
    main()

# ================================== Практическое задание: разработка сканера уязвимостей =====================================
import requests
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(level = logging.INFO)

# Функция для отправки запроса и получения ответа
def send_request(url):
    try:
        response = requests.get(url)
        return response
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

# Функция для проверки на SQL-инъекции
def check_sql_injection(url):
    payloads = ["'", "\"", "1' OR .'1'='1", "1\" OR \"1\"=\"1"]
    for payload in payloads:
        full_url = f"{url}{payload}"
        response = send_request(full_url)
        if response and ("error" in response.text or "SQL" in response.text):
            logging.info(f"Potential SQL Injection found at {full_url}")

# Функция для проверки на XSS
def check_xss(url):
    payloads = ["<script>alert('XSS')</script>","\"<script>alert('XSS')</script>"]
    for payload in payloads:
        response = send_request(url)
        if response and payload in response.text:
            logging.info(f"Potential XSS found at {url}")

# Основная функция сканера
def scan(url):
    logging.info(f"Scanning {url}")
    check_sql_injection(url)
    check_xss(url)

# Пример использования
if __name__== "__main__":
    target_url = "http://example.com/search?q="
    scan(target_url)

# =====================================================================================================================================
# Install required packages: pip install requests beautifulsoup4
# Run the scanner: python scanner.py http://example.com --threads 10

# Web Application Vulnerability Scanner
import requests
from bs4 import BeautifulSoup
import re
import logging
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler('vulnerability_scanner.log'),
        logging.StreamHandler()
    ]
)

class WebVulnerabilityScanner:
    def __init__(self, base_url, max_threads = 5):
        self.base_url = base_url
        self.session = requests.Session()
        self.max_threads = max_threads
        self.vulnerabilities_found = []
        
        # Set a reasonable timeout for requests
        self.session.timeout = 10
        
        # Common user agent to avoid blocking
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def send_request(self, url, method = 'GET', params = None, data = None):
        try:
            if method.upper() == 'GET':
                response = self.session.get(url, params = params)
            elif method.upper() == 'POST':
                response = self.session.post(url, data = data)
            else:
                logging.warning(f"Unsupported HTTP method: {method}")
                return None
            
            return response
        except requests.RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
            return None
    
    def check_sql_injection(self, url, params = None):
        """Check for SQL injection vulnerabilities"""
        payloads = [
            "'", "\"", 
            "' OR '1'='1", "\" OR \"1\"=\"1", 
            "' OR 1=1--", "\" OR 1=1--", 
            "1' ORDER BY 1--", 
            "1' UNION SELECT null,table_name FROM information_schema.tables--"
        ]
        
        for payload in payloads:
            test_params = params.copy() if params else {}
            for key in test_params.keys():
                test_params[key] = payload
                
            response = self.send_request(url, params = test_params)
            
            if response and self._detect_sql_errors(response.text):
                vulnerability = {
                    'type': 'SQL Injection',
                    'url': url,
                    'payload': payload,
                    'evidence': 'Database error message detected'
                }
                self._log_vulnerability(vulnerability)
                return
    
    def _detect_sql_errors(self, text):
        """Detect common SQL error patterns in response text"""
        sql_errors = [
            r"SQL syntax.*MySQL",
            r"Warning.*mysql_.*",
            r"Unclosed quotation mark",
            r"PostgreSQL.*ERROR",
            r"Microsoft SQL Server",
            r"ODBC Driver",
            r"ORA-[0-9]{4}",
            r"Syntax error.*SQL",
            r"Unclosed.*quotation mark"
        ]
        
        for error_pattern in sql_errors:
            if re.search(error_pattern, text, re.IGNORECASE):
                return True
        return False
    
    def check_xss(self, url, params = None):
        """Check for Cross-Site Scripting (XSS) vulnerabilities"""
        payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "\"><script>alert('XSS')</script>",
            "javascript:alert('XSS')",
            "<svg/onload=alert('XSS')>"
        ]
        
        for payload in payloads:
            test_params = params.copy() if params else {}
            for key in test_params.keys():
                test_params[key] = payload
                
            response = self.send_request(url, params = test_params)
            
            if response and payload in response.text:
                vulnerability = {
                    'type': 'XSS',
                    'url': url,
                    'payload': payload,
                    'evidence': 'Payload reflected in response'
                }
                self._log_vulnerability(vulnerability)
                return
    
    def check_csrf(self, url):
        """Check for missing CSRF protection tokens"""
        response = self.send_request(url)
        if not response:
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        
        for form in forms:
            if form.get('method', '').upper() == 'POST':
                csrf_tokens = form.find_all('input', {'name': re.compile(r'csrf|token', re.IGNORECASE)})
                if not csrf_tokens:
                    vulnerability = {
                        'type': 'Potential CSRF',
                        'url': url,
                        'evidence': 'Form without CSRF token found'
                    }
                    self._log_vulnerability(vulnerability)
    
    def check_directory_traversal(self, url):
        """Check for directory traversal vulnerabilities"""
        payloads = [
            "../../../../etc/passwd",
            "..%2F..%2F..%2Fetc%2Fpasswd",
            "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
        ]
        
        for payload in payloads:
            test_url = f"{url}?file={payload}" if '?' in url else f"{url}/{payload}"
            response = self.send_request(test_url)
            
            if response and ("root:x:" in response.text or "bin:x:" in response.text):
                vulnerability = {
                    'type': 'Directory Traversal',
                    'url': test_url,
                    'payload': payload,
                    'evidence': 'Sensitive file content detected'
                }
                self._log_vulnerability(vulnerability)
                return
    
    def check_command_injection(self, url, params = None):
        """Check for command injection vulnerabilities"""
        payloads = [
            ";id",
            "|id",
            "&&id",
            "||id",
            "\nid\n"
        ]
        
        for payload in payloads:
            test_params = params.copy() if params else {}
            for key in test_params.keys():
                test_params[key] = payload
                
            response = self.send_request(url, params = test_params)
            
            if response and ("uid=" in response.text or "groups=" in response.text):
                vulnerability = {
                    'type': 'Command Injection',
                    'url': url,
                    'payload': payload,
                    'evidence': 'Command output detected'
                }
                self._log_vulnerability(vulnerability)
                return
    
    def crawl_and_scan(self):
        """Crawl the website and scan all discovered pages"""
        logging.info(f"Starting scan of {self.base_url}")
        
        # Start with the base URL
        discovered_urls = set()
        queue = [self.base_url]
        
        while queue:
            current_url = queue.pop(0)
            
            if current_url in discovered_urls:
                continue
                
            discovered_urls.add(current_url)
            logging.info(f"Scanning: {current_url}")
            
            # Scan the current page
            self.scan_page(current_url)
            
            # Find links on the page to add to the queue
            response = self.send_request(current_url)
            if response:
                new_urls = self._extract_links(response.text, current_url)
                for url in new_urls:
                    if url not in discovered_urls and url.startswith(self.base_url):
                        queue.append(url)
        
        logging.info(f"Scan completed. Found {len(self.vulnerabilities_found)} vulnerabilities.")
        return self.vulnerabilities_found
    
    def _extract_links(self, html, base_url):
        """Extract all links from HTML content"""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        
        for tag in soup.find_all(['a', 'link', 'img', 'script', 'iframe']):
            url = tag.get('href', '') or tag.get('src', '')
            if url and not url.startswith(('javascript:', 'mailto:', 'tel:', '#')):
                absolute_url = urljoin(base_url, url)
                links.add(absolute_url)
        
        return links
    
    def scan_page(self, url):
        """Scan a single page for all vulnerabilities"""
        # Get the page first to analyze forms and parameters
        response = self.send_request(url)
        if not response:
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for GET parameters
        if '?' in url:
            base_url, query = url.split('?', 1)
            params = dict(pair.split('=') for pair in query.split('&') if '=' in pair)
            
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                executor.submit(self.check_sql_injection, base_url, params)
                executor.submit(self.check_xss, base_url, params)
                executor.submit(self.check_command_injection, base_url, params)
        
        # Check forms for POST parameters
        forms = soup.find_all('form')
        for form in forms:
            form_action = form.get('action', '')
            form_method = form.get('method', 'GET').upper()
            form_url = urljoin(url, form_action)
            
            inputs = form.find_all('input')
            form_data = {}
            for input_tag in inputs:
                if input_tag.get('type') in ['text', 'password', 'hidden', 'search']:
                    form_data[input_tag.get('name', '')] = 'test'
            
            if form_method == 'POST' and form_data:
                with ThreadPoolExecutor(max_workers = self.max_threads) as executor:
                    executor.submit(self.check_sql_injection, form_url, None, form_data)
                    executor.submit(self.check_xss, form_url, None, form_data)
                    executor.submit(self.check_command_injection, form_url, None, form_data)
        
        # Check for other vulnerabilities that don't need parameters
        self.check_csrf(url)
        self.check_directory_traversal(url)
    
    def _log_vulnerability(self, vulnerability):
        """Log and store found vulnerabilities"""
        self.vulnerabilities_found.append(vulnerability)
        logging.warning(
            f"VULNERABILITY FOUND: {vulnerability['type']} at {vulnerability['url']}\n"
            f"Payload: {vulnerability.get('payload', 'N/A')}\n"
            f"Evidence: {vulnerability.get('evidence', 'N/A')}\n"
        )


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description = 'Web Application Vulnerability Scanner')
    parser.add_argument('url', help = 'Base URL to scan')
    parser.add_argument('--threads', type = int, default = 5, help = 'Maximum number of threads')
    
    args = parser.parse_args()
    
    scanner = WebVulnerabilityScanner(args.url, args.threads)
    vulnerabilities = scanner.crawl_and_scan()
    
    # Print summary
    print("\n=== Scan Summary ===")
    print(f"Scanned URL: {args.url}")
    print(f"Total vulnerabilities found: {len(vulnerabilities)}")
    
    if vulnerabilities:
        print("\n=== Vulnerabilities Details ===")
        for vuln in vulnerabilities:
            print(f"\nType: {vuln['type']}")
            print(f"URL: {vuln['url']}")
            if 'payload' in vuln:
                print(f"Payload: {vuln['payload']}")
            print(f"Evidence: {vuln.get('evidence', 'N/A')}")

#  ================================== Практическое задание: создание инструмента для обнаружения АRР-отравления ===========================

from scapy.all import sniff, ARP
import logging

logging.basicConfig (level = logging. INFO, format = '%(asctime) s - %(message)s')

# Словарь для хранения IP и МАС адресов
ip_mac_mapping = {}

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        try:
            real_mac = ip_mac_mapping[packet[ARP].psrc]
            response_mac = packet[ARP].hwsrc
            if real_mac != response_mac:
                logging. warning(f"ARP Spoofing detected:{packet[ARP].psrc} is being spoofed. Real MAC: {real_mac}, Fake MAC: {response_mac}")
        except KeyError:
            ip_mac_mapping[packet[ARP].psrc]
            packet[ARP].hwsrc
       
def monitor_network(interface):
    logging. info(f"Starting ARP Spoofing detection on {interface}")
    sniff(store = False, prn = detect_arp_spoof, iface = interface)

if __name__== "__main__":
    network_interface = "eth0" # Замените на нужный интерфейс
    monitor_network(network_interface)

# =================================================================================================================================
# Install required packages: pip install scapy
# Run the monitor: sudo python arp_monitor.py
# Test with arpspoof: sudo arpspoof -i eth0 -t target_ip gateway_ip

# ARP Spoofing Detection Tool
#!/usr/bin/env python3
from scapy.all import sniff, ARP, get_if_hwaddr, get_if_addr
import logging
import time
import smtplib
from email.mime.text import MIMEText
from threading import Thread
import json
import os
import socket

# Configuration
CONFIG = {
    "network_interface": "eth0",  # Change to your network interface
    "log_file": "arp_monitor.log",
    "alert_email": {
        "enabled": False,  # Set to True to enable email alerts
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "smtp_user": "your_email@example.com",
        "smtp_password": "your_password",
        "recipient": "admin@example.com"
    },
    "alert_threshold": 3,  # Number of violations before alert
    "whitelist": [],  # List of trusted MAC addresses
    "persistent_mapping": True,  # Save IP-MAC mappings between runs
    "mapping_file": "ip_mac_mappings.json"
}

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(CONFIG['log_file']),
        logging.StreamHandler()
    ]
)

class ARPMonitor:
    def __init__(self):
        self.ip_mac_mapping = {}
        self.suspicious_activity = {}
        self.interface = CONFIG['network_interface']
        self.self_mac = get_if_hwaddr(self.interface)
        self.self_ip = get_if_addr(self.interface)
        
        # Load persistent mappings if enabled
        if CONFIG['persistent_mapping'] and os.path.exists(CONFIG['mapping_file']):
            try:
                with open(CONFIG['mapping_file'], 'r') as f:
                    self.ip_mac_mapping = json.load(f)
                logging.info(f"Loaded {len(self.ip_mac_mapping)} IP-MAC mappings from file")
            except Exception as e:
                logging.error(f"Failed to load mappings: {e}")
        
        # Initialize whitelist with gateway and local MACs
        self.whitelist = set(CONFIG['whitelist'])
        self.whitelist.add(self.self_mac.lower())
        
        logging.info(f"Starting ARP monitor on interface {self.interface}")
        logging.info(f"Local IP: {self.self_ip}, MAC: {self.self_mac}")

    def detect_arp_spoof(self, packet):
        """Analyze ARP packets for spoofing attempts"""
        if packet.haslayer(ARP):
            arp = packet[ARP]
            
            # Only analyze responses (op=2 is reply)
            if arp.op == 2:
                src_ip = arp.psrc
                src_mac = arp.hwsrc.lower()
                
                # Ignore our own ARP responses
                if src_mac == self.self_mac.lower():
                    return
                
                # Check if MAC is in whitelist
                if src_mac in self.whitelist:
                    return
                
                # Check for existing mapping
                if src_ip in self.ip_mac_mapping:
                    stored_mac = self.ip_mac_mapping[src_ip].lower()
                    
                    # Detect ARP spoofing
                    if stored_mac != src_mac:
                        self.handle_spoofing_attempt(src_ip, stored_mac, src_mac)
                else:
                    # New mapping - store it
                    self.ip_mac_mapping[src_ip] = src_mac
                    logging.info(f"Learned new mapping: {src_ip} -> {src_mac}")
    
    def handle_spoofing_attempt(self, ip, real_mac, spoofed_mac):
        """Handle detected ARP spoofing attempts"""
        # Track suspicious activity
        key = f"{ip}_{spoofed_mac}"
        self.suspicious_activity[key] = self.suspicious_activity.get(key, 0) + 1
        
        # Log warning
        warning_msg = (f"ARP Spoofing detected! IP: {ip} is being spoofed. "
                      f"Real MAC: {real_mac}, Fake MAC: {spoofed_mac} "
                      f"(Count: {self.suspicious_activity[key]})")
        logging.warning(warning_msg)
        
        # Send alert if threshold reached
        if self.suspicious_activity[key] >= CONFIG['alert_threshold']:
            self.send_alert(ip, real_mac, spoofed_mac)
    
    def send_alert(self, ip, real_mac, spoofed_mac):
        """Send alert about ARP spoofing"""
        hostname = socket.gethostname()
        subject = f"[ALERT] ARP Spoofing Detected on {hostname}"
        message = (
            f"ARP Spoofing attack detected!\n\n"
            f"IP Address: {ip}\n"
            f"Legitimate MAC: {real_mac}\n"
            f"Spoofed MAC: {spoofed_mac}\n\n"
            f"Timestamp: {time.ctime()}\n"
            f"Host: {hostname}\n"
            f"Interface: {self.interface}"
        )
        
        # Log alert
        logging.critical(f"Sending alert about ARP spoofing: {ip} -> {spoofed_mac}")
        
        # Email alert
        if CONFIG['alert_email']['enabled']:
            Thread(target = self.send_email_alert, args = (subject, message)).start()
    
    def send_email_alert(self, subject, message):
        """Send email alert"""
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = CONFIG['alert_email']['smtp_user']
            msg['To'] = CONFIG['alert_email']['recipient']
            
            with smtplib.SMTP(
                CONFIG['alert_email']['smtp_server'],
                CONFIG['alert_email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    CONFIG['alert_email']['smtp_user'],
                    CONFIG['alert_email']['smtp_password']
                )
                server.send_message(msg)
            
            logging.info("Email alert sent successfully")
        except Exception as e:
            logging.error(f"Failed to send email alert: {e}")
    
    def save_mappings(self):
        """Save IP-MAC mappings to file"""
        if CONFIG['persistent_mapping']:
            try:
                with open(CONFIG['mapping_file'], 'w') as f:
                    json.dump(self.ip_mac_mapping, f)
                logging.info(f"Saved {len(self.ip_mac_mapping)} IP-MAC mappings to file")
            except Exception as e:
                logging.error(f"Failed to save mappings: {e}")
    
    def start_monitoring(self):
        """Start monitoring network for ARP spoofing"""
        try:
            logging.info("Starting network monitoring...")
            sniff(
                store = False,
                prn = self.detect_arp_spoof,
                iface = self.interface,
                filter = "arp"
            )
        except KeyboardInterrupt:
            logging.info("Stopping ARP monitor...")
            self.save_mappings()
        except Exception as e:
            logging.error(f"Error in monitoring: {e}")
            self.save_mappings()

def main():
    monitor = ARPMonitor()
    monitor.start_monitoring()

if __name__ == "__main__":
    main()

#  =========================== Практическое задание: реализация инструмента для обнаружения сетевого сниффинга =========================

from scapy.all import sniff
import psutil
import logging

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(message)s')

# Функция для анализа пакетов
def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"] .src
        dst_ip = packet["IP"].dst
        logging.info(f"Packet: {src_ip} -> {dst_ip}")

# Функция для мониторинга сети
def monitor_network(interface):
    logging.info(f"Starting network monitoring on {interface}")
    sniff(iface = interface, prn = packet_callback, store = False)

if __name__== "__main__":
    network_interface = psutil.net_if_addrs().keys() # Получение списка сетевых интерфейсов
    monitor_network(network_interface[0]) # Используйте нужный интерфейс

# -------------------------------------------------------------------------------------------------------------

from scapy.all import ARP, sniff

# Функция для анализа АRР-пакетов
def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        try:
            real_mac = ip_mac_mapping[packet[ARP].psrc]
            response_mac = packet[ARP].hwsrc
            if real_mac != response_mac:
                logging.warning(f"ARP Spoofing detected:{packet[ARP].psrc} is being spoofed. Real MAC: {real_mac}, Fake MAC: {response_mac}")
        except KeyError:
            ip_mac_mapping[packet[ARP].psrc] = packet[ARP].hwsrc
            sniff(store = False, prn = detect_arp_spoof, iface = interface)

# -------------------------------------------------------------------------------------------------------------------

import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg["Subject"] = "Network Alert"
    msg["From"] = "your_email@example.com"
    msg["To"] = "admin@example.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_email@example.com", "admin@example.com", msg.as_string())

# Используйте функцию send_alert в анализе пакетов
if real_mac != response_mac:
    message = f"ARP Spoofing detected: {packet[ARP].psrc} is being spoofed. Real MAC: {real_mac}, Fake MAC: {response_mac}"
    logging.warning(message)
    send_alert(message)

# ----------------------------------------------------------------------------------------------------------------------------

from scapy.all import sniff, ARP
import logging
import smtplib
from email.mime.text import MIМEText

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(message)s')
ip_mac_mapping = { }

def send_alert(message):
    msg = MIМEText(message)
    msg["Subject"] = "Network Alert"
    msg["From"] = "your_email@example.com"
    msg-["To"] = "admin@example.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_ernail@exarnple.com", "admin@example.corn", msg.as_string())

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        real_rnac = ip_mac_mapping.get(packet[ARP].psrc)
        response_mac = packet[ARP].hwsrc

        if real_rnac and real_rnac != response_mac:
            rnessage = f"ARP Spoofing detected: {packet[ARP].psrc} is being spoofed. Real MAC: {real_mac}, Fake MAC: {response_mac}"
            logging.warning(message)
            send_alert(rnessage)
    else:
        response_mac
        ip_mac_mapping[packet[ARP].psrc]

def rnonitor_network(interface):
    logging.info(f"Starting ARP Spoofing detection on {interface}")
    sniff(store = False, prn = detect_arp_spoof, iface = interface)

if __name__=="__main__":
    network_interface = "eth0" # Замените на нужный интерфейс
    rnonitor_network(network_interface)

# ==========================================================================================================================================

# Install required packages: pip install scapy psutil
# Run the monitor (requires root privileges): sudo python network_monitor.py
# Test with ARP spoofing tools: sudo arpspoof -i eth0 -t target_ip gateway_ip
# Test port scanning: nmap -sS target_ip

# Network Sniffing Detection Tool
#!/usr/bin/env python3
from scapy.all import sniff, Ether, IP, TCP, UDP, ARP, get_if_hwaddr
import logging
import time
import smtplib
from email.mime.text import MIMEText
from threading import Thread, Lock
import json
import os
import socket
from collections import defaultdict
import psutil

# Configuration
CONFIG = {
    "network_interface": "eth0",  # Change to your network interface
    "log_file": "network_monitor.log",
    "alert_email": {
        "enabled": True,
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "smtp_user": "your_email@example.com",
        "smtp_password": "your_password",
        "recipient": "admin@example.com"
    },
    "detection_thresholds": {
        "arp_spoofing": 3,
        "unusual_packet_rate": 1000,  # Packets per second
        "promiscuous_mode": True,
        "dns_spoofing": True
    },
    "whitelist": {
        "mac_addresses": [],
        "ip_addresses": []
    },
    "monitoring": {
        "arp": True,
        "tcp": True,
        "udp": True,
        "dns": True
    }
}

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(CONFIG['log_file']),
        logging.StreamHandler()
    ]
)

class NetworkMonitor:
    def __init__(self):
        self.interface = CONFIG['network_interface']
        self.self_mac = get_if_hwaddr(self.interface)
        self.self_ip = self._get_interface_ip()
        
        # Data structures for detection
        self.ip_mac_mapping = {}
        self.packet_counts = defaultdict(int)
        self.suspicious_activity = defaultdict(int)
        self.lock = Lock()
        
        # Initialize whitelists
        self.mac_whitelist = set(mac.lower() for mac in CONFIG['whitelist']['mac_addresses'])
        self.mac_whitelist.add(self.self_mac.lower())
        self.ip_whitelist = set(CONFIG['whitelist']['ip_addresses'])
        self.ip_whitelist.add(self.self_ip)
        
        logging.info(f"Starting network monitor on interface {self.interface}")
        logging.info(f"Local IP: {self.self_ip}, MAC: {self.self_mac}")
        
        # Start background thread for rate monitoring
        self._running = True
        self.monitor_thread = Thread(target = self._monitor_packet_rates)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
    
    def _get_interface_ip(self):
        """Get the IP address of the monitoring interface"""
        addrs = psutil.net_if_addrs().get(self.interface, [])
        for addr in addrs:
            if addr.family == socket.AF_INET:
                return addr.address
        return ""
    
    def packet_handler(self, packet):
        """Handle incoming packets and perform detection"""
        try:
            # Check for promiscuous mode
            if self._check_promiscuous_mode(packet):
                self._handle_alert("Promiscuous mode detected", packet.summary())
            
            # Layer-specific analysis
            if packet.haslayer(ARP) and CONFIG['monitoring']['arp']:
                self._analyze_arp(packet)
            
            if packet.haslayer(IP):
                ip = packet[IP]
                
                # Check for unusual packet rates
                with self.lock:
                    self.packet_counts[ip.src] += 1
                
                # TCP analysis
                if packet.haslayer(TCP) and CONFIG['monitoring']['tcp']:
                    self._analyze_tcp(packet)
                
                # UDP analysis
                if packet.haslayer(UDP) and CONFIG['monitoring']['udp']:
                    self._analyze_udp(packet)
                
                # DNS analysis
                if packet.haslayer(DNS) and CONFIG['monitoring']['dns']:
                    self._analyze_dns(packet)
        
        except Exception as e:
            logging.error(f"Error processing packet: {e}")

    def _analyze_arp(self, packet):
        """Analyze ARP packets for spoofing"""
        arp = packet[ARP]
        
        # Only analyze replies (op=2)
        if arp.op == 2:
            src_ip = arp.psrc
            src_mac = arp.hwsrc.lower()
            
            # Ignore our own ARP responses
            if src_mac == self.self_mac.lower():
                return
            
            # Check if MAC is in whitelist
            if src_mac in self.mac_whitelist:
                return
            
            # Check for existing mapping
            if src_ip in self.ip_mac_mapping:
                stored_mac = self.ip_mac_mapping[src_ip].lower()
                
                # Detect ARP spoofing
                if stored_mac != src_mac:
                    key = f"arp_spoof_{src_ip}_{src_mac}"
                    self.suspicious_activity[key] += 1
                    
                    if self.suspicious_activity[key] >= CONFIG['detection_thresholds']['arp_spoofing']:
                        self._handle_alert(
                            "ARP Spoofing detected",
                            f"IP: {src_ip} is being spoofed. Real MAC: {stored_mac}, Fake MAC: {src_mac}"
                        )
            else:
                # New mapping - store it
                self.ip_mac_mapping[src_ip] = src_mac
                logging.info(f"Learned new ARP mapping: {src_ip} -> {src_mac}")

    def _analyze_tcp(self, packet):
        """Analyze TCP packets for suspicious activity"""
        ip = packet[IP]
        tcp = packet[TCP]
        
        # Detect port scanning (many SYN packets to different ports)
        if tcp.flags == "S":  # SYN flag set
            key = f"tcp_scan_{ip.src}"
            self.suspicious_activity[key] += 1
            
            if self.suspicious_activity[key] > 50:  # Threshold for port scanning
                self._handle_alert(
                    "Possible TCP port scan detected",
                    f"Source IP: {ip.src} is sending many SYN packets"
                )

    def _analyze_udp(self, packet):
        """Analyze UDP packets for suspicious activity"""
        ip = packet[IP]
        udp = packet[UDP]
        
        # Detect UDP flood (many UDP packets)
        key = f"udp_flood_{ip.src}"
        self.suspicious_activity[key] += 1
        
        if self.suspicious_activity[key] > 1000:  # Threshold for UDP flood
            self._handle_alert(
                "Possible UDP flood detected",
                f"Source IP: {ip.src} is sending many UDP packets"
            )

    def _analyze_dns(self, packet):
        """Analyze DNS packets for spoofing attempts"""
        dns = packet[DNS]
        
        # Check for DNS responses with potentially spoofed answers
        if dns.qr == 1:  # DNS response
            if dns.an and any(attr for attr in ['a', 'aaaa', 'cname'] if hasattr(dns.an[0], attr)):
                # Check if response is coming from unexpected source
                if packet[IP].src not in self.ip_whitelist:
                    self._handle_alert(
                        "Possible DNS spoofing",
                        f"DNS response from unexpected source: {packet[IP].src}"
                    )

    def _check_promiscuous_mode(self, packet):
        """Check for signs of promiscuous mode sniffing"""
        # Check for packets not addressed to our MAC but with our IP
        if Ether in packet and IP in packet:
            if (packet[Ether].dst.lower() != self.self_mac.lower() and
                packet[IP].dst == self.self_ip):
                return True
        return False

    def _monitor_packet_rates(self):
        """Monitor packet rates for unusual activity"""
        while self._running:
            time.sleep(10)  # Check every 10 seconds
            
            with self.lock:
                current_counts = self.packet_counts.copy()
                self.packet_counts.clear()
            
            for ip, count in current_counts.items():
                if count > CONFIG['detection_thresholds']['unusual_packet_rate']:
                    self._handle_alert(
                        "High packet rate detected",
                        f"IP: {ip} is sending {count} packets per 10 seconds"
                    )

    def _handle_alert(self, alert_type, details):
        """Handle security alerts"""
        hostname = socket.gethostname()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        message = (
            f"Network Security Alert\n\n"
            f"Type: {alert_type}\n"
            f"Details: {details}\n\n"
            f"Timestamp: {timestamp}\n"
            f"Host: {hostname}\n"
            f"Interface: {self.interface}"
        )
        
        # Log alert
        logging.critical(f"{alert_type}: {details}")
        
        # Email alert
        if CONFIG['alert_email']['enabled']:
            Thread(target = self._send_email_alert, args = (alert_type, message)).start()

    def _send_email_alert(self, subject, message):
        """Send email alert"""
        try:
            msg = MIMEText(message)
            msg['Subject'] = f"[ALERT] {subject}"
            msg['From'] = CONFIG['alert_email']['smtp_user']
            msg['To'] = CONFIG['alert_email']['recipient']
            
            with smtplib.SMTP(
                CONFIG['alert_email']['smtp_server'],
                CONFIG['alert_email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    CONFIG['alert_email']['smtp_user'],
                    CONFIG['alert_email']['smtp_password']
                )
                server.send_message(msg)
            
            logging.info("Email alert sent successfully")
        except Exception as e:
            logging.error(f"Failed to send email alert: {e}")

    def start_monitoring(self):
        """Start network monitoring"""
        try:
            logging.info("Starting network traffic monitoring...")
            sniff(
                iface = self.interface,
                prn = self.packet_handler,
                store = False,
                filter = "arp or (ip and (tcp or udp))"
            )
        except KeyboardInterrupt:
            logging.info("Stopping network monitor...")
            self._running = False
            self.monitor_thread.join()
        except Exception as e:
            logging.error(f"Error in monitoring: {e}")
            self._running = False
            self.monitor_thread.join()

def main():
    monitor = NetworkMonitor()
    monitor.start_monitoring()

if __name__ == "__main__":
    main()

# ==================================== Практическое задание: разработка простого файрвола ==========================================

from netfilterqueue import NetfilterQueue
from scapy.all import IP, ТСР, UDP, ICMP
import logging

logging.basicConfig(level = logging.INFO, format = '% (asctime)s - % (message)s')

# Правила фильтрации
rules = [
    {'action': 'DROP', 'protocol': 'ТСР', 'port': 80},
    {'action': 'DROP', 'protocol': 'UDP', 'port': 53},
    { 'action' : 'АССЕРТ', 'protocol': 'ICMP'}
]

# Функция для применения правил фильтрации
def apply_rules(packet):
    scapy_packet = IP(packet.get_payload())
    for rule in rules:
        if rule['protocol'] == 'ТСР' and scapy_packet.haslayer(TCP) and scapy_packet[TCP].dport == rule['port']:
            if rule['action'] == 'DROP':
                logging.info(f"Dropped ТСР packet: {scapy_packet.summary()} ")
                packet.drop()
                return
        elif rule['protocol'] == 'UDP' and scapy_packet.haslayer(UDP) and scapy_packet[UDP].dport == rule['port']:
            if rule['action'] == 'DROP':
                logging.info(f"Dropped UDP packet: {scapy_packet.summary()}")
                packet.drop()
                return
        elif rule ['protocol'] == 'ICMP' and scapy_packet.haslayer(ICMP):
            if rule [ 'action' ] == 'DROP' :
                logging.info(f"Dropped ICMP packet: {scapy_packet.surnmary()}")
                packet.drop()
                return
    packet.accept()

# Функция для запуска фаервола
def start_firewall () :
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, apply_rules)
    try:
        logging.info("Starting firewall")
        nfqueue.run()
    except KeyboardInterrupt:
        logging.info("Stopping firewall")
        nfqueue.unbind()

if __name__=="__main__":
    start_firewall()

# ------------------------------------------------------------------------------------------------------------------------

import signal

def load_rules():
    # Загрузка правил из конфигурационного файла или базы данных
    return [
        {'action': 'DROP', 'protocol': 'ТСР', 'port': 80},
        {'action': 'DROP', 'protocol': 'UDP', 'port': 53},
        {'action': 'АССЕ РТ', 'protocol': 'ICMP' }
    ]

def reload_rules(signum, frame):
    global rules
    rules = load_rules()
    logging.info("Rules reloaded")

if __name__ == "__main__":
    signal.signal(signal.SIGHUP, reload_rules)
    rules = load_rules()
    start_firewall()

# ======================================================================================================================================================

# Install dependencies: pip install netfilterqueue scapy
# Run the firewall (requires root): sudo python firewall.py


# Python Firewall with Advanced Features
#!/usr/bin/env python3
from netfilterqueue import NetfilterQueue
from scapy.all import IP, TCP, UDP, ICMP, DNS, DHCP, IPv6
import logging
import signal
import json
import os
import threading
import time
from datetime import datetime

# Configuration
CONFIG = {
    "log_file": "firewall.log",
    "rules_file": "firewall_rules.json",
    "queue_num": 1,
    "enable_ipv6": False,
    "default_policy": "DROP"  # Default action if no rules match (ACCEPT/DROP)
}

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(CONFIG['log_file']),
        logging.StreamHandler()
    ]
)

class PyFirewall:
    def __init__(self):
        self.rules = []
        self.rule_lock = threading.Lock()
        self.running = True
        self.nfqueue = NetfilterQueue()
        
        # Load initial rules
        self.load_rules()
        
        # Set up signal handlers
        signal.signal(signal.SIGHUP, self.reload_rules)
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        
        logging.info("PyFirewall initialized")

    def load_rules(self):
        """Load rules from JSON file"""
        try:
            if os.path.exists(CONFIG['rules_file']):
                with open(CONFIG['rules_file'], 'r') as f:
                    new_rules = json.load(f)
                
                with self.rule_lock:
                    self.rules = new_rules
                
                logging.info(f"Loaded {len(new_rules)} firewall rules")
                return True
            else:
                logging.warning(f"Rules file {CONFIG['rules_file']} not found")
                return False
        except Exception as e:
            logging.error(f"Error loading rules: {e}")
            return False

    def reload_rules(self, signum = None, frame = None):
        """Reload rules on SIGHUP"""
        logging.info("Received SIGHUP, reloading rules...")
        self.load_rules()

    def packet_handler(self, packet):
        """Process each network packet"""
        try:
            scapy_packet = IP(packet.get_payload())
            action = self.evaluate_packet(scapy_packet)
            
            if action == "DROP":
                packet.drop()
                self.log_packet(scapy_packet, "DROPPED")
            else:
                packet.accept()
                self.log_packet(scapy_packet, "ALLOWED")
                
        except Exception as e:
            logging.error(f"Error processing packet: {e}")
            packet.accept()  # Default to accept if there's an error

    def evaluate_packet(self, packet):
        """Evaluate packet against firewall rules"""
        with self.rule_lock:
            for rule in self.rules:
                if self._match_rule(packet, rule):
                    return rule['action']
        
        return CONFIG['default_policy']

    def _match_rule(self, packet, rule):
        """Check if packet matches a specific rule"""
        try:
            # Protocol matching
            if 'protocol' in rule:
                if rule['protocol'] == 'TCP' and not packet.haslayer(TCP):
                    return False
                if rule['protocol'] == 'UDP' and not packet.haslayer(UDP):
                    return False
                if rule['protocol'] == 'ICMP' and not packet.haslayer(ICMP):
                    return False
                if rule['protocol'] == 'DNS' and not packet.haslayer(DNS):
                    return False
                if rule['protocol'] == 'DHCP' and not packet.haslayer(DHCP):
                    return False

            # IP address matching
            if 'src_ip' in rule and packet[IP].src not in rule['src_ip']:
                return False
            if 'dst_ip' in rule and packet[IP].dst not in rule['dst_ip']:
                return False

            # Port matching
            if 'src_port' in rule:
                if packet.haslayer(TCP) and packet[TCP].sport not in rule['src_port']:
                    return False
                if packet.haslayer(UDP) and packet[UDP].sport not in rule['src_port']:
                    return False

            if 'dst_port' in rule:
                if packet.haslayer(TCP) and packet[TCP].dport not in rule['dst_port']:
                    return False
                if packet.haslayer(UDP) and packet[UDP].dport not in rule['dst_port']:
                    return False

            # Interface matching
            if 'in_interface' in rule and packet.get('in_interface', '') not in rule['in_interface']:
                return False
            if 'out_interface' in rule and packet.get('out_interface', '') not in rule['out_interface']:
                return False

            return True

        except Exception as e:
            logging.error(f"Error matching rule: {e}")
            return False

    def log_packet(self, packet, action):
        """Log packet details"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'src_ip': packet[IP].src if IP in packet else '',
            'dst_ip': packet[IP].dst if IP in packet else '',
            'protocol': '',
            'src_port': '',
            'dst_port': '',
            'length': len(packet)
        }

        if packet.haslayer(TCP):
            log_entry['protocol'] = 'TCP'
            log_entry['src_port'] = packet[TCP].sport
            log_entry['dst_port'] = packet[TCP].dport
        elif packet.haslayer(UDP):
            log_entry['protocol'] = 'UDP'
            log_entry['src_port'] = packet[UDP].sport
            log_entry['dst_port'] = packet[UDP].dport
        elif packet.haslayer(ICMP):
            log_entry['protocol'] = 'ICMP'
        elif packet.haslayer(DNS):
            log_entry['protocol'] = 'DNS'
        elif packet.haslayer(DHCP):
            log_entry['protocol'] = 'DHCP'

        logging.info(
            f"{action} {log_entry['protocol']} packet: "
            f"{log_entry['src_ip']}:{log_entry['src_port']} -> "
            f"{log_entry['dst_ip']}:{log_entry['dst_port']}"
        )

    def start(self):
        """Start the firewall"""
        try:
            logging.info(f"Starting PyFirewall on queue {CONFIG['queue_num']}")
            self.nfqueue.bind(CONFIG['queue_num'], self.packet_handler)
            
            # Set up iptables rules
            self._setup_iptables()
            
            self.nfqueue.run()
        except Exception as e:
            logging.error(f"Firewall error: {e}")
            self.shutdown()

    def _setup_iptables(self):
        """Configure iptables to redirect packets to our queue"""
        try:
            # Flush existing rules
            os.system("iptables -F")
            os.system("iptables -X")
            
            # Redirect inbound traffic to our queue
            os.system(f"iptables -A INPUT -j NFQUEUE --queue-num {CONFIG['queue_num']}")
            os.system(f"iptables -A FORWARD -j NFQUEUE --queue-num {CONFIG['queue_num']}")
            
            # Allow established connections
            os.system("iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
            
            # Allow local traffic
            os.system("iptables -A INPUT -i lo -j ACCEPT")
            
            logging.info("iptables rules configured")
        except Exception as e:
            logging.error(f"Error configuring iptables: {e}")

    def _cleanup_iptables(self):
        """Clean up iptables rules"""
        try:
            os.system("iptables -F")
            os.system("iptables -X")
            logging.info("iptables rules cleaned up")
        except Exception as e:
            logging.error(f"Error cleaning up iptables: {e}")

    def shutdown(self, signum = None, frame = None):
        """Clean shutdown of the firewall"""
        logging.info("Shutting down PyFirewall...")
        self.running = False
        self._cleanup_iptables()
        self.nfqueue.unbind()
        logging.info("PyFirewall stopped")

def main():
    firewall = PyFirewall()
    firewall.start()

if __name__ == "__main__":
    main()

# Example Firewall Rules (firewall_rules.json)
[
    {
        "action": "ACCEPT",
        "protocol": "TCP",
        "dst_port": [22],
        "description": "Allow SSH"
    },
    {
        "action": "ACCEPT",
        "protocol": "TCP",
        "dst_port": [80, 443],
        "description": "Allow HTTP/HTTPS"
    },
    {
        "action": "ACCEPT",
        "protocol": "UDP",
        "dst_port": [53],
        "description": "Allow DNS"
    },
    {
        "action": "DROP",
        "protocol": "TCP",
        "dst_port": [23],
        "description": "Block Telnet"
    },
    {
        "action": "DROP",
        "protocol": "ICMP",
        "description": "Block ping requests"
    },
    {
        "action": "DROP",
        "src_ip": ["10.0.0.100"],
        "description": "Block traffic from specific IP"
    }
]