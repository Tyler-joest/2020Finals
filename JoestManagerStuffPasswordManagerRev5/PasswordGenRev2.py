import random

class PasswordGen:

    def __init__(self):
        self

    
    def proc(self,q,s):
        procedure = ("question",input("q"))                 #yes, once again copied from my mad lib. you've seen this a couple times now
    
    def numberCheck(self,q,s):
        s = 0
        while True:
            if s.isdigit():   
                    break
            s=input(q)
        return s

    
    def generate(self):                             #it also just happens to be that this is an almost direct copy of my password generator assignment.
                                                        #instead of user input, it just gives a random integer from the range and then prints
                                                        #out the password
        output = ""
        userPass=[]
        specList = [33,35,36,37,38,40,41,42,64,94]
        userCap = random.randint(4,10)
        userLower = random.randint(5,12)
        userNum = random.randint(6,11)
        userSpec = random.randint(3,7)
        for i in range(userCap):
            userPass.append(chr(random.randint(65,91)))          #bunch of appending all down this line. basically making the
        for i in range(userLower):                                   #password based off the numbers above
            userPass.append(chr(random.randint(97,123)))
        for i in range(userNum):
            userPass.append(chr(random.randint(48,58)))
        for i in range(userSpec):
            userPass.append(chr(specList[random.randint(0,9)]))
        random.shuffle(userPass)                                #shuffling the password to actually be difficult to break
        for i in range(len(userPass)):
            output = output + userPass[i]                         #prints out the password all in one line for the user
        return output