Chat ID: 6547885190
8450849961:AAFcZejoVCRaFIZ0GNSHWaV9f04MIt5A4RE

sudo apt update
sudo apt install -y rkhunter chkrootkit
sudo rkhunter --update
sudo rkhunter --check --sk
sudo chkrootkit
file /bin/ls
strings /bin/ls | less
sha256sum /bin/ls or sha256sum /bin/ls > ls.sha256
git clone https://github.com/technicaldada/pentbox
cd pentbox
ls
cd pentbox-1.8/
ls
ruby ./pentbox.rb

select option 2 for network tool
select 3 for honey pot
seklect 1 for fast auto configuration

then open a new temainal then start nc 127.0.0.1 80

# 1. Update the APT package index

```bash
sudo apt update
```

# 2. Install rootkit-detection tools

```bash
sudo apt install -y rkhunter chkrootkit
```

# 3. Update rkhunter's data

```bash
sudo rkhunter --update
```

# 4. Run rkhunter

```bash
sudo rkhunter --check --sk
```

# 5. Run chkrootkit

```bash
sudo chkrootkit
```

# 6. Identify /bin/ls

```bash
file /bin/ls
```

# 7. Inspect printable strings

```bash
strings /bin/ls | less
```

# 8. Calculate a SHA-256 hash

```bash
sha256sum /bin/ls
```

# 9. Clone the Pentbox repository

```bash
git clone https://github.com/technicaldada/pentbox
```

# 10. Enter the downloaded directory

```bash
cd pentbox
```

# 11. List its contents

```bash
ls
```

# 12. Unzip it

```bash
tar -xzf filename
```

# 13. Enter the Pentbox program directory

```bash
cd pentbox-1.8/
```

# 14. List the files again

```bash
ls
```

# 15. Start Pentbox

```bash
ruby ./pentbox.rb
```

# 16. Open another terminal and connect with Netcat

```bash
nc 127.0.0.1 80
```
