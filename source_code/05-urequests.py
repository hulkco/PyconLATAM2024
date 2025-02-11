import urequests
import network
from time import sleep

# Request a random cat fact from the Meowfacts API
url = "https://meowfacts.herokuapp.com/"

WIFI_NETWORK='XXXXXXXXXXXXXXXX'
WIFI_PASSWORD='XXXXXXXXXXXXXXXXX'
 
print("\n This programa make a random request to the Meow Facts API")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_NETWORK, WIFI_PASSWORD)

# Pause required to configure Wi-Fi
print("\n Wait 5 seconds to WiFi Up")
sleep (5)

print("\n Connected to ",WIFI_NETWORK)
sleep (2)
# We should have a valid IP now via DHCP
print("\n Wi-Fi Connected ", wlan.ifconfig())

# Pause required to get response
print("\n Wait 3 seconds for response")
sleep (3)

response = urequests.get(url)
print(response.text)

