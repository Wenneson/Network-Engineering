import os

from dotenv import load_dotenv
from netmiko import ConnectHandler

load_dotenv()

device = {
    "device_type": "cisco_ios",
    "host": "10.99.2.161",
    "username": os.environ["NET_USERNAME"],
    "password": os.environ["NET_PASSWORD"],
}

config_commands = [
    "banner motd ^",
    "Unauthorized access is prohibited!",
    "^",
]

with ConnectHandler(**device) as conn:
    output = conn.send_config_set(config_commands)
    print(output)
