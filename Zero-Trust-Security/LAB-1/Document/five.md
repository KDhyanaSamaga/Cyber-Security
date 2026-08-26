# Softtech Solutions GNS3 Network Project — DHCP Configuration README

## Project Overview

This README documents the commands executed during the **DHCP configuration and testing phase** of the Softtech Solutions GNS3 network project.

The network contains three VLANs:

| Department | VLAN | Network           | Gateway        |
| ---------- | ---: | ----------------- | -------------- |
| IT         |   10 | `172.16.0.0/23`   | `172.16.0.1`   |
| Sales      |   20 | `172.16.2.0/25`   | `172.16.2.1`   |
| Finance    |   30 | `172.16.2.128/26` | `172.16.2.129` |

DHCP is configured on **R1**, and the five VPCS clients obtain their network configuration automatically.

---

# 1. Enter Privileged EXEC Mode

## What This Command Does

Enters privileged EXEC mode on the Cisco router, allowing access to administrative and configuration commands.

## Command

```cisco
enable
```

---

# 2. Enter Global Configuration Mode

## What This Command Does

Enters global configuration mode, where router-wide settings such as DHCP pools and excluded addresses can be configured.

## Command

```cisco
configure terminal
```

---

# 3. Exclude Reserved IP Addresses

These commands prevent DHCP from assigning important infrastructure addresses.

---

## 3.1 Exclude IT Reserved Addresses

## What This Command Does

Reserves addresses `172.16.0.1` through `172.16.0.9`.

The gateway `172.16.0.1` will not be assigned to a DHCP client.

