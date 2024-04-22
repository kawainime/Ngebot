#!/usr/bin/env python2
# Author: Maxim3lian

from __future__ import print_function
import requests
import re
import pyfiglet
import os
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class DomainGrabber:

    @staticmethod
    def banner():
        os.system("cls||clear")
        __banner__ = pyfiglet.figlet_format("TLD - Grabber", font="slant", justify="center")
        print(__banner__)
        print("\tAuthor : @Maxim3lian - Contact :https://t.me/Maxim3lian_Channel \n")
        print("\tDomain Grabber By TLD - ( Top-level domain EX: com\id\gov\etc ) ")
        print("")

    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)

    @staticmethod
    def checkTLD(domain):
        req = requests.get("https://zoxh.com/tld").text
        all_tld = re.findall('/tld/(.*?)"', req)
        if domain in all_tld:
            return True
        else:
            return False
    
    @staticmethod
    def TLD(domain_tld):
        req = requests.get("https://zoxh.com/tld/{}".format(domain_tld)).text
        total_domain = int(re.findall('href="/tld/{}/(.*?)"'.format(domain_tld), req)[-2])

        for i in range(total_domain):
            i += 1
            try:
                req_grab = requests.get("https://zoxh.com/tld/{}/{}".format(domain_tld, i)).text
                all_domain = "\n".join(re.findall('/i/(.*?)"', req_grab)).strip("\r\n")
                total_domain = len(all_domain.split("\n"))
                open("tld_{}.txt".format(domain_tld), "a").write(all_domain + "\n")
                print("\t[>] Grabbed {} Domain | Page {}".format(total_domain, i))
            except:
                pass

if __name__ == "__main__":
    DomainGrabber.banner()
    input_tld = raw_input("\tENTER TLD (ex: com) : ") 

    if DomainGrabber.checkTLD(input_tld):
        DomainGrabber.TLD(input_tld)
    else:
        exit("[!] Unknown Domain TLD [!]")
