#from PasswordStoreRev3 import PasswordStore

class PasswordCheck:        #welcome to PasswordCheck. This is the password pulling, checking, redoing, and deleting hub for your
                                #entertainment.
                                #                                               -Eric

    def __init__(self):     #although it appears I did all the work, I'm really just copying over Tyler's code in this one.
        self        

    def letterCheck(self,q,s):  #you might have seen this before 
        while True:
            if s.isalpha():   
                    break
            s=input(q)
        return s

    def catCheck(self,l):
        passType=PasswordCheck.letterCheck(self,"Please enter a category: ",input("Where is your login stored?: ")) #if the user actually inputs a category
        loop = True         #necessary to not get stuck in a million for loop instances, but just to go through the loop set once
        for i in range(len(l)):
                for m in range(len(l[i])):
                    if passType in l[i][m]:
                        for n in range(len(l[i][m])):   #for number in range of lists. basically, the same thing as the storePass method in PasswordStore
                            if loop == True:
                                print(f"""
                                Program: {l[i][m+1][n]}
                                Username: {l[i][m+1][n+1]}
                                Password: {l[i][m+1][n+2]}""")      #a nice and pretty printout for the user again
                                print()
                                redoAccount=input("Would you like to redo your username and password for this account? ").lower()
                                if redoAccount == "yes":            #if the user wants to redo their username and passwor
                                    l[i][m+1] = ['','','']            #sets the user's info blank so that they start fresh on the storePass side of things
                                    redo = "redo"
                                    return redo     #seems counterintuitive, but redo is a variable necessary for the redoDelete() function in PasswordStore
                                else:
                                    accountDelete=input("Would you like to delete this account? ").lower()
                                    if accountDelete == "yes":  
                                        l[i][m+1] = ['','','']      #else, if the user wants to delete their account, say yes and its gone
                                        redo = "delete"     
                                        return redo
                                    else:
                                        pass        #bunch of empty statements that just get pass values 
                                pass
                            
                            loop = False    #sets the loop to false to avoid infinite loops