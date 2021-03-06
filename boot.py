# boot.py -- run on boot-up
from network import WLAN
import machine
import keys
wlan = WLAN(mode=WLAN.STA)

"""
Use wifi pass and ssid in keys.py.
"""

nets = wlan.scan()
for net in nets:
    if net.ssid == keys.wifi_ssid:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, keys.wifi_password), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        print(wlan.ifconfig())
        break