# ansible_automation

Ansible-based network automation lab targeting a 4-router Cisco IOS-XE topology
running in Cisco Modeling Labs (CML). Maps to the **Infrastructure as Code** and
**Network Programmability and Automation** areas of the CCIE Automation v1.1
blueprint.

## Layout

```
ansible_automation/
├── ansible.cfg              # Runtime config (inventory path, timeouts, logging)
├── inventory/
│   ├── inventory.yml        # 4 routers under the `cisco` group
│   ├── group_vars/
│   │   └── cisco.yml.example   # Template — copy to cisco.yml and fill in
│   └── host_vars/
│       ├── localhost.yml.example  # Template — copy to localhost.yml
│       └── router{1-4}.yml     # Per-router OSPFv2 config (no secrets)
├── playbooks/
│   ├── backup.yml           # Save `show version` + `show running-config`
│   ├── ospf.yml             # Configure OSPFv2 processes and interfaces
│   ├── set_loopback.yml     # Configure Loopback0 per router
│   ├── set_ntp.yml          # Configure and verify NTP
│   ├── show_interfaces.yml  # Display `show ip interface brief`
│   ├── start_cml_lab.yml    # Start the CML lab via REST API
│   └── stop_cml_lab.yml     # Stop the CML lab via REST API
└── backups/                 # Output directory for backup.yml (gitignored)
```

## Setup

```bash
# From the repo root
python -m venv venv
source venv/bin/activate
pip install ansible
ansible-galaxy collection install cisco.ios ansible.netcommon
```

## Credentials

Credentials live in two files that are **gitignored**. Copy the templates and
fill them in for your lab:

```bash
cd ansible_automation/inventory
cp group_vars/cisco.yml.example group_vars/cisco.yml
cp host_vars/localhost.yml.example host_vars/localhost.yml
# then edit both files
```

For production use, upgrade to [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html)
to keep encrypted secrets in the repo.

## Topology

```
          ┌──────────────────────────┐
          │       CML host           │
          │  (REST API endpoint)     │
          └────────────┬─────────────┘
                       │ 10.99.2.0/24
       ┌───────────┬───┴───┬───────────┐
       │           │       │           │
   router1     router2  router3     router4
   .161        .162     .163        .164
   (IOS-XE)    (IOS-XE) (IOS-XE)    (IOS-XE)
```

## Playbook Reference

Run from the `ansible_automation/` directory.

| Playbook | Purpose | Command |
|---|---|---|
| `start_cml_lab.yml` | Start the CML lab via REST API | `ansible-playbook playbooks/start_cml_lab.yml` |
| `stop_cml_lab.yml` | Stop the CML lab via REST API | `ansible-playbook playbooks/stop_cml_lab.yml` |
| `show_interfaces.yml` | Collect `show ip interface brief` from all routers | `ansible-playbook playbooks/show_interfaces.yml` |
| `set_loopback.yml` | Configure Loopback0 on each router | `ansible-playbook playbooks/set_loopback.yml` |
| `set_ntp.yml` | Push NTP server config and verify associations | `ansible-playbook playbooks/set_ntp.yml` |
| `ospf.yml` | Configure OSPFv2 processes and interfaces from host_vars | `ansible-playbook playbooks/ospf.yml` |
| `backup.yml` | Save `show version` + `show running-config` to `backups/<timestamp>/` | `ansible-playbook playbooks/backup.yml` |
