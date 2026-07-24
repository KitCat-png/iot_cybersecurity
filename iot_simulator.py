import time
import random
from datetime import datetime
import json

with open("devices.json", "r") as file:
    device_map = json.load(file)

possible_ports = [80, 443, 22, 23]

request_count = 0

strike_count = {}
blacklist = []

def inspect_packages(packet, strikes, blacklist):

    is_attack = False

    if packet["bytes_sent"] > 1200:
        is_attack = True
        print(f"[{packet['timestamp']}] 🚨 ALERT: High traffic from {packet['device_id']}! ({packet['bytes_sent']} bytes)")
        with open("security_alerts.log", "a") as file:
            file.write(f"[{packet['timestamp']}] 🚨 ALERT: High traffic from {packet['device_id']}! ({packet['bytes_sent']} bytes)\n")

    elif packet["target_port"] in [22, 23]:
        is_attack = True
        print(f"[{packet['timestamp']}] ⚠️ ALERT: Suspicious port access from {packet['device_id']}! (Port: {packet['target_port']})")
        with open("security_alerts.log", "a") as file:
            file.write(f"[{packet['timestamp']}] ⚠️ ALERT: Suspicious port access from {packet['device_id']}! (Port: {packet['target_port']})\n")
    else:
        print(f"Device Packet: {packet}")

    if is_attack:
        device_id = packet["device_id"]
        ip = packet["ip_address"]
        strikes[device_id] = strikes.get(device_id, 0) + 1

        if strikes[device_id] >= 3 and ip not in blacklist:
            blacklist.append(ip)
            print(f"🚫 QUARANTINE: {device_id} blacklisted! (IP: {ip})")

try:
    while True:
        bytes_sent = random.randint(50, 1500)
        current_device = random.choice(list(device_map.keys()))
        current_ip = device_map[current_device]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_port = random.choices(possible_ports, weights=[45, 45, 5, 5])[0]

        if current_ip in blacklist:
            print(f"⚠️ ALERT: Packet from blacklisted IP {current_ip} ignored.")
            continue

        device_packet = {
        "device_id": current_device,
        "bytes_sent": bytes_sent,
        "ip_address": current_ip,
        "status": "connected",
        "request_count": request_count,
        "timestamp": current_time,
        "target_port": current_port
        }

        request_count += 1

        inspect_packages(device_packet, strike_count, blacklist)
            
        time.sleep(1)

except KeyboardInterrupt:
    print(f"\n🛑 System shutting down. Total packets scanned: {request_count}")