import os

from dotenv import load_dotenv
from netmiko import ConnectHandler

load_dotenv()

USERNAME = os.environ["NET_USERNAME"]
PASSWORD = os.environ["NET_PASSWORD"]

devices = [
    "10.99.2.161",
    "10.99.2.162",
    "10.99.2.163",
    "10.99.2.164",
]

config_commands = [
    "banner motd ^",
    "Unauthorized access is prohibited!",
    "^",
]

for host in devices:
    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": USERNAME,
        "password": PASSWORD,
    }

    print(f"\nConnecting to {host}...")

    with ConnectHandler(**device) as conn:
        output = conn.send_config_set(config_commands)
        print(output)
