# ==================================================================================================================================
# Wi-Fi (Wireless Fidelity) - это технология, обеспечивающая беспроводную передачу данных по радиоканалам, 
# которая используется для подключения устройств к сети Интернет и локальным сетям без использования проводов.
# ==================================================================================================================================

# Основы беспроводных сетей

# Pywifi. Библиотека pywifi предоставляет доступ к функциям управления беспроводными интерфейсами на уровне операционной системы. 
# С по­мощью pywifi можно сканировать доступные сети, подключаться к сетям, управлять параметрами безопасности и многое другое. 
# Пример использо­вания pywifi для сканирования доступных сетей:

# Пример использования pywifi для сканирования доступных сетей
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
results = iface.scan_results()
for network in results:
    print("SSID:", network.ssid, "Signal Strength:", network.signal)

# Scapy. Библиотека scapy позволяет создавать, отправлять и анализиро­вать сетевые пакеты. С помощью scapy можно работать с беспроводными пакетами, 
# захватывать трафик, проводить анализ сети и многое другое. Пример использования scapy для захвата и анализа беспроводного тра­фика:

# Пример использования scapy для захвата и анализа беспроводного трафика
from scapy.all import *

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            print("Probe Request:", pkt.addr2)

sniff(iface= "wlan0", prn = packet_handler)

# Wifi. Библиотека wifi предоставляет простой интерфейс для работы с бес­проводными сетями, такими как сканирование и подключение к сетям.
# С помощью wifi можно получать информацию о текущем подключении, сканировать доступные сети и многое другое. Пример использования wifi
# для сканирования доступных сетей:

# Пример использования wifi для сканирования доступных сетей
import wifi

networks = wifi.Cell.all('wlan0')
for network in networks:
    print("SSID:", network.ssid, "Signal Strength:", network.signal)


# Пример сканирования доступных сетей с использованием библиотеки pywifi
import pywifi
from pywifi import const

wifi = pywifi. PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
results = iface.scan_results()
for network in results:
    print("SSID:", network.ssid, "Signal Strerigth:", network.signal)

from scapy.all import *

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            print("Probe Request:", pkt.addr2)

sniff(iface = "wlan0", prn = packet_handler)

import wifi

iface = 'wlan0'
ssid = 'YourNetworkSSID'
password = 'YourNetworkPassword'

cell = wifi.Cell.all(iface) [0]
scheme = wifi.Scheme.for_cell(iface, ssid, cell, password)
scheme.activate()

# ======================================================================================================================================

# Изучение теоретических основ Wi-Fi-стандартов:
