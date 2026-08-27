# Softtech Solutions GNS3 Network Project

## Continuation README

**Current project status:** VLANs, VLSM, Router-on-a-Stick, inter-VLAN routing, DHCP, and connectivity testing are completed. The current phase is adding a lightweight Alpine Linux server to provide DNS and, optionally, a web service for `softech.com`.

**Exact stopping point:** The Alpine Linux appliance was installed and added to the topology. A GNS3/QEMU Telnet console port conflict on TCP port `5012` was identified and cleared. GNS3 now needs to be started again, the existing project reopened, and the Alpine server console tested.

---

# 1. Project Overview

Softtech Solutions is building a small company network using the main address:

```text
172.16.0.0
```

The company has three departments:

| Department | Hosts Required | VLAN |
|---|---:|---:|
| IT | 300 | VLAN 10 |
| Sales | 120 | VLAN 20 |
| Finance | 50 | VLAN 30 |

The project implements:

- VLSM subnetting
- VLAN segmentation
- Router-on-a-Stick
- Inter-VLAN routing
- DHCP
- DNS
- A lightweight Linux server
- Optional web hosting for `www.softech.com`

---

# 2. VLSM Addressing Plan

## VLAN 10 — IT

```text
Network:        172.16.0.0/23
Subnet Mask:    255.255.254.0
Gateway:        172.16.0.1
Usable Range:   172.16.0.1 - 172.16.1.254
Broadcast:      172.16.1.255
```

## VLAN 20 — Sales

```text
Network:        172.16.2.0/25
Subnet Mask:    255.255.255.128
Gateway:        172.16.2.1
Usable Range:   172.16.2.1 - 172.16.2.126
Broadcast:      172.16.2.127
```

## VLAN 30 — Finance

```text
Network:        172.16.2.128/26
Subnet Mask:    255.255.255.192
Gateway:        172.16.2.129
Usable Range:   172.16.2.129 - 172.16.2.190
Broadcast:      172.16.2.191
```

---

# 3. Current Topology

Devices used:

```text
1 × Cisco c3745 Router
1 × Built-in GNS3 Ethernet Switch
5 × VPCS clients
1 × Alpine Linux Virt server
```

Device names:

```text
R1
S1
IT-1
IT-2
SA-1
SA-2
FIN-1
DNS-Web-Server
```

Current physical layout:

```text
                         R1
                         |
                   FastEthernet0/0
                         |
                    S1 Ethernet0
                         |
        -----------------------------------
        |          |          |            |
     Ethernet1  Ethernet2  Ethernet3...  Ethernet6
        |          |          |            |
       IT-1       IT-2       ...     DNS-Web-Server
```

Detailed switch mapping:

```text
S1 Ethernet0 → R1 FastEthernet0/0
S1 Ethernet1 → IT-1
S1 Ethernet2 → IT-2
S1 Ethernet3 → SA-1
S1 Ethernet4 → SA-2
S1 Ethernet5 → FIN-1
S1 Ethernet6 → DNS-Web-Server eth0
```

---

# 4. Completed Router Configuration

## Enter privileged and global configuration mode

```cisco
enable
configure terminal
```

## Enable the physical router interface

```cisco
interface FastEthernet0/0
no shutdown
exit
```

## VLAN 10 — IT subinterface

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

## VLAN 20 — Sales subinterface

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

## VLAN 30 — Finance subinterface

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

## Verify router interfaces

```cisco
show ip interface brief
```

The router-on-a-stick configuration was successfully tested.

---

# 5. Completed Switch VLAN Configuration

The built-in GNS3 Ethernet Switch was configured through:

```text
Right-click S1 → Configure
```

Access ports:

```text
Port 1 → VLAN 10 → access
Port 2 → VLAN 10 → access

Port 3 → VLAN 20 → access
Port 4 → VLAN 20 → access

Port 5 → VLAN 30 → access
Port 6 → VLAN 30 → access
```

Port 6 was added specifically for the new Alpine server:

```text
S1 Ethernet6
VLAN: 30
Type: access
```

The router-facing port is configured as a dot1Q trunk carrying the required VLANs.

Native VLAN:

```text
VLAN 1
```

Tagged VLANs:

```text
VLAN 10
VLAN 20
VLAN 30
```

---

# 6. Completed DHCP Configuration

