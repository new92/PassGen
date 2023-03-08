"""
Author: new92
Github: @new92

Script for Generating strong passwords !
"""

from random import choice
from time import sleep
import string

caps=list(string.ascii_uppercase)
lows=list(string.ascii_lowercase)
nums=[str(i) for i in range(10)]
spesChars=["!","@","#","$","%","^","&","*","|","/"]

def main():
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[1] Generate password")
    print("[2] Exit")
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 2 or num == None:
        if num == None:
            print("[!] This field can't be blank !")
        else:
            print("[!] Invalid number !")
        num=int(input("[::] Please enter again a number (from the above ones): "))
    if num == 1:
        cap=str(input("[?] Do you want to include cappital letters ? [Y/N] "))
        while (cap != "y" and cap != "Y" and cap != "n" and cap != "N") or cap == None:
            print("[!] Invalid input !")
            sleep(1)
            cap=str(input("[?] Do you want to include cappital letters ? [Y/N] "))
        if cap == "y" or cap == "Y":
            capital = True
        else:
            capital = False

        low=str(input("[?] Do you want to include low letters ? [Y/N] "))
        while (low != "y" and low != "Y" and low != "n" and low != "N") or low == None:
            print("[!] Invalid input !")
            sleep(1)
            low=str(input("[?] Do you want to include low letters ? [Y/N] "))
        if low == "y" or low == "Y":
            lower = True
        else:
            lower = False

        num=str(input("[?] Do you want to include numbers ? [Y/N] "))
        while num != "y" and num != "Y" and num != "n" and num != "N" or num == None:
            print("[!] Invalid input !")
            sleep(1)
            num=str(input("[?] Do you want to include numbers ? [Y/N] "))
        if num == "y" or num == "Y":
            numbers = True
        else:
            numbers = False

        speschar=str(input("[?] Do you want to include special characters ? [Y/N] "))
        while speschar != "y" and speschar != "Y" and speschar != "n" and speschar != "N"  or speschar == None:
            print("[!] Invalid input !")
            sleep(1)
            speschar=str(input("[?] Do you want to include special characters ? [Y/N] "))
        if speschar == "y" or speschar == "Y":
            specialchar = True
        else:
            specialchar = False

        length=int(input("[::] Please enter the password length: "))
        while length < 4:
            print("[!] Weak password !")
            sleep(1)
            length=int(input("[::] Please enter again length of the password: "))

        RANDLIST = []
        if capital:
            RANDLIST += caps
        if lower:
            RANDLIST += lows
        if numbers:
            RANDLIST += nums
        if specialchar:
            RANDLIST += spesChars
        psw = ""
        for i in range(length):
            psw += choice(RANDLIST)

        print(f"[✓] Generated password: {psw}")
   else:
    print("[+] Thank you for using my script 😁")
    sleep(2)
