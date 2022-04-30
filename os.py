import os
import time
from colorama import Fore, Back, Style,init
from termcolor import colored
import pc_tools
import psutil

# colorama init
init()

# neofetch command

def neofetch():
    print(Back.GREEN + Fore.BLACK + "") 
    print("_______    ___   __    ____   _____                         n")
    print(" |___  / |  | \ \ / /   / __ \ / ____|                      ")
    print("    / /| |  | |\ V /   | |  | | (___                        ")
    print("   / / | |  | | > <    | |  | |\___ \                       ")
    print("  / /__| |__| |/ . \   | |__| |____) |                      ")
    print(" /_____|\____//_/ \_\   \____/|_____/                       ")
    print(Back.BLUE + Fore.WHITE + "") 
    print("OS: ZUX OS") 
    print("OS VERSION: 1.0")     
    print("Architecture: ", pc_tools.architecture())
    print("Kernel: Xkernel")
    print('RAM used in %:', psutil.virtual_memory()[2])
    print(Back.BLACK + "") 
    menu()

# help command
 
def help():
    print(Back.BLUE + "ALL commands")
    print(Back.BLUE + "neofetch") 
    print(Back.BLUE + "help") 
    print(Fore.BLACK + Back.GREEN + "More commands soon")       
    print(Back.BLACK + Fore.WHITE +  "")  
    menu()           

# main menu
def menu():
    choice = input(">>>")

    if choice == "Neofetch" or choice =="neofetch":
        neofetch()
    elif choice == "Help" or choice =="help":
        help()
    elif choice=="Q" or choice=="q":
        print("test")
    else:
        print("Unkown command, use 'help' command ")
        menu()       
        
def main():
   menu()    
                                      
    

print(Fore.BLACK + Back.GREEN + "OS STARTED!")
print(Back.BLACK + Fore.WHITE + "")
menu()




