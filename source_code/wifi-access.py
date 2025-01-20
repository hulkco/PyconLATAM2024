"""
Conectar a una red WiFi y hacer una petición
SSID='INFINITUM723C' # Network SSID
KEY='vK4xNVPxPX'  # Network key
"""

import network, socket
from time import sleep

# AP info
SSID='INFINITUM723C' # Network SSID
KEY='vK4xNVPxPX'  # Network key

PORT = 80
HOST = "www.google.com"

# Init wlan module and connect to network
print("\nTrying to connect. Note this may take a while...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, KEY)
sleep (3)
# We should have a valid IP now via DHCP
print("\nWi-Fi Connected ", wlan.ifconfig())

# Get addr info via DNS
addr = socket.getaddrinfo(HOST, PORT)[0][4]
print(addr)

# Create a new socket and connect to addr
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# Set timeout
client.settimeout(3.0)

# Send HTTP request and recv response
client.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%(HOST))
print(client.recv(1024))

# Close socket
client.close()
