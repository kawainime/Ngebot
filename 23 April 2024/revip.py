import traceback, threading, time
import sys, os
from concurrent.futures import ThreadPoolExecutor
from requests import get
from bs4 import BeautifulSoup as bs
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel as nel
from rich import print as cetak
from rich.progress import Progress
from random import choice
def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')
        
clear()
black  = '\33[30m'
red    = '\33[31m'
green  = '\33[32m'
yellow = '\33[33m'
blue   = '\33[34m'
VIOLET = '\33[35m'
BEIGE  = '\33[36m'
white  = '\33[37m'
banner = f"""\t[white]Tool Information :
\t[red]❖ [green] Tool Name [white]: [yellow]Revers IP
\t[red]❖ [green] Description [white]: [yellow]Priv8 RevIP Unlimited
\t[red]❖ [green] Creator [white]: [yellow]AXVDIGITAL
\t[red]❖ [green] Program [white]: [yellow]Python
\t[red]❖ [green] Copyright [white]: [yellow]t.me/AXVDIGITAL
\t[red]❖ [green] Website [white]: [yellow]https://axvdigital.com
\t[red]❖ [green] Version [white]: [yellow]2.0"""

class Reverse:
    def __init__(self) -> None:
        self.header = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
        self.url = "https://domains.tntcode.com/ip/{}"
        self.ip_list = []
        self.result = ""
        self.scrape_text = "[blue][ {0} ][/blue] [gray]Scraping [white]==> [cyan]{1}"
        self.true_text = "[blue][ {0} ][/blue] [green]Got [red]{1} [green]domains [white]==> [cyan]{2}\n[yellow][ {3} ]"
        self.false_text = "[blue][ {0} ][/blue] [red]Got Nothing [white]==> [red]{1}"
        self.process_done = "\n\n[green][✓]Done processing [white]{0} [green]IP, result saved to [white]{1}"

    def parse_data(self, ip):
        try:
            result = {
                'count': 0,
                'country': ''
            }
            res = 0
            country = ''
            parse = bs(get(self.url.format(ip), headers=self.header).text, "html.parser")
            if parse.textarea:
                for z in parse.select('body > table > tbody > tr:nth-child(1) > td:nth-child(2)'):
                    result['country'] = z.text
                for x in parse.textarea.text.strip().splitlines():
                    result['count'] += 1
                    open(self.result, "a").write(x+"\n")
                # --
            return result
        except Exception:
            print(traceback.format_exc())
            return result

    def reverse(self, threadNum): #, progress, task
        try:
            console = Console()
            with console.status('[bold green]Fetching data...') as status:
                threadNumber = 0
                ip_list = self.ip_list
                total_ip = len(ip_list)
                for ip in ip_list:
                    threadNumber += 1
                    status.update(self.scrape_text.format(str(threadNumber) + "/" + str(total_ip), ip))
                    parsed = self.parse_data(ip)
                    total_domain = parsed['count']
                    country = parsed['country']
                    if total_domain > 0:
                        console.log(self.true_text.format(str(threadNumber) + "/" + str(total_ip), total_domain, ip, country if country else '-'))
                    else:
                        console.log(self.false_text.format(str(threadNumber) + "/" + str(total_ip), ip))
                console.log(self.process_done.format(total_ip, self.result))
        except Exception as e:
            print(traceback.format_exc())
    
    def start_thread(self):
        print()
        for threadNum in range(self.thread):
            self.reverse(threadNum) #progress, 
        # --
    # --

    def main(self):
        
        cetak(nel(banner, style='white')),print('\n')
        ip_path = Prompt.ask(f"{red}[{yellow}#{red}]{white} IP list (example : iplist.txt) : ")
        out_path = Prompt.ask(f"{red}[{yellow}#{red}]{white} Save as (default : result.txt) : ")
        thred = Prompt.ask(f"{red}[{yellow}#{red}]{white} Thereds : ")
        self.result = out_path if out_path else 'result.txt'
        self.thread = 1 #int(thread_str) if thread_str else 2
        ips = open(ip_path, "r").read().splitlines()
        ips = list(dict.fromkeys(ips))
        self.ip_list = ips
        self.start_thread()

if __name__ == "__main__":
    try:
        reverse = Reverse()
        reverse.main()
    except Exception:
        print(traceback.format_exc())
