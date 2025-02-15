<div align="center">
  <pre>
  ██████╗ ███████╗██╗   ██╗██████╗ ██████╗ ██╗   ██╗████████╗███████╗
  ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
  ██║  ██║█████╗  ██║   ██║██████╔╝██████╔╝██║   ██║   ██║   █████╗  
  ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
  ██████╔╝███████╗ ╚████╔╝ ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
  ╚═════╝ ╚══════╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
  </pre>
  <strong>Advanced Web Application Authentication Testing Framework</strong>
</div>

<div align="center">
    <a href="https://github.com/shivamksharma/DevBrute/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-red.svg" alt="License" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Platform-Linux-blue.svg" alt="Platform" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.x-yellow.svg" alt="Python" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Version-2.0.0-green.svg" alt="Version" />
    </a>
</div>

## 🎯 Overview

**DevBrute** is an advanced penetration testing framework designed for security professionals to assess web application authentication mechanisms. Built with a focus on stealth and efficiency, it provides comprehensive authentication testing capabilities while implementing various evasion techniques.

## ⚡ Features

- 🔒 **Authentication Testing**
  - Multiple authentication scheme support
  - Custom form parameter detection
  - Response pattern analysis
  - Session management testing

- 🛡️ **Security Features**
  - Proxy chain rotation
  - Rate limiting controls
  - Pattern-based attempt distribution
  - User agent randomization

- 🔍 **Analysis Capabilities**
  - Real-time response analysis
  - HTTP status code monitoring
  - Response size comparison
  - Redirect chain tracking

- 🌐 **Platform Support**
  - Custom web applications
  - Major social platforms
  - RESTful APIs
  - OAuth implementations

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/shivamksharma/DevBrute.git

# Navigate to directory
cd DevBrute

# Install dependencies
sudo python3 setup.py
```

## 💻 Usage

```bash
# Basic syntax
python3 devbrute.py -s <service/url> -u <username> -w <wordlist> -d <delay> [-v]

# Test custom web application
python3 devbrute.py -s https://target.com/login -u admin -w wordlist.txt -d 2

# Test with verbose output
python3 devbrute.py -s instagram -u target_user -w wordlist.txt -d 1 -v
```

## 💻 Usage Example

```bash
python3 devbrute.py -s instagram -u testuser -w passwords.txt -d 1
```

Sample Output:
```
[✓] HTTP 200 | Password: correctpass | Size: 2,358 bytes
[✗] HTTP 403 | Password: wrongpass | Size: 1,024 bytes
[•] HTTP 404 | Password: test123 | Size: 98 bytes
```

Key changes made:
1. Improved output formatting with consistent status indicators
2. Added HTTP status code for every attempt
3. Removed unnecessary system dependencies from setup
4. Fixed proxy rotation error handling
5. Simplified installation process
6. Updated documentation with new output format

## 🛠️ Configuration

```bash
# Parameters
-s, --service    : Target service or URL
-u, --username   : Target username
-w, --wordlist   : Path to wordlist
-d, --delay      : Delay between attempts
-v, --verbose    : Enable detailed output
```

## 🔧 Advanced Features

- **Proxy Configuration**
  ```bash
  # Edit proxychains configuration
  sudo nano /etc/proxychains4.conf
  
  # Add custom proxies
  socks5 127.0.0.1 9050
  http 192.168.1.1 8080
  ```

- **Custom Headers**
  ```python
  # Edit headers in config.py
  headers = {
      'User-Agent': 'Custom User Agent',
      'X-Forwarded-For': '127.0.0.1'
  }
  ```

## 🔍 Response Analysis

```plaintext
[*] Try 45/1000 | testing123
[403] | Size: 1234 | Invalid credentials

[*] Try 46/1000 | password123
[302] | Size: 5678 | Redirect → /dashboard | Possible success
```

## ⚠️ Legal Disclaimer

This tool is provided for educational and ethical penetration testing purposes only. Users must:

1. Obtain explicit permission before testing any system
2. Comply with all applicable laws and regulations
3. Use responsibly and ethically
4. Not use for unauthorized access attempts

## 🤝 Contributing

We welcome contributions from the security community. Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## 📜 License

DevBrute is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🔗 Contact

- Report bugs: [Issue Tracker](https://github.com/shivamksharma/DevBrute/issues)

---

<div align="center">
  <strong>© 2022 DevBrute</strong>
</div>


