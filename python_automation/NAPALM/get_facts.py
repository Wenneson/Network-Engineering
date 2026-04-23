from napalm import get_network_driver
from rich import print

devices = [
    "10.99.2.161",
    "10.99.2.162",
    "10.99.2.163",
    "10.99.2.164",
]

driver = get_network_driver("ios")

for host in devices:
    print(f"\nConnecting to {host}...")
    
    device = driver(
        hostname=host,
        username="lab_admin",
        password="Cisco123",   
    )
    
    device.open()
    
    facts = device.get_facts()
    
    print("Hostname:", facts["hostname"])
    #print("Vendor:", facts["vendor"])
    print("Model:", facts["model"])
    print("OS Version:", facts["os_version"])
    print("Uptime (s):", facts["uptime"])
    #print("Serial Number:", facts["serial_number"])
    #print(facts)
    
    device.close()

