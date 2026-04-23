from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def configure_ntp(task):
    ntp_server = task.host["ntp_server"]
    
    task.run(
        task=netmiko_send_config,
        config_commands=[f"ntp server {ntp_server}"]
    )
    
    task.run(
    task=netmiko_send_command,
    command_string="write memory"
)
    
results = nr.run(task=configure_ntp)
print_result(results)