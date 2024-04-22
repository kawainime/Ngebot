#!/usr/bin/env python2
# Author: Maxim3lian

import requests
import os
import time
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style, init

init(autoreset=True)

def ask_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        x = requests.get('https://askdns.com/ip/'+url, headers=headers, timeout=30).content
        if 'Domain Name' in x:
            regex = re.findall('<a href="/domain/(.*?)">', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name
                print("GRABBED: {}".format(website_url))
                open('Reversed.txt', 'a').write(website_url + '\n')
        else:
            print("BAD : " + url)
    except:
        pass


def rapid_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        x = requests.get('https://rapiddns.io/s/'+url+'?full=1&down=1#result/', headers=headers, timeout=30).content
        if '<th scope="row ">' in x:
            regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
                print("GRABBED: {}".format(website_url))
                open('Reversed.txt', 'a').write(website_url + '\n')
        else:
            print("BAD : " + url)
    except:
        pass


def reverse_ip_lookup(url):
    try:
        rapid_dns(url)
        ask_dns(url)
    except:
        pass


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        ip_list = raw_input("IPS LIST : ")
        urls = open(ip_list, 'r').read().splitlines()
        num_threads = raw_input("THREAD : ")
        pool = ThreadPool(int(num_threads))
        pool.map(reverse_ip_lookup, urls)
    except:
        pass


if __name__ == '__main__':
    main()
