# if it's free, just use it :)
# © @GrazzMean @fiola_tools
# for buy reverse IP @fiola_tools

import requests, re, os
from colorama import Fore,init
from multiprocessing.dummy import Pool
init()
g = Fore.GREEN; r = Fore.RED; reset = Fore.RESET

total = 0

headers = {
    'Connection': 'Keep-Alive',
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

# def api1(f, t): --> this fucking api died
#     global total 
#     t += 1
#     for fiola in range(f, t):
#         req = requests.get(f'http://bitverzo.com/recent_ip?p={fiola}', headers=headers).text
#         if 'Recent IP reviews' in req:
#             ip = re.findall('<a href="http://bitverzo.com/ip/(.*?)">', req)
#             total += len(ip)
#             #print(g+'\n'.join(list(dict.fromkeys(ip)))+reset)
#             #print(ip)
#             open('result_1.txt', 'a+', encoding="utf-8").write('\n'.join(list(dict.fromkeys(ip))))
#         else:
#             print("\nLimit!, Exiting.."); exit()
    
def api1(f, t):
    global total 
    t += 1
    for fiola in range(f, t):
        req = requests.get(f'http://macrobyte.net/recent_ip?p={fiola}', headers=headers).text
        if 'Recent IP reviews' in req:
            ip = re.findall('<a href="http://macrobyte.net/ip/(.*?)">', req)
            total += len(ip)
            print('\n'.join(list(dict.fromkeys(ip))))
            #print(ip)
            open('result_1.txt', 'a+', encoding="utf-8").write('\n'.join(list(dict.fromkeys(ip))))
        else:
            print("\nLimit!, Exiting.."); exit()

def api2(f, t):
    global total 
    t += 1
    for fiola in range(f, t):
        req = requests.get(f'http://viewsforcash.com/recent_ip?p={fiola}', headers=headers).text
        if 'Recent IP reviews' in req:
            ip = re.findall('<a href="http://viewsforcash.com/ip/(.*?)">', req)
            total += len(ip)
            print('\n'.join(list(dict.fromkeys(ip))))
            #print(ip)
            open('result_2.txt', 'a+', encoding="utf-8").write('\n'.join(list(dict.fromkeys(ip))))
        else:
            print("\nLimit!, Exiting.."); exit()

def main():
    print("\nIP Grabber By @GrazzMean\n")
    server = int(input("Select Server (1/2) --> "))
    if server == 1: server = 1
    elif server == 2: server = 2
    else: print("\nServer Not Found!, Try Again"); exit()
    frompage = int(input("From Page --> "))
    topage = int(input("To Page --> "))
    thread = int(input("Thread --> "))
    if server == 1:
        pool = Pool(thread)
        pool.starmap(api1, zip([frompage], [topage]))
        pool.close(); pool.join()
        input("\nDone. For Reverse IP You Can Buy From @fiola_tools!.")
    elif server == 2:
        pool = Pool(thread)
        pool.starmap(api2, zip([frompage], [topage]))
        pool.close(); pool.join()
        input("\nDone. For Reverse IP You Can Buy From @fiola_tools!.")
    #with wife(max_workers=thread) as j:
    #    j.submit(api1, frompage, topage)
    #    j.shutdown(wait=False)
        
if __name__ == '__main__':
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    main()