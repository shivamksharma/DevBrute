import os, math, sys
from time import sleep
from subprocess import call

os.system("sudo apt install python3-pip && sudo apt install tor")
os.system("pip3 install -u selenium")
os.system("pip3 install -u pyvirtualdisplay")
os.system("pip3 install -u pysocks")
os.system("pip3 install -u mechanize")
os.system("pip3 install -u xvfb")
os.system("pip3 install -u argparse")
os.system("pip3 install -u requests")

os.system('firefox -v > tmp')
result = open('tmp', 'r').read()
marker = result.find('Firefox')+8
version = result[marker:].splitlines()[0]
a,b,c = version.split('.')
os.remove('tmp')

FirefoxVersion = int(a)
second = 0

if FirefoxVersion < 53:
    
    first = 16
    second = 1
    os_bit = 64

elif FirefoxVersion == 53 or FirefoxVersion == 54:
    
    first = 18

elif FirefoxVersion > 54:
        
        first = 19

os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,OS_bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")
chmod +x setup.py
