# Scan Example
# This example shows how to scan for Wi-Fi networks.
import time, network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("\nPycon Latam 2024 Mazatlán")
print("\nScanning...")
while (True):
    scan_result = wlan.scan()
    for ap in scan_result:
        #print("Channel:%d RSSI:%d Auth:%d BSSID:%s SSID:%s"%(ap))
        print("SSID:%s BSSID:%s Channel:%d RSSI:%d Auth:%d hidden:%d  "%(ap))
    print()
    time.sleep_ms(1000)

