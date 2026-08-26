# Softtech Solutions GNS3 Network Project

## Complete README — Commands Executed and Their Purpose

This document contains the **commands actually executed during the GNS3 network configuration and testing process**. It includes the command, what it does, and the relevant configuration details.

---

# 1. Project Overview

The project simulates a small company network for **Softtech Solutions** using:

* Cisco c3745 Router
* Built-in GNS3 Ethernet Switch
* 5 VPCS clients
* VLANs
* VLSM
* Router-on-a-Stick
* Inter-VLAN Routing

## Main Network

```text
172.16.0.0
```

## Department and VLAN Allocation

| Department | VLAN | Network         | Subnet Mask     | Gateway      |
| ---------- | ---: | --------------- | --------------- | ------------ |
| IT         |   10 | 172.16.0.0/23   | 255.255.254.0   | 172.16.0.1   |
| Sales      |   20 | 172.16.2.0/25   | 255.255.255.128 | 172.16.2.1   |
| Finance    |   30 | 172.16.2.128/26 | 255.255.255.192 | 172.16.2.129 |

---

# 2. Router Basic Configuration

## Enter Privileged EXEC Mode

### What this command does

Moves from normal user mode into privileged mode, allowing administrative commands to be executed.

```cisco
enable
```

---

## Enter Global Configuration Mode

### What this command does

Enters router configuration mode, where interfaces, IP addresses, routing, and other settings can be configured.

```cisco
configure terminal
```

---

# 3. Enable the Physical Router Interface

The router connects to the GNS3 switch through:

```text
FastEthernet0/0
```

## Enter the Interface

### What this command does

Selects the physical FastEthernet0/0 interface for configuration.

```cisco
interface FastEthernet0/0
```

## Enable the Interface

### What this command does

Administratively enables the interface.

```cisco
no shutdown
```

## Exit Interface Configuration

### What this command does

Exits the current interface configuration mode.

```cisco
exit
```

---

# 4. Configure VLAN 10 — IT Department

## Enter VLAN 10 Subinterface

### What this command does

Creates/selects a logical subinterface for VLAN 10.

```cisco
interface FastEthernet0/0.10
```

## Configure 802.1Q VLAN Tagging

### What this command does

Associates this router subinterface with VLAN 10 using IEEE 802.1Q encapsulation.

```cisco
encapsulation dot1Q 10
```

## Assign the VLAN 10 Gateway Address

### What this command does

Assigns the default gateway address for devices in the IT network.

```cisco
ip address 172.16.0.1 255.255.254.0
```

---

# 5. Configure VLAN 20 — Sales Department

## Enter VLAN 20 Subinterface

### What this command does

Creates/selects a logical router subinterface for VLAN 20.

```cisco
interface FastEthernet0/0.20
```

## Configure VLAN 20 Encapsulation

### What this command does

Associates this subinterface with VLAN 20.

```cisco
encapsulation dot1Q 20
```

## Assign the VLAN 20 Gateway Address

### What this command does

Sets the default gateway for devices in the Sales network.

```cisco
ip address 172.16.2.1 255.255.255.128
```

---

# 6. Configure VLAN 30 — Finance Department

## Enter VLAN 30 Subinterface

### What this command does

Creates/selects a logical router subinterface for VLAN 30.

```cisco
interface FastEthernet0/0.30
```

## Configure VLAN 30 Encapsulation

### What this command does

Associates this subinterface with VLAN 30 using 802.1Q tagging.

```cisco
encapsulation dot1Q 30
```

## Assign the VLAN 30 Gateway Address

### What this command does

Sets the default gateway for devices in the Finance network.

```cisco
ip address 172.16.2.129 255.255.255.192
```

---

# 7. Verify Router Interfaces

## Display Interface Status

### What this command does

Displays:

* Interface names
* IP addresses
* Interface status
* Line protocol status

```cisco
show ip interface brief
```

## Verified Result

The important interfaces were successfully configured as:

```text
FastEthernet0/0       up/up

FastEthernet0/0.10    172.16.0.1       up/up
FastEthernet0/0.20    172.16.2.1       up/up
FastEthernet0/0.30    172.16.2.129     up/up
```

---

# 8. Save Router Configuration

## Save Running Configuration

### What this command does

Copies the current router configuration from RAM into startup configuration so that it remains after a router restart.

```cisco
copy running-config startup-config
```

---

# 9. GNS3 Built-in Ethernet Switch Configuration