Reserved/excluded addresses:

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9
ip dhcp excluded-address 172.16.2.1 172.16.2.9
ip dhcp excluded-address 172.16.2.129 172.16.2.139
```

## IT DHCP Pool

```cisco
ip dhcp pool IT_POOL
network 172.16.0.0 255.255.254.0
default-router 172.16.0.1
dns-server 172.16.2.130
domain-name softech.com
exit
```

## Sales DHCP Pool

```cisco
ip dhcp pool SALES_POOL
network 172.16.2.0 255.255.255.128
default-router 172.16.2.1
dns-server 172.16.2.130
domain-name softech.com
exit
```

## Finance DHCP Pool

```cisco
ip dhcp pool FINANCE_POOL
network 172.16.2.128 255.255.255.192
default-router 172.16.2.129
dns-server 172.16.2.130
domain-name softech.com
exit
```

Verification commands:

```cisco
show ip dhcp pool
show ip dhcp binding
```

The VPCS clients were configured to request addresses using:

```text
dhcp
```

Verified DHCP leases:

```text
IT-1  → 172.16.0.12
IT-2  → 172.16.0.13

SA-1  → 172.16.2.12
SA-2  → 172.16.2.13

FIN-1 → 172.16.2.141
```

---

# 7. Completed Connectivity Tests

Successful tests included:

```text
IT-1 ↔ IT-2
SA-1 ↔ SA-2
FIN-1 → Finance gateway

FIN-1 → IT-1
FIN-1 → SA-1
IT-1 → SA-1
SA-1 → FIN-1
```

Specific final tests:

From IT-1 to Sales:

```text
ping 172.16.2.12
```

From IT-1 to Finance:

```text
ping 172.16.2.141
```

Both were successful.

---

# 8. Router Configuration Saved

The router configuration was saved with:

```cisco
copy running-config startup-config
```

When prompted:

```text
Destination filename [startup-config]?
```

Press:

```text
Enter
```

---

# 9. Why Ubuntu Was Replaced

The original plan was to use an Ubuntu 22.04 Desktop appliance. This required a large VMware VMDK image and would run inside the following environment:

```text
VirtualBox
└── Kali Linux VM
    └── GNS3
        └── Linux Server VM
```

Because Ubuntu Desktop is unnecessarily heavy for a DNS/web server lab, the decision was made to use a lightweight operating system instead.

The selected replacement is:

```text
Alpine Linux Virt
Version: 3.18.4
Image format: qcow2
Approximate image size: 48.7 MB
```

The server will eventually provide:

```text
DNS for softech.com
www.softech.com → 172.16.2.130

