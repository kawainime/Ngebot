# Import Module
import requests, re

# Colors 
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

def oke(page,site,outs):
	ok = requests.get(f'https://site-stats.org/domains/.{site}/{page}/').text
	a = re.findall('<tr><td><a href="/(.*?)/"', ok)
	print(f"[#]===============[PAGE : {page}]===============[#]")
	for i in a:
		with open(outs, "a") as okss:
			okss.write('http://'+str(i)+'\n')
		print(f'\n{p}{bgm}[--] {p}{h}Domain {p}{k}: {p}{h}http://{str(i)}')
		
def banner():
	print("""{}
[#]==============================[#]
[ ! ] Grab Site By Extension
[ ! ] Priv8 Api
[ ! ] Coded By : viper1337
[ ! ] Remaked By : viper1337
[ ! ] Version : v3.0
[ ! ] Code in : Python3
[#]==============================[#]	
	{}""".format(k,p))

if __name__ == "__main__":
	banner()
	ext = input("\n{}[ ? ] Enter Extension : {}".format(bgm,p))
	oks = int(input('{}[ ? ] Total Page : {}'.format(bgm,p)))
	out = input("{}[ ? ] Output File [Ex - result.txt] : {}".format(bgm,p))

for i in range(0,oks): oke(i,ext,out)
