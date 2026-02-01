import os

ips = ["8.8.8.8", "8.8.4.4"]

for ip in ips:
    response = os.system(f"ping -c 1 {ip}")
    if response == 0:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")