Optional lightweight web service
```

---

# 10. Alpine Linux Appliance Installation Completed

The following GNS3 installation steps were completed:

```text
File → New Template
```

Selected:

```text
Install an appliance from the GNS3 server
```

Selected appliance:

```text
Alpine Linux Virt
```

Selected server:

```text
Install the appliance on the main server
```

Available versions included:

```text
Alpine Linux Virt version 3.18.4
Alpine Linux Virt version 3.16
```

Version selected:

```text
Alpine Linux Virt version 3.18.4
```

Required file downloaded:

```text
alpine-virt-3.18.4.qcow2
```

The file status changed to:

```text
Ready to install
```

Installation was confirmed and completed successfully.

The appliance is now visible in the GNS3 device list.

---

# 11. Alpine Server Added to the Topology

The Alpine Linux Virt appliance was dragged into the existing topology and renamed:

```text
DNS-Web-Server
```

Network connection:

```text
DNS-Web-Server eth0 → S1 Ethernet6
```

Switch configuration for the server:

```text
Port: 6
VLAN: 30
Type: access
```

This places the server in the Finance subnet.

Planned server addressing:

```text
IP Address: 172.16.2.130/26
Subnet Mask: 255.255.255.192
Gateway: 172.16.2.129
DNS Server: 172.16.2.130
```

---

# 12. Alpine Console Problem Encountered

When attempting to open the server console, GNS3 displayed:

```text
Trying ::1...
Connection failed: Connection refused
Trying 127.0.0.1...
Connection failed: Connection refused
```

After stopping and starting the node, the GNS3/Kali terminal showed the important error:

```text
Could not start Telnet QEMU console [Errno 98]
error while attempting to bind on address ('0.0.0.0', 5012):
[Errno 98] Address already in use
```

This identified the problem as a **console port conflict**, not a VLAN or network configuration problem.

---

# 13. Troubleshooting Performed for Port 5012

The following command was used:

```bash
sudo lsof -i :5012
```

It showed that `gns3server` was listening on TCP port `5012`.

The GNS3 GUI was then closed and the following command was used:

```bash
ps aux | grep gns3
```

The output showed that the GNS3 GUI was no longer running, but a server process had previously remained associated with the port.

An attempt was made to stop the old process:

```bash
sudo kill 1212
```

The result was:

```text
kill: (1212): No such process
```

This indicated that the original process had already disappeared.

The port was checked again:

```bash
sudo lsof -i :5012
```

This returned no output.

## Current conclusion

```text
TCP port 5012 is now free.
```

---

# 14. Exact Current Stopping Point

The last completed troubleshooting step was confirming that:

```bash
sudo lsof -i :5012
```

returns no output.

The next action is to restart GNS3:

```bash
gns3
```

Then:

1. Open the existing Softtech Solutions project.
2. Confirm the full topology is present.
3. Check that `DNS-Web-Server` is still connected to `S1 Ethernet6`.
4. Do not change the existing VLAN configuration.
5. Start `DNS-Web-Server`.
6. Wait approximately 15–20 seconds.
7. Open its console.

Expected result:

```text
Alpine Linux boot output
...
localhost login:
```

If the console opens successfully, continue with Alpine configuration.

---

# 15. Next Steps After the Console Works

## Step 1 — Log in to Alpine

At:

```text
localhost login:
```

Use the default login appropriate to the appliance state. Do not assume a password until the console prompt is visible.

## Step 2 — Identify network interfaces

Run:

```sh
ip addr
```

Expected network interface:

```text
eth0
```

## Step 3 — Configure the static server IP

The required configuration is:

```text
IP Address: 172.16.2.130/26
Gateway:    172.16.2.129
```

The exact Alpine commands should be configured after confirming the available interface and Alpine installation state.

## Step 4 — Test local network connectivity

Test the Finance gateway:

```sh
ping 172.16.2.129
```

Then test another VLAN client, for example:

```sh
ping 172.16.0.12
```

Successful replies will confirm that the server can use the existing inter-VLAN routing.

---

# 16. DNS Configuration Goal

The domain to configure is:

```text
softech.com
```

The required DNS record is:

```text
www.softech.com → 172.16.2.130
```

The project originally planned BIND9 on Ubuntu. Since the server is now Alpine Linux, the DNS installation and configuration commands will need to be adapted to Alpine.

The intended workflow is:

```text
1. Configure static networking
2. Confirm connectivity
3. Install DNS server software
4. Configure softech.com zone
5. Create A record for www.softech.com
6. Start/enable the DNS service
7. Test DNS resolution
```

The DHCP pools already advertise:

```text
DNS Server: 172.16.2.130
Domain Name: softech.com
```

Therefore, once the DNS server is operational, DHCP clients should already have the correct DNS server information.

---

# 17. Optional Web Server Goal

After DNS works, a lightweight web server can be installed.

Preferred approach for this lightweight Alpine setup:

```text
nginx
```

The target behavior is:

```text
Client
  |
  | DNS query
  v
www.softech.com
  |
  v
172.16.2.130
  |
  v
Alpine DNS-Web-Server
  |
  v
Web page
```

The website should be reachable through:

```text
www.softech.com
```

---

# 18. Current Project Status

| Component | Status |
|---|---|
| VLSM design | Completed |
| VLAN 10 — IT | Completed |
| VLAN 20 — Sales | Completed |
| VLAN 30 — Finance | Completed |
| Switch access ports | Completed |
| Router trunk connection | Completed |
| Router-on-a-Stick | Completed |
| Inter-VLAN routing | Completed |
| DHCP exclusions | Completed |
| IT DHCP pool | Completed |
| Sales DHCP pool | Completed |
| Finance DHCP pool | Completed |
| VPCS DHCP configuration | Completed |
| DHCP binding verification | Completed |
| Inter-VLAN connectivity testing | Completed |
| Router configuration saved | Completed |
| Ubuntu plan | Replaced |
| Alpine Linux Virt appliance | Installed |
| Alpine server added to topology | Completed |
| Server connected to S1 Ethernet6 | Completed |
| S1 Ethernet6 VLAN 30 access | Completed |
| Alpine console | Pending re-test |
| Server static IP | Not yet configured |
| DNS service | Not yet configured |
| `softech.com` DNS zone | Not yet configured |
| `www.softech.com` record | Not yet configured |
| Web server | Not yet configured |
| Final end-to-end test | Not yet completed |

---

# 19. Important Do-Not-Change Items

Do not redo or modify the following unless a later troubleshooting step specifically requires it:

```text
VLAN 10 configuration
VLAN 20 configuration
VLAN 30 configuration
Router subinterface addresses
DHCP pools
DHCP exclusions
S1 Ethernet1 through Ethernet5 assignments
S1 Ethernet6 VLAN 30 access assignment
Existing PC addressing/DHCP configuration
```

The network infrastructure has already been successfully tested.

---

# 20. Immediate Continuation Prompt for the Next Chat

Use the following context when continuing:

```text
We are continuing the Softtech Solutions GNS3 network project.

