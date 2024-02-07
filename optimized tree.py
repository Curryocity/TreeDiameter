import sys
import time
class tree:
    def __init__(self,parent=None):
        if parent is None:
            self.root=None
            self.parent=self.fillparent()
        else:
            self.root=self.findroot()
            self.parent=parent

        self.child=self.childlize()
        
        self.tail,self.taildepth = self.findtail()
        self.diagonal=max(self.taildepth)
        self.corner1=self.root
        self.corner2=self.tail.pop(self.taildepth.index(self.diagonal))
        self.maxtaildepth=self.taildepth.pop(self.taildepth.index(self.diagonal))
        self.maxdistance()
        self.tail.append(self.corner2)
        self.taildepth.append(self.maxtaildepth)
        
    def fillparent(self):    #create the list "parent" by asking the user. For mapping child into parent later on.
        print("\n------------------------------------------------------")
        print("Create the tree by input")
        print("The members(node) of the tree are all named with subsequent natural numbers")
        print("Each member(node) has only zero or one parent")
        print("Please create a tree that make sense, and I'll try my best to prevent you doing nonsense")
        print("Now start!")
        print("------------------------------------------------------\n")
        try:
            pop=input("Enter the population of family tree: ").strip()
            pop=int(pop)
        except ValueError:
            print(f"Surely '{pop}' is an positve integer, let's see how the program runs the population '{pop}' ")
            print("(The Program is still running, Trust)")
            print("......\n\n")
            print("Leaked System Log:")
            print(f"{time.asctime()} Alert! System is disrupted by a retard\n")
            sys.exit(1)
        parent=[]  
        i=0
        while i < pop:
            try:
                claimed_parent=int(input(f"Who's {i}'s parent?(-1 if None): ").strip())
                if claimed_parent > pop-1 or claimed_parent < -1 :
                    print(f"Please enter a integer from -1 to {pop-1}\nTry Again!\n") 
                    continue
                if claimed_parent==i:
                    print("The parent couldn't be itself\nTry Again!\n")
                    continue

                if claimed_parent == -1:
                    if self.root is None:
                        self.root = i
                    else:
                        print("Root with no parent should only exist one in a tree\nTry Again!\n")
                        continue

            except ValueError:
                print("This doesnt look like a number, idiot\nTry Again!\n")
                continue
            parent.append(claimed_parent)
            i+=1
            
        return parent

    def childlize(self):  #convert the parent-mapping list into child-mapping list 
        child=[None]*len(self.parent)
        for c,p in enumerate(self.parent):
            if p==-1:
                continue
            if child[p] is None:
                child[p]=[c]
            else:
                child[p].append(c)
        return child
        
    def findroot(self): #find the root(common origin) of the family tree, not need if the parent list were created by filling
        a=0
        for i in range(len(self.parent)):
            if self.parent[a]!=-1:
                a=self.parent[a]
            else:
                break
        return a
        
    def findtail(self,init_node=None,init_depth=None):     #find all the dead ends of the family tree 
        tail,taildepth=[],[] 
        node=init_node
        current_depth=init_depth
        if init_node is None:
            node=self.root
            current_depth=0
        while self.child[node]!= None:
            if len(self.child[node])==1:
                node=self.child[node][0]
                current_depth+=1
                continue

            for i in self.child[node]:
                t, l = self.findtail(i,1+current_depth)
                tail+=t
                taildepth+=l
            return tail, taildepth
        
        tail.append(node)
        taildepth.append(current_depth)
        return tail, taildepth

    def forkpath(self,a):     #create a ONLY FORK path from node "a" to root  
        apath=[]
        while self.parent[a]!=-1:
            a=self.parent[a]
            if len(self.child[a])>1:
                apath.append(a)    

        return apath
    
    def finddepth(self,a):
        depth=0
        for i in range(len(self.parent)):
            if self.parent[a]!=-1:
                a=self.parent[a]
                depth+=1
            else:
                break
        return depth

    def distance(self,a,b,da=None,db=None):  #caculate the minimum distance between node "a" and "b"
        apath=self.forkpath(a)          
        bpath=set(self.forkpath(b))         
        if da is None:
            da = self.finddepth(a)   
        if db is None:    
            db = self.finddepth(b)

        for i in apath:
            if i in bpath:
                return da+db-2*self.finddepth(i)
                    
    def maxdistance(self):   #the final boss: find the maximum distance in the entire family tree
        for i in range(len(self.tail)):
            d=self.distance(self.tail[i],self.corner2,self.taildepth[i],self.maxtaildepth)
            if d > self.diagonal:
                self.diagonal=d
                self.corner1=self.tail[i]
        return None
                
    def showmax(self):
        print("------------------------------------------------------")
        print(f"The tree mapping(child to parent): \n {T.parent} \n")
        print(f"The reverse tree mapping(parent to child): \n {T.child} \n")
        print(f"Max distance:{T.diagonal}")
        print(f"From: node {T.corner1} to node {T.corner2}")
        print(f"(Note: only shows one of the solutions)")
        print("------------------------------------------------------")

T=tree()
T.showmax()