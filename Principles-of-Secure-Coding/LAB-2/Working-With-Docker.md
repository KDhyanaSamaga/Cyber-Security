# Install Docker in Kali Linux
# Docker.io
### Step 1:
```bash
sudo apt update
```
---

### Step 2:
```bash
sudo apt install -y docker.io
```
---

### Step 3:
```bash
sudo systemctl enable --now docker
```

---
### Step 4:
```bash
sudo docker run --rm -p 80:80 vanuraalities/web-server
                   or
sudo docker run -rm -= n80:80 nginx
```

---
### Step 5:
```bash
sudo nmap -sV -p- 127.0.0.1
```

---
### Step 6:
```bash
sudo ss -tulpn
```
---
### Step 7:
```bash
curl -I http://127.0.0.1
```
---
