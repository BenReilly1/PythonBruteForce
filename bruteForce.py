import sys
from itertools import product
import time

def init():
    global passwordAlphabet, firstTime
    passwordAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$* "
    firstTime = True
    firstTimeMenu()

def crack():
    found = False 
    BFCounter = 0
    BFclearCounter = 0
    
    for length in range(1, 10):
        password_to_attempt = product(passwordAlphabet, repeat=length)
                                     
        for attempt in password_to_attempt:
            attempt = ''.join(attempt)
            BFCounter += 1
            BFclearCounter += 1

            if BFclearCounter > 4999999:
                print("Brute force in progress...          Attempt #", BFCounter)
                BFclearCounter = 0

            if attempt == user_password:
                print("The password is "+ attempt +"! It was found in" , BFCounter, "attempts!")
                
                found = True
                break
        if found:
            break
    if found:
        firstTime = False
        menu()

def firstTimeMenu():
    print("************Welcome to Password Cracker**************")
    print()
    choice = input("""
        A: Run the Password Cracker
        B: Quit Program

        Please enter your choice: """)

        
    if choice == "A" or choice =="a":
        usrPass()
    elif choice == "B" or choice =="b":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def menu():
    print()
    print()
    print()       
    print("************Welcome to Password Cracker**************")
    choice = input("""
        A: Run again
        B: Quit Program

        Please enter your choice: """).strip()

        
    if choice == "A" or choice =="a":
        usrPass()
    elif choice == "B" or choice =="b":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def usrPass():
    global user_password
    user_password = input("Enter a password: ").upper()
    crack()

init()
