import requests,os
from time import sleep
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
logo=(f'''\033[1;32m _ \033[1;31m  _  \033[1;32m _   \033[1;31m_  \033[1;32m _
\033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \  
 \033[1;32mN | A | D | E | R 
\033[1;31m\_/ \033[1;32m\_/\033[1;31m \_/ \033[1;32m\_/ \033[1;31m\_/

{G}[G] GitHub    : {B}==>@N_0_N_7
{G}[I] InstaGram : {B}==>@nader20090
{G}[F] FaceBook  : {B}==>NADER.DZA
{G}[T] TeleGram  : {B}==>ABO EAD''')
print(logo)
print(f'{E}ـ'*40)
co=input(f'{B}[+] FaceBook Cookies : {G}')
print(f'{E}ـ'*40)
res=requests.post('https://flikers.net/android/android_check_new_cookie.php',headers={"Cookie":co,"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; Plume L2 Build/O00623)","Host": "flikers.net","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "0"},timeout=60).json()
if res['status'] == 'SUCCESS':
 name=res['name']
 msg=res['message']
 cn=res['country']
 os.system('clear')
 print(logo)
 print(f'{E}ـ'*40)
 print(f'''{B}[√] Message : {G}{msg}
{B}[√] Name : {G}{name}
{B}[√] Country : {G}{cn}''')
 print(f'{E}ـ'*40)
 link=(f'https://m.facebook.com/story.php?story_fbid=pfbid0qxarcks4csxkxiBTQqYbgT96YtXFxoQS3hKvuyi2sbu6EeX5Vg58Dxmq3pqtXfzRl&id=1385711176&mibextid=NOb6eG').replace('/','\/')
 print(f'{E}ـ'*40)
 devil=input(f'''{G}[01] {S}Haha 😂
{G}[02] {E}Love ❤️
{G}[03] {B}Like 👍🏻
{G}[04] {E}Angry 😡
{G}[05] {S}Care 🤗
{G}[06] {S}Wow 😲
{E}ــــــــــــــــــــــــــــــــــــــــ
{G}[<>] Choose : {B}''')
 print(f'{E}ـ'*40)
 if devil == '1' or devil == '01':
  type='HAHA'
 elif devil == '2' or devil == '02':
  type='LOVE'
 elif devil == '3' or devil == '03':
  type='LIKE'
 elif devil == '4' or devil == '04':
  type='ANGRY'
 elif devil == '5' or devil == '05':
  type='CARE'
 elif devil == '6' or devil == '06':
  type='WOW'
 else:
  type='LOVE'
 data='{"post_id":"'+link+'","react_type":"'+type+'"}'
 head1={"Cookie":co,"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; Plume L2 Build/O00623)","Host": "flikers.net","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length":str(len(data))}
 res1=requests.post('https://flikers.net/android/android_get_react.php',data=data,headers=head1).json()
 if res1['status'] == 'SUCCESS':
  msg=res1['message']
  print(f'{G}[√] {msg}')
  sleep(1800)
 else:
  msg=res1['message']
  print(f'{E}[×] {msg}')
else:
 msg=res['message']
 print(f'{E}[×] {msg}')
