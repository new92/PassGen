"""
Author: @new92
Password Generator Program
"""
import random
import time

caps=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lows=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums=["1","2","3","4","5","6","7","8","9"]
spesChars=["!","@","#","$","%","^","&","*","|","/"]
cap=input("Do you want to include cappital letters ?[Y/N] ")
while cap != "y" and cap != "Y" and cap != "n" and cap != "N":
    print("Invalid parameter !")
    cap=input("\nPlease enter again: ")
if cap == "y" or cap == "Y":
    capital=True
else:
    capital=False
low=input("\nDo you want to include low letters ?[Y/N] ")
while low != "y" and low != "Y" and low != "n" and low != "N":
    print("Invalid parameter")
    low=input("\nPlease enter again: ")
if low == "y" or low == "Y":
    lower=True
else:
    lower = False
num=input("\nDo you want to include numbers ?[Y/N] ")
while num != "y" and num != "Y" and num != "n" and num != "N":
    print("Invalid parameter")
    num=input("\nPlease enter again: ")
if num == "y" or num == "Y":
    numbers=True
else:
    numbers = False
speschar=input("\nDo you want to include special characters ?[Y/N] ")
while speschar != "y" and speschar != "Y" and speschar != "n" and speschar != "N":
    print("Invalid parameter")
    speschar=input("\nPlease enter again: ")
if speschar == "y" or speschar == "Y":
    specialchar = True
else:
    specialchar = False
length=int(input("Please enter the password length: "))
while length < 8:
    print("Too Short Password Length")
    length=int(input("Please enter the password length: "))

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

print("Password: "+str(psw))
