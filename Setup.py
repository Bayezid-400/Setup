import os 
import requests
menu=("""
  [1] BASIC setup
  [2] exit
  """)
  

def main():
  os.system("clear")
  print(logo)
  print(menu)
  xd=input("CHOOSE : ")
  if xd=='1':
    setup()
  if xd=='2':
    exit('THANKS FOR USING!!')
  else:
    exit()
def setup():
  os.system('apt update && apt upgrade && apt install git && apt install python && apt install python2 && apt install wget && apt install curl && apt install gaks')

  
  
logo=("""

Just For Testing
➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤
[✔] Author: BAYEZID 
[✔] Facebook: BAYEZID 
➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤➤""")
main()
