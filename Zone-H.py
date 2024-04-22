import colorama
import smtplib
import sys
import ctypes
import re
import os
import shutil
import requests
from colorama import Fore, Back, Style
from os import system
from bs4 import BeautifulSoup

colorama.init(autoreset=True)

banner = '''
						Join : @flash_kiss
'''
print(banner)

pages = int(input("How Many Pages You Need : "))


def change_cookie():
    new_cookie = input("Enter new PHPSESSID cookie value: ")
    cookie['PHPSESSID'] = new_cookie
    new_cookie = input("Enter new ZHE cookie value: ")
    cookie['ZHE'] = new_cookie

cookie = {          
    "ZHE" :"99245ff31cd5d51fc06bc734603c1e27",                                
    "PHPSESSID" : '1'
}

#system('mode con: cols=50 lines=70')                 
#os.system('cls' if os.name == 'nt' else 'clear')     
#columns = shutil.get_terminal_size().columns        
print(Fore.RED + "|==   Zone-H Grabber   ==|")
notifiers = []                                
print('Grabbing Urls from 1st ' + str(pages) + ' pages...')
for n in range(pages):                             
    usr = requests.get('https://zone-h.org/archive/published=0/page='+str(n+1), cookies=cookie).content
    if 'If you often get this captcha when gathering data' in usr.decode('utf-8'):
        change_cookie()  
        usr = requests.get('https://zone-h.org/archive/published=0/page='+str(n+1), cookies=cookie).content
    soup = BeautifulSoup(usr, 'html.parser')
    links = soup.findAll('a')
    for i in range(len(links)):
        if '/archive/notifier=' in str(links[i]):
            vv = str(links[i]).replace('<a href="/archive/notifier=', '')
            notif = ''
            verif=usr.decode('utf-8')
            bitisp = re.findall('<td>(.*)\n							</td>',verif)
            for oo in bitisp:
                newurl = str(oo.split('/')[0])
                if newurl not in notifiers and ".." not in newurl :
                   notifiers.append(newurl)
                   open('Zone-h-Results.txt','a+').write('http://'+newurl+'\n')
                   print(Fore.GREEN + "[+]" + Fore.WHITE + 'http://'+ newurl) 
