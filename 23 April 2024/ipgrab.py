import requests,re,os,time
from colorama import *

green = Fore.GREEN
blue = Fore.BLUE
red = Fore.RED
cyan = Fore.CYAN
yellow = Fore.YELLOW
white = Fore.WHITE

def banner():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("\n\n"+white+"\n\t"+red+"██╗██████╗"+blue+"      ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ \n\t"+red+"██║██╔══██╗ "+blue+"   ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗\n\t"+red+"██║██████╔╝ "+blue+"   ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝\n\t"+red+"██║██╔═══╝  "+blue+"   ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗\n\t"+red+"██║██║      "+blue+"   ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║\n\t"+red+"╚═╝╚═╝      "+blue+"    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n")
    print('\t\t-- --=['+red+'Coded By ASTRO'+white+']\n\t\t-- --=[    '+red+'Ver 1.0'+white+'   ]\n')

def save(name,cont):
    for arch in cont:
        f = open(name, "a+")
        f.write(str(arch)+"\n")
        f.close()

def Aremove(fname):
    file = open(fname, "r").readlines()
    f = [f.strip() for f in file]
    clean = list(set(f))
    f = open(fname, "w")
    for ip in clean:
        f.write(ip+"\n")
    f.close()

banner()
domain = input("┌──("+red+"root"+white+"@"+blue+"ASTRO"+")-["+green+"(com/net/org/gov/..)"+white+"]\n└─"+red+"#"+white+" ")
ent = int(input("┌──("+red+"root"+white+"@"+blue+"ASTRO"+white+")-["+green+"Enter Start Page"+white+"]\n└─"+red+"#"+white+" "))
end = int(input("┌──("+red+"root"+white+"@"+blue+"ASTRO"+white+")-["+green+"Enter End Page"+white+"]\n└─"+red+"#"+white+" "))
print("\n"+cyan+"  Grabbing Started..\n\n")
time.sleep(3)

ip_count = 0
for ent in range(end):
    url = "https://site-stats.org/domains/."+domain+"/"+str(ent)+"/"
    req = requests.get(url).text
    grb = re.findall("<a href=\"/ip/(.*?)/\"", str(req))
    save("ips.txt", grb)
    print(green + "\n  Grabbed IPs: "+str(len(grb)))
    print(blue + "\n  Filtering IPs")
    time.sleep(3)
    Aremove("ips.txt")
    ip_count += len(grb)
f = open("ips.txt","r").readlines()
print(green + "  Total IPs: "+str(len(f)))
