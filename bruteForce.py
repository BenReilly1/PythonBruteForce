import sys
from itertools import product
import time

def full(): # Max 3 chars
    maxchars = str(input("Enter max number of characters to be tried: "))
    intmaxchars = int(maxchars)
    user_password = input("Enter a "+ maxchars +" character password: ").upper()
    found = False
    BFCounter = 0
    passwordAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    intmaxchars += 1

    for length in range(1, intmaxchars):
        password_to_attempt = product(passwordAlphabet, repeat=length)

    for attempt in password_to_attempt:
        attempt = ''.join(attempt)
        BFCounter += 1
        print("Attempt Number:", BFCounter, "with attempt of", attempt)

        if attempt == user_password:
            print("Your password is:", attempt,"and was found in", BFCounter,"attempts!")
            found = True
            break

        if found:
            break

def mid(): # Max 5 chars
    maxchars = str(input("Enter max number of characters to be tried: "))
    intmaxchars = int(maxchars)
    user_password = input("Enter a "+ maxchars +" character password: ").upper()
    found = False
    BFCounter = 0
    BFCounterClear = 0
    passwordAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    intmaxchars += 1

    for length in range(1, intmaxchars):
        password_to_attempt = product(passwordAlphabet, repeat=length)

    for attempt in password_to_attempt:
        attempt = ''.join(attempt)
        BFCounter += 1
        BFCounterClear += 1

        if BFCounter < 100001 and BFCounterClear == 1000:
            print("Attempt number:", BFCounter,"with attempt of", attempt)
            BFCounterClear = 0
            
        if BFCounter > 100000 and BFCounter < 1000001 and BFCounterClear == 10000:
            print("Attempt number:", BFCounter,"with attempt of", attempt)
            BFCounterClear = 0

        if BFCounter > 1000001 and BFCounterClear == 100000:
            print("Attempt number:", BFCounter,"with attempt of", attempt)
            BFCounterClear = 0
        
        if attempt == user_password:
            print("Your password is:", attempt,"and was found in", BFCounter,"attempts!")
            found = True
            break

        if found:
            break

def low():
    maxchars = str(input("Enter max number of characters to be tried: "))
    intmaxchars = int(maxchars)
    user_password = input("Enter a "+ maxchars +" character password: ").upper()
    found = False
    print("Starting to Brute force...")
    BFCounter = 0
    passwordAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    intmaxchars += 1

    for length in range(1, intmaxchars):
        password_to_attempt = product(passwordAlphabet, repeat=length)

    for attempt in password_to_attempt:
        attempt = ''.join(attempt)
        BFCounter += 1

        if attempt == user_password:
            print("Your password is:", attempt,"and was found in", BFCounter,"attempts!")
            found = True
            break

        if found:
            break

menu = int(input("Enter which mode you want, 1) Full 2) Mid 3) Low : "))
if menu == 1:
    full()
if menu == 2:
    mid()
if menu == 3:
    low()
