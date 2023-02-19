import os
from subprocess import call

os.system("sudo apt install python3-pip && sudo apt install tor")
os.system("sudo pip3 install -U selenium pyvirtualdisplay pysocks mechanize xvfb argparse requests")


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
