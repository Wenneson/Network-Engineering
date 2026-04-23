from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(
    task=netmiko_send_command,
    command_string ="show ip interface brief"
)

print_result(results)