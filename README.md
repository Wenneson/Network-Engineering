<img width="1604" height="980" alt="image" src="https://github.com/user-attachments/assets/36d411bc-f238-4ade-b5d2-4a437e3551e5" />



# Network Engineering

Public portfolio of my lab work as I study for the **Cisco CCIE Automation v1.1**
(the rebrand of DevNet Expert, effective February 3, 2026). Each subdirectory
is a self-contained study area with its own README.

Maintained by **Michael Wenneson** — [GitHub @Wenneson](https://github.com/Wenneson) · [LinkedIn](https://www.linkedin.com/in/michael-wenneson/)

## Subprojects

| Area | Tools | Blueprint Topic | Description |
|---|---|---|---|
| [ansible_automation/](./ansible_automation) | Ansible, Cisco IOS-XE, CML | Infrastructure as Code | Playbooks for OSPFv2, NTP, loopbacks, device backups, and CML lab lifecycle. |

_Planned as I work through the blueprint:_ Terraform · Python scripting against
device and controller APIs · NETCONF/RESTCONF + YANG · pyATS/Genie assurance ·
Git-backed CI/CD pipelines · observability and source-of-truth patterns.

## Lab Environment

- Cisco Modeling Labs (CML) running a 4-router IOS-XE topology
- Ansible 2.16+ with the `cisco.ios` collection
- Python 3.12 virtualenv (see each subproject's README for setup)

## About

I'm a network engineer studying toward the Cisco CCIE Automation v1.1 blueprint.
This repo is my public notebook — follow along, or reach out if you're studying too.

Blueprint reference: [CCIE Automation v1.1 Lab Exam Topics (Cisco)](https://learningcontent.cisco.com/documents/marketing/exam-topics/CCIE_Automation_V1.1_BP.pdf)
