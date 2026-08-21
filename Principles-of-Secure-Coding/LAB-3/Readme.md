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
