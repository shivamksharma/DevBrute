<div align="center">
  <h1>DevBrute</h1>
  <p>A password brute-forcing tool !</p>
</div>

<div align="center">
    <a href="https://github.com/shivamksharma/terminal_portfolio/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License" />
    </a>  
    <a href="https://github.com/shivamksharma/terminal_portfolio/releases">
        <img src="https://img.shields.io/badge/version0.0.0-blue.svg" alt="Version" />
    </a>
</div>

**DevBrute** is a powerful and versatile tool designed for developers to perform automated login attempts on various social media platforms. It is a casual and random project in the field of Information Security, offering a robust framework for brute-forcing with advanced features to minimize detection risks.

In today's web applications, brute-forcing is often inefficient due to modern security measures like **Account Locking**. While tools like DevBrute can help uncover passwords, the success of such attempts heavily depends on the target website's security mechanisms.

## **Key Features**

- **Brute Force**: Advanced algorithms for efficient brute-force attacks.
- **Customization**: Flexible parameters to adapt to specific use cases.
- **Multi-threaded**: Concurrent execution for faster results.
- **Logging**: Detailed logs for monitoring and debugging.

## **Installation**

Getting started with DevBrute is simple and can be done in just a few steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shivamksharma/DevBrute.git
   ```

2. **Navigate to the Directory**

   ```bash
   cd DevBrute
   ```

3. **Run the Setup File**

   ```bash
   python3 setup.py
   ```

4. **Run DevBrute**

   ```bash
   python3 devbrute.py [options]
   ```

   Replace `[options]` with your desired configurations.

### **Common Options**

- `--target`: Specify the target IP address.
- `--port`: Define the target port.
- `--threads`: Set the number of threads for concurrent execution.

### **Example Usage**

- **Brute Force Attack**:

  ```bash
  python3 devbrute.py --target <target_IP> --port <port> --threads <num_threads>
  ```

- **Custom Configuration**:

  ```bash
  python3 devbrute.py -s facebook -u username -w wordlist.txt -d 2
  ```

## **Contributing**

We welcome contributions to DevBrute! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/awesome-feature`).
6. Create a pull request.

Please ensure you follow the [Contribution Guidelines](CONTRIBUTING.md).

---

## **Recent Fixes**

- Fixed Website URLs Error
- Resolved Wordlist Issues
- Addressed errors during feature additions
- Improved handling of Account Locking

## **Recent Updates**

- Added delays between password attempts.
- Introduced Proxy and IP Rotation for enhanced anonymity.
- Implemented Pattern Avoidance to reduce detection risks.
- Added VPN support for secure operations.

---

> **Disclaimer**  
> This tool is intended for ethical and authorized use only. Unauthorized access or brute-forcing of accounts is against the terms of service of most websites and may be illegal in many jurisdictions. Use this tool responsibly and at your own risk.

