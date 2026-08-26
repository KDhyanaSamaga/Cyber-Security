# Softtech Solutions GNS3 Network Project

## Executed Configuration Commands

This README documents the commands and configuration actions that were actually executed during the current GNS3 setup session.

---

## 1. Enter Privileged EXEC Mode

### What this command does
Moves from normal user mode to privileged mode, where administrative and configuration commands are available.

### Command

```cisco
enable
```

---

## 2. Enter Global Configuration Mode

### What this command does
Enters global configuration mode so router settings and interfaces can be configured.

### Command

```cisco
configure terminal
```

---

## 3. Check Router Interface Status

### What this command does
Displays router interfaces, their IP addresses, and whether they are administratively enabled and operational.

### Command

```cisco
do show ip interface brief
```

> `do` allows an EXEC command to be run while inside configuration mode.

---

## 4. Select the Physical Interface Connected to the Switch

### What this command does
Selects `FastEthernet0/0`, the physical router interface connected to S1.

### Command

```cisco
interface FastEthernet0/0
```

---

## 5. Enable the Physical Router Interface

### What this command does
Administratively enables `FastEthernet0/0`.

### Command

```cisco
no shutdown
```

---

## 6. Exit Interface Configuration Mode

### What this command does
Returns from interface configuration mode to global configuration mode.

### Command

```cisco
exit
```

---

# Router-on-a-Stick Configuration

The router uses subinterfaces on `FastEthernet0/0` to route traffic between VLAN 10, VLAN 20, and VLAN 30.

---

## 7. Configure VLAN 10 — IT Department

### What these commands do
Creates subinterface `FastEthernet0/0.10`, associates it with VLAN 10 using IEEE 802.1Q tagging, and assigns the IT department's default gateway IP address.

### Commands

```cisco
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0
```

### Result

```text
VLAN: 10
Department: IT
Network: 172.16.0.0/23
Gateway: 172.16.0.1
```

---

## 8. Configure VLAN 20 — Sales Department

### What these commands do
Creates subinterface `FastEthernet0/0.20`, associates it with VLAN 20 using IEEE 802.1Q tagging, and assigns the Sales department's default gateway IP address.

### Commands

```cisco
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128
```

### Result

```text
VLAN: 20
Department: Sales
Network: 172.16.2.0/25
Gateway: 172.16.2.1
```

---

## 9. Configure VLAN 30 — Finance Department

### What these commands do
Creates subinterface `FastEthernet0/0.30`, associates it with VLAN 30 using IEEE 802.1Q tagging, and assigns the Finance department's default gateway IP address.

### Commands

```cisco
interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192
```

### Result

```text
VLAN: 30
Department: Finance
Network: 172.16.2.128/26
Gateway: 172.16.2.129
```

---

## 10. Return to Privileged EXEC Mode

### What this command does
Exits configuration mode and returns directly to privileged EXEC mode.

### Command

```cisco
end
```

---

## 11. Verify Router Interfaces and Subinterfaces

### What this command does
Shows the status and IP addresses of all router interfaces and subinterfaces.

### Command

```cisco
show ip interface brief
```

### Verified Configuration

```text
FastEthernet0/0      -> Physical interface connected to S1
FastEthernet0/0.10   -> 172.16.0.1
FastEthernet0/0.20   -> 172.16.2.1
FastEthernet0/0.30   -> 172.16.2.129
```

---

## 12. Save the Router Configuration

### What this command does
Copies the current running configuration to startup configuration so the router can restore the configuration after a reload.

### Command

```cisco
copy running-config startup-config
```

### Prompt Encountered

```text
Destination filename [startup-config]?
```

Press:

```text
Enter
```

A successful save typically displays:

```text
[OK]
```

---

# GNS3 Built-in Ethernet Switch Configuration

S1 is the built-in GNS3 Ethernet switch, not an IOS switch. Therefore, VLANs were configured through:

```text
Right-click S1 -> Configure
```

No Cisco IOS switch commands were executed on S1.

The switch configuration uses:

```text
Port
VLAN
Type
Add
Apply
OK
```

The available port types used were:

```text
access
dot1q
```

---

## 13. Configure Port 0 for VLAN 10

### What this configuration does
Allows tagged VLAN 10 traffic between S1 and R1.

### Settings

```text
Port: 0
VLAN: 10
Type: dot1q
```

Action:

```text
Click Add
```

---

## 14. Configure Port 0 for VLAN 20

### What this configuration does
Allows tagged VLAN 20 traffic between S1 and R1.

### Settings

```text
Port: 0
VLAN: 20
Type: dot1q
```

