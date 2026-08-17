```markdown
# Network Simulation & Device Configuration Guide

A comprehensive quick-reference guide for setting up network topologies, configuring Virtual PC Simulators (VPCS), setting packet capture permissions, and managing Cisco IOS Routers.

---

## 1. GNS3 / IOS Device Template Setup

Follow this sequence to import and configure an IOS router/switch template:

1. **Open Preferences:** Navigate to `Edit` > `Preferences`.
2. **Add IOS Router:** 
   - Select **IOS Routers** on the left menu.
   - Click **New**.
   - Select **New Image** > Browse and choose your image (decompress if prompted) > Click **Next**.
   - Set the **Name** of the device/switch > Click **Next**.
   - Keep the **Default RAM** (do not change) > Click **Next**.
3. **Configure Slots / Network Modules:**
   - Click on **Slot 1**.
   - Select the network interface module (e.g., `NM-16ESW` for switching or `NM-1FE-TX` / FastEthernet).
   - Click **Next** > **Next** > **Finish**.
4. **Finalize:** Click **Apply** > **OK**.

---

## 2. VPCS (Virtual PC Simulator) Reference

### IP Addressing & Network Configuration

* **Static IP (Standard Format):**
  ```text
  ip <ip-address> <subnet-mask> <default-gateway>

```

*Example:*

```text
VPCS> ip 172.16.34.123 255.255.255.0 172.16.34.1

```

* **Static IP (CIDR Notation):**
```text
ip <ip-address>/<prefix> <default-gateway>

```


*Example:*
```text
VPCS> ip 172.16.34.123/24 172.16.34.1

```


* **DHCP Configuration (Obtain IP automatically):**
```text
VPCS> ip dhcp

```


* **DNS Server Configuration:**
```text
VPCS> ip dns <dns-ip-address>

```


*Example:*
```text
VPCS> ip dns 145.40.130.90

```



### Management & Maintenance

* **Change Hostname:**
```text
VPCS> set pcname <name>

```


* **Verify IP & TCP/IP Settings:**
```text
VPCS> show ip

```


* **Clear IP Configuration:**
```text
VPCS> clear ip

```


* **Save Configuration:**
```text
VPCS> save <filename>

```


*(If `<filename>` is omitted, the configuration is saved to the default file.)*

### Diagnostics & Connectivity Testing

* **Standard Ping / Ping with Count:**
```text
VPCS> ping 192.168.1.2 -c 5

```


* **TCP Ping (Protocol Number 6):**
```text
VPCS> ping <ip-address> -P 6 -p <port>

```


* **UDP Ping (Protocol Number 17):**
```text
VPCS> ping <ip-address> -P 17 -p <port>

```


* **Traceroute:**
```text
VPCS> trace <ip-address>

```


* **View / Verify ARP Cache:**
```text
VPCS> show arp
VPCS> arp -a

```



---

## 3. Packet Capture Permissions (Terminal)

To run packet captures (such as Wireshark / `dumpcap`) without root permission errors:

```bash
sudo chmod 4711 $(sudo which dumpcap)

```

---

## 4. Cisco IOS Router Configuration

### Command Modes & Navigation

* **Available Commands Help:**
```text
Router>?

```


* **Enter Privileged EXEC Mode:**
```text
Router> enable
Router#

```


* **Exit / Disable Privileged EXEC Mode:**
```text
Router# disable
Router>

```


* **Enter Global Configuration Mode:**
```text
Router# config t
Router(config)#

```


* **Return to Privileged EXEC Mode:**
```text
Router(config-if)# end
Router#

```


* **Exit / Terminate Session:**
```text
Router# logout

```



### Interface Configuration

```text
Router# config t
Router(config)# interface FastEthernet0/0
Router(config-if)# ip address <ip-address> <subnet-mask>
Router(config-if)# no shutdown
Router(config-if)# end

```

### Static Routing & Routing Table Operations

* **Configure Static Route:**
```text
Router(config)# ip route <destination-network> <subnet-mask> <next-hop-ip>

```


* **View Routing Table:**
```text
Router# show ip route

```


* **Clear Routing Table Entries:**
```text
Router# clear ip route *

```


* **View IP Routing Cache:**
```text
Router# show ip cache

```



### Monitoring & Verification

* **View Active Running Configuration:**
```text
Router# show running-config

```


* **Check Interface Status & Statistics:**
```text
Router# show interfaces

```



```

```