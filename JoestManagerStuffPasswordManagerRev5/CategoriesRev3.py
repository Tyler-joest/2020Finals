class Categories:

    def __init__(self,master):      #initializing the category class.
        self.master = master

    def categoryAdd(self,l,master):
        c = input("What would you like to call your category? " )   #nothing much here. What do you want to call the category?
        listC = [c]
        master.append(listC)
        l.append(listC)     #all this stuff appends the new category to both the master list and the l (everything) list.
        return l,master
        