from PasswordStoreRev5 import PasswordStore
import random
import pathlib
from pathlib import Path
pathToDir = pathlib.Path(__file__).parent.absolute().__str__()      #the beginning of the askGaege() quest \/\/\/\/
pathToUserFile = Path(f"{pathToDir}\\login.txt")
def askGaege():
    if not pathToUserFile.is_file():
        username = input("Create a new username: ")
        password = input("Create a new password: ")
        userFile = open(f"{pathToUserFile}", "w")
        userFile.write(username + '\n' + password)  #ask Gaege ^^^^^^ plz idk what this is
 
def logIn():        #defining the logIn() function. Allows the user to log into the password manager. 
    askGaege()
    tries = 5       #initializing tries as a counter variable
    for i in range(tries):
        userFile = open(f"{pathToUserFile}", "r") 
        userInfo = userFile.read().split("\n")
        logPass = userInfo[1]       #necessary value for the hint variable below.
        if userInfo[0] == input("Enter your username: ") and userInfo[1] == input("Enter your password: "): #if the username and password are correct, allows the user to log in
            return True
        else:
            tries -= 1                                  #decreasse the amount of tries by 1
            print(f"You have {tries} tries left!")      #print how many tries the user has left
            if tries == 3:                              #if the user goes down to 3 tries
                hint = logPass[random.randint(0,(len(logPass)-1))]  #hint will be set to a random letter from logPass, in this case any letter from the word "test"
                print(f"Hint: {hint}")  #print the user's hint
            if tries == 0:
                print("You ran out of tries! Shutting down.")
                return False           #if the user doesn't input the correct username and password within 5 tries, return false

masterList = [["entertainment"],["home"],["work"],["school"],["bills"]]
placeholder = ""    #acts as a placeholder for the self value in the PasswordStore class
def manager():  
    if logIn():         #if logIn() is true, then initialize the program
        categoryList = [["Entertainment"],["Home"],["Work"],["School"],["Bills"]]   #default category list. the user will be able to add new categories later.
        checkOrStoreOrAdd = input("Welcome to your Password Manager!\nWould you like to check stored passwords, store a new password, or add a new category?: ").lower()   #variable that asks the user if they'd like to check or store a password
        while checkOrStoreOrAdd != "check" or checkOrStoreOrAdd != "store" or checkOrStoreOrAdd != "add": 
            if checkOrStoreOrAdd == "check" or checkOrStoreOrAdd == "store" or checkOrStoreOrAdd == "add":
                break
            checkOrStoreOrAdd = input('Please type in "check," "store," or "add.": ').lower()
        PasswordStore.checkStoreAdd(placeholder,checkOrStoreOrAdd,categoryList,masterList)     #pulls the checkStore() function from PasswordStore to begin the password storage process

manager()   #runs the program