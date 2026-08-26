# Softtech Solutions GNS3 Network Project

## Project Overview

This project implements a small company network in **GNS3** using:

* VLSM
* VLANs
* Router-on-a-Stick
* Inter-VLAN Routing
* DHCP
* DNS Server configuration
* Linux server integration
* Optional Apache Web Server

The main network address is:

```text
172.16.0.0
```

The company has three departments:

| Department | Hosts Required |    VLAN |
| ---------- | -------------: | ------: |
| IT         |            300 | VLAN 10 |
| Sales      |            120 | VLAN 20 |
| Finance    |             50 | VLAN 30 |

---

# 1. Network Addressing Using VLSM

## VLAN 10 — IT

```text
Network Address: 172.16.0.0/23
Subnet Mask:     255.255.254.0
Gateway:         172.16.0.1
Usable Range:    172.16.0.1 - 172.16.1.254
Broadcast:       172.16.1.255
```

## VLAN 20 — Sales

```text
Network Address: 172.16.2.0/25
Subnet Mask:     255.255.255.128
Gateway:         172.16.2.1
Usable Range:    172.16.2.1 - 172.16.2.126
Broadcast:       172.16.2.127
```

## VLAN 30 — Finance

```text
Network Address: 172.16.2.128/26
Subnet Mask:     255.255.255.192
Gateway:         172.16.2.129
Usable Range:    172.16.2.129 - 172.16.2.190
Broadcast:       172.16.2.191
```

---

# 2. Devices Used

The current topology contains:

```text
1 × Cisco c3745 Router
1 × Built-in GNS3 Ethernet Switch
5 × VPCS
```

## Router

```text
R1
```

## Switch

```text
S1
```

## PCs

```text
IT-1
IT-2
SA-1
SA-2
FIN-1
```

A Linux server will be added later for DNS.

---

# 3. Physical Topology

```text
                    R1
                    |
             FastEthernet0/0
                    |
                S1 Ethernet0
                    |
       ______________________________
       |       |       |       |     |
 Ethernet1 Ethernet2 Ethernet3 Ethernet4 Ethernet5
       |       |       |       |     |
      IT-1    IT-2    SA-1    SA-2  FIN-1
```

## Port Mapping

```text
S1 Ethernet0 → R1 FastEthernet0/0

S1 Ethernet1 → IT-1
S1 Ethernet2 → IT-2

S1 Ethernet3 → SA-1
S1 Ethernet4 → SA-2

S1 Ethernet5 → FIN-1
```

---

# 4. Enable Router Configuration Mode

## What this command does

Enters privileged EXEC mode and then enters global configuration mode so router interfaces and services can be configured.

## Command

```cisco
enable
configure terminal
```

---

# 5. Enable the Physical Router Interface

## What this command does

Enables the physical FastEthernet interface connected between the router and the GNS3 Ethernet switch.

## Command

```cisco
interface FastEthernet0/0
no shutdown
exit
```

---

# 6. Configure VLAN 10 — IT

## What this command does

Creates a router subinterface for VLAN 10 and assigns the IT department gateway address.

## Command

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

---

# 7. Configure VLAN 20 — Sales

## What this command does

Creates a router subinterface for VLAN 20 and assigns the Sales department gateway address.

## Command

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

---

# 8. Configure VLAN 30 — Finance

## What this command does

Creates a router subinterface for VLAN 30 and assigns the Finance department gateway address.

## Command

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

---

# 9. Verify Router Interfaces

## What this command does

Displays all router interfaces, their assigned IP addresses, and their operational status.

## Command

```cisco
show ip interface brief
```

## Verified Result

```text
FastEthernet0/0       → up/up
FastEthernet0/0.10    → 172.16.0.1
FastEthernet0/0.20    → 172.16.2.1
FastEthernet0/0.30    → 172.16.2.129
```

---

# 10. Configure Switch Access Ports

The built-in GNS3 Ethernet Switch was configured using:

```text
Right-click S1 → Configure
```

## IT Ports

```text
Port 1 → VLAN 10 → access
Port 2 → VLAN 10 → access
```

## Sales Ports

```text
Port 3 → VLAN 20 → access
Port 4 → VLAN 20 → access
```

## Finance Port

```text
Port 5 → VLAN 30 → access
```

---

# 11. Configure the Router Trunk Port

The switch port connected to R1 was configured as a dot1Q trunk.

```text
Port 0 → VLAN 1 → dot1q
Port 0 → VLAN 10 → dot1q
Port 0 → VLAN 20 → dot1q
Port 0 → VLAN 30 → dot1q
```

## VLAN Behavior

```text
VLAN 1  → Native VLAN
VLAN 10 → Tagged
VLAN 20 → Tagged
VLAN 30 → Tagged
```

A previous configuration problem occurred when VLAN 30 was configured as the native VLAN. This was corrected by setting VLAN 1 as the native VLAN.

---

# 12. Initial Manual PC Configuration

Before DHCP, the PCs were manually configured as follows:

```text
IT-1  → 172.16.0.10/23
IT-2  → 172.16.0.11/23

SA-1  → 172.16.2.10/25
SA-2  → 172.16.2.11/25

FIN-1 → 172.16.2.140/26
```

