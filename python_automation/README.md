# python_automation

Python-based network automation lab targeting the same 4-router Cisco IOS-XE
topology in CML that the Ansible side of this repo uses. Maps to the
**Network Programmability and Automation** area of the CCIE Automation v1.1
blueprint.

Currently covers three libraries side-by-side so the same lab tasks can be
compared across idioms:

- **Netmiko** — SSH-driven screen-scraping for config push and show-command collection.
- **NAPALM** — multi-vendor abstraction on top of the device APIs, used here for structured fact collection.
- **Nornir** — inventory-driven automation framework that parallelizes Netmiko/NAPALM tasks across the fleet.

Planned siblings: pyATS/Genie for assurance, NETCONF/RESTCONF + YANG for
model-driven config.

## Layout

```
python_automation/
├── .env.example                              # Copy to .env and fill in; .env is gitignored
├── netmiko/
│   ├── banner_update.py                      # Push MOTD banner to one router
│   ├── banner_update2.py                     # Push MOTD banner to all 4 routers
│   ├── netmiko_show_version_example.py       # Collect `show version` from one router
│   ├── practice.py                           # Collect `show ip int brief` from all 4 (context-manager style)
│   └── sh_ip_inter_brie.py                   # Collect `show ip interface brief` from all 4
├── NAPALM/
│   └── get_facts.py                          # Pull structured facts (hostname, model, version, uptime) via NAPALM
└── Nornir/
    ├── config.yaml                           # Nornir runner + SimpleInventory config
    ├── inventory/                            # hosts.yaml, groups.yaml, defaults.yaml
    ├── show_ip_int_brief.py                  # Run `show ip interface brief` across the inventory
    ├── ntp_server.py                         # Push NTP server config from per-host inventory var
    └── ntp_server_advanced.py                # Idempotent NTP reconciliation (diff desired vs. running-config)
```

## Setup

```bash
# From the repo root
python -m venv venv
source venv/bin/activate
pip install netmiko python-dotenv napalm nornir nornir-netmiko nornir-utils rich
```

## Credentials

Credentials are read from environment variables at runtime. The Netmiko scripts
call `load_dotenv()`, so a `.env` file next to them is picked up automatically.
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

Nornir reads credentials from `Nornir/inventory/defaults.yaml` (or per-host
overrides); the NAPALM example currently hard-codes lab credentials inline
and should be migrated to `.env` before running outside the lab.

## Topology

Same lab as the Ansible side — four IOS-XE routers at `10.99.2.161–164` in CML.
See [`ansible_automation/README.md`](../ansible_automation/README.md#topology)
for the full diagram.

## Script Reference

Run from the `python_automation/` directory so the scripts pick up `.env`.
Nornir scripts must be run from the `Nornir/` directory so `config.yaml` and
the `inventory/` paths resolve.

### Netmiko

| Script | Purpose | Command |
|---|---|---|
| `netmiko/netmiko_show_version_example.py` | `show version` from router1 | `python netmiko/netmiko_show_version_example.py` |
| `netmiko/sh_ip_inter_brie.py` | `show ip interface brief` from all 4 routers | `python netmiko/sh_ip_inter_brie.py` |
| `netmiko/practice.py` | `show ip interface brief` from all 4 using `ConnectHandler` as a context manager | `python netmiko/practice.py` |
| `netmiko/banner_update.py` | Push MOTD banner to router1 | `python netmiko/banner_update.py` |
| `netmiko/banner_update2.py` | Push MOTD banner to all 4 routers | `python netmiko/banner_update2.py` |

### NAPALM

| Script | Purpose | Command |
|---|---|---|
| `NAPALM/get_facts.py` | Collect hostname, model, OS version, and uptime via `get_facts()` | `python NAPALM/get_facts.py` |

### Nornir

| Script | Purpose | Command |
|---|---|---|
| `Nornir/show_ip_int_brief.py` | Run `show ip interface brief` across the inventory in parallel | `cd Nornir && python show_ip_int_brief.py` |
| `Nornir/ntp_server.py` | Push a single NTP server from each host's `ntp_server` inventory var | `cd Nornir && python ntp_server.py` |
| `Nornir/ntp_server_advanced.py` | Idempotent NTP reconciliation — diffs desired vs. running-config, adds/removes only what's needed, saves config | `cd Nornir && python ntp_server_advanced.py` |
