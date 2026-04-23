from netmiko import ConnectHandler

username = "lab_admin"
password = "Cisco123"

devices = [
    "10.99.2.161",
    "10.99.2.162",
    "10.99.2.163",
    "10.99.2.164"
]

for ip in devices:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password    
    }
    
    print(f"\nConnecting to {ip}...\n")
    
    with ConnectHandler(**device) as conn:
        output = conn.send_command("show ip interface brief")
        print(f"Output from {ip} is:\n{output}\n{'-'*80}")