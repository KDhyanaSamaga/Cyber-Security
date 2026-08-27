# Softtech Solutions GNS3 Network Project

## Continuation README — Alpine DNS/Web Server Troubleshooting

This document records the current state of the Softtech Solutions GNS3 network project, including the previously completed network configuration and the additional Alpine Linux troubleshooting performed during the latest session.

The purpose of this README is to allow the project to continue in a new conversation without repeating completed work.

---

# 1. Project Overview

The project is a small company network for **Softtech Solutions** using:

```text
Main Network: 172.16.0.0
```

The company contains three departments:

| Department | VLAN | Network         | Gateway      |
| ---------- | ---: | --------------- | ------------ |
| IT         |   10 | 172.16.0.0/23   | 172.16.0.1   |
| Sales      |   20 | 172.16.2.0/25   | 172.16.2.1   |
| Finance    |   30 | 172.16.2.128/26 | 172.16.2.129 |

The project implements:

* VLSM
* VLAN segmentation
* Router-on-a-Stick
* Inter-VLAN routing
* DHCP
* Alpine Linux server
* DNS for `softech.com`
* DNS record for `www.softech.com`
* Optional lightweight web server using nginx

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

Devices:

```text
1 × Cisco c3745 Router
1 × Built-in GNS3 Ethernet Switch
5 × VPCS Clients
1 × Alpine Linux Virt Server
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

Physical connections:

```text
R1 FastEthernet0/0
        |
        |
S1 Ethernet0
        |
        ├── Ethernet1 → IT-1
        ├── Ethernet2 → IT-2
        ├── Ethernet3 → SA-1
        ├── Ethernet4 → SA-2
        ├── Ethernet5 → FIN-1
        └── Ethernet6 → DNS-Web-Server eth0
```

---

# 4. Completed Router Configuration

## Enter configuration mode

```cisco
enable
configure terminal
```

## Enable the physical interface

```cisco
interface FastEthernet0/0
no shutdown
exit
```

## VLAN 10 — IT

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

## VLAN 20 — Sales

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

## VLAN 30 — Finance

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

## Verify router interfaces

```cisco
show ip interface brief
```

The latest verification showed:

```text
FastEthernet0/0       unassigned      up      up
FastEthernet0/0.10    172.16.0.1      up      up
FastEthernet0/0.20    172.16.2.1      up      up
FastEthernet0/0.30    172.16.2.129    up      up
```

This confirms that the Router-on-a-Stick configuration is active.

---

# 5. Completed Switch Configuration

The built-in GNS3 Ethernet Switch is configured as follows:

| Port | VLAN | Type   | Connected Device   |
| ---: | ---: | ------ | ------------------ |
|    0 |    1 | dot1q  | R1 FastEthernet0/0 |
|    1 |   10 | access | IT-1               |
|    2 |   10 | access | IT-2               |
|    3 |   20 | access | SA-1               |
|    4 |   20 | access | SA-2               |
|    5 |   30 | access | FIN-1              |
|    6 |   30 | access | DNS-Web-Server     |

Important verified settings:

```text
Port 0
VLAN: 1
Type: dot1q
```

```text
Port 6
VLAN: 30
Type: access
```

The physical connection was also verified:

```text
DNS-Web-Server eth0 → S1 Ethernet6
```

No switch configuration should currently be changed.

---

# 6. Completed DHCP Configuration

## Excluded addresses

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

## DHCP verification commands

```cisco
show ip dhcp pool
show ip dhcp binding
```

---

# 7. Completed Inter-VLAN Testing

Previously successful tests included communication between:

```text
IT-1 ↔ IT-2
SA-1 ↔ SA-2
FIN-1 → Finance Gateway

FIN-1 → IT-1
FIN-1 → SA-1
IT-1 → SA-1
SA-1 → FIN-1
```

Example commands:

```text
ping 172.16.2.12
```

```text
ping 172.16.2.141
```

Router configuration was saved using:

```cisco
copy running-config startup-config
```

Then:

```text
Destination filename [startup-config]?
```

Press:

```text
Enter
```

---

# 8. Alpine Linux Server

The original Ubuntu server plan was replaced with a lightweight Alpine Linux appliance.

Installed appliance:

```text
Alpine Linux Virt
Version: 3.18.4
Image: alpine-virt-3.18.4.qcow2
```

Server name:

```text
DNS-Web-Server
```

Network connection:

```text
DNS-Web-Server eth0 → S1 Ethernet6
```

Switch configuration:

```text
Port: 6
VLAN: 30
Type: access
```

Planned server configuration:

```text
IP Address: 172.16.2.130/26
Subnet Mask: 255.255.255.192
Gateway: 172.16.2.129
DNS Server: 172.16.2.130
```

---

# 9. Issue 1 — GNS3 Alpine Console Port Conflict

## Problem

When attempting to open the Alpine console, the following error occurred:

```text
Trying ::1...
Connection failed: Connection refused

