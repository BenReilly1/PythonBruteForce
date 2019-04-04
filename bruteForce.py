
import sys
from itertools import product
import time
import hashlib

def init():
    global passwordAlphabet, firstTime
    passwordAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$* "
    firstTime = True
    firstTimeMenu()

def crack():
    u_password = user_password.upper()
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

            if attempt == u_password:
                print("The password is "+ attempt +"! It was found in" , BFCounter, "attempts!")
                
                found = True
                break
        if found:
            break
    if found:
        time.sleep(1)
        menu()

def debug():
    u_password = user_password.upper()
    found = False 
    BFCounter = 0
    BFclearCounter = 0
    
    for length in range(1, 10):
        password_to_attempt = product(passwordAlphabet, repeat=length)
                                     
        for attempt in password_to_attempt:
            attempt = ''.join(attempt)
            BFCounter += 1
            BFclearCounter += 1
            BFCounterWord = str(BFCounter)
            print("Attempt #"+ BFCounterWord +", Word Attempt Was "+ attempt)

            if BFclearCounter == 10000000:
                sys._clear_type_cache
            if attempt == u_password:
                print("The password is "+ attempt +"! It was found in" , BFCounter, "attempts!")
                
                found = True
                break
        if found:
            break
    if found:
        time.sleep(1)
        menu()

def firstTimeMenu():
    global choice
    print("************Welcome to Password Cracker**************")
    print()
    choice = input("""
        A: Run the Password Cracker
        B: Generate hash
        Q: Quit Program
        Please enter your choice: """)

        
    if choice == "A" or choice =="a":
        usrPass()
    elif choice == "B" or choice == "b":
      usrPass()
    elif choice == "Q" or choice =="q":
        sys.exit
    elif choice == "DEBUG" or choice == "debug" or choice == "Debug":
        usrPass()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def menu():
    global choice
    print()
    print()
    print()       
    print("************Welcome to Password Cracker**************")
    choice = input("""
        A: Run again
        B: Generate hash
        Q: Quit Program
        Please enter your choice: """).strip()

        
    if choice == "A" or choice =="a":
        usrPass()
    elif choice == "B" or choice == "b":
      usrPass()
    elif choice == "Q" or choice =="q":
        sys.exit
    elif choice == "DEBUG" or choice == "debug" or choice == "Debug":
        usrPass()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def hashGen():
    hashVal = hashlib.md5(user_password.encode())
    hashRead = hashVal.hexdigest()
    print("The password was "+ user_password+", the hash value of the password is", hashRead)
    menu()

def usrPass():
    global user_password
    if choice == "DEBUG" or choice == "debug" or choice == "Debug":
        user_password = input("Enter a password: ")
        debug()
    elif choice == "B" or choice == "b":
        user_password = input("Enter a password to be hashed: ")
        hashGen()
    else:
        user_password = input("Enter a password: ")
        crack()

init()