Completed:
- VLSM
- VLAN 10 IT: 172.16.0.0/23, gateway 172.16.0.1
- VLAN 20 Sales: 172.16.2.0/25, gateway 172.16.2.1
- VLAN 30 Finance: 172.16.2.128/26, gateway 172.16.2.129
- Router-on-a-Stick
- Inter-VLAN routing
- DHCP
- Successful inter-VLAN connectivity tests
- Router configuration saved

Alpine Linux:
- Installed Alpine Linux Virt 3.18.4 in GNS3
- Image: alpine-virt-3.18.4.qcow2
- Added to topology as DNS-Web-Server
- Connected DNS-Web-Server eth0 to S1 Ethernet6
- S1 Ethernet6 is VLAN 30 access
- Planned server IP: 172.16.2.130/26
- Gateway: 172.16.2.129

Problem encountered:
- GNS3 QEMU Telnet console failed because TCP port 5012 was already in use.
- After closing GNS3 and troubleshooting, `sudo lsof -i :5012` returned no output, so the port is now free.

Exact next step:
1. Start GNS3 with `gns3`.
2. Open the existing Softtech Solutions project.
3. Start DNS-Web-Server.
4. Wait 15–20 seconds.
5. Open the console.
6. If the Alpine console works, continue step-by-step with static IP configuration, then DNS, then the web server.

Please continue one step at a time and wait for me to reply `done` or provide a screenshot before moving to the next step.
```

---

# 21. Final Target Architecture

```text
                              ┌───────────────┐
                              │      R1       │
                              │ DHCP + Router │
                              │ Inter-VLAN    │
                              └───────┬───────┘
                                      │
                                    Trunk
                                      │
                              ┌───────┴───────┐
                              │      S1       │
                              └───┬───┬───┬───┘
                                  │   │   │
                             VLAN10 VLAN20 VLAN30
                                │      │      │
                                IT    Sales Finance
                                               │
                                      ┌────────┴────────┐
                                      │ DNS-Web-Server  │
                                      │ Alpine Linux    │
                                      │ 172.16.2.130    │
                                      └────────┬────────┘
                                               │
                                      DNS: softech.com
                                               │
                                  www.softech.com
                                               │
                                     Optional nginx
```

---

# 22. Project Completion Checklist

- [x] Design VLSM addressing
- [x] Configure VLAN 10
- [x] Configure VLAN 20
- [x] Configure VLAN 30
- [x] Configure switch access ports
- [x] Configure trunk port
- [x] Configure Router-on-a-Stick
- [x] Configure inter-VLAN routing
- [x] Test inter-VLAN connectivity
- [x] Configure DHCP exclusions
- [x] Configure IT DHCP pool
- [x] Configure Sales DHCP pool
- [x] Configure Finance DHCP pool
- [x] Configure VPCS clients for DHCP
- [x] Verify DHCP bindings
- [x] Save router configuration
- [x] Install Alpine Linux Virt 3.18.4
- [x] Add Alpine server to topology
- [x] Connect Alpine server to S1 Ethernet6
- [x] Configure Ethernet6 as VLAN 30 access
- [x] Identify and clear the GNS3 console port conflict
- [ ] Restart GNS3
- [ ] Verify Alpine console access
- [ ] Configure Alpine static IP address
- [ ] Test server-to-router connectivity
- [ ] Test server inter-VLAN connectivity
- [ ] Install and configure DNS service
- [ ] Configure `softech.com`
- [ ] Create `www.softech.com` DNS record
- [ ] Test DNS resolution from clients
- [ ] Install/configure lightweight web server
- [ ] Test `www.softech.com`
- [ ] Perform final end-to-end testing
