import os

def install_requirements():
    print("[*] Installing required Python packages...")
    exit_code = os.system("pip3 install -r requirements.txt")
    return exit_code == 0

def main():
    print("DevBrute Setup\n")
    if not install_requirements():
        print("\n[!] Failed to install Python packages")
        exit(1)
    print("\n[+] Setup completed successfully!")

if __name__ == "__main__":
    main()
