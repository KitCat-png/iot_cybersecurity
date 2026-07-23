import time
import random

device_list = ["camera_01", "thermostat_02", "smart_lock_03", "smart_lock_04", "smart_light_05", "smart_light_06", "smart_light_07", "smart_light_08", "smart_light_09", "smart_light_10"]

request_count = 0

def inspect_packages(packet):
    if packet["bytes_sent"] > 1200:
        print(f"🚨 ALERT: High traffic from {packet['device_id']}! ({packet['bytes_sent']} bytes)")
    else:
        print(f"Device Packet: {packet}")

while True:
    bytes_sent = random.randint(50, 1500)
    current_device = random.choice(device_list)

    device_packet = {
    "device_id": current_device,
    "bytes_sent": bytes_sent,
    "ip_address": "192.168.1.100",
    "status": "connected",
    "request_count": request_count,
    }

    request_count += 1

    inspect_packages(device_packet)
        
    time.sleep(1)