The built-in GNS3 Ethernet Switch does not use a Cisco IOS CLI.

The switch was configured using:

```text
Right-click S1 → Configure
```

## Final Switch Port Configuration

| Port      | VLAN | Type   | Connected Device   |
| --------- | ---: | ------ | ------------------ |
| Ethernet0 |    1 | dot1q  | R1 FastEthernet0/0 |
| Ethernet0 |   10 | dot1q  | R1 FastEthernet0/0 |
| Ethernet0 |   20 | dot1q  | R1 FastEthernet0/0 |
| Ethernet0 |   30 | dot1q  | R1 FastEthernet0/0 |
| Ethernet1 |   10 | access | IT-1               |
| Ethernet2 |   10 | access | IT-2               |
| Ethernet3 |   20 | access | SA-1               |
| Ethernet4 |   20 | access | SA-2               |
| Ethernet5 |   30 | access | FIN-1              |

## Important VLAN 30 Fix

Initially, VLAN 30 was configured as the native VLAN on Ethernet0.

This caused the Finance PC to fail to reach its gateway.

The configuration was corrected so that:

```text
Native VLAN: VLAN 1
```

while VLAN 10, VLAN 20, and VLAN 30 remain tagged using:

```text
dot1q
```

This allowed VLAN 30 traffic to correctly reach:

```text
R1 FastEthernet0/0.30
```

---

# 10. Configure IT-1

## Assign Static IP Address

### What this command does

Assigns:

* IP address: `172.16.0.10`
* Subnet mask: `255.255.254.0`
* Default gateway: `172.16.0.1`

```text
ip 172.16.0.10 255.255.254.0 172.16.0.1
```

## Display Current VPCS IP Configuration

### What this command does

Displays the VPCS name, IP address, gateway, MAC address, and other interface information.

```text
show ip
```

## Save VPCS Configuration

### What this command does

Saves the current VPCS configuration.

```text
save
```

## Test Connection to VLAN 10 Gateway

### What this command does

Tests connectivity from IT-1 to the router gateway.

```text
ping 172.16.0.1
```

### Result

Successful.

---

# 11. Configure IT-2

## Assign Static IP Address

### What this command does

Assigns:

* IP address: `172.16.0.11`
* Subnet mask: `255.255.254.0`
* Gateway: `172.16.0.1`

```text
ip 172.16.0.11 255.255.254.0 172.16.0.1
```

## Test Connection to VLAN 10 Gateway

### What this command does

Tests whether IT-2 can communicate with its default gateway.

```text
ping 172.16.0.1
```

### Result

Successful.

## Test Communication Between IT PCs

### What this command does

Tests communication between IT-2 and IT-1 within VLAN 10.

```text
ping 172.16.0.10
```

### Result

Successful.

---

# 12. Configure SA-1

## Assign Static IP Address

### What this command does

Assigns:

* IP address: `172.16.2.10`
* Subnet mask: `255.255.255.128`
* Gateway: `172.16.2.1`

```text
ip 172.16.2.10 255.255.255.128 172.16.2.1
```

## Test Connection to VLAN 20 Gateway

### What this command does

Tests communication between SA-1 and the VLAN 20 router gateway.

```text
ping 172.16.2.1
```

### Result

Successful.

---

# 13. Configure SA-2

## Assign Static IP Address

### What this command does

Assigns:

* IP address: `172.16.2.11`
* Subnet mask: `255.255.255.128`
* Gateway: `172.16.2.1`

```text
ip 172.16.2.11 255.255.255.128 172.16.2.1
```

## Test Connection to VLAN 20 Gateway

### What this command does

Tests communication between SA-2 and its default gateway.

```text
ping 172.16.2.1
```

### Result

Successful.

## Test Communication Between Sales PCs

### What this command does

Tests communication from SA-2 to SA-1 within VLAN 20.

```text
ping 172.16.2.10
```

### Result

Successful.

---

# 14. Configure FIN-1

## Assign Static IP Address

### What this command does

Assigns:

* IP address: `172.16.2.140`
* Subnet mask: `255.255.255.192`
* Gateway: `172.16.2.129`

```text
ip 172.16.2.140 255.255.255.192 172.16.2.129
```

## Display Finance PC IP Configuration

### What this command does

Displays the configured IP address and gateway on FIN-1.

```text
show ip
```

## Save Finance PC Configuration

### What this command does

Saves the FIN-1 VPCS configuration.

```text
save
```

