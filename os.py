import pystyle
import os
import time
import psutil
import platform
import socket
import logging
import pystyle
import subprocess
from subprocess import Popen
from pathlib import Path
from pystyle import Colors, Colorate, Add, Center, Box, Write




# variables
hostname = socket.gethostname()  
list = "./external_programs"


# neofetch command

def neofetch():
    print(Colorate.Horizontal(Colors.purple_to_red, "", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "  _______    ___   __    ____   _____                       ", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, " |___  / |  | \ \ / /   / __ \ / ____|                      ", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "    / /| |  | |\ V /   | |  | | (___                        ", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "   / / | |  | | > <    | |  | |\___ \                       ", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "  / /__| |__| |/ . \   | |__| |____) |                      ", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, " /_____|\____//_/ \_\   \____/|_____/                       ", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "OS: ZUX OS", 1)) 
    print(Colorate.Horizontal(Colors.purple_to_red, "OS VERSION: 1.1", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "Kernel: Xkernel", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "hostname: " + socket.gethostname(), 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "Processor Architecture: " + platform.machine(), 1)) 
    print(Colorate.Horizontal(Colors.purple_to_red, "", 1))
    menu()

# help command
 
def help():
    print(Colorate.Horizontal(Colors.purple_to_red, "ALL commands", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "neofetch - displaying info about pc", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "help - showing all commands", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "apt install 'package name' - install selected package", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "apt list - showing all packages", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "run - Run custom program", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "More commands soon", 1))     
    print(Colorate.Horizontal(Colors.purple_to_red,"", 1))
    menu()   
   
# installing app 
def install():
    print(Colorate.Horizontal(Colors.purple_to_red, "enter package link that you want install", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "ex. http://assets.azordon.cf/packages/test.py", 1))
    packagelnk = input("")
    print(Colorate.Horizontal(Colors.purple_to_red, "enter package name that you want install", 1))
    print(Colorate.Horizontal(Colors.purple_to_red, "ex. test.py", 1))
    print("ex. test.py")
    packagename = input("")
    print("Installing " + packagename)
    r = requests.get(packagelnk)
    with open("./" + packagename, 'wb') as outfile:
     outfile.write(r.content)
    Path(packagename).rename("./external_programs/" + packagename)
    time.sleep(3)
    menu()        
  
  
# showing packages    
def packages():
    list1 = []
 
    for (root, dirs, file) in os.walk(list):
       for f in file:
        if '.py' in f:
            print(f)
            menu()
            
# running packages
def run():
    print(Colorate.Horizontal(Colors.purple_to_red, "Enter app name that you want run", 1))
    apprun = input("")
    Popen("python ./external_programs/" + apprun)
    menu()
    

# main menu
def menu():
    choice = input(Colorate.Horizontal(Colors.purple_to_blue, "root@" + socket.gethostname() + ":~$ ",  1))

    if choice == "Neofetch" or choice =="neofetch":
        neofetch()
    elif choice == "Help" or choice =="help":
        help()
    elif choice=="apt install" or choice=="Apt install":
        install()
    elif choice=="apt list" or choice=="Apt list":
        packages()
    elif choice=="run" or choice=="Run":
        run()      
    else:
        print("Unkown command, use 'help' command ")
        menu()       
        
def main():
   menu()    
                                      


# START OS
print(Colorate.Horizontal(Colors.purple_to_red, "OS STARTED!", 1))
print(Colorate.Horizontal(Colors.purple_to_red, "", 1))
menu()




