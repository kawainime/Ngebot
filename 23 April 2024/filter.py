#!/usr/bin/env python3
import sys
import requests
import re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

log = """
   ______      __       _______ ____   ____  _       _____ 
  / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
 | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
 | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
 | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
  \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                          OVA-TOOLS  https://t.me/ovacloud                                                                                              
                                  Filter All CMS 
    """
print(log)

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('/')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


def URL(url):
    if url[-1] == "/":
        pattern = re.compile('(.*)/')
        site = re.findall(pattern, url)
        url = site[0]
    if url[:7] != "http://" and url[:8] != "https://":
        url = "http://" + url
    return url


def check_wordpress(site):
    pet = re.compile('<meta name="generator" content="(.*)" />')
    try:
        site = URL(site)
        src = requests.get(site, timeout=15).content.decode('utf-8')
        if re.findall(pet, src):
            generator = re.findall(pet, src)[0]
            if 'WordPress' in generator:
                print(' --| ' + site + ' --> {}[WordPress]'.format(fg))
                with open('wordpress.txt', mode='a') as d:
                    d.write(site + '/\n')
        else:
            if 'wp-content/themes' in src:
                print(' --| ' + site + ' --> {}[WordPress]'.format(fg))
                with open('wordpress.txt', mode='a') as d:
                    d.write(site + '/\n')
    except Exception as e:
        print(' --| ' + site + ' --> {}[Error: {}]'.format(fr, e))


def check_joomla(site):
    pet = re.compile('<meta name="generator" content="(.*)" />')
    try:
        site = URL(site)
        src = requests.get(site, timeout=15).content.decode('utf-8')
        if re.findall(pet, src):
            generator = re.findall(pet, src)[0]
            if 'Joomla' in generator:
                print(' --| ' + site + ' --> {}[Joomla]'.format(fg))
                with open('joomla.txt', mode='a') as d:
                    d.write(site + '/\n')
        else:
            if '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src:
                print(' --| ' + site + ' --> {}[Joomla]'.format(fg))
                with open('joomla.txt', mode='a') as d:
                    d.write(site + '/\n')
    except Exception as e:
        print(' --| ' + site + ' --> {}[Error: {}]'.format(fr, e))


def check_drupal(site):
    pet = re.compile('<meta name="generator" content="(.*)" />')
    try:
        site = URL(site)
        src = requests.get(site, timeout=15).content.decode('utf-8')
        if re.findall(pet, src):
            generator = re.findall(pet, src)[0]
            if 'Drupal' in generator:
                print(' --| ' + site + ' --> {}[Drupal]'.format(fg))
                with open('drupal.txt', mode='a') as d:
                    d.write(site + '/\n')
        else:
            if 'sites/all/themes' in src:
                print(' --| ' + site + ' --> {}[Drupal]'.format(fg))
                with open('drupal.txt', mode='a') as d:
                    d.write(site + '/\n')
    except Exception as e:
        print(' --| ' + site + ' --> {}[Error: {}]'.format(fr, e))


def check_prestashop(site):
    pet = re.compile('<meta name="generator" content="(.*)" />')
    try:
        site = URL(site)
        src = requests.get(site, timeout=15).content.decode('utf-8')
        if re.findall(pet, src):
            generator = re.findall(pet, src)[0]
            if 'PrestaShop' in generator:
                print(' --| ' + site + ' --> {}[PrestaShop]'.format(fg))
                with open('prestashop.txt', mode='a') as d:
                    d.write(site + '/\n')
        else:
            if 'js/jquery/plugins/' in src:
                print(' --| ' + site + ' --> {}[PrestaShop]'.format(fg))
                with open('prestashop.txt', mode='a') as d:
                    d.write(site + '/\n')
    except Exception as e:
        print(' --| ' + site + ' --> {}[Error: {}]'.format(fr, e))


while True:
    print("\nChoose an option:")
    print("1. Check for WordPress")
    print("2. Check for Joomla")
    print("3. Check for Drupal")
    print("4. Check for PrestaShop")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        mp = Pool(150)
        mp.map(check_wordpress, target)
        mp.close()
        mp.join()
    elif choice == '2':
        mp = Pool(150)
        mp.map(check_joomla, target)
        mp.close()
        mp.join()
    elif choice == '3':
        mp = Pool(150)
        mp.map(check_drupal, target)
        mp.close()
        mp.join()
    elif choice == '4':
        mp = Pool(150)
        mp.map(check_prestashop, target)
        mp.close()
        mp.join()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
