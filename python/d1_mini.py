""" Helper file for D1 Mini form factor boards
    https://wiki.wemos.cc/products:d1:d1_mini
    https://www.banggood.com/LILYGO-TTGO-MINI-32-V2_0-ESP32-WiFi-bluetooth-Module-Development-Board-p-1286046.html?cur_warehouse=CN
"""

from sys import platform

if platform == 'esp8266':
    D0 = 16
    D1 = SCL = 5
    D2 = SDA = 4
    D3 = 0  # 10k pull-up
    D4 = LED = 2  # 10k pull-up
    D5 = SCK = 14
    D6 = MISO = 12
    D7 = MOSI = 13
    D8 = SS = CS = 15  # 10k pull-down

elif platform == 'esp32':
    D0 = 26
    D1 = SCL = LED = 22
    D2 = SDA = 21
    D3 = 17
    D4 = 16
    D5 = SCK = 18
    D6 = MISO = 19
    D7 = MOSI = 23
    D8 = SS = CS = 5

else:
    raise NotImplementedError('Unknown platform! No pin definitions created!')
