# GNS3 Softtech Solutions Network Project — Complete Command Reference

This README contains the commands executed during the GNS3 network configuration so far.

The project includes:

* VLSM subnetting
* VLAN 10, VLAN 20, and VLAN 30
* Router-on-a-Stick
* Inter-VLAN Routing
* Manual VPCS IP configuration
* Connectivity testing
* DHCP configuration on the Cisco c3745 router

---

# 1. Network Addressing Summary

## VLAN 10 — IT

| Setting     | Value           |
| ----------- | --------------- |
| Network     | `172.16.0.0/23` |
| Subnet Mask | `255.255.254.0` |
| Gateway     | `172.16.0.1`    |
| VLAN ID     | `10`            |

## VLAN 20 — Sales

| Setting     | Value             |
| ----------- | ----------------- |
| Network     | `172.16.2.0/25`   |
| Subnet Mask | `255.255.255.128` |
| Gateway     | `172.16.2.1`      |
| VLAN ID     | `20`              |

## VLAN 30 — Finance

| Setting     | Value             |
| ----------- | ----------------- |
| Network     | `172.16.2.128/26` |
| Subnet Mask | `255.255.255.192` |
| Gateway     | `172.16.2.129`    |
| VLAN ID     | `30`              |

---

# 2. Enter Privileged and Global Configuration Mode

## What this does

Enters privileged EXEC mode and then global configuration mode on the Cisco router.

```cisco
enable
configure terminal
```

---

# 3. Enable the Physical Router Interface

## What this does

Selects the physical interface connected to the GNS3 switch and enables it.

```cisco
interface FastEthernet0/0
no shutdown
exit
```

---

# 4. Configure VLAN 10 — IT Router Subinterface

## What this does

Creates a subinterface for VLAN 10, enables IEEE 802.1Q encapsulation, and assigns the IT department's default gateway address.

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

---

# 5. Configure VLAN 20 — Sales Router Subinterface

## What this does

Creates a subinterface for VLAN 20 and assigns the Sales department's default gateway.

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

---

# 6. Configure VLAN 30 — Finance Router Subinterface

## What this does

Creates a subinterface for VLAN 30 and assigns the Finance department's default gateway.

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

---

# 7. Verify Router Interfaces

## What this does

Displays the status and IP address of all router interfaces and subinterfaces.

```cisco
show ip interface brief
```

Expected important interfaces:

```text
FastEthernet0/0       up/up
FastEthernet0/0.10    172.16.0.1
FastEthernet0/0.20    172.16.2.1
FastEthernet0/0.30    172.16.2.129
```

---

# 8. Save the Router Configuration

## What this does

Saves the current running configuration into startup configuration so the configuration remains after a router restart.

```cisco
copy running-config startup-config
```

When prompted for the destination filename, press:

```text
Enter
```

Successful output:

```text
[OK]
```

---

# 9. Configure IT-1 with a Static IP Address

## What this does

Assigns IT-1 a static IP address, subnet mask, and default gateway.

```text
ip 172.16.0.10 255.255.254.0 172.16.0.1
```

## Save the VPCS Configuration

```text
save
```

---

# 10. Configure IT-2 with a Static IP Address

## What this does

Assigns IT-2 an IP address in VLAN 10.

```text
ip 172.16.0.11 255.255.254.0 172.16.0.1
```

---

# 11. Configure SA-1 with a Static IP Address

## What this does

Assigns SA-1 an IP address in the Sales VLAN.

```text
ip 172.16.2.10 255.255.255.128 172.16.2.1
```

---

# 12. Configure SA-2 with a Static IP Address

## What this does

Assigns SA-2 an IP address in the Sales VLAN.

```text
ip 172.16.2.11 255.255.255.128 172.16.2.1
```

---

# 13. Configure FIN-1 with a Static IP Address

## What this does

Assigns FIN-1 an IP address in the Finance VLAN.

```text
ip 172.16.2.140 255.255.255.192 172.16.2.129
```

## Save the VPCS Configuration

```text
save
```

