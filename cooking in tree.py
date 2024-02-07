import sys
import time
class tree:
    def __init__(self,parent=None):
        self.root=None
        if parent is None:
            parent=self.fillparent()
        else:
            self.root=self.findroot()
        self.parent=parent
        self.newparent=[*self.parent]
        self.listlength=len(self.newparent)
        self.child=self.childlize(parent)
        self.newchild=[*self.child]
        

        self.newroot=None
        self.trimlength=0
        self.trimtree()

        self.tail,self.taildepth = self.findtail()
        self.maximum=0
        self.maximumnodes=[0,0]
        self.maxdistance()
        
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
        temproot=0
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
                        temproot = i
                    else:
                        print("Root with no parent should only exist one in a tree\nTry Again!\n")
                        continue

                elif i==temproot:
                    if claimed_parent<i:
                        print("You are trying to construct a loop inside a tree, don't do that!\nTry Again!\n")
                        continue
                    temproot=claimed_parent

            except ValueError:
                print("invalid input, see what you have done, idiot\nTry Again!\n")
                continue
            parent.append(claimed_parent)
            i+=1
            
        return parent

    def childlize(self,parent):  #convert the parent-mapping list into child-mapping list 
        child=[-1]*self.listlength
        for i in range(self.listlength):
            if parent[i]==-1:
                continue
            if child[parent[i]]==-1:
                child[parent[i]]=[i]
            else:
                child[parent[i]].append(i)
        return child
        
    def findroot(self): #find the root(common origin) of the family tree 
        a=0
        for i in range(self.listlength):
            if self.newparent[a]!=-1:
                a=self.newparent[a]
            else:
                break
        return a

    def trimtree(self):    #trim the tree from the original root until the root is a fork, help with the speed i guess 
        self.newroot=self.root
        while self.newchild[self.newroot]!=-1:
            if len(self.newchild[self.newroot])==1:
                self.newparent[self.newroot]="trimmed"
                temp=self.newchild[self.newroot][0]
                self.newchild[self.newroot]="trimmed"
                self.newroot=temp
                self.trimlength+=1
            else:
                break
        self.newparent[self.newroot]=-1
        self.listlength-=self.trimlength
        
    def findtail(self,init=None):     #find all the dead ends of the family tree 
        tail=[]
        taildepth=[]
        counter=0
        node=init
        if init is None:
            node=self.newroot
        while self.newchild[node]!=-1:
            if len(self.newchild[node])==1:
                node=self.newchild[node][0]
                counter+=1
            else:
                for i in self.newchild[node]:
                    t, l = self.findtail(i)
                    for j in range(len(l)) :
                        l[j]+=1+counter
                    tail+=t
                    taildepth+=l
                break
        
        if self.newchild[node]==-1:
            tail.append(node)
            taildepth.append(counter)
        return tail, taildepth

    def forkpath(self,a):     #create a ONLY FORK path from node "a" to root  
        apath=[]
        for i in range(self.listlength):
            if self.newparent[a]!=-1:
                a=self.newparent[a]
                if len(self.newchild[a])>1:
                    apath.append(a)
            else:
                break
        return apath
    
    def finddepth(self,a):
        depth=0
        for i in range(self.listlength):
            if self.newparent[a]!=-1:
                a=self.newparent[a]
                depth+=1
            else:
                break
        return depth

    def distance(self,a,b):  #caculate the minimum distance between node "a" and "b"
        apath=self.forkpath(a)          
        bpath=self.forkpath(b)         
        c=None
        l=0       
        da = self.finddepth(a)       
        db = self.finddepth(b)

        for i in apath:
            for j in bpath:
                if i==j :
                    return da+db-2*self.finddepth(i)
                    
    def maxdistance(self):   #the final boss: find the maximum distance in the entire family tree
        maxtaildepth=max(self.taildepth)
        self.maximum=maxtaildepth+self.trimlength
        self.maximumnodes=[self.root, self.tail[self.taildepth.index(maxtaildepth)]]
        combisum=[]
        sumsource=[]
        if len(self.tail)==1:
            return None
        for i in range(len(self.taildepth)-1):           #generate the combination of sum
            for j in range(i+1,len(self.taildepth)):
                combisum.append(self.taildepth[i]+self.taildepth[j])
                sumsource.append([self.tail[i], self.tail[j]])
        combisum,sumsource=optquicksort_with_partner(combisum,sumsource)
        combisum.reverse()
        sumsource.reverse()
        for i in range(len(combisum)):
            d=self.distance(sumsource[i][0],sumsource[i][1])
            if self.maximum<d:
                    self.maximum=d
                    self.maximumnodes=sumsource[i]
            if d==combisum[i]: 
                return None
        return None
    
    def showmax(self):
        print("------------------------------------------------------")
        print(f"The tree mapping(child to parent): \n {T.parent} \n")
        print(f"The reverse tree mapping(parent to child): \n {T.child} \n")
        print(f"Max distance:{T.maximum}")
        print(f"From: node {T.maximumnodes[0]} to node {T.maximumnodes[1]}")
        print(f"(Note: only shows one of the solutions)")
        print("------------------------------------------------------")

def optquicksort(thelist):                                         
    pivot=thelist[int((len(thelist)-1)/2)]        #if the list is nearly sorted, choosing middle as pivot would save time
    thelist[int((len(thelist)-1)/2)]=thelist[-1]       #actual pivot has collision box so i take it away
    thelist.pop()

    if thelist == []:
        return [pivot]
    P=0                                          #position of the virtual pivot
    e=0                                          #the amounts of elements that is same as 
    for i in range(len(thelist)):                #divide the list into, smaller, equal, and larger by pivot
        if thelist[i-e]<pivot:
            temp=thelist[P]
            thelist[P]=thelist[i-e]
            thelist[i-e]=temp
            P+=1
            
        elif thelist[i-e]==pivot:
            temp=thelist[len(thelist)-1-e]                  #swap it with the element before last e elements
            thelist[len(thelist)-1-e]=thelist[i-e]
            thelist[i-e]=temp
            e+=1
    L=[]              
    if P!=0:
        L= optquicksort(thelist[:P])
    
    L.append(pivot)                          
    
    if P==len(thelist):
        return L
    
    L+=thelist[len(thelist)-e:]             #add the "equal part"
    
    if P!=len(thelist)-e:                 #check if P is the element on the "equal" section (larger section doesnt exist)
        U= optquicksort(thelist[P:len(thelist)-e])
        L+=U
  
    return L

def optquicksort_with_partner(target,partner):
    if len(target)!=len(partner):
        print("the length of partner list does not match the target list")
        print("the sort would not be excuted")
        return target,partner
    
    bind=[]
    for i in range(len(target)):
        bind.append([target[i],partner[i]])
    
    bind=optquicksort(bind)

    target=[]
    partner=[]
    for i in bind:
        target.append(i[0])
        partner.append(i[1])

    return target, partner 

T=tree()
T.showmax()
