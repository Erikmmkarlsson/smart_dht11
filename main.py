import time
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom
from iftt import iftt

#initialize data pin for dht11
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)

#global variables
dehumidifier_active = False

while True:
    dht_result = th.read()
    while not dht_result.is_valid():
        time.sleep(.5)
        dht_result = th.read() #keep reading until valid result is given
    
    temp = dht_result.temperature
    humidity = dht_result.humidity

    if (humidity > 65):
        iftt.send_request("moisture_high")
        dehumidifier_active = True
    elif (humidity < 50):
        iftt.send_request("moisture_low")
        dehumidifier_active = False

    print('Temp: ', temp)
    print('RH: ', humidity)
    print('Dehumidifier active: ', dehumidifier_active)

    time.sleep(5*60) #Every 5 minutes

