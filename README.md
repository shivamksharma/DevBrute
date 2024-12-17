<div align="center">
# **DevBrute**  
**A Password Brute Forcer Tool**

[![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)](https://github.com/shivamksharma/DevBrute/releases/tag/v1.0.0)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

**DevBrute** is a versatile password brute-forcing tool aimed at automating login attempts across various social media platforms. Designed for developers, this tool explores advanced techniques to bypass security and minimize detection risks. While web application defenses have evolved, DevBrute adapts to challenges like account locking and other preventative measures.

---

## **FEATURES**

- **Brute Force**: Executes powerful brute-force attacks.  
- **Customization**: Flexible settings for tailored usage.  
- **Multi-threaded**: Faster execution with concurrent tasks.  
- **Logging**: Generates detailed logs for easy debugging.

---

## **INSTALLATION**

### Step 1: Clone the Repository

```bash
git clone https://github.com/shivamksharma/DevBrute.git
```

### Step 2: Install Dependencies

```bash
cd DevBrute
python3 -m pip install -r requirements.txt
```

### Step 3: Run the Tool

```bash
python3 devbrute.py [options]
```

---

## **USAGE**

Customize your brute force attacks with various options:

- `--target`: Target IP address.  
- `--port`: Target port number.  
- `--threads`: Number of threads to use.

### Examples

- Basic Brute Force Attack:

```bash
python3 devbrute.py --target <target_IP> --port <port> --threads <num_threads>
```

- For Social Media (e.g., Facebook):

```bash
python3 devbrute.py -s facebook -u username -w wordlist.txt -d 2
```

---

## **CONTRIBUTING**

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/awesome-feature`).  
3. Make your changes.  
4. Commit your changes (`git commit -am 'Add new feature'`).  
5. Push to your branch (`git push origin feature/awesome-feature`).  
6. Create a pull request.

See [Contribution Guidelines](CONTRIBUTING.md) for more details.

---

## **FIXES**

- URL parsing errors fixed.  
- Wordlist processing issues addressed.  
- Bugs in feature integration resolved.  
- Enhanced handling of account locking scenarios.

---

## **UPDATES**

- Delays between password attempts added.  
- Proxy and IP rotation capabilities integrated.  
- Pattern avoidance logic implemented.  
- VPN support for enhanced anonymity.

---

> **_DISCLAIMER_**  
> Use responsibly and ensure proper authorization before using this tool. Unauthorized brute-forcing may be illegal and violates most websites' terms of service.

---
