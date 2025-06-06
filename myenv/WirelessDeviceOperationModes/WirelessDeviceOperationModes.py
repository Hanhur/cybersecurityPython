# Для подключения к беспроводной точке доступа в режиме инфраструк­туры можно использовать библиотеки, такие как pywifi.
# Пример кода на Python для подключения к Wi-Fi-ceти в режиме инфраструктуры:
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

profile = pywifi.Profile()
profile.ssid = "YourNetworkSSID"
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.СПРНЕR_ТУРЕ_ССМР
profile.key = "YourNetworkPassword"

iface. remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)
iface. connect(tmp_profile)

# Для настройки беспроводного устройства на работу в режиме ад-хок можно использовать ту же библиотеку pywifi, изменяя параметры под­ключения.
# Режим ад-хок (Ad-hoc Mode):
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces() (0)

profile = pywifi.Profile()
profile.ssid = "AdHocNetwork"
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_NONE)
profile.cipher = const. CIPHER_TYPE_NONE

iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)
iface.connect(tmp_profile)

# пример, который демонстрирует работу с библиотекой pywifi для сканирования доступных Wi-Fi-ceтeй
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
results = iface.scan_results()
for network in results:
    print("SSID:", network.ssid, "Signal Strength:", network.signal)