## Command

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9
```

---

## 3.2 Exclude Sales Reserved Addresses

## What This Command Does

Reserves addresses `172.16.2.1` through `172.16.2.9`.

The gateway `172.16.2.1` will not be assigned to a DHCP client.

## Command

```cisco
ip dhcp excluded-address 172.16.2.1 172.16.2.9
```

---

## 3.3 Exclude Finance Reserved Addresses

## What This Command Does

Reserves addresses `172.16.2.129` through `172.16.2.139`.

The gateway `172.16.2.129` and reserved infrastructure addresses will not be assigned through DHCP.

## Command

```cisco
ip dhcp excluded-address 172.16.2.129 172.16.2.139
```

---

# 4. Create the IT DHCP Pool

## What This Command Does

Creates a DHCP pool named `IT_POOL`.

## Command

```cisco
ip dhcp pool IT_POOL
```

---

# 5. Configure the IT Network

## What This Command Does

Defines the IT subnet from which the DHCP server can assign IP addresses.

## Command

```cisco
network 172.16.0.0 255.255.254.0
```

---

# 6. Configure the IT Default Gateway

## What This Command Does

Tells DHCP clients in the IT VLAN to use `172.16.0.1` as their default gateway.

## Command

```cisco
default-router 172.16.0.1
```

---

# 7. Configure the IT DNS Server

## What This Command Does

Provides DHCP clients with the DNS server address.

The planned DNS server address is `172.16.2.130`.

## Command

```cisco
dns-server 172.16.2.130
```

---

# 8. Configure the IT Domain Name

## What This Command Does

Assigns the domain name `softech.com` to DHCP clients.

## Command

```cisco
domain-name softech.com
```

---

# 9. Exit the IT DHCP Pool

## What This Command Does

Leaves the IT DHCP pool configuration mode and returns to global configuration mode.

## Command

```cisco
exit
```

---

# 10. Create the Sales DHCP Pool

## What This Command Does

Creates a DHCP pool named `SALES_POOL`.

## Command

```cisco
ip dhcp pool SALES_POOL
```

---

# 11. Configure the Sales Network

## What This Command Does

Defines the Sales subnet from which DHCP addresses will be assigned.

## Command

```cisco
network 172.16.2.0 255.255.255.128
```

---

# 12. Configure the Sales Default Gateway

## What This Command Does

Tells Sales DHCP clients to use `172.16.2.1` as their default gateway.

## Command

```cisco
default-router 172.16.2.1
```

---

# 13. Configure the Sales DNS Server

## What This Command Does

Provides the DNS server address to Sales DHCP clients.

## Command

```cisco
dns-server 172.16.2.130
```

---

# 14. Configure the Sales Domain Name

## What This Command Does

Assigns the domain name `softech.com` to Sales DHCP clients.

## Command

```cisco
domain-name softech.com
```

---

# 15. Exit the Sales DHCP Pool

## What This Command Does

Leaves the `SALES_POOL` configuration mode and returns to global configuration mode.

## Command

```cisco
exit
```

---

# 16. Create the Finance DHCP Pool

## What This Command Does

Creates a DHCP pool named `FINANCE_POOL`.

## Command

```cisco
ip dhcp pool FINANCE_POOL
```

---

# 17. Configure the Finance Network

## What This Command Does

Defines the Finance subnet from which DHCP addresses will be assigned.

## Command

```cisco
network 172.16.2.128 255.255.255.192
```

---

# 18. Configure the Finance Default Gateway

## What This Command Does

Tells Finance DHCP clients to use `172.16.2.129` as their default gateway.

## Command

```cisco
default-router 172.16.2.129
```

---

# 19. Configure the Finance DNS Server

## What This Command Does

Provides the DNS server address to Finance DHCP clients.

## Command

```cisco
dns-server 172.16.2.130
```

---

# 20. Configure the Finance Domain Name

## What This Command Does

Assigns the domain name `softech.com` to Finance DHCP clients.

## Command

```cisco
domain-name softech.com
```

---

# 21. Exit the Finance DHCP Pool

## What This Command Does

Leaves the `FINANCE_POOL` configuration mode and returns to global configuration mode.

## Command

```cisco
exit
```

---

# 22. Verify All DHCP Pools

## What This Command Does

Displays information about all configured DHCP pools, including:

* Pool name
* Network size
* Number of available addresses
* Number of leased addresses

## Command

```cisco
show ip dhcp pool
```

The project verification showed the following pools:

```text
IT_POOL
SALES_POOL
FINANCE_POOL
```

---

# 23. Save the Router Configuration

## What This Command Does

Copies the current running configuration to startup configuration.

This ensures the DHCP configuration remains available after the router is restarted.

## Command

```cisco
copy running-config startup-config
```

If prompted with:

```text
Destination filename [startup-config]?
```

Press:

```text
Enter
```

A successful save should display:

```text
[OK]
```

---

# 24. Configure IT-1 to Use DHCP

## What This Command Does

Sends a DHCP request from IT-1 to R1 and automatically configures its:

* IP address
* Subnet mask
* Default gateway

## Command

```text
dhcp
```

IT-1 successfully received:

```text
IP Address: 172.16.0.12/23
Gateway:    172.16.0.1
```

---

# 25. Display IT-1 IP Configuration

## What This Command Does

Displays the IP configuration currently assigned to the VPCS client.

## Command

```text
show ip
```

---

# 26. Test IT-1 Connectivity to Its Gateway

## What This Command Does

Tests connectivity between IT-1 and the VLAN 10 gateway.

## Command

```text
ping 172.16.0.1
```

The ping completed successfully.

---

# 27. Configure IT-2 to Use DHCP

## What This Command Does

Requests an IP address automatically from the `IT_POOL`.

## Command

```text
dhcp
```

IT-2 successfully received a DHCP address from the IT subnet.

---

# 28. Test IT-2 Connectivity to Its Gateway

## What This Command Does

Tests whether IT-2 can communicate with the VLAN 10 gateway.

## Command

```text
ping 172.16.0.1
```

The connectivity test completed successfully.

---

# 29. Configure SA-1 to Use DHCP

## What This Command Does

Requests an IP address automatically from the `SALES_POOL`.

## Command

```text
dhcp
```

SA-1 successfully received an IP address from the Sales subnet.

---

# 30. Test SA-1 Connectivity to Its Gateway

## What This Command Does

Tests connectivity between SA-1 and the VLAN 20 gateway.

## Command

```text
ping 172.16.2.1
```

The connectivity test completed successfully.

---

# 31. Configure SA-2 to Use DHCP

## What This Command Does

Requests an IP address automatically from the `SALES_POOL`.

## Command

```text
dhcp
```

SA-2 successfully received an IP address from the Sales subnet.

---

# 32. Test SA-2 Connectivity to Its Gateway

## What This Command Does

Tests connectivity between SA-2 and the VLAN 20 gateway.

## Command

```text
ping 172.16.2.1
```

The connectivity test completed successfully.

---

# 33. Configure FIN-1 to Use DHCP

## What This Command Does

Requests an IP address automatically from the `FINANCE_POOL`.

## Command

```text
dhcp
```

FIN-1 successfully received an IP address from the Finance subnet.

---

# 34. Test FIN-1 Connectivity to Its Gateway

## What This Command Does

Tests connectivity between FIN-1 and the VLAN 30 gateway.

## Command

```text
ping 172.16.2.129
```

The connectivity test completed successfully.

---

# 35. Verify DHCP Lease Bindings

## What This Command Does

Displays all IP addresses currently leased by the Cisco DHCP server.

It also shows the client identifier, lease expiration, and assignment type.

## Command

```cisco
show ip dhcp binding
```

The following DHCP leases were verified:

| DHCP IP Address | Assignment Type |
| --------------- | --------------- |
| `172.16.0.12`   | Automatic       |
| `172.16.0.13`   | Automatic       |
| `172.16.2.12`   | Automatic       |
| `172.16.2.13`   | Automatic       |
| `172.16.2.141`  | Automatic       |

This confirms that all five VPCS clients successfully received DHCP addresses.

---

# Final DHCP Address Assignments

| Device | DHCP Address   | Subnet | Gateway        |
| ------ | -------------- | ------ | -------------- |
| IT-1   | `172.16.0.12`  | `/23`  | `172.16.0.1`   |
| IT-2   | `172.16.0.13`  | `/23`  | `172.16.0.1`   |
| SA-1   | `172.16.2.12`  | `/25`  | `172.16.2.1`   |
| SA-2   | `172.16.2.13`  | `/25`  | `172.16.2.1`   |
| FIN-1  | `172.16.2.141` | `/26`  | `172.16.2.129` |

---

# DHCP Command Summary

## Router Commands

```cisco
enable
configure terminal

