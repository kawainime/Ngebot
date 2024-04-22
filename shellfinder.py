import requests as rq
from multiprocessing.dummy import Pool as pl
import sys


paths = ['/simple.php','/about.php','/install.php','/dropdown.php','/chosen.php?p=','/mah.php','/wp-admin/about.php','/wp-content/about.php','/wp-admin/install.php','/wp-admin/js/about.php7',
'/wp-content/install.php','/wp-admin/user/about.php','/wp-includes/install.php','/wp-admin/images/admin.php','/wp-includes/Text/about.php','/wp-admin/network/admin.php','/wp-admin/maint/atomlib.php',
'/wp-admin/network/index.php','/wp-content/plugins/index.php','/wp-content/uploads/index.php','/wp-content/themes/twentytwentythree/patterns/index.php']

def v(url, p='http'):
    for path in paths:
        yield f'{p}://{url}{path}'

def c(u):
    try:
        p = ['http', 'https']
        for pr in p:
            for s in v(u, pr):
                try:
                    r = rq.get(s, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'}, timeout=10)
                    if 'type="submit" value="upload"' in r.text:
                        print(f'Found      {s}')
                        with open('Shells.txt', 'a') as f:
                            f.write(f'{s}\n')
                        return
                except Exception as e:
                    print(f'Error occurred while processing {s}: {e}')
                    continue
        print(f'Not Found {u}')
    except Exception as e:
        print(f'Error occurred while processing {u}: {e}')

def bn():
    print("""
<!--      _          _ _    __ _           _            -->
<!--  ___| |__   ___| | |  / _(_)_ __   __| | ___ _ __  -->
<!-- / __| '_ \ / _ \ | | | |_| | '_ \ / _` |/ _ \ '__| -->
<!-- \__ \ | | |  __/ | | |  _| | | | | (_| |  __/ |    -->
<!-- |___/_| |_|\___|_|_| |_| |_|_| |_|\__,_|\___|_|    -->

hi !                 
 """)
    
def m():
    try:
        if len(sys.argv) < 2:
            print("Usage: python script.py sites.txt")
            return
        
        f = sys.argv[1]
        with open(f, 'r', errors='ignore') as fl:
            urls = fl.read().splitlines()

        if not urls:
            print("File is empty.")
            return

        pool = pl(100)
        pool.map(c, urls)

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    bn()
    m()