Initial VLAN connectivity was successfully tested.

---

# 13. Inter-VLAN Routing Tests

The following communications were successfully tested:

```text
IT-1 ↔ IT-2
SA-1 ↔ SA-2
FIN-1 → Finance Gateway

FIN-1 → IT-1
FIN-1 → SA-1
IT-1 → SA-1
SA-1 → FIN-1
```

This confirms:

```text
VLAN 10 ↔ VLAN 20 ✓
VLAN 10 ↔ VLAN 30 ✓
VLAN 20 ↔ VLAN 30 ✓
```

---

# 14. Enter DHCP Configuration Mode

## What this command does

Enters router configuration mode to configure DHCP services.

## Command

```cisco
enable
configure terminal
```

---

# 15. Exclude Reserved DHCP Addresses

## What this command does

Prevents DHCP from assigning gateway and reserved infrastructure addresses to clients.

## Command

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9
ip dhcp excluded-address 172.16.2.1 172.16.2.9
ip dhcp excluded-address 172.16.2.129 172.16.2.139
```

---

# 16. Create the IT DHCP Pool

## What this command does

Creates a DHCP pool for VLAN 10 and automatically provides IP addresses, gateway information, DNS information, and the domain name.

## Command

```cisco
ip dhcp pool IT_POOL
network 172.16.0.0 255.255.254.0
default-router 172.16.0.1
dns-server 172.16.2.130
domain-name softech.com
exit
```

---

# 17. Create the Sales DHCP Pool

## What this command does

Creates a DHCP pool for VLAN 20.

## Command

```cisco
ip dhcp pool SALES_POOL
network 172.16.2.0 255.255.255.128
default-router 172.16.2.1
dns-server 172.16.2.130
domain-name softech.com
exit
```

---

# 18. Create the Finance DHCP Pool

## What this command does

Creates a DHCP pool for VLAN 30.

## Command

```cisco
ip dhcp pool FINANCE_POOL
network 172.16.2.128 255.255.255.192
default-router 172.16.2.129
dns-server 172.16.2.130
domain-name softech.com
exit
```

---

# 19. Verify DHCP Pools

## What this command does

Displays DHCP pools and verifies the configured address ranges.

## Command

```cisco
show ip dhcp pool
```

## Verified Pools

```text
IT_POOL
SALES_POOL
FINANCE_POOL
```

---

# 20. Request DHCP Addresses on the PCs

## What this command does

Makes each VPCS request an IP address automatically from the DHCP server on R1.

## Command

Run this on each VPCS:

```text
dhcp
```

The following PCs successfully received DHCP addresses:

```text
IT-1
IT-2
SA-1
SA-2
FIN-1
```

---

# 21. Verify DHCP Bindings

## What this command does

Displays the IP addresses currently leased by the router's DHCP service.

## Command

```cisco
show ip dhcp binding
```

## Verified DHCP Addresses

```text
IT-1  → 172.16.0.12
IT-2  → 172.16.0.13

SA-1  → 172.16.2.12
SA-2  → 172.16.2.13

FIN-1 → 172.16.2.141
```

All DHCP leases were listed as:

```text
Type: Automatic
```

---

# 22. Save the Router Configuration

## What this command does

Saves the current running configuration to startup configuration.

This ensures the following configurations remain available after restarting R1:

* Router-on-a-Stick
* VLAN subinterfaces
* IP addressing
* Inter-VLAN routing
* DHCP pools
* DHCP exclusions

## Command

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

The configuration was successfully saved after the final DHCP verification.

---

# 23. Test IT to Sales Communication

## What this command does

Tests connectivity from IT-1 in VLAN 10 to SA-1 in VLAN 20.

## Command

Run on IT-1:

```text
ping 172.16.2.12
```

## Result

```text
Successful
```

Packets were successfully exchanged.

---

# 24. Test IT to Finance Communication

## What this command does

Tests connectivity from IT-1 in VLAN 10 to FIN-1 in VLAN 30.

## Command

Run on IT-1:

```text
ping 172.16.2.141
```

## Result

```text
Successful
```

Packets were successfully exchanged.

---

# 25. Current Project Status

The following components are successfully completed:

```text
VLSM                       ✓ Completed
VLAN 10 — IT               ✓ Completed
VLAN 20 — Sales            ✓ Completed
VLAN 30 — Finance          ✓ Completed

Switch VLAN Configuration  ✓ Completed
Trunk Configuration        ✓ Completed

Router-on-a-Stick          ✓ Completed
Inter-VLAN Routing         ✓ Completed

DHCP Configuration         ✓ Completed
DHCP Testing               ✓ Completed
DHCP Binding Verification  ✓ Completed

IT → Sales Test            ✓ Successful
IT → Finance Test          ✓ Successful

