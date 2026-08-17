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