ip dhcp excluded-address 172.16.0.1 172.16.0.9
ip dhcp excluded-address 172.16.2.1 172.16.2.9
ip dhcp excluded-address 172.16.2.129 172.16.2.139

ip dhcp pool IT_POOL
network 172.16.0.0 255.255.254.0
default-router 172.16.0.1
dns-server 172.16.2.130
domain-name softech.com
exit

ip dhcp pool SALES_POOL
network 172.16.2.0 255.255.255.128
default-router 172.16.2.1
dns-server 172.16.2.130
domain-name softech.com
exit

ip dhcp pool FINANCE_POOL
network 172.16.2.128 255.255.255.192
default-router 172.16.2.129
dns-server 172.16.2.130
domain-name softech.com
exit

show ip dhcp pool
show ip dhcp binding

copy running-config startup-config
```

---

## VPCS Commands

### IT-1

```text
dhcp
show ip
ping 172.16.0.1
```

### IT-2

```text
dhcp
ping 172.16.0.1
```

### SA-1

```text
dhcp
ping 172.16.2.1
```

### SA-2

```text
dhcp
ping 172.16.2.1
```

### FIN-1

```text
dhcp
ping 172.16.2.129
```

---

# Current Project Status

The following components have been successfully completed:

* [x] VLSM subnet design
* [x] VLAN 10 — IT
* [x] VLAN 20 — Sales
* [x] VLAN 30 — Finance
* [x] Router-on-a-Stick configuration
* [x] Inter-VLAN routing
* [x] DHCP excluded addresses
* [x] IT DHCP pool
* [x] Sales DHCP pool
* [x] Finance DHCP pool
* [x] IT-1 DHCP configuration
* [x] IT-2 DHCP configuration
* [x] SA-1 DHCP configuration
* [x] SA-2 DHCP configuration
* [x] FIN-1 DHCP configuration
* [x] Gateway connectivity testing
* [x] DHCP lease verification

## Current Next Step

The last confirmed verification command was:

```cisco
show ip dhcp binding
```

The five DHCP leases were successfully displayed.

The next step is to ensure the latest router configuration is saved:

```cisco
copy running-config startup-config
```

After DHCP is fully finalized, the next major project phase is:

1. Add a Linux server.
2. Assign it `172.16.2.130/26`.
3. Use `172.16.2.129` as the gateway.
4. Configure the server for VLAN 30.
5. Install and configure BIND9 DNS.
6. Configure the `softech.com` domain.
7. Create the DNS record:

```text
www.softech.com → 172.16.2.130
```

8. Test DNS resolution from the DHCP clients.
9. Optionally configure an Apache web server.