Router Configuration Save  ✓ Completed
```

---

# 26. Linux Server / DNS Setup Progress

The next phase of the project is adding an Ubuntu server to GNS3.

The following steps have been completed:

```text
File → New Template
```

Selected:

```text
Install an appliance from the GNS3 server
```

Then selected:

```text
Ubuntu Desktop Guest
```

Server location selected:

```text
Install the appliance on the main server
```

Ubuntu version selected:

```text
Ubuntu 22.04
```

The GNS3 appliance requires:

```text
Ubuntu 22.04 (64bit).vmdk
```

The required image was not available locally, so GNS3 showed:

```text
Missing files
```

The download process redirected to the Ubuntu appliance download page.

The selected download option is:

```text
Ubuntu 22.04 Jammy Jellyfish
VMware
VMware (VMDK) 64bit
Size: approximately 2.57 GB
```

The download process then opened the SourceForge project page.

---

# 27. Remaining Tasks

The following work is still remaining.

## Task 1 — Download the Ubuntu VMDK Image

Download the required:

```text
Ubuntu 22.04 VMware (VMDK) 64bit
```

After downloading, make sure the `.vmdk` file is available on the computer.

---

## Task 2 — Import the Ubuntu Image into GNS3

Return to the Ubuntu appliance installation screen.

Use:

```text
Import
```

Select the downloaded:

```text
Ubuntu 22.04 (64bit).vmdk
```

Complete the appliance installation.

---

## Task 3 — Add the Ubuntu Server to the Topology

After the appliance is successfully installed:

1. Drag the Ubuntu server into the GNS3 workspace.
2. Rename it appropriately, for example:

```text
DNS-SERVER
```

---

## Task 4 — Connect the Server to the Switch

Connect the Ubuntu server to an available port on S1.

The switch port must be configured as:

```text
VLAN 30
Access Port
```

This places the DNS server inside the Finance subnet.

---

## Task 5 — Configure the Linux Server IP Address

The planned server configuration is:

```text
IP Address: 172.16.2.130/26
Gateway:    172.16.2.129
DNS Server: 172.16.2.130
```

The exact Linux commands have **not yet been executed** in this project.

---

## Task 6 — Test Connectivity to the Router

After assigning the server IP address, test connectivity to the Finance gateway:

```text
ping 172.16.2.129
```

Then test communication with clients in other VLANs.

---

## Task 7 — Install BIND9

Install the BIND9 DNS server on Ubuntu.

The DNS configuration commands have **not yet been executed**.

---

## Task 8 — Configure the DNS Domain

The required domain is:

```text
softech.com
```

---

## Task 9 — Create the DNS Record

Create the following DNS record:

```text
www.softech.com → 172.16.2.130
```

---

## Task 10 — Test DNS Resolution

After configuring BIND9, test DNS resolution from the network.

The expected hostname is:

```text
www.softech.com
```

The expected resolved address is:

```text
172.16.2.130
```

---

## Task 11 — Optional Apache Web Server

Optionally install and configure Apache on the Ubuntu server.

The server could then host a website accessible through:

```text
www.softech.com
```

---

# Final Project Goal

The completed network should provide:

```text
                    ┌─────────────┐
                    │     R1      │
                    │ DHCP Server │
                    │ Inter-VLAN  │
                    │   Routing   │
                    └──────┬──────┘
                           │
                         Trunk
                           │
                    ┌──────┴──────┐
                    │      S1     │
                    └───┬───┬───┬─┘
                        │   │   │
                  VLAN 10 VLAN20 VLAN30
                    IT     Sales  Finance
                                    │
                               DNS Server
                              172.16.2.130
                                    │
                             www.softech.com
```

---

# Project Completion Checklist

* [x] Design the VLSM addressing scheme
* [x] Configure VLAN 10
* [x] Configure VLAN 20
* [x] Configure VLAN 30
* [x] Configure switch access ports
* [x] Configure trunk port
* [x] Configure Router-on-a-Stick
* [x] Configure Inter-VLAN Routing
* [x] Test inter-VLAN connectivity
* [x] Configure DHCP exclusions
* [x] Configure IT DHCP pool
* [x] Configure Sales DHCP pool
* [x] Configure Finance DHCP pool
* [x] Configure all PCs to use DHCP
* [x] Verify DHCP bindings
* [x] Save router configuration
* [x] Test IT to Sales communication
* [x] Test IT to Finance communication
* [ ] Download Ubuntu 22.04 VMware VMDK image
* [ ] Import Ubuntu into GNS3
* [ ] Add the Linux server to the topology
* [ ] Configure the Linux server IP address
* [ ] Configure the server switch port for VLAN 30
* [ ] Install BIND9
* [ ] Configure the `softech.com` DNS domain
* [ ] Create the `www.softech.com` DNS record
* [ ] Test DNS resolution
* [ ] Optionally configure Apache Web Server
* [ ] Perform final end-to-end project testing

---

# Current Exact Stopping Point

The project is currently at the **Ubuntu server installation stage**.

The Ubuntu 22.04 appliance was selected, and the required VMware `.vmdk` file was found to be missing.

The download process was started and redirected to the SourceForge project page.

## Next Step

Continue downloading the required Ubuntu image:

```text
Ubuntu 22.04 Jammy Jellyfish
VMware (VMDK) 64bit
```

After the image is downloaded, return to GNS3 and import the `.vmdk` file into the Ubuntu Desktop Guest appliance.
