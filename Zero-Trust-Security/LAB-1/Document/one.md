# Softtech Solutions Network Project — GNS3 Implementation Guide

> **Platform:** GNS3 running on Kali Linux  
> **Current router:** Cisco c3745  
> **Current switch:** GNS3 built-in Ethernet Switch  
> **End devices:** VPCS  
> **Design:** VLSM + VLANs + Inter-VLAN Routing + DHCP + DNS + Optional Web Server

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Network Requirements](#2-network-requirements)
3. [VLSM Calculation](#3-vlsm-calculation)
4. [Final Addressing Plan](#4-final-addressing-plan)
5. [Topology](#5-topology)
6. [Devices Used](#6-devices-used)
7. [Build the Topology in GNS3](#7-build-the-topology-in-gns3)
8. [Configure the Router](#8-configure-the-router)
9. [Configure VLANs on the GNS3 Ethernet Switch](#9-configure-vlans-on-the-gns3-ethernet-switch)
10. [Configure Router-on-a-Stick](#10-configure-router-on-a-stick)
11. [Configure DHCP](#11-configure-dhcp)
12. [Configure the VPCS Clients](#12-configure-the-vpcs-clients)
13. [Add and Configure the Linux DNS Server](#13-add-and-configure-the-linux-dns-server)
14. [Optional Web Server](#14-optional-web-server)
15. [Testing and Verification](#15-testing-and-verification)
16. [Saving the Configuration](#16-saving-the-configuration)
17. [Troubleshooting](#17-troubleshooting)
18. [Current Project Progress](#18-current-project-progress)

---

# 1. Project Overview

Softtech Solutions needs a network for three departments:

- **IT**
- **Sales**
- **Finance**

The project uses the main address space:

```text
172.16.0.0
```

The network must provide:

- Variable Length Subnet Masking (VLSM)
- Separate VLANs for each department
- Inter-VLAN routing
- DHCP for automatic IP assignment
- A DNS server
- Optionally, a web server

Because this is a simulation, only a few VPCS devices are required to represent the departments. We do **not** need to create hundreds of actual PCs.

---

# 2. Network Requirements

| Department | Required Hosts | VLAN |
|---|---:|---:|
| IT | 300 | VLAN 10 |
| Sales | 120 | VLAN 20 |
| Finance | 50 | VLAN 30 |

The subnets must be allocated from largest host requirement to smallest.

---

# 3. VLSM Calculation

## 3.1 IT Department — 300 Hosts

We need at least 300 usable IP addresses.

```text
2^8 - 2 = 254  → Not enough
2^9 - 2 = 510  → Enough
```

Therefore, IT requires 9 host bits.

```text
32 - 9 = 23
```

### IT Subnet

```text
Network:        172.16.0.0/23
Subnet Mask:    255.255.254.0
Usable Range:   172.16.0.1 – 172.16.1.254
Broadcast:      172.16.1.255
Gateway:        172.16.0.1
```

---

## 3.2 Sales Department — 120 Hosts

We need at least 120 usable IP addresses.

```text
2^7 - 2 = 126  → Enough
```

Therefore:

```text
32 - 7 = 25
```

### Sales Subnet

The next available network after `172.16.0.0/23` is `172.16.2.0`.

```text
Network:        172.16.2.0/25
Subnet Mask:    255.255.255.128
Usable Range:   172.16.2.1 – 172.16.2.126
Broadcast:      172.16.2.127
Gateway:        172.16.2.1
```

---

## 3.3 Finance Department — 50 Hosts

We need at least 50 usable IP addresses.

```text
2^6 - 2 = 62  → Enough
```

Therefore:

```text
32 - 6 = 26
```

### Finance Subnet

The next available network is:

```text
Network:        172.16.2.128/26
Subnet Mask:    255.255.255.192
Usable Range:   172.16.2.129 – 172.16.2.190
Broadcast:      172.16.2.191
Gateway:        172.16.2.129
```

---

# 4. Final Addressing Plan

| Department | VLAN | Network | CIDR | Subnet Mask | Gateway |
|---|---:|---|---|---|---|
| IT | 10 | 172.16.0.0 | /23 | 255.255.254.0 | 172.16.0.1 |
| Sales | 20 | 172.16.2.0 | /25 | 255.255.255.128 | 172.16.2.1 |
| Finance | 30 | 172.16.2.128 | /26 | 255.255.255.192 | 172.16.2.129 |

We use the first usable address in each subnet as the default gateway.

---

# 5. Topology

```text
                         R1
                  Cisco c3745 Router
                         |
                         | FastEthernet0/0
                         |
                      S1 Ethernet0
                         |
        __________________________________________
        |            |             |             |
     VLAN 10      VLAN 20       VLAN 30
        IT          SALES        FINANCE
      /    \       /    \          |
   IT1     IT2   SALES1 SALES2   FINANCE1
```

A Linux DNS server will later be connected to the Finance VLAN.

Final conceptual design:

```text
                           R1
                 +---------------------+
                 | Fa0/0.10 VLAN 10    | 172.16.0.1
                 | Fa0/0.20 VLAN 20    | 172.16.2.1
                 | Fa0/0.30 VLAN 30    | 172.16.2.129
                 +----------+----------+
                            |
                         802.1Q
                            |
                            S1
              ______________|_______________
             |              |               |
          VLAN 10        VLAN 20        VLAN 30
             IT            SALES         FINANCE
          IT PCs         Sales PCs      Finance PC
                                            |
                                       DNS Server
                                       172.16.2.130
```

---

# 6. Devices Used

The available GNS3 devices include:

```text
c3745
Ethernet switch
Ethernet hub
VPCS
Cloud
NAT
ATM switch
Frame Relay switch
```

This project uses:

```text
1 × Cisco c3745 router
1 × GNS3 Ethernet switch
5 × VPCS clients
1 × Linux server later for DNS
```

The router is named:

```text
R1
```

The switch is named:

```text
S1
```

---

# 7. Build the Topology in GNS3

## Step 7.1 — Create a Project

1. Open GNS3.
2. Click **File → New Blank Project**.
3. Name the project:

```text
Softtech_Network
```

4. Click **OK**.

---

## Step 7.2 — Add the Router

1. Drag a `c3745` router into the workspace.
2. Rename it:

```text
R1
```

If the router is already running, stop it before attempting to rename it.

### Why?

The Cisco 3745 router will perform:

- Default gateway functions
- Inter-VLAN routing
- DHCP services

---

## Step 7.3 — Add the Switch

1. Drag an **Ethernet switch** into the workspace.
2. Rename it:

```text
S1
```

### Important

The built-in GNS3 Ethernet switch is **not the same as a Cisco IOS Layer 2 switch**. It does not provide the normal Cisco switch CLI used for commands such as:

```cisco
switchport mode access
switchport mode trunk
```

Its VLAN configuration must therefore be done through its GNS3 configuration mechanism.

---

## Step 7.4 — Connect R1 to S1

Connect:

```text
R1 FastEthernet0/0
        |
        |
S1 Ethernet0
```

This is the main router-to-switch link.

---

## Step 7.5 — Add the VPCS Devices

Add five VPCS devices.

Rename them:

```text
PC-IT1
PC-IT2
PC-SALES1
PC-SALES2
PC-FINANCE1
```

---

## Step 7.6 — Connect the PCs

Use the following port mapping:

| Device | Device Interface | Switch Port |
|---|---|---|
| R1 | FastEthernet0/0 | Ethernet0 |
| PC-IT1 | Ethernet0 | Ethernet1 |
| PC-IT2 | Ethernet0 | Ethernet2 |
| PC-SALES1 | Ethernet0 | Ethernet3 |
| PC-SALES2 | Ethernet0 | Ethernet4 |
| PC-FINANCE1 | Ethernet0 | Ethernet5 |

---

# 8. Configure the Router

## Step 8.1 — Start the Devices

Click the green **Start/Play** button in GNS3.

Open the R1 console.

If asked:

```text
Would you like to enter the initial configuration dialog? [yes/no]:
```

Type:

```text
no
```

---

## Step 8.2 — Enter Privileged EXEC Mode

At:

```text
Router>
```

Type:

```cisco
enable
```

You should get:

```text
Router#
```

### What it does

`enable` enters privileged EXEC mode, where administrative and configuration commands can be accessed.

---

## Step 8.3 — Enter Global Configuration Mode

Type:

```cisco
configure terminal
```

Prompt:

```text
R1(config)#
```

### What it does

This enters global configuration mode.

### Note

Do not type `configure terminal` again when you are already at:

```text
R1(config)#
```

If you need to run a `show` command from configuration mode, use:

```cisco
do show ip interface brief
```

---

## Step 8.4 — Check Router Interfaces

From:

```text
R1(config)#
```

Type:

```cisco
do show ip interface brief
```

### What it does

Displays:

- Interface names
- IP addresses
- Administrative status
- Protocol status

The Cisco 3745 in this project has:

```text
FastEthernet0/0
FastEthernet0/1
```

Initially they may show:

```text
administratively down
```

This is normal before `no shutdown` is applied.

---

## Step 8.5 — Enable FastEthernet0/0

The switch is connected to `FastEthernet0/0`.

Type:

```cisco
interface FastEthernet0/0
no shutdown
exit
```

### What each command does

#### `interface FastEthernet0/0`

Enters configuration mode for the physical interface.

#### `no shutdown`

Administratively enables the interface.

#### `exit`

Returns to the previous configuration mode.

---

# 9. Configure VLANs on the GNS3 Ethernet Switch

> **Important:** Do not attempt to open a Cisco-style CLI on the built-in Ethernet switch. It is not IOSvL2.

The required VLAN assignment is:

| Switch Port | Connected Device | VLAN |
|---|---|---:|
| Ethernet0 | R1 FastEthernet0/0 | Trunk carrying 10, 20, 30 |
| Ethernet1 | PC-IT1 | 10 |
| Ethernet2 | PC-IT2 | 10 |
| Ethernet3 | PC-SALES1 | 20 |
| Ethernet4 | PC-SALES2 | 20 |
| Ethernet5 | PC-FINANCE1 | 30 |

The built-in switch must be configured so that:

- Ethernet1 and Ethernet2 belong to VLAN 10
- Ethernet3 and Ethernet4 belong to VLAN 20
- Ethernet5 belongs to VLAN 30
- Ethernet0 carries the VLAN traffic between the router and switch

The exact UI labels can vary by GNS3 version. Open the switch configuration by stopping the node if necessary and using the node's **Configure** or equivalent settings option.

Do not substitute Cisco IOS switch commands unless you later replace this switch with an IOSvL2/IOU L2/IOL L2 image.

---

# 10. Configure Router-on-a-Stick

Router-on-a-Stick allows one physical router interface to route traffic for multiple VLANs.

The physical interface is:

```text
FastEthernet0/0
```

We create three subinterfaces:

```text
FastEthernet0/0.10 → VLAN 10 → IT
FastEthernet0/0.20 → VLAN 20 → Sales
FastEthernet0/0.30 → VLAN 30 → Finance
```

The parent interface must be enabled first:

```cisco
interface FastEthernet0/0
no shutdown
exit
```

---

## Step 10.1 — Configure VLAN 10 / IT

Type:

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

### What each command does

#### `interface FastEthernet0/0.10`

Creates or enters the logical subinterface associated with VLAN 10.

#### `encapsulation dot1Q 10`

Configures IEEE 802.1Q VLAN tagging for VLAN 10.

#### `ip address 172.16.0.1 255.255.254.0`

Assigns the IT default gateway address.

---

## Step 10.2 — Configure VLAN 20 / Sales

Type:

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

### What it does

Creates the VLAN 20 subinterface and assigns the Sales default gateway.

---

## Step 10.3 — Configure VLAN 30 / Finance

Type:

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

### What it does

Creates the VLAN 30 subinterface and assigns the Finance default gateway.

---

## Step 10.4 — Verify the Router Interfaces

Return to privileged EXEC mode or use `do`.

```cisco
do show ip interface brief
```

Expected logical interfaces:

```text
FastEthernet0/0
FastEthernet0/0.10
FastEthernet0/0.20
FastEthernet0/0.30
```

The subinterfaces should have:

```text
Fa0/0.10 → 172.16.0.1
Fa0/0.20 → 172.16.2.1
Fa0/0.30 → 172.16.2.129
```

---

# 11. Configure DHCP

The router will act as the DHCP server.

## Step 11.1 — Exclude Reserved Addresses

From global configuration mode:

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9
ip dhcp excluded-address 172.16.2.1 172.16.2.9
ip dhcp excluded-address 172.16.2.129 172.16.2.139
```

### What it does

Prevents DHCP from assigning addresses reserved for:

- Default gateways
- Static infrastructure
- DNS server

---

## Step 11.2 — Create the IT DHCP Pool

```cisco
ip dhcp pool IT_POOL
network 172.16.0.0 255.255.254.0
default-router 172.16.0.1
dns-server 172.16.2.130
domain-name softech.com
```

### What it does

Creates a DHCP pool for VLAN 10.

Clients receive:

- An IP address from the IT subnet
- Default gateway `172.16.0.1`
- DNS server `172.16.2.130`

---

## Step 11.3 — Create the Sales DHCP Pool

```cisco
ip dhcp pool SALES_POOL
network 172.16.2.0 255.255.255.128
default-router 172.16.2.1
dns-server 172.16.2.130
domain-name softech.com
```

### What it does

Creates the DHCP configuration for Sales VLAN 20.

---

## Step 11.4 — Create the Finance DHCP Pool

```cisco
ip dhcp pool FINANCE_POOL
network 172.16.2.128 255.255.255.192
default-router 172.16.2.129
dns-server 172.16.2.130
domain-name softech.com
```

### What it does

Creates the DHCP configuration for Finance VLAN 30.

---

## Step 11.5 — Verify DHCP

Use:

```cisco
do show ip dhcp pool
```

To view assigned leases:

```cisco
do show ip dhcp binding
```

---

# 12. Configure the VPCS Clients

For each VPCS:

1. Open its console.
2. Request an address from DHCP.

Type:

```text
ip dhcp
```

Then verify:

```text
show ip
```

### Expected Results

#### IT PCs

Should receive:

```text
IP:      172.16.0.x
Mask:    255.255.254.0
Gateway: 172.16.0.1
```

#### Sales PCs

Should receive:

```text
IP:      172.16.2.x
Mask:    255.255.255.128
Gateway: 172.16.2.1
```

#### Finance PC

Should receive:

```text
IP:      172.16.2.x
Mask:    255.255.255.192
Gateway: 172.16.2.129
```

The exact host address depends on DHCP assignment.

---

# 13. Add and Configure the Linux DNS Server

The DNS server will belong to the Finance subnet.

## Step 13.1 — Connect the Server

Connect the Linux server to a switch port assigned to:

```text
VLAN 30
```

## Step 13.2 — Configure a Static IP

Use:

```text
IP Address:   172.16.2.130
Subnet Mask:  255.255.255.192
Gateway:      172.16.2.129
DNS Server:   172.16.2.130
```

## Step 13.3 — Install BIND9

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install bind9
```

### What it does

- `apt update` refreshes the package information.
- `apt install bind9` installs the BIND DNS server.

The intended DNS record is:

```text
www.softech.com → 172.16.2.130
```

> The exact BIND9 zone-file configuration should be completed and tested when the Linux server has been added to the topology.

---

# 14. Optional Web Server

The same Linux machine can also host a website.

Install Apache:

```bash
sudo apt install apache2
```

### What it does

Installs the Apache HTTP web server.

Test using:

```text
http://172.16.2.130
```

After DNS is configured, the intended hostname is:

```text
http://www.softech.com
```

---

# 15. Testing and Verification

Perform tests in this order.

## Test 1 — Router Interface Status

On R1:

```cisco
show ip interface brief
```

Verify the configured addresses.

---

## Test 2 — DHCP

On every VPCS:

```text
ip dhcp
show ip
```

Verify that each client receives an address from the correct subnet.

---

## Test 3 — Gateway Connectivity

From an IT PC:

```text
ping 172.16.0.1
```

From a Sales PC:

```text
ping 172.16.2.1
```

From a Finance PC:

```text
ping 172.16.2.129
```

Each PC should first be able to reach its own gateway.

---

## Test 4 — Same VLAN Connectivity

Test communication between devices in the same department.

Example:

```text
PC-IT1 → ping PC-IT2
PC-SALES1 → ping PC-SALES2
```

---

## Test 5 — Inter-VLAN Routing

Test communication across departments.

Examples:

```text
PC-IT1 → ping PC-SALES1
PC-IT1 → ping PC-FINANCE1
PC-SALES1 → ping PC-FINANCE1
```

A successful path is conceptually:

```text
IT PC
  ↓
S1
  ↓
R1
  ↓
S1
  ↓
Sales or Finance PC
```

---

## Test 6 — DNS

From a Linux client or suitable host:

```bash
nslookup www.softech.com 172.16.2.130
```

Expected result:

```text
www.softech.com
Address: 172.16.2.130
```

Then:

```bash
ping www.softech.com
```

If a web server is installed:

```bash
curl http://www.softech.com
```

---

# 16. Saving the Configuration

After successful router configuration:

```cisco
end
copy running-config startup-config
```

### What it does

Copies the active configuration from RAM to NVRAM so that it can survive a router reload.

You can also use:

```cisco
write memory
```

Verify the saved configuration when needed with:

```cisco
show startup-config
```

In GNS3, also save the project using:

```text
File → Save Project
```

---

# 17. Troubleshooting

## Problem: `Invalid input detected at '^' marker`

### Possible reason

A command was entered in the wrong configuration mode.

### Example

If you are already at:

```text
R1(config)#
```

Do not enter:

```cisco
configure terminal
```

again.

To run a show command from configuration mode:

```cisco
do show ip interface brief
```

---

## Problem: Interface is `administratively down`

Enter the interface and run:

```cisco
no shutdown
```

Example:

```cisco
interface FastEthernet0/0
no shutdown
```

---

## Problem: Router cannot be renamed

If GNS3 displays a message that a powered-on node cannot be renamed:

1. Stop the node.
2. Rename it.
3. Start it again.

---

## Problem: PC Cannot Obtain a DHCP Address

Check the following:

1. The PC is connected to the correct switch port.
2. The switch port belongs to the correct VLAN.
3. The VLAN reaches the router correctly.
4. The correct router subinterface exists.
5. The DHCP pool network and subnet mask are correct.
6. The router interface is enabled.
7. Check:

```cisco
show ip dhcp pool
show ip dhcp binding
```

---

## Problem: Inter-VLAN Ping Fails

Check:

```cisco
show ip interface brief
```

Verify:

```text
Fa0/0.10 → VLAN 10 → 172.16.0.1
Fa0/0.20 → VLAN 20 → 172.16.2.1
Fa0/0.30 → VLAN 30 → 172.16.2.129
```

Also verify the switch VLAN membership and the VLAN transport on the router-switch connection.

---

# 18. Current Project Progress

## Completed

- [x] Opened GNS3
- [x] Added Cisco c3745 router
- [x] Renamed router to `R1`
- [x] Added GNS3 Ethernet switch
- [x] Renamed switch to `S1`
- [x] Connected `R1 FastEthernet0/0` to `S1 Ethernet0`
- [x] Added 5 VPCS devices
- [x] Renamed all VPCS devices
- [x] Connected all VPCS devices to S1
- [x] Started the devices
- [x] Entered router configuration mode
- [x] Checked router interfaces
- [x] Enabled `FastEthernet0/0`
- [x] Configured the VLAN 10 / IT router subinterface

### VLAN 10 configuration already entered

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

## Next Step

Continue with **VLAN 20 — Sales**:

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

After that, configure **VLAN 30 — Finance**:

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

Then configure the built-in GNS3 Ethernet switch VLAN membership and continue with DHCP.

---

# Final Configuration Checklist

- [x] VLSM calculated
- [x] Addressing plan created
- [x] R1 added
- [x] S1 added
- [x] Five VPCS devices added
- [x] Physical connections created
- [x] Fa0/0 enabled
- [x] VLAN 10 router subinterface configured
- [ ] VLAN 20 router subinterface configured
- [ ] VLAN 30 router subinterface configured
- [ ] Switch VLAN membership configured
- [ ] Router-switch VLAN transport verified
- [ ] DHCP pools configured
- [ ] VPCS clients obtain DHCP addresses
- [ ] Linux server added
- [ ] DNS server configured
- [ ] Optional Apache web server configured
- [ ] Same-VLAN connectivity tested
- [ ] Inter-VLAN routing tested
- [ ] DNS resolution tested
- [ ] Router configuration saved
- [ ] GNS3 project saved

---

## Project Command Summary

### Router

```cisco
enable
configure terminal

interface FastEthernet0/0
no shutdown

interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0

interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128

interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

### DHCP

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9
ip dhcp excluded-address 172.16.2.1 172.16.2.9
ip dhcp excluded-address 172.16.2.129 172.16.2.139

ip dhcp pool IT_POOL
network 172.16.0.0 255.255.254.0
default-router 172.16.0.1
dns-server 172.16.2.130
domain-name softech.com

ip dhcp pool SALES_POOL
network 172.16.2.0 255.255.255.128
default-router 172.16.2.1
dns-server 172.16.2.130
domain-name softech.com

ip dhcp pool FINANCE_POOL
network 172.16.2.128 255.255.255.192
default-router 172.16.2.129
dns-server 172.16.2.130
domain-name softech.com
```

### Verification

```cisco
show ip interface brief
show ip dhcp pool
show ip dhcp binding
show running-config
```

### Save

```cisco
copy running-config startup-config
```
