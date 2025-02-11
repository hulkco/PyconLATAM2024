# NTP Example
#
# This example shows how to get the current time using NTP

import network, usocket, ustruct, utime
from time import sleep

# AP info
SSID='XXXXXXXX' # Network SSID
KEY='XXXXXXXXXX'  # Network key

import network, usocket, ustruct, utime

TIMESTAMP = 2208988800

# Create new socket
client = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
client.bind(("", 8080))
client.settimeout(3.0)

# Get addr info via DNS
addr = usocket.getaddrinfo("pool.ntp.org", 123)[0][4]

# Send query
client.sendto('\x1b' + 47 * '\0', addr)
data, address = client.recvfrom(1024)

# Print time
t = ustruct.unpack(">IIIIIIIIIIII", data)[10] - TIMESTAMP
print ("Year:%d Month:%d Day:%d Time: %d:%d:%d" % (utime.localtime(t)[0:6]))

# Close socket
client.close()