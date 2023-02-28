"""
Author: new92
Github: @new92

Script for Generating strong passwords !
"""

import random
from time import sleep

caps=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lows=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums=["1","2","3","4","5","6","7","8","9"]
spesChars=["!","@","#","$","%","^","&","*","|","/"]

cap=str(input("[?] Do you want to include cappital letters ?[Y/N] "))
while (cap != "y" and cap != "Y" and cap != "n" and cap != "N") or cap == None:
    print("[!] Invalid input !")
    sleep(1)
    cap=str(input("\n [::] Please enter again: "))
if cap == "y" or cap == "Y":
    capital=True
else:
    capital=False
    
low=str(input("\n [?] Do you want to include low letters ?[Y/N] "))
while low != "y" and low != "Y" and low != "n" and low != "N" or low == None:
    print("[!] Invalid input !")
    sleep(1)
    low=input("\n[::] Please enter again: ")
if low == "y" or low == "Y":
    lower=True
else:
    lower = False
num=input("\n [?] Do you want to include numbers ?[Y/N] ")
while num != "y" and num != "Y" and num != "n" and num != "N" or num == None:
    print("[!] Invalid Input !")
    num=input("\n [::] Please enter again: ")
if num == "y" or num == "Y":
    numbers=True
else:
    numbers = False
speschar=input("\n[?] Do you want to include special characters ?[Y/N] ")
while speschar != "y" and speschar != "Y" and speschar != "n" and speschar != "N"  or speschar == None:
    print("[!] Invalid Input !")
    speschar=input("\n[::] Please enter again: ")
if speschar == "y" or speschar == "Y":
    specialchar = True
else:
    specialchar = False
length=int(input("\n[::] Please enter the password length: "))
while length < 4:
    print("[!] Cannot generate password with that length !")
    time.sleep(1)
    length=int(input("\n[::] Please enter again the password length: "))

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
    psw += random.choice(RANDLIST)

print("\n[+] Your Password: "+str(psw))
