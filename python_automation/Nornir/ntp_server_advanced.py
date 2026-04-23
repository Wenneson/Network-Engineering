from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result

nr = InitNornir(config_file="config.yaml")

def configure_ntp(task):
    desired_ntp_servers = task.host["ntp_servers"]  # expect list
    desired_set = set(desired_ntp_servers)

    # 1. Get current config
    result = task.run(
        task=netmiko_send_command,
        command_string="show running-config | include ^ntp server"
    )

    current_lines = result.result.strip().splitlines()
    
    # Extract just the IPs
    current_set = set()
    for line in current_lines:
        parts = line.split()
        if len(parts) >= 3:
            current_set.add(parts[2])  # ntp server X.X.X.X

    # 2. Compare
    to_add = desired_set - current_set
    to_remove = current_set - desired_set

    commands = []

    # 3. Build config changes
    for server in to_add:
        commands.append(f"ntp server {server}")

    for server in to_remove:
        commands.append(f"no ntp server {server}")

    # 4. If nothing to change → exit cleanly
    if not commands:
        return Result(
            host=task.host,
            changed=False,
            result="NTP already compliant"
        )

    # 5. Apply changes
    task.run(
        task=netmiko_send_config,
        config_commands=commands
    )

    # 6. Save config
    task.run(
        task=netmiko_send_command,
        command_string="write memory"
    )

    return Result(
        host=task.host,
        changed=True,
        result=f"Added: {list(to_add)}, Removed: {list(to_remove)}"
    )

results = nr.run(task=configure_ntp)
print_result(results)