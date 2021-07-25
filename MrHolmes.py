#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import random
from Core.Support import Font
from Core import Searcher
from Core import config
from Core import Searcher_phone
from Core import Searcher_website
from configparser import ConfigParser

class Main:
    
    @staticmethod
    def banner(r):
        os.system("cls" if os.name == "nt" else "clear")
        f = open("Version/Version.txt", "r", newline=None)
        for line in f:
            r = line.replace("\n", "")
        version = f.read() + r
        f.close()
        Quotes = [  "Quotes1.txt","Quotes4.txt","Quotes3.txt","Quotes7.txt",
                    "Quotes6.txt","Quotes2.txt","Quotes5.txt","Quotes8.txt",
                    "Quotes9.txt","Quotes10.txt","Quotes11.txt","Quotes12.txt",
                    "Quotes13.txt","Quotes14.txt","Quotes15.txt","Quotes16.txt"
                ]
        choice = random.choice(Quotes)
        f = open("Quotes/" + choice,"r", newline=None)
        text = f.read()
        f.close()
        u = "|                           🇲​​​​​🇷​​​​​.🇭​​​​​🇴​​​​​🇱​​​​​🇲​​​​​🇪​​​​​🇸​​​​​                       |"    
        print(Font.Color.WHITE + "---------------------------------------------------------------------")
        print(Font.Color.WHITE + u)
        print(Font.Color.GREEN + text                                                                
        +
        Font.Color.WHITE + "| A COMPLETE OSINT TOOL:)      " +      Font.Color.BANNER + "CODED BY LUCKSI" + Font.Color.RESET + Font.Color.WHITE + "                      |\n|                                                                   |")
        print(Font.Color.WHITE + "|[+]" + Font.Color.GREEN + "VERSION:" + version + Font.Color.WHITE + "                                               |")
        print(
            Font.Color.YELLOW + "|Instagram:lucks_022                                                |\n|EMAIL:lukege287@gmail.com                                          |\n|GIT-HUB:Lucksi                                                     |\n|Website:https://sosuke.altervista.org                              |")
        print(Font.Color.WHITE + "---------------------------------------------------------------------")
    
    @staticmethod
    def main():
        while True:
            try:
                Main.banner(r=True)
                option = "(1)SOCIAL-ACCOUNT-OSINT\n(2)PHONE-NUMBER-OSINT\n(3)DOMAIN/IP-OSINT\n(4)CONFIGURATION\n(5)UPDATE\n(6)EXIT"
                options = str(option)
                print(Font.Color.GREEN + "[INSERT AN OPTION 'PRESS 0 TO REFRESH THE QUOTE']")
                print(Font.Color.WHITE + options)
                sce = int(input(Font.Color.GREEN + "\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if sce == 1:
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ATTENTION SOME OF THE RESULTS MAY BE FALSE POSITIVES")
                    username = str(input(
                        Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "INSERT THE USERNAME" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Searcher.MrHolmes.search(username)
                elif sce == 2:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "INSERT THE PHONE NUMBER WITHOUT(+)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Searcher_phone.Phone_search.searcher(username)
                elif sce == 3:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "INSERT A DOMAIN OR A IP ADDRESS(IPv4/IPv6)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Searcher_website.Web.search(username)
                elif sce == 4:
                    config.Config.main()
                elif sce == 5:
                    os.system("Core/./update.sh")
                elif sce == 6:
                    print("\nHAVE A NICE DAY BYE:)\n")
                    exit()
                elif sce == 0:
                    Main.main()
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT A WRONG OPTION EXIT...")
                    exit()
            except ValueError as e :
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT A WRONG OPTION EXIT...")
                exit()

if __name__ == "__main__":
    try:
        Main.main()
    except KeyboardInterrupt:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT 'CTRL-C' EXIT...")
        exit()