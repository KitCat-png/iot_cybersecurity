ddos_atacks = 0
port_scans = 0

with open("security_alerts.log", "r") as file:
    for line in file:
        if "High traffic" in line:
            ddos_atacks += 1
        elif "Suspicious port access" in line:
            port_scans += 1

print(f"Total DDoS attacks detected: {ddos_atacks}")
print(f"Total suspicious port scans detected: {port_scans}")