# =============================== Основы кибербезопасности =============================================

# Как вам уже известно, концепция кибербезопасности является ключевым аспектом в современном информационном мире, 
# где данные играют крити­ческую роль в повседневной жизни как для индивидуумов, так и для органи­заций.

# Пример использования криптографии для защиты данных
from cryptography.fernet import Fernet

# Генерируем ключ
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифруем данные
message = "Секретные данные"
encrypted_message = cipher.encrypt(message.encode())

# Расшифровываем данные
decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Иcxoднoe сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
# Защита целостности данных
# Пример использования хэш-функций для проверки целостности данных
import hashlib

# Создаем хэш сообщения
message = "Секретное сообщение"
hash_value = hashlib.sha256(message.encode()).hexdigest()

# Предположим, ч-rо данные были изменены
modified_message = "Измененное сообщение"

# Проверяем целостность данных
new_hash_value = hashlib.sha256(modified_message.encode()).hexdigest()
if hash_value == new_hash_value:
    print("Целостность данных подтверждена")
else:
    print("Данные были изменены")


# Защита доступности данных
# Пример использования резервного копирования для обеспечения доступности данных
import shutil

# Создаем резервную копию файла
source_file = "important_document. txt"
backup_file = "backup_important_document.txt"

shutil.copy(source_file, backup_file)

print("Резервная копия создана:", backup_file)

# Шифрование и расшифровка данных:
from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифрование данных
message = "Секретные данные"
encrypted_message = cipher.encrypt(message.encode())

# Расшифровка данных
decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Иcxoднoe сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)


# Snort - открытый IDS, который может анализировать трафик в режиме реального времени и обнаруживать атаки с использованием сигнатур.
# sudo apt-get install snort
# snort -А console -i ethO -с /etc/snort/snort.conf

# Suricata - система обнаружения вторжений в реальном времени, кото­рая может анализировать сетевой трафик и обнаруживать атаки.
# sudo apt-get install suricata
# suricata -с /etc/suricata/suricata.yaml -i eth0

# Snort с активированной функцией IPS:
# sudo snort -А console -Q -с /etc/snort/snort.conf -i eth0

# OSSEC - Система мониторинга журналов и обнаружения вторжений с открытым исходным кодом.
# sudo apt-get install ossec-hids
# sudo /var/ossec/Ыn/ossec-control start

# Wireshark - популярный инструмент для анализа сетевого трафика.
# sudo apt-get install wireshark
# wireshark

# Zeek (ранее известный как Bro) - система мониторинга сети и анализа трафика
# sudo apt-get install zeek
# zeekctl deploy

# ELK Stack (Elasticsearch, Logstash, Kibana) с интеграцией машинного обучения для анализа и визуализации данных.
# sudo apt-get install elasticsearch logstash kibana

# Мониторинг сетевого трафика:
import pyshark

# Запуск захвата сетевого трафика
capture = pyshark.LiveCapture(interface = 'eth0')

# Обработка пакетов
for packet in capture.sniff_continuously(packet_count = 10):
    # Анализ пакетов для обнаружения подозрительной активности
    print(packet)


# Анализ журналов событий:
# Python также может быть использован для анализа и мониторинга системных журналов для обнаружения необычной активности.
import subprocess
# Чтение системных журналов
command = "journalctl -p 3 -n 10" # Получить 10 последних сообщений с приоритетом выше 3
result = subprocess.run(command, shell = True, capture_output = True, text = True)

# Анализ журналов для обнаружения подозрительной активности
print(result.stdout)

# Существует несколько IDS-систем с открытым исходным кодом, которые могут быть интегрированы с Python для обнаружения аномалий в сети, 
# та­кие как Suricata или Snort.
# Использование систем обнаружения вторжений (IDS):
import os
# Запуск Suricata для мониторинга сетевого трафика
os.system("suricata -с suricata.yaml -i eth0")

# Мониторинг сетевого трафика с использованием библиотеки PyShark
import pyshark

# Запуск захвата сетевого трафика
capture = pyshark.LiveCapture(interface = 'eth0')

# Обработка пакетов
for packet in capture.sniff_continuously(packet_count = 10):
    # Анализ пакетов для обнаружения подозрительной активности
    print(packet)

# Анализ журналов событий Linux
import subprocess

# Чтение системных журналов
command = "journalctl -p 3 -n 10" # Получить 10 последних сообщений с приоритетом выше 3
result = subprocess.run(command, shell = True, capture_output = True, text = True)

# Анализ журналов для обнаружения подозрительной активности
print(result.stdout)

# Мониторинг аномальной активности на сервере
import psutil

# Проверка использования ресурсов сервера
cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent

# Анализ активности для обнаружения аномалий
if cpu_usage > 90 or memory_usage > 90:
    print("Подозрительная активность на сервере!")