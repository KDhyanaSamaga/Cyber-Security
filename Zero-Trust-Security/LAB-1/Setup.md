# Install for GNS in your System
[Reference]:https://docs.gns3.com/docs/getting-started/installation/linux
1.Search GNS3 in browser
2.Open the documentation in that navigate to Debian-based distributions section
3.Open the termainal
### Step 4:
```bash 
sudo apt update
```
### Step 5:
Remove that "dynamips software-properties-common" from the command 
```bash
sudo apt install python3 python3-pip pipx python3-pyqt6 python3-pyqt6.qtwebsockets python3-pyqt6.qtsvg qemu-kvm qemu-utils libvirt-clients libvirt-daemon-system virtinst ca-certificates curl gnupg2 
```
### Step 6:
```bash
sudo apt install python3 python3-pip pipx python3-pyqt6 python3-pyqt6.qtwebsockets python3-pyqt6.qtsvg qemu-kvm qemu-utils libvirt-clients libvirt-daemon-system virtinst ca-certificates curl gnupg2 
```
### Step 7:
```bash
pipx install gns3-server && pipx ensurepath
```

### Step 8:
```bash
pipx install gns3-gui && pipx ensurepath
```
### Step 9:
```bash
pipx inject gns3-gui gns3-server PyQt6 && pipx ensurepath
```
### Step 10:
```bash
rm -rf vpcs
```
### Step 11:
```bash
git clone https://github.com/GNS3/vpcs.git
```
### Step 12:
```bash
cd vpcs/src
```
### Step 13:
```bash
./mk.sh 64
```
### Step 14:
```bash
sudo cp vpcs /usr/local/bin/vpcs
```
### Step 15:
```text
Re-Start the System
```
### Step 16:
**Open the terminal and dont close it**
```bash
gns3
```
---
4.The IT department requires large 