Trying 127.0.0.1...
Connection failed: Connection refused
```

The GNS3 terminal showed:

```text
Could not start Telnet QEMU console [Errno 98]

error while attempting to bind on address ('0.0.0.0', 5012):

[Errno 98] Address already in use
```

This identified a **TCP port 5012 conflict**.

---

# 10. Troubleshooting the Port Conflict

The following command was used:

```bash
sudo lsof -i :5012
```

This initially showed that a process was using port `5012`.

The following command was also used:

```bash
ps aux | grep gns3
```

An attempt was made to terminate the old process:

```bash
sudo kill 1212
```

The result was:

```text
kill: (1212): No such process
```

The port was checked again:

```bash
sudo lsof -i :5012
```

This returned no output.

## Resolution

The port was free.

GNS3 was restarted using:

```bash
gns3
```

The existing Softtech Solutions project was opened.

The Alpine server was started and the console successfully reached:

```text
Welcome to Alpine!

alpine:~#
```

### Issue status

```text
GNS3 console port conflict: SOLVED
Alpine console access: WORKING
```

---

# 11. Alpine Interface Identification

The following command was executed:

```sh
ip addr
```

The output confirmed that the network interface is:

```text
eth0
```

The interface was:

```text
UP
```

Initially, no IPv4 address was configured.

---

# 12. Temporary Static IP Configuration

The following command was used to temporarily assign the server address:

```sh
ip addr add 172.16.2.130/26 dev eth0
```

The address was verified using:

```sh
ip addr
```

The output confirmed:

```text
inet 172.16.2.130/26 scope global eth0
```

### Current status

The Alpine server now has a **temporary IPv4 address**:

```text
172.16.2.130/26
```

Important: this address has **not yet been made persistent**.

---

# 13. Gateway Connectivity Test

The Finance VLAN gateway was tested:

```sh
ping 172.16.2.129
```

Result:

```text
19 packets transmitted
0 packets received
100% packet loss
```

This showed that the Alpine server could not communicate with its gateway.

---

# 14. ARP / Neighbor Table Test

The following command was executed:

```sh
ip neigh show
```

Result:

```text
172.16.2.129 dev eth0 used ... probes 6 FAILED
```

This indicated that the server attempted to resolve the gateway through ARP but did not receive a response.

---

# 15. Router Verification

On `R1`, the following command was used:

```cisco
show ip interface brief
```

The relevant interface showed:

```text
FastEthernet0/0.30    172.16.2.129    up    up
```

Therefore:

```text
VLAN 30 router subinterface: WORKING
Gateway IP: 172.16.2.129
Status: up/up
```

No router configuration was changed.

---

# 16. Switch Verification

The following components were checked and verified:

## Server switch port

```text
S1 Port 6
VLAN: 30
Type: access
```

## Router switch port

```text
S1 Port 0
VLAN: 1
Type: dot1q
```

## Physical connection

```text
DNS-Web-Server eth0 → S1 Ethernet6
```

All of these appear correctly configured.

No switch configuration was changed.

---

# 17. Alpine Routing Table Check

The following command was executed:

```sh
ip route
```

The output showed:

```text
172.16.2.128/26 dev eth0 scope link src 172.16.2.130
```

This confirms that Alpine knows its directly connected VLAN 30 network.

No default route has been configured yet.

Important:

The missing default route does **not** explain why the server could not ping `172.16.2.129`, because both addresses are in the same subnet:

```text
Server:  172.16.2.130/26
Gateway: 172.16.2.129/26

