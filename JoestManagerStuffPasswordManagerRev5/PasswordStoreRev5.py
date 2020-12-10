from PasswordCheckRev3 import PasswordCheck
from CategoriesRev3 import Categories
from PasswordGenRev2 import PasswordGen

class PasswordStore:    #class method for storing new passwords - Eric

    def __init__(self):     #initializing the class. There are no characteristics for this
        self                    #class, so I just initialized self.

    def redoDelete(self,redo,c,l,master):       #this is for the redo/delete function seen in PasswordCheck.py
        if redo == "redo":  
            c = input("Please retype the category your password was stored in: ")
            for m in range(len(master)):             #for master category in range(length of category list)
                for i in range(len(master[m])):          #for category in range(length of category) (to allow for comparison of strings in next line)
                    if c == master[m][i]:                    #if the user's input is a category in the list: (if "Home" == "Home")
                        #for n in range(len(l[m][i])):          #unsure if I need this for loop yet, but i'll keep it just in case.
                        b = input("What program will your username and password be used to access?: ")  
                        c = input(f"What is your username for {b}?: ")
                        d = input(f"What is your password for {b}?: ")
                        #passwordInCat = [b,c,d]         #the password in the category = a list of [Program,Username,Password]
                        l[m][i+1][0] = b         #after resetting the input to blank in PasswordCheck.py's categoryAdd(), these variables are
                        l[m][i+1][1] = c            #necessary for remaking the passwords how the user wants them
                        l[m][i+1][2] = d
                        print(f"""
                        Username and password for {b} stored successfully!
                        Username: {c}
                        Password: {d}       
                        """)                #nice and pretty printout for the user to see their final results 
                        PasswordStore.skipLogIn(self,l,master)      #run the skipLogIn function to ask the user what they want to do next
        elif redo == "delete":
                    PasswordStore.skipLogIn(self,l,master)      #all the dirty work is done in PasswordCheck.py for this
        else:
            PasswordStore.skipLogIn(self,l,master)  #if all else fails, just ask the user what they want to do again


    def printCat(self, master):              #printCat() is the functon that prints out the categories (l is the categoryList provided in the manager() function in the passwordManager.py file)
        print()
        for m in range(len(master)):                #for m (master category) in range(length of the categoryList):
            for i in range(1):              #for i (item in category) in range(length of the category chosen):
                print(f'{m+1}',master[m][i].title())                 #print the index of the category (+1 to avoid category 0) plus the category (prints out "1 Entertainment", etc.) 
        print()   
    
    def checkStoreAdd(self,c,l,master):                   #the checkStore() function runs the functions for storing, checking passwords, or 
                                                            #adding categories depending on the user's input (c)
        if c == "store":                        
            PasswordStore.printCat(self,master)         #runs the printCat() function, defined above
            PasswordStore.storePass(self,c,l,master)      #runs the storePass() function, defined below
        if c == "check":
            PasswordStore.printCat(self,master)     #runs printCat() to print the cats (and not the animal kind)
            PasswordStore.redoDelete(self,PasswordCheck.catCheck(self,l),c,l,master)    
                                    #serves a dual purpose. runs the catCheck() function defined in PasswordCheck.py, as well as
                                        #runs the redoDelete() function defined above. redoDelete() takes in the result of catCheck() and 
                                            #uses it in its algorithm                                    
            PasswordStore.skipLogIn(self,l,master)  #runs skipLogIn() again
        if c == "add":
            Categories.categoryAdd(self,l,master)   #variables "l" and "master" are explained in detail below
            PasswordStore.printCat(self,master)
            
        '''
            By now, you're definitely wondering where all the masters came from.
            Truth be told, master was kind of thrown in there when I had a sort of crisis and 
            realized that I needed two lists or else all my categories would also print out
            their contents.
            
            Basically, master means the masterList seen in passwordManagerRev#.py. It is what the printCat()
            function uses to print out the categories.
            If I had used l, my original list variable, everything would have broken and it most likely would have
            been a mess to clean up. Either way, it's already kind of a mess.

            To dumb it down, l = everything list (including all the categories and what is inside of them).
            master = category list (just the categories to avoid getting the prints of the passwords stored inside the list when I didn't want that).

            Thank you for coming to my TED Talk.

                                                                    -Eric
        '''
        
    def skipLogIn(self,l,master):        #the skipLogIn() function simply asks the user if they'd like to check or store more passwords without asking them to log in again, unlike manager().
                                    #essentially, a bypass for users that are already logged in.
        categoryList = l    #in this sense, categorylist = l because l is my "everything list" i described earlier. it keeps the functions running
                                #so that the category list isn't reset every time
        checkOrStore = input("Would you like to check stored passwords, store another password, or add a new category?: ")       
        PasswordStore.checkStoreAdd(self,checkOrStore,categoryList,master)  #once again, master is the list that simply acts as the categories,
                                                                                #not actually storing any of the user's data

    def storePass(self,c,l,master):           #the main function for storing the username and password. takes in the user's input from either manager() or skipLogIn() and the categoryList.
        c = input("Which category would you like to store your password?: ").lower()
        for m in range(len(master)):             #for master category in range(length of category list:
            for i in range(len(master[m])):          #for category in range(length of category) (to allow for comparison of strings in next line)
                if c == master[m][i]:                    #if the user's input is a category in the list: (if "Home == "Home")
                    #for n in range(len(l[m][i])):          #unsure if I need this for loop yet, but i'll keep it just in case.
                        b = input("What program will your username and password be used to access?: ")  
                        c = input(f"What is your username for {b}?: ")
                        d = input('Type "random" for your very own password!\n'f"What is your password for {b}?: ")
                        if d == "random":
                            passwordInCat = [b,c,PasswordGen.generate('')]
                        else:
                            passwordInCat = [b,c,d]                        #the password in the category = a list of [Program,Username,Password]
                        #print(passwordInCat)
                        l[m].append(passwordInCat)             #append the list described above to the category (this creates a three dimensional list: [Category[]])
                    #print(l[m][i+1])                #Allows for printout of [Program,Username,Password]. Using for testing purposes
                        print(f"""
                        Username and password for {b} stored successfully!
                        Username: {c}
                        Password: {passwordInCat[2]}       
                        """)                #nice and pretty printout for the user to see their final results 
                        PasswordStore.skipLogIn(self,l,master)       #run the skipLogIn function to ask the user what they want to do next