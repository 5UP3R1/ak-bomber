import os
import requests
from requests.structures import CaseInsensitiveDict
import os,sys,time,requests,random,string
import random

os.system("clear")
logo = ("""\033[1;32m


    ___                        
   /   |  ____ ___  ____ _____ 
  / /| | / __ `__ \/ __ `/ __ \
  
 / ___ |/ / / / / / /_/ / / / /
/_/  |_/_/ /_/ /_/\__,_/_/ /_/ 
                                     
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━━━━━━━━━━━━━━━━━┓
  ┃ ┏━━[+]  AUTHOR   ➤ Aman khan ┃TOOL➤ SMS BOMBER ┃
  ┃ ┣━━[+]  GITHUB   ➤ 5UP3R1    ┃VERSION ➤ 1.0.0  ┃
  ┃ ┣━━[+]  TYPE     ➤ PREMIUM   ┗━━━━━━━━━━━━━━━━━┃
  ┃ ┣━━[+]  NETWORK  ➤ DATA AND WIFI               ┃
  ┃ ┣━━[+]  STATUS   ➤ Active...                   ┃
  ┃ ┣━━[+]  FACEBOOK ➤ sorry1314                   ┃
  ┃ ┗━━[+]  TELEGRAM ➤ @aman_sdp                   ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n\n\033[1;37m""")

def superuser():
    UMO="AmaN-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print("\033[1;91mChecking Approval...\033[1;91m")
    DARK=requests.get("https://github.com/5UP3R1/ak-bomber/blob/main/Aproval.ax").text
    if id in DARK:
        os.system("clear")
        os.system("python v2.0.py")
    else:
        os.system("clear")
        time.sleep(1.0)
        
        print(logo)
        print("\t\033[30m   [\033[1;32m\033[47m First Get Approvel\033[00m\033[1;30m]")
        print ("Note. This is paid tool.")
        print("                Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        name = input(" Your Name : ")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://www.facebook.com/sorry1314")
        superuser()
superuser()