Network: 172.16.2.128/26
```

---

# 18. FIN-1 Connectivity Test

To test communication from another VLAN 30 device to the server, the following command was run on `FIN-1`:

```text
ping 172.16.2.130
```

The result was repeated timeouts.

Then the FIN-1 configuration was checked:

```text
show ip
```

The output showed:

```text
IP/MASK : 0.0.0.0/0
GATEWAY : 0.0.0.0
DNS : 0.0.0.0
```

The console also showed:

```text
Can't find dhcp server
```

This identified another issue.

---

# 19. Issue 2 — FIN-1 Lost Its DHCP Address

## Problem

`FIN-1` no longer had:

```text
IPv4 Address
Gateway
DNS Configuration
```

Its configuration was:

```text
IP/MASK : 0.0.0.0/0
GATEWAY : 0.0.0.0
DNS : 0.0.0.0
```

Because FIN-1 had no IP address, its earlier ping test to the Alpine server was not a valid connectivity test.

---

# 20. FIN-1 DHCP Recovery

The following command was executed:

```text
dhcp
```

The result was:

```text
DDORA IP 172.16.2.140/26 GW 172.16.2.129
```

This means FIN-1 successfully received:

```text
IP Address: 172.16.2.140/26
Gateway: 172.16.2.129
```

### Issue status

```text
FIN-1 missing DHCP configuration: SOLVED
FIN-1 DHCP: WORKING
FIN-1 current IP: 172.16.2.140/26
Gateway: 172.16.2.129
```

---

# 21. Exact Current Stopping Point

The **last command given** was:

```text
ping 172.16.2.130
```

This command should now be executed from:

```text
FIN-1
```

FIN-1 has successfully recovered its DHCP configuration:

```text
FIN-1 IP:      172.16.2.140/26
Gateway:       172.16.2.129
```

The next required action is:

```text
FIN-1> ping 172.16.2.130
```

Then observe whether replies are received.

## Important

Do not change any router, switch, VLAN, or DHCP configuration before checking this result.

The next troubleshooting decision depends on whether FIN-1 can now reach the Alpine server.

---

# 22. Current Project Status

| Component                               | Status             |
| --------------------------------------- | ------------------ |
| VLSM design                             | Completed          |
| VLAN 10 — IT                            | Completed          |
| VLAN 20 — Sales                         | Completed          |
| VLAN 30 — Finance                       | Completed          |
| Switch access ports                     | Completed          |
| Switch trunk                            | Completed          |
| Router-on-a-Stick                       | Completed          |
| Inter-VLAN routing                      | Completed          |
| DHCP configuration                      | Completed          |
| IT DHCP                                 | Completed          |
| Sales DHCP                              | Completed          |
| Finance DHCP                            | Completed          |
| Previous inter-VLAN tests               | Completed          |
| Router configuration saved              | Completed          |
| Alpine Linux Virt installed             | Completed          |
| DNS-Web-Server added                    | Completed          |
| Server connected to S1 Ethernet6        | Completed          |
| S1 Ethernet6 VLAN 30 access             | Verified           |
| GNS3 console port conflict              | Solved             |
| Alpine console access                   | Working            |
| Alpine interface identified             | Completed          |
| Temporary server IPv4 address           | Configured         |
| Persistent Alpine IP configuration      | Not completed      |
| Server → Gateway ping                   | Failing            |
| Server ARP to gateway                   | Failing            |
| R1 VLAN 30 subinterface                 | Verified up/up     |
| S1 VLAN 30 configuration                | Verified           |
| FIN-1 lost DHCP address                 | Solved             |
| FIN-1 DHCP lease                        | Restored           |
| FIN-1 → Server test after DHCP recovery | Pending            |
| Alpine default gateway                  | Not yet configured |
| Persistent static networking            | Not yet configured |
| DNS service                             | Not configured     |
| `softech.com` zone                      | Not configured     |
| `www.softech.com` record                | Not configured     |
| nginx web server                        | Not configured     |
| Final end-to-end testing                | Not completed      |

---

# 23. Important Commands Executed in This Session

## Start GNS3

```bash
gns3
```

## Check Alpine interfaces

```sh
ip addr
```

## Temporarily assign Alpine IP

```sh
ip addr add 172.16.2.130/26 dev eth0
```

## Test Alpine gateway

```sh
ping 172.16.2.129
```

Stop ping with:

```text
Ctrl + C
```

## Check ARP/neighbor information

```sh
ip neigh show
```

## Check Alpine routing table

```sh
ip route
```

## Check router interfaces

```cisco
show ip interface brief
```

## Check FIN-1 configuration

```text
show ip
```

## Request DHCP on FIN-1

```text
dhcp
```

## Next command to execute

```text
ping 172.16.2.130
```

---

# 24. Do Not Change These Configurations

Do not modify the following unless troubleshooting specifically proves that a change is necessary:

```text
VLAN 10 configuration
VLAN 20 configuration
VLAN 30 configuration