---

# 15. Test Finance Gateway

## Ping the VLAN 30 Gateway

### What this command does

Tests communication between FIN-1 and the VLAN 30 router subinterface.

```text
ping 172.16.2.129
```

## Initial Result

Initially, the command returned:

```text
host (172.16.2.129) not reachable
```

## Cause

The issue was caused by S1 Ethernet0 having VLAN 30 configured as the native VLAN.

## Fix

The native VLAN was changed to VLAN 1, while VLAN 30 remained configured as a tagged `dot1q` VLAN.

## Final Result

After the switch configuration was corrected:

```text
ping 172.16.2.129
```

was successful.

---

# 16. Connectivity Tests Successfully Completed

## VLAN 10

```text
IT-1 → 172.16.0.1       Successful
IT-2 → 172.16.0.1       Successful
IT-2 → IT-1             Successful
```

Commands:

```text
ping 172.16.0.1
```

```text
ping 172.16.0.10
```

---

## VLAN 20

```text
SA-1 → 172.16.2.1       Successful
SA-2 → 172.16.2.1       Successful
SA-2 → SA-1             Successful
```

Commands:

```text
ping 172.16.2.1
```

```text
ping 172.16.2.10
```

---

## VLAN 30

```text
FIN-1 → 172.16.2.129    Successful
```

Command:

```text
ping 172.16.2.129
```

---

# 17. Current Network Status

The following components have been successfully configured and tested:

```text
VLSM Addressing                    ✓
VLAN 10 — IT                       ✓
VLAN 20 — Sales                    ✓
VLAN 30 — Finance                  ✓
Router-on-a-Stick                  ✓
802.1Q VLAN Tagging                ✓
IT Gateway Connectivity            ✓
Sales Gateway Connectivity         ✓
Finance Gateway Connectivity       ✓
Same-VLAN Communication            ✓
```

---

# 18. Next Step

The next command to execute is an inter-VLAN routing test from Finance to IT:

## Test Finance to IT Communication

### What this command does

Tests whether R1 can route traffic from:

```text
VLAN 30 → VLAN 10
```

The traffic path will be:

```text
FIN-1
172.16.2.140
     ↓
VLAN 30
     ↓
R1 FastEthernet0/0.30
     ↓
Inter-VLAN Routing
     ↓
R1 FastEthernet0/0.10
     ↓
VLAN 10
     ↓
IT-1
172.16.0.10
```

Command:

```text
ping 172.16.0.10
```

---

# 19. Planned Commands Not Yet Executed

The following commands were planned for later stages of the project but **have not yet been executed**.

## DHCP Configuration

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9

ip dhcp excluded-address 172.16.2.1 172.16.2.9

ip dhcp excluded-address 172.16.2.129 172.16.2.139
```

```cisco
ip dhcp pool IT_POOL
network 172.16.0.0 255.255.254.0
default-router 172.16.0.1
dns-server 172.16.2.130
domain-name softech.com
```

```cisco
ip dhcp pool SALES_POOL
network 172.16.2.0 255.255.255.128
default-router 172.16.2.1
dns-server 172.16.2.130
domain-name softech.com
```

```cisco
ip dhcp pool FINANCE_POOL
network 172.16.2.128 255.255.255.192
default-router 172.16.2.129
dns-server 172.16.2.130
domain-name softech.com
```

## DHCP Client Command

```text
ip dhcp
```

## Linux DNS Installation

```bash
sudo apt update
```

```bash
sudo apt install bind9
```

## Optional Apache Web Server

```bash
sudo apt install apache2
```

---

# 20. Final Topology

```text
                         R1
                  Cisco c3745 Router
                         |
                  FastEthernet0/0
                         |
              802.1Q Tagged VLANs
                   10, 20, 30
                         |
                     S1 Ethernet0
                         |
        ____________________________________
        |          |          |        |      |
    Ethernet1  Ethernet2  Ethernet3 Ethernet4 Ethernet5
        |          |          |        |      |
       IT-1       IT-2       SA-1     SA-2   FIN-1
     VLAN 10    VLAN 10    VLAN 20  VLAN 20 VLAN 30
```

---

# Project Progress

**Current stage: Manual VLAN testing completed successfully.**

The next stage is:

```text
Inter-VLAN Routing Testing
        ↓
DHCP Configuration
        ↓
Linux DNS Server
        ↓
Optional Apache Web Server
        ↓
Final End-to-End Testing
```
