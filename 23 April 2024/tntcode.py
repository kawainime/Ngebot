from requests import get
from re import findall
from multiprocessing.dummy import Pool
# Private Reverse ips Lookup bY OVA-TOOLS  https://t.me/ovacloud
print ("""

   ______      __       _______ ____   ____  _       _____ 
  / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
 | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
 | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
 | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
  \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                          OVA-TOOLS  https://t.me/ovacloud   
                                                           
""")

def rev(ip) :
    try :
        url = 'https://domains.tntcode.com/ip/'+ip
        send_data = get(url, timeout=10).text
        attack  = findall(r'href="/domain/([^"]+)"',send_data)[3:]
        

        for domain in attack :
            print(domain)
            open('tntcode_rev.txt','a').write('http://'+domain+'\n')
    except :
        pass
def main () :
    ad = input('Enter list ip : ')
    opens = open(ad, mode='r', errors='ignore').read().splitlines()
    utchiha = Pool(int(100))
    utchiha.map(rev, opens)
   

main()