R1 FastEthernet0/0.10
R1 FastEthernet0/0.20
R1 FastEthernet0/0.30

DHCP pools
DHCP exclusions

S1 Port 0 trunk configuration

S1 Ports 1–6 VLAN assignments

Existing IT and Sales client configuration
```

The existing network infrastructure had previously passed inter-VLAN connectivity testing.

---

# 25. Next Conversation Continuation Prompt

Copy the following into the next conversation:

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
- Previous inter-VLAN connectivity tests
- Router configuration saved

Topology:
- R1 FastEthernet0/0 → S1 Ethernet0
- S1 Port 1 → IT-1
- S1 Port 2 → IT-2
- S1 Port 3 → SA-1
- S1 Port 4 → SA-2
- S1 Port 5 → FIN-1
- S1 Port 6 → DNS-Web-Server eth0

Alpine server:
- Alpine Linux Virt 3.18.4
- Server name: DNS-Web-Server
- eth0 connected to S1 Ethernet6
- S1 Ethernet6 = VLAN 30 access
- Temporary server IP configured:
  172.16.2.130/26

Issue solved:
- GNS3 Alpine QEMU Telnet console failed because TCP port 5012 was already in use.
- The port was cleared and GNS3 restarted.
- Alpine console now works correctly.

Commands executed:
- gns3
- ip addr
- ip addr add 172.16.2.130/26 dev eth0
- ping 172.16.2.129
- ip neigh show
- ip route
- show ip interface brief
- show ip
- dhcp

Current troubleshooting:
- Alpine server cannot ping gateway 172.16.2.129.
- Ping result:
  19 packets transmitted, 0 packets received, 100% packet loss.
- ip neigh show showed gateway 172.16.2.129 as FAILED.
- R1 FastEthernet0/0.30 = 172.16.2.129 and is up/up.
- S1 Port 0 is dot1q trunk.
- S1 Port 6 is VLAN 30 access.
- Physical connection confirmed:
  DNS-Web-Server eth0 → S1 Ethernet6.

FIN-1 issue:
- FIN-1 had lost its DHCP configuration and showed 0.0.0.0/0.
- Running dhcp solved it.
- FIN-1 now has:
  IP: 172.16.2.140/26
  Gateway: 172.16.2.129

EXACT CURRENT STOPPING POINT:
The next command must be run from FIN-1:

ping 172.16.2.130

Check whether FIN-1 can now reach the Alpine server.

Continue one step at a time.
Do not skip steps.
Wait for me to reply done or provide a screenshot before moving to the next step.
Do not modify working router, switch, VLAN, or DHCP configurations unless troubleshooting specifically proves it is necessary.
```

---

# 26. Final Target Architecture

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
                                      nginx web server
```

---

# 27. Remaining Completion Checklist

* [x] Configure VLSM
* [x] Configure VLAN 10
* [x] Configure VLAN 20
* [x] Configure VLAN 30
* [x] Configure switch access ports
* [x] Configure switch trunk
* [x] Configure Router-on-a-Stick
* [x] Configure inter-VLAN routing
* [x] Configure DHCP
* [x] Test previous inter-VLAN connectivity
* [x] Save router configuration
* [x] Install Alpine Linux Virt
* [x] Add DNS-Web-Server
* [x] Connect server to S1 Ethernet6
* [x] Resolve GNS3 console port conflict
* [x] Access Alpine console
* [x] Identify `eth0`
* [x] Temporarily configure `172.16.2.130/26`
* [x] Restore FIN-1 DHCP configuration
* [ ] Test FIN-1 → Alpine server after DHCP recovery
* [ ] Determine why Alpine cannot communicate with the VLAN 30 gateway
* [ ] Configure permanent Alpine static IP
* [ ] Configure permanent default gateway
* [ ] Test server-to-router connectivity
* [ ] Test server inter-VLAN connectivity
* [ ] Install DNS service
* [ ] Configure `softech.com`
* [ ] Create `www.softech.com` A record
* [ ] Test DNS resolution
* [ ] Install nginx
* [ ] Configure web page
* [ ] Test `www.softech.com`
* [ ] Perform final end-to-end testing
