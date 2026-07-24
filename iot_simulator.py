import time
import random
from datetime import datetime

device_map = {
    "camera_01": "192.168.1.101",
    "thermostat_02": "192.168.1.102",
    "smart_lock_03": "192.168.1.103",
    "smart_lock_04": "192.168.1.104",
    "smart_light_05": "192.168.1.105",
    "smart_light_06": "192.168.1.106",
    "smart_light_07": "192.168.1.107",
    "smart_light_08": "192.168.1.108",
    "smart_light_09": "192.168.1.109",
    "smart_light_10": "192.168.1.110"
}

request_count = 0

def inspect_packages(packet):
    if packet["bytes_sent"] > 1200:
        print(f"[{packet['timestamp']}] 🚨 ALERT: High traffic from {packet['device_id']}! ({packet['bytes_sent']} bytes)")
        with open("security_alerts.log", "a") as file:
            file.write(f"[{packet['timestamp']}] 🚨 ALERT: High traffic from {packet['device_id']}! ({packet['bytes_sent']} bytes)\n")
    else:
        print(f"Device Packet: {packet}")

while True:
    bytes_sent = random.randint(50, 1500)
    current_device = random.choice(list(device_map.keys()))
    current_ip = device_map[current_device]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    device_packet = {
    "device_id": current_device,
    "bytes_sent": bytes_sent,
    "ip_address": current_ip,
    "status": "connected",
    "request_count": request_count,
    "timestamp": current_time
    }

    request_count += 1

    inspect_packages(device_packet)
        
    time.sleep(1)