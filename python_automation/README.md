# python_automation

Python-based network automation lab targeting the same 4-router Cisco IOS-XE
topology in CML that the Ansible side of this repo uses. Maps to the
**Network Programmability and Automation** area of the CCIE Automation v1.1
blueprint.

Currently: Netmiko for SSH-driven config push and show-command collection.
Planned siblings: pyATS/Genie for assurance, NETCONF/RESTCONF + YANG for
model-driven config.

## Layout

```
python_automation/
├── .env.example                              # Copy to .env and fill in; .env is gitignored
└── netmiko/
    ├── banner_update.py                      # Push MOTD banner to one router
    ├── banner_update2.py                     # Push MOTD banner to all 4 routers
    ├── netmiko_show_version_example.py       # Collect `show version` from one router
    └── sh_ip_inter_brie.py                   # Collect `show ip interface brief` from all 4
```

## Setup

```bash
# From the repo root
python -m venv venv
source venv/bin/activate
pip install netmiko python-dotenv
```

## Credentials

Credentials are read from environment variables at runtime. The scripts call
`load_dotenv()`, so a `.env` file next to them is picked up automatically.
`.env` is **gitignored** via the root `.gitignore`.

```bash
cd python_automation
cp .env.example .env
# then edit .env and set NET_USERNAME / NET_PASSWORD for your lab
```

Required variables:

| Variable | Purpose |
|---|---|
| `NET_USERNAME` | SSH username for the IOS-XE devices |
| `NET_PASSWORD` | SSH password for the IOS-XE devices |

If either variable is missing the scripts fail fast with a `KeyError` rather
than sending `None` to SSH.

## Topology

Same lab as the Ansible side — four IOS-XE routers at `10.99.2.161–164` in CML.
See [`ansible_automation/README.md`](../ansible_automation/README.md#topology)
for the full diagram.

## Script Reference

Run from the `python_automation/` directory so the scripts pick up `.env`.

| Script | Purpose | Command |
|---|---|---|
| `netmiko/netmiko_show_version_example.py` | `show version` from router1 | `python netmiko/netmiko_show_version_example.py` |
| `netmiko/sh_ip_inter_brie.py` | `show ip interface brief` from all 4 routers | `python netmiko/sh_ip_inter_brie.py` |
| `netmiko/banner_update.py` | Push MOTD banner to router1 | `python netmiko/banner_update.py` |
| `netmiko/banner_update2.py` | Push MOTD banner to all 4 routers | `python netmiko/banner_update2.py` |
