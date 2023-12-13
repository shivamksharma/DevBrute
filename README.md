# **DevBrute** - **A Password Brute Forcer Tool**

[![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)](https://github.com/shivamksharma/DevBrute/releases/tag/v1.0.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DevBrute** is powerful tool designed for developers to perform automated task like login attempts on various social media platforms.

**DevBrute** is my casual and random project in Infomation Security and it is a versatile BruteForce Framework that allows you to perform automated login attempts on various social media platforms. It incorporates several advanced features to enhance its effectiveness and minimize the risk of detection. Nowadays, Brute Forcing on any Web Applications is like wasting time because most web apps uses plethora of techniques to prevent brute forcing on their websites. You can notice a common technique on most websites which is **Locking Account**. You might use one of greatest brute force tool or You might found some password but in those two scenario, it always depends on websites.

## FEATURES

- **Brute Force**: Utilize robust algorithms for brute force attacks on various systems.
- **Customization**: Tailor parameters and settings to suit specific requirements.
- **Multi-threaded**: Execute tasks concurrently for faster results.
- **Logging**: Detailed logs for monitoring and troubleshooting.

## **INSTALLATION**

The installation of this tool is easy and you can install this tool in just three steps.
To install DevBrute, follow these steps:

1. Clone the Repository

```bash
git clone https://github.com/shivamksharma/DevBrute.git
```

2. Install the Dependencies :

```bash
cd DevBrute
python3 -m pip install -r requirements.txt
```

3. Run DevBrute

```bash
python3 bruteforce.py [options]
```

Replace `[options]` with the desired configurations and parameters.

DevBrute supports various configurations through command-line options. Some common options include:

- `--target`: Specify the target IP address.
- `--port`: Define the target port.
- `--threads`: Set the number of threads to be used.

### Examples

- Brute force attack:

```bash
python devbrute.py --target <target_IP> --port <port> --threads <num_threads>
```

- Custom Configuration:

```bash
python devbrute.py --target <target_IP> --port <port> --threads <num_threads> --options <additional_options>
```

- For Example:

```python
python3 bruteforce.py -s facebook -u username -w wordlist.txt -d 2
```

### CONTRUBUTING TO DEVBRUTE

To contribute to DevBrute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/awesome-feature`).
6. Create a pull request.

Please ensure to follow the [Contribution Guidelines](CONTRIBUTING.md).

---

### FIXES

- Fixed some bugs
  - Fixed Website URLS Error
  - Fixed Wordlist Issue
  - Fixed some errors while adding new features
  - Fixed Account Locking

### UPDATES

- Added some delays while trying for next passwords.
  - Added Tracking of Web Backend to detect the
  - Added Proxy and IP Rotation Feature
  - Added Pattern Avoidance
  - Added VPN support

> **_DISCLAIMER_** - Please use this framework responsibly and ensure you have proper authorization before conducting any testing or automated interactions with websites. Unauthorized access or brute-forcing of accounts is against the terms of service of most websites and may be illegal in many jurisdictions. Use this tool at your own risk which makes you accountable for your own actions if you use it for any questionable purpose !
