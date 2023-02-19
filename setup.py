import os
from subprocess import call

os.system("sudo apt install python3-pip && sudo apt install tor")
os.system("pip3 install -U selenium pyvirtualdisplay pysocks mechanize xvfb argparse requests")

os.system('firefox -v > tmp')
with open('tmp', 'r') as f:
    marker = f.read().find('Firefox')+8
    version = f.read()[marker:].splitlines()[0]
os.remove('tmp')
a,b,c = version.split('.')
FirefoxVersion = int(a)

if FirefoxVersion < 53:
    call(["wget", "https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz"])
    os_bit = 64

elif FirefoxVersion == 53 or FirefoxVersion == 54:
    call(["wget", "https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz"])
    os_bit = 64

elif FirefoxVersion > 54:
    call(["wget", "https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz"])
    os_bit = 64

call(["tar", "-xvzf", "geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,os_bit)])
os.remove("geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,os_bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")
os.system("chmod +x setup.py")