---

# 14. Test IT-1 Connectivity to Its Gateway

## What this does

Tests whether IT-1 can communicate with the VLAN 10 default gateway.

Run on **IT-1**:

```text
ping 172.16.0.1
```

---

# 15. Test IT-2 Connectivity to Its Gateway

## What this does

Tests whether IT-2 can communicate with the VLAN 10 gateway.

Run on **IT-2**:

```text
ping 172.16.0.1
```

---

# 16. Test Communication Between IT Devices

## What this does

Tests same-VLAN communication between IT-2 and IT-1.

Run on **IT-2**:

```text
ping 172.16.0.10
```

---

# 17. Test SA-1 Connectivity to Its Gateway

## What this does

Tests whether SA-1 can reach the VLAN 20 default gateway.

Run on **SA-1**:

```text
ping 172.16.2.1
```

---

# 18. Test SA-2 Connectivity to Its Gateway

## What this does

Tests whether SA-2 can reach the VLAN 20 default gateway.

Run on **SA-2**:

```text
ping 172.16.2.1
```

---

# 19. Test Communication Between Sales Devices

## What this does

Tests same-VLAN communication between SA-2 and SA-1.

Run on **SA-2**:

```text
ping 172.16.2.10
```

---

# 20. Test FIN-1 Connectivity to Its Gateway

## What this does

Tests whether FIN-1 can communicate with the VLAN 30 default gateway.

Run on **FIN-1**:

```text
ping 172.16.2.129
```

---

# 21. Test Inter-VLAN Routing — Finance to IT

## What this does

Tests whether traffic can travel from VLAN 30 to VLAN 10 through the router.

Run on **FIN-1**:

```text
ping 172.16.0.10
```

Traffic path:

```text
FIN-1
VLAN 30
   ↓
R1
   ↓
VLAN 10
   ↓
IT-1
```

---

# 22. Test Inter-VLAN Routing — Finance to Sales

## What this does

Tests communication from VLAN 30 to VLAN 20.

Run on **FIN-1**:

```text
ping 172.16.2.10
```

---

# 23. Test Inter-VLAN Routing — IT to Sales

## What this does

Tests communication from VLAN 10 to VLAN 20.

Run on **IT-1**:

```text
ping 172.16.2.10
```

---

# 24. Test Inter-VLAN Routing — Sales to Finance

## What this does

Tests communication from VLAN 20 to VLAN 30.

Run on **SA-1**:

```text
ping 172.16.2.140
```

---

# 25. Exclude Reserved IT Addresses from DHCP

## What this does

Prevents the router from assigning the gateway address and the reserved IT addresses `.1` through `.9`.

```cisco
ip dhcp excluded-address 172.16.0.1 172.16.0.9
```

---

# 26. Exclude Reserved Sales Addresses from DHCP

## What this does

Prevents DHCP from assigning the Sales gateway and reserved addresses.

```cisco
ip dhcp excluded-address 172.16.2.1 172.16.2.9
```

---

# 27. Exclude Reserved Finance Addresses from DHCP

## What this does

Prevents DHCP from assigning:

* Finance gateway: `172.16.2.129`
* DNS server address: `172.16.2.130`
* Other reserved addresses through `172.16.2.139`

```cisco
ip dhcp excluded-address 172.16.2.129 172.16.2.139
```

---

# 28. Create the IT DHCP Pool

## What this does

Creates a DHCP pool called `IT_POOL`.

```cisco
ip dhcp pool IT_POOL
```

---

# 29. Define the IT DHCP Network

## What this does

Tells the DHCP pool which network and subnet mask belong to IT.

```cisco
network 172.16.0.0 255.255.254.0
```

---

# 30. Configure the IT Default Gateway

## What this does

Automatically provides IT clients with `172.16.0.1` as their default gateway.

```cisco
default-router 172.16.0.1
```

---

# 31. Configure the IT DNS Server

## What this does

Provides IT clients with the DNS server address.

```cisco
dns-server 172.16.2.130
```

---

# 32. Configure the IT Domain Name

## What this does

Assigns the domain name `softech.com` to clients receiving DHCP information.

```cisco
domain-name softech.com
```

---

# 33. Exit the IT DHCP Pool

## What this does

Leaves DHCP pool configuration mode and returns to global configuration mode.

```cisco
exit
```

---

# 34. Create the Sales DHCP Pool

## What this does

Creates a DHCP pool named `SALES_POOL`.

```cisco
ip dhcp pool SALES_POOL
```

---

# 35. Define the Sales DHCP Network

## What this does

Tells the router to assign addresses from the Sales network.

```cisco
network 172.16.2.0 255.255.255.128
```

---

# 36. Configure the Sales Default Gateway

## What this does

Provides Sales clients with the correct default gateway.

```cisco
default-router 172.16.2.1
```

---

# 37. Configure the Sales DNS Server

## What this does

Provides Sales clients with the DNS server address.

```cisco
dns-server 172.16.2.130
```

---

# 38. Configure the Sales Domain Name

## What this does

Sets the domain name for Sales clients.

```cisco
domain-name softech.com
```

---

# 39. Exit the Sales DHCP Pool

## What this does

Leaves the `SALES_POOL` configuration mode.

```cisco
exit
```

---

# 40. Create the Finance DHCP Pool

## What this does

Creates a DHCP pool named `FINANCE_POOL`.

```cisco
ip dhcp pool FINANCE_POOL
```

---

# 41. Define the Finance DHCP Network

## What this does

Tells the router to assign addresses from the Finance network.

```cisco
network 172.16.2.128 255.255.255.192
```

---

# 42. Configure the Finance Default Gateway

## What this does

Provides Finance clients with `172.16.2.129` as their default gateway.

```cisco
default-router 172.16.2.129
```

---

# 43. Configure the Finance DNS Server

## What this does

Provides Finance clients with the DNS server address.

```cisco
dns-server 172.16.2.130
```

---

# 44. Configure the Finance Domain Name

## What this does

Sets `softech.com` as the domain name for Finance DHCP clients.

```cisco
domain-name softech.com
```

---

# 45. Exit the Finance DHCP Pool

## What this does

Leaves the `FINANCE_POOL` configuration mode and returns to global configuration mode.

```cisco
exit
```

---

# 46. Final DHCP Configuration Summary

The DHCP configuration completed so far is:

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

---

# 47. Current Project Status

| Feature                 | Status                        |
| ----------------------- | ----------------------------- |
| VLSM Addressing         | Complete                      |
| VLAN 10 — IT            | Working                       |
| VLAN 20 — Sales         | Working                       |
| VLAN 30 — Finance       | Working                       |
| Router-on-a-Stick       | Working                       |
| Same-VLAN Communication | Working                       |
| Inter-VLAN Routing      | Working                       |
| IT DHCP Pool            | Configured                    |
| Sales DHCP Pool         | Configured                    |
| Finance DHCP Pool       | Configured                    |
| DHCP Client Testing     | Not yet completed             |
| DNS Server              | Not yet configured            |
| Apache Web Server       | Optional / Not yet configured |

---

# 48. Next Steps

The next stage of the project should be:

1. Exit the Finance DHCP pool if not already done.
2. Verify the DHCP configuration.
3. Save the router configuration.
4. Change the VPCS clients from static addressing to DHCP.
5. Verify that each PC receives the correct:

   * IP address
   * Subnet mask
   * Default gateway
   * DNS server
6. Test connectivity again.
7. Add a Linux server to VLAN 30.
8. Configure the Linux server with:

```text
IP Address:   172.16.2.130
Subnet Mask:  255.255.255.192
Gateway:      172.16.2.129
```

9. Install BIND9.
10. Configure:

```text
www.softech.com → 172.16.2.130
```

11. Optionally install Apache Web Server.

---

**Current stopping point:** The `FINANCE_POOL` DHCP configuration has been completed. The next command to execute is:

```cisco
exit
```

After that, continue with DHCP verification and client testing.
