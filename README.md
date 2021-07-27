# `smart_dht11`
 Using IFTT to control a wifi outlet (from anywhere). This allows you to automate fans, dehumidifiers, and anything else really. 
 By Erik Karlsson.
 Inspired by smartfan by Zerox13 (Abdulsalam Aldahir).
 
Prerequesites
* A wifi outlet with IFTT integration (I use a tp link kasa, but there are many others)
* A micropython device, such as the pycom lopy4

Before you can use this please make an account on IFTT and create a webhook event (input, this is the event you'll refer to in the code) with an accompanying action (output). You can search for webhook when creating event, and then your wi-fi outlet's system (such as kasa) when creating the action.

After that insert your wi-fi credentials and your iftt key which you can find [here](https://ifttt.com/maker_webhooks) and then press "documentation".

In this example my event is moisture_high and low. You can change this for your specific sensor, purpose and event.