Action:

```text
Click Add
```

---

## 15. Configure Port 0 for VLAN 30

### What this configuration does
Allows tagged VLAN 30 traffic between S1 and R1.

### Settings

```text
Port: 0
VLAN: 30
Type: dot1q
```

Action:

```text
Click Add
```

### Result

Port 0 carries:

```text
VLAN 10
VLAN 20
VLAN 30
```

This provides the tagged connection required for Router-on-a-Stick.

---

## 16. Configure Port 1 for PC-IT1

### What this configuration does
Places PC-IT1 into VLAN 10 as an access port.

### Settings

```text
Port: 1
VLAN: 10
Type: access
```

Action:

```text
Click Add
```

---

## 17. Configure Port 2 for PC-IT2

### What this configuration does
Places PC-IT2 into VLAN 10 as an access port.

### Settings

```text
Port: 2
VLAN: 10
Type: access
```

Action:

```text
Click Add
```

---

## 18. Configure Port 3 for PC-SALES1

### What this configuration does
Places PC-SALES1 into VLAN 20 as an access port.

### Settings

```text
Port: 3
VLAN: 20
Type: access
```

Action:

```text
Click Add
```

---

## 19. Configure Port 4 for PC-SALES2

### What this configuration does
Places PC-SALES2 into VLAN 20 as an access port.

### Settings

```text
Port: 4
VLAN: 20
Type: access
```

Action:

```text
Click Add
```

---

## 20. Configure Port 5 for PC-FINANCE1

### What this configuration does
Places PC-FINANCE1 into VLAN 30 as an access port.

### Settings

```text
Port: 5
VLAN: 30
Type: access
```

Action:

```text
Click Add
```

---

## 21. Apply and Save the Switch Configuration

### What this action does
Applies the VLAN port assignments and closes the switch configuration window.

### Actions

```text
Click Apply
Click OK
```

---

# Final Configuration Summary

## Router

```text
R1 FastEthernet0/0
```

Router subinterfaces:

```text
FastEthernet0/0.10 -> VLAN 10 -> 172.16.0.1/23
FastEthernet0/0.20 -> VLAN 20 -> 172.16.2.1/25
FastEthernet0/0.30 -> VLAN 30 -> 172.16.2.129/26
```

## Switch

```text
Port 0 -> VLAN 10 -> dot1q
Port 0 -> VLAN 20 -> dot1q
Port 0 -> VLAN 30 -> dot1q

Port 1 -> VLAN 10 -> access
Port 2 -> VLAN 10 -> access

Port 3 -> VLAN 20 -> access
Port 4 -> VLAN 20 -> access

Port 5 -> VLAN 30 -> access
```

## Device-to-Port Mapping

```text
S1 Port 0 -> R1 FastEthernet0/0

S1 Port 1 -> PC-IT1
S1 Port 2 -> PC-IT2

S1 Port 3 -> PC-SALES1
S1 Port 4 -> PC-SALES2

S1 Port 5 -> PC-FINANCE1
```

## VLAN Summary

| VLAN | Department | Network | Gateway |
|---|---|---|---|
| 10 | IT | 172.16.0.0/23 | 172.16.0.1 |
| 20 | Sales | 172.16.2.0/25 | 172.16.2.1 |
| 30 | Finance | 172.16.2.128/26 | 172.16.2.129 |

---

# Commands Executed So Far — Quick Reference

```cisco
enable
configure terminal

do show ip interface brief

interface FastEthernet0/0
no shutdown
exit

interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 172.16.0.1 255.255.254.0

interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 172.16.2.1 255.255.255.128

interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 172.16.2.129 255.255.255.192

end

show ip interface brief

copy running-config startup-config
```

---

# Current Project Status

Completed:

- [x] Added and connected R1, S1, and five VPCS devices
- [x] Renamed devices
- [x] Enabled R1 FastEthernet0/0
- [x] Configured Router-on-a-Stick
- [x] Configured VLAN 10
- [x] Configured VLAN 20
- [x] Configured VLAN 30
- [x] Verified router interfaces
- [x] Saved router configuration
- [x] Configured GNS3 switch VLAN assignments
- [x] Applied switch configuration

Not yet confirmed/executed:

- [ ] Configure PC-IT1 with a manual IP address
- [ ] Test ping from PC-IT1 to its gateway
- [ ] Test same-VLAN connectivity
- [ ] Test inter-VLAN routing
- [ ] Configure DHCP
- [ ] Configure Linux DNS server
- [ ] Configure optional Apache web server
- [ ] Perform final end-to-end testing
