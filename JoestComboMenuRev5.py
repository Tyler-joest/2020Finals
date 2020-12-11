#typically at the very top you will create the global variables
def checkInput(variableName,wantedInputList):
     if variableName in wantedInputList:
          return True
     return False
finalOrderList=[]
finalOrderListList=[]
wantedEntreeList=["k","dk","tk","d","f","s","g"]
wantedQuestionInput=["y","n","Y","N"]
wantedbeverageInput=["k","s","m","l"]
wantedSideInput=["k","s","m","l"]
order=[]
orderList=[]
orderNum=0
finalTotal=0
taxCalc=0
#list.append(item)
total=0
sandwhichSelected=False         #flag variable
beverageSelected=False
friesSelected=False
orderInitiation=input("would you like to order (y or n) ") #creating a later varaible for a while loop
while(orderInitiation!="n"):
     order.clear()
     orderNum+=1
     finalOrderList.append(f"order: {orderNum}")
     entrees = input("Please pick a type of sandwhich, Krabby patty(k) for $1.25, Double Krabby patty(dk) for $2.00, Triple Krabby patty(tk) for $3.00, Salty Sea Dog(d) for $1.25, Footlong(f) for $2.00, Sailors Suprise(s) for $3.00, or the GOLDEN LOAF(g) for $2.00. ")
     if (entrees=="k" or entrees=="dk" or entrees=="tk" or entrees=="d" or entrees=="f" or entrees=="s" or entrees=="g" ): #          another valid method for the discount
          sandwhichSelected=True
          if entrees=="k":
               finalOrderList.append("Krabby Patty")
               chesse=input("would you like sea cheese on your krabby patty, just for .25 cents more? (y or n) ") 
               if chesse=="y":
                    total+=1.50
                    taxCalc+=1.50*0.07 #doing the math for calcuating the total and final total which is sub total plus tax
                    finalTotal+=1.50+taxCalc
               else:
                    total+=1.25
                    taxCalc+=1.25*0.07
                    finalTotal+=1.25+taxCalc
          elif entrees=="dk":
               finalOrderList.append("Double Krabby Patty")
               chesse=input("would you like sea cheese on your krabby patty, just for .25 cents more? (y or n) ")
               if chesse=="y":
                    total+=2.25
                    taxCalc+=2.25*0.07
                    finalTotal+=2.25+taxCalc
               else:
                    total+=2.00
                    taxCalc+=2.00*0.07
                    finalTotal+=2.00+taxCalc
          elif entrees=="tk":
               finalOrderList.append("Triple Krabby Patty")
               chesse=input("would you like sea cheese on your krabby patty, just for .25 cents more? (y or n) ")
               if chesse=="y":
                    total+=3.25
                    taxCalc+=3.25*0.07
                    finalTotal+=3.25+taxCalc
               else:
                    total+=3.00
                    taxCalc+=3.00*0.07
                    finalTotal+=3.00+taxCalc
          elif entrees=="d":
               finalOrderList.append("Salty Sea Dog")
               total+=1.25
               taxCalc+=1.25*0.07
               finalTotal+=1.25+taxCalc
          elif entrees=="f":
               finalOrderList.append("Footlong")
               total+=2.00
               taxCalc+=2.00*0.07
               finalTotal+=2.00+taxCalc
          elif entrees=="s":
               finalOrderList.append("Salior's Suprise")
               total+=3.00
               taxCalc+=3.00*0.07
               finalTotal+=3.00+taxCalc
          elif entrees=="g":
               finalOrderList.append("GOLDEN LOAF")
               sauce=input("would you like to add sauce for .50 cents more? (y or n) ")
               if sauce=="y":
                    total+=2.50
                    taxCalc+=2.50*0.07
                    finalTotal+=2.50+taxCalc
               else:
                    total+=2.00
                    taxCalc+=2.00*0.07
                    finalTotal+=2.00+taxCalc
          taxCalc-=taxCalc      
     order.append(entrees)   #appending adds to the bottom of the list
     print(entrees)
     beverage = input("Would you like a drink, y or n? ")
     if(beverage=="y"):
          beverageSelected=True
          beverage=input("You can have a kelp shake(k) for 2.00 or you can have a Seafoam soda, a small(s) is $1.00, a medium(m) is $1.25, and a large(l) is $1.50 ")
          print("you said ",beverage, " drink.")  #print(string,string,string,string)
          if beverage=="s":
               finalOrderList.append("Small Seafoam Soda")
               total += 1.00
               taxCalc+=1.00*0.07
               finalTotal+=1.00+taxCalc
          elif beverage=="m":
               finalOrderList.append("Medium Seafoam Soda")
               total += 1.25
               taxCalc+=1.25*0.07
               finalTotal+=1.25+taxCalc
          elif beverage=="l":
               finalOrderList.append("Large Seafoam Soda")
               total += 1.50
               taxCalc+=1.50*0.07
               finalTotal+=1.50+taxCalc
          elif beverage=="k":
               finalOrderList.append("Kelp Shake")
               total += 2.00
               taxCalc+=2.00*0.07
               finalTotal+=2.00+taxCalc
          taxCalc-=taxCalc
     order.append(beverage)
     #iteration 3 asking for fries
     side = input("Would you like a side, y or n? ")
     if(side=="y"):
          side = input("Would you like a order of coral bits? a small(s) is $1.00, a medium(m) is $1.25, and a large(l) is $1.50 or if you don't want that you can have Kelp rings(k) just for $1.50 ")
          friesSelected=True
          if (side == "s"):
               finalOrderList.append("Small Coral Bits")
               total = total + 1
               taxCalc+=1*0.07
               finalTotal+=1+taxCalc
          elif (side == "m"):
               finalOrderList.append("medium Coral Bits")
               total = total + 1.25
               taxCalc+=1.25*0.07
               finalTotal+=1.25+taxCalc
          elif (side == "l"):
               finalOrderList.append("Large Coral Bits")
               total+=1.50
               taxCalc+=1.50*0.07
               finalTotal+=1.50+taxCalc
          elif (side=="k"):
               finalOrderList.append("Kelp Rings")
               secondSauce=input("Would you like salty sauce with your kelp rings for an extra .50 cents? (y or n) ")
               if secondSauce=="y":
                    total+=2.00
                    taxCalc+=2.00*0.07
                    finalTotal+=2.00+taxCalc
               else:
                    total+=1.50
                    taxCalc+=1.50*0.07
                    finalTotal+=1.50+taxCalc
          taxCalc-=taxCalc
     order.append(side)
     ketchup=int((input("How many ketchup packets would you like? ")))
     total+=ketchup*.25
     taxCalc+=ketchup*.25*0.07
     finalTotal+=ketchup*.25+taxCalc
     order.append(ketchup)
     order.append(orderNum) #adding the order number so the usrr can tell what order it is and for later deleting if choosen
     if(sandwhichSelected and beverageSelected and friesSelected):     #and looks for 2 true statements
     #if variable==true   AND variable==true   AND variable==true
          total-=1
     #print("You're total is",total)
     #print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of {4}'.format(sandwhich,beverage,fries,ketchup,total))
     total=round(total)
     finalTotal=round(finalTotal)
     print(order)
     print(f'''
     order number:{orderNum}
     Your order is: {entrees} entree, {beverage} drink, {side} side, {ketchup} packets
     subtotal: ${total}
     tax amount: 7%
     final amount: ${finalTotal}
     ''')
     print(finalOrderList)
     #print('${:,.2f}'.format(total))  #string formatting
     orderList.append(order)
     finalOrderListList.append(finalOrderList)
     editOrder=input("Would you like to edit your order? (y or n) ")
     if editOrder=="y":
          partToChange=input("What part would you like to change, entree(e), beverage(b), side(s), ketchup(k)? ") #asking foe waht tehy want to change
          if partToChange=="e":
               replacement=input("What would you like to change it to.\na Krabby patty(k) for $1.25, a Double Krabby patty(dk) for $2.00, a Triple Krabby patty(tk) for $3.00, a Salty Sea Dog(d) for $1.25, a Footlong(f) for $2.00, a Sailors Suprise(s) for $3.00, or the GOLDEN LOAF(g) for $2.00.") what they want to make it to
               order[0]=replacement #set order[o] which is the entree to the new input
               if replacement=="k":
                    finalOrderList[1]="Krabby Patty" #these  check what the user inputted and change it to the actual title instead of just initals
               elif replacement=="dk":
                    finalOrderList[1]="Double Krabby Patty"
               elif replacement=="tk":
                    finalOrderList[1]="Triple Krabby Patty"
               elif replacement=="d":
                    finalOrderList[1]="Salty Sea Dog"
               elif replacement=="f":
                    finalOrderList[1]="Footlong"
               elif replacement=="s":
                    finalOrderList[1]="Sailors Suprise"
               elif replacement=="g":
                    finalOrderList[1]="Golden Loaf"
          elif partToChange=="b":
               replacement=input("What would you like to change it to.\na kelp shake(k) for 2.00 or you can have a Seafoam soda, a small(s) is $1.00, a medium(m) is $1.25, and a large(l) is $1.50 ")
               order[1]=replacement
               if replacement=="k":
                    finalOrderList[2]="Kelp Shake"
               elif replacement=="s":
                    finalOrderList[2]="Small Seafoam Soda"
               elif replacement=="m":
                    finalOrderList[2]="Medium Seafoam Soda"
               elif replacement=="l":
                    finalOrderList[2]="Large Seafoam Soda"
          elif partToChange=="s":
               replacement=input("What would you like to change it to.\ncoral bits? a small(s) is $1.00, a medium(m) is $1.25, and a large(l) is $1.50 or if you don't want that you can have Kelp rings(k) just for $1.50 ")
               order[2]=replacement
               if replacement=="k":
                    finalOrderList[3]="Kelp Rings"
               elif replacement=="s":
                    finalOrderList[3]="Small Coral Bits"
               elif replacement=="m":
                    finalOrderList[3]="Medium Coral Bits"
               elif replacement=="l":
                    finalOrderList[3]="Large Coral Bits"
          elif partToChange=="k":
               replacement=int((input("How many ketchup packets would you like? ")))
               order[3]=replacement
          print(f'''
          order number:{orderNum}
          Your order is: {order[0]} entree, {order[1]} drink, {order[2]} side, {order[3]} packets
          ''') #reprint the order
     deleteOrder=input("Would you like to delete an order order? (y or n) ")
     if deleteOrder=="y":
          numToRemove=int(input("What was the order number? "))#ask what order they want to remove
          orderList.remove(orderList[numToRemove-1])#removes the order from the order list and since the index would be 1 less i minused 1
          finalOrderListList.remove(finalOrderList[numToRemove-1])#same thing here but with the order with the titles 
     orderInitiation=input("would you like to make another order? (y or n) ")
     if orderInitiation=="y":
          order.clear() #set things to nothing like back in the begining
          total-=total
          taxCalc-=taxCalc
          finalTotal-=finalTotal
     else:
          for i in finalOrderListList:
               print(i) # tried to get it to print like the suggested output but it really din't work