'''
Module Description
--------------------
module filename: clinkedlist.py
module name: clinkedlist (Circular Linked List)
Content: Functions: dataType() 
        Class: Node, DLinkedList (Doubly Linked List)
Description: This module creates circular doubly linked list which can be traversed 
    both in forward and backward directions. The list is made of node objects. Each 
    Node object holds data and has two links and one unique indix. Nodes are linked 
    by the next and prev attributes or pointers. It is a closed list where the last
    node is linked to the first node with next and prev links.

    Node Class:
        Constructor: Node(data,index)
        setData(data), getData(), setIndex(index), getIndex(), __str__(), 
        __repr__(), copy()

    CLinkedList (circular linked list) Class:
        Constructor: CLinkedList(name="CLNKList")
        Class Methods: getHead(), getName(), getCurrentIndex(), tell(), 
        getCurrentNode(), getCurrentData(), changeCurrentData(data), getSize(),

        append(data), getNodeAt(index=0), getDataAt(index=0), editDataAt(data,index=0),
        moveNext(), moveLast(), movePrev(), moveFirst(), moveToHead(), 
        seek(offset,location), 
        
        getAllData(), convert2dict(), addDataFromList(listobj=[]), 
        addDataFromTuple(tupleobj=()), insertDataAt(data,index=0), 
        deleteDataAt(index=0), searchData(searchdata), rotateLeft(dataunits=1),
        rotateRight(dataunits=1), clear(), __len__(), __str__(), __repr__(), copy() 
        
        isFilePreserved(), setFilePreserve(preserve=True), getFileAddress(),
        setFileAddress(directory=datadir, filename=None),
        save(directory=datadir, filename="clinkedlist", enc=True), 
        loadDataFromFile(fileaddr=None), removeDataFile(),

    Suported Data Types: int, float, str, bool, NoneType, tuple, list, dictionary

    Data are saved in a binary file with extension .pcds (python common data structure file)
    Data are saved with md5hash to ensure data integrity. 
    Data encryption is supported for data security.

Author: A K M Aminul Islam
Last Modified: Monday August 05 2024 11:30 PM
Version:1.0.0
Dependencies: utilities, encrypt, os
'''

version="1.0.0"

import os
from pcds import utilities as u
from pcds import encrypt


import pcds
datadir=pcds.getDataDirectory()




# dataType(variable) returns the data type of the given variable
# >>> dataType(34)
# 'int'
# >>> dataType([])
# 'list'
# >>> dataType({})
# 'dict'
# >>> dataType(None)
# 'NoneType'
def dataType(arg):
    return str(type(arg)).split("'")[1]



# ----------------------------- class Node ---------------------------------
class Node:
    __data=None
    __index=0


    # constructor function of Node class
    # >>> import dlinkedList as dlnkl
    # >>> n1=dlnkl.Node(20,2)
    # >>> n1
    # <Node: 20 at index 2>
    def __init__(self,data=None,index=-1):
        try:
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
            if dataType(index) != 'int':
                raise TypeError("Index is an integer type data.")            
            if index<-1:
                raise ValueError("Index must be a positive integer, zero or -1.")
        except Exception as e: print(e); return None        
        if data==None:
            print("Warning! None type data is entered.")
        self.__data=data
        self.next=None
        self.prev=None
        self.__index=index


    # setter and getter methods
    # self.__data both readable and writable
    # >>> n1.getData()
    # 'hello'
    def getData(self):
        return self.__data


    # setData(self,data=None) returns node data
    # >>> n1.setData('hello')
    # >>> n1
    # <Node: hello at index 4>
    def setData(self,data=None):
        try:
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except TypeError as e: print(e); return
        if data==None:
            print("Warning! None type data is entered.")
        self.__data=data


    # setIndex(self,index=0) sets the index of the node
    # >>> n1.setIndex(4)
    # >>> n1
    # <Node: 20 at index 4>
    def setIndex(self,index=0):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index is an integer type data.")            
            if index<-1:
                raise ValueError("Index must be a positive integer, zero or -1.")
        except Exception as e: print(e); return
        self.__index=index


    # getIndex(self) returns the index of the node
    # >>> n1.getIndex()
    # 2
    def getIndex(self):
        if self.__index>=-1:
            return self.__index
        else:
            print("Warning! Index is not set.")


    # __str__(self) returns the string representation of the node instance
    # when str(node) function is used
    # >>> str(n1)
    # <Node: 20 at index 2>
    def __str__(self):
        if self.__index==-1:
            return "<Head Node at index -1>"
        elif self.__index>-1:
            if self.__data==None:
                return "<Node: None at index "+str(self.__index)+">"
            else:
                if dataType(self.__data)=='str':
                    return "<Node: '"+str(self.__data)+"' at index "+str(self.__index)+">"
                else:
                    return "<Node: "+str(self.__data)+" at index "+str(self.__index)+">"
        else:
            return ""


    # __repr__(self) returns the printable version of the 
    # node instance when repr(node) or print(node) function is used
    # >>> n1
    # <Node: 20 at index 2>
    def __repr__(self):
        return self.__str__()


    # copy() copies a node instance (deep copy)
    def copy(self):
        newnode=Node(self.__data,self.__index)    # self.__class__()
        if self.next!=None: newnode.next=self.next.copy()
        if self.prev!=None: newnode.prev=self.prev.copy()
        return newnode



    

# ----------------------------- class CLinkedList ---------------------------------
class CLinkedList:
    __head=None     # head of the linked list
    __size=-1       # read-only private property
    __curNode=None  # holds the current node of the doubly linked list
    __fileaddr=None # holds the file address (path+'\\'+filename) string
    __preserve=True # data file will not be deleted when the list variable is deleted
        
   


    # constructor of the circular linked list
    # Head node has index -1
    def __init__(self,name="CLNKList"):
        try:
            if dataType(name) != 'str':
                raise TypeError("CLinkedList name is a string type data.")
        except TypeError as e: print(e); return None
        # setting private variables        
        self.__head=Node(name,-1)        
        self.__size=0
        self.__curNode=self.__head
        



    # ------------------ setter and getter methods --------------------
    # getHead(self) returns the head node of the circular linked list
    def getHead(self):
        return self.__head




    # getName(self) returns the name of the circular linked list
    def getName(self):
        return self.__head.getData()




    # getCurrentIndex(self) returns the current location of the list pointer
    def getCurrentIndex(self):
        if self.__curNode:
            return self.__curNode.getIndex()




    # tell(self) returns also the current location of the list pointer
    def tell(self):
        if self.__curNode:
            return self.__curNode.getIndex()




    # getCurrentIndex(self) returns the current node object of the list pointer
    def getCurrentNode(self):
        if self.__curNode:
            return self.__curNode




    # getCurrentData(self) returns the current data of the list
    def getCurrentData(self):
        if self.__curNode:
            return self.__curNode.getData()




    # changeCurrentData(self) changes the current data of the list
    def changeCurrentData(self,data):
        if self.__curNode:
            self.__curNode.setData(data)




    # getSize(self) returns size (number of nodes) of the circular linked list
    def getSize(self):
        if self.__head.next==None: return 0
        return self.__size


    # -------------- End of setter and getter methods ---------------

    # append(self,data) adds the given data at the end of the circular linked list.
    # List size and index of the last node are updated accordingly.
    def append(self,data):
        try:
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except TypeError as e: print(e); return None
        # moving to the last node and adding the new node with new data
        new_node=Node(data,self.__size)
        if self.__size==0:
            self.__head.next=new_node
            new_node.next=new_node
            new_node.prev=new_node
            self.__size=1
            self.__curNode=new_node
            new_node.setIndex(0)
        elif self.__size==1:
            firstNode=self.__head.next
            firstNode.next=new_node
            new_node.next=firstNode
            new_node.prev=firstNode
            firstNode.prev=new_node
            self.__size=2
            new_node.setIndex(1)
            self.__curNode=new_node
        else:            
            firstNode=self.__head.next
            lastnode=self.__head.next.prev
            firstNode.prev=new_node
            new_node.next=firstNode
            lastnode.next=new_node
            new_node.prev=lastnode
            new_node.setIndex(self.__size)
            self.__curNode=new_node           
            self.__size=self.__size+1
        



    # getNodeAt(self,index=0) returns the node at the specific index position
    def getNodeAt(self,index=0):
        if self.__head.next==None: return None
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
        except Exception as e: print(e); return None
        self.seek(index,0)
        return self.__curNode




    # getDataAt(self,index=0) returns data of the node at the given index 
    def getDataAt(self,index=0):
        if self.__head.next==None: return None
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
        except Exception as e: print(e); return None
        self.seek(index,0)
        return self.__curNode.getData()
        



    # editDataAt(self,data,index=0) edits data at the given index
    def editDataAt(self,data,index=0):
        if self.__head.next==None: return None
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except Exception as e: print(e); return None
        self.seek(index,0)
        self.__curNode.setData(data)





    # moveNext(self) moves the list pointer to the next available node
    def moveNext(self):
        if self.__head.next==None: return None
        if self.__curNode.next:
            self.__curNode = self.__curNode.next        




    # moveLast(self) moves the list pointer to the end of the list
    def moveLast(self):
        if self.__head.next==None: return None
        if self.__size>0:        
            self.__curNode = self.__head.next.prev
        



    # movePrev(self) moves the list pointer to the previous node
    def movePrev(self):
        if self.__head.next==None: return None
        if self.__curNode.prev:
            self.__curNode = self.__curNode.prev       




    # moveFirst(self) moves the list pointer to the beginning of the list
    def moveFirst(self):
        if self.__head.next==None: return None
        if self.__head.next:
            self.__curNode = self.__head.next        




    # moveToHead(self) moves the list pointer to the beginning of the list
    def moveToHead(self):
        if self.__head.next==None: return None
        self.__curNode = self.__head




    # seek(self,offset=0,location=0) moves the list pointer by the offset value
    # from the reference location (0=from begining, 1=from current, 2=from end)
    def seek(self,offset=0,location=0):
        if self.__head.next==None: return None
        try:
            if dataType(offset) != 'int':
                raise TypeError("Argument offset is an integer type data.")
            if dataType(location) != 'int':
                raise TypeError("Argument location is an integer type data.")
            if location not in [0,1,2]:
                raise ValueError("Argument location has value either 0, 1 or 2 only.")
        except TypeError as e: print(e); return None
        except ValueError as e: print(e); return None
        # reducing the offset value if it exceeds the size
        if offset>0:
            if offset >= self.__size:
                offset=offset-(offset//self.__size)*self.__size
        elif offset<0:
            offset=-1*offset
            if offset >= self.__size:
                offset=offset-(offset//self.__size)*self.__size
            offset=-1*offset

        curIndex=self.__curNode.getIndex()
        movement=0
        # offset from the beginning of the list
        if location==0:
            if offset==0:
                self.__curNode=self.__head.next
                return None
            movement=curIndex-offset
            if movement==0: return None                
            elif movement>0: # move left
                i=0
                while i<movement and self.__curNode.prev: 
                    self.__curNode=self.__curNode.prev
                    i=i+1
            elif movement<0: # move right
                i=0; movement=-1*movement
                while i<movement and self.__curNode.next: 
                    self.__curNode=self.__curNode.next
                    i=i+1
        # offset from the current location
        elif location==1:            
            if offset==0: return None                
            elif offset>0: # move right
                i=0
                while i<offset and self.__curNode.next: 
                    self.__curNode=self.__curNode.next
                    i=i+1
            elif offset<0: # move left
                i=0; offset=-1*offset
                while i<offset and self.__curNode.prev: 
                    self.__curNode=self.__curNode.prev
                    i=i+1
        # offset from the end of the list
        elif location==2:
            if offset==0:
                self.__curNode=self.__head.next.prev
                return None 
            listsize=self.__size
            movement=listsize-1+offset-curIndex
            if movement==0: return None                
            elif movement>0: # move right
                i=0
                while i<movement and self.__curNode.next: 
                    self.__curNode=self.__curNode.next
                    i=i+1
            elif movement<0: # move left
                i=0; movement=-1*movement
                while i<movement and self.__curNode.prev: 
                    self.__curNode=self.__curNode.prev
                    i=i+1



    # addDataFromList(listobj=[]) appends data from the list
    def addDataFromList(self, listobj=[]):
        try:
            if dataType(listobj) != "list":
                raise TypeError("Argument is not a list data type.")
            if len(listobj)==0:
                raise ValueError("List is empty.")
        except Exception as e: print(e); return None
        # append data
        for data in listobj:
            self.append(data)
            


    # addDataFromTuple(listobj=()) appends data from the tuple given
    def addDataFromTuple(self, tupleobj=()):
        try:
            if dataType(tupleobj) != "tuple":
                raise TypeError("Argument is not a tuple data type.")
            if len(tupleobj)==0:
                raise ValueError("Tuple is empty.")
        except Exception as e: print(e); return None
        # append data
        for data in tupleobj:
            self.append(data)




    # getAllData(self) returns all data of the circular linked list in tuple form
    def getAllData(self):
        if self.__head.next==None: return ()
        cur_node=self.__head.next
        i=0; tmplist=[]
        for i in range(self.__size):
            tmplist.append(cur_node.getData())        
            cur_node = cur_node.next            
        return tuple(tmplist)




    # convert2dict(self) returns doubly linked list data in dictionary form 
    def convert2dict(self):
        if self.__head.next==None: return {}
        cur_node=self.__head.next
        tmpdict={'name':self.getName(),'class':'CLinkedList','size':self.__size}
        i=0;
        for i in range(self.__size):
            tmpdict[cur_node.getIndex()]=cur_node.getData()
            cur_node = cur_node.next            
        return tmpdict



    # insertDataAt(self,data,index=0) inserts new data at the given index position
    def insertDataAt(self,data,index=0):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index > self.__size: 
                raise ValueError("Index out of the range.")
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except Exception as e: print(e); return None       
        # inserting and creating bidirectional links
        if index==self.__size:
            self.append(data); return None
        new_node=Node(data,index)
        self.seek(index,0)
        curnode=self.__curNode
        prevnode=self.__curNode.prev        
        if index==0:
            self.__head.next=new_node
        new_node.next=curnode
        curnode.prev=new_node
        new_node.prev=prevnode
        prevnode.next=new_node
        self.__curNode=new_node
        # updating indices
        for i in range(index,self.__size+1):
            self.__curNode.setIndex(i)
            self.__curNode=self.__curNode.next
        self.__size = self.__size + 1
        



    # deleteDataAt(self,index=0) deletes the node at the given index and updates
    # the other indices
    def deleteDataAt(self,index=0):
        if self.__head.next==None: return None
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
        except Exception as e: print(e); return None
        if self.__size==0: return None
        elif self.__size==1: 
            self.__head=None; return None
        elif self.__size==2:
            firstnode=self.__head.next
            senondnode=self.__head.next.next
            if index==0:
                secondnode.next=secondnode
                secondnode.prev=secondnode
                secondnode.setIndex(0)
                self.__head.next=secondnode
                self.__curNode=secondnode
                return None
            elif index==1:
                firstnode.next=firstnode
                firstnode.prev=firstnode                
                self.__curNode=firstnode
                return None
        # moving to the current index, cutting and rejoining the links
        self.seek(index,0)
        prevnode=self.__curNode.prev
        nextnode=self.__curNode.next        
        prevnode.next=nextnode
        nextnode.prev=prevnode
        if index==0: self.__head.next=nextnode
        self.__curNode=nextnode
        # updating indices
        for i in range(index,self.__size-1):
            self.__curNode.setIndex(i)
            self.__curNode=self.__curNode.next
        self.__size = self.__size - 1





    # searchData(self, searchdata) returns the indices and data of the linkedlist
    # where the searchdata is found. It returns a dictionary {index:data, ...}
    # Supported search data type: str, int, float, bool, NoneType, list, tuple, dict
    # >>> cll
    # <CLinked List: size=16, Data=(['jaon', 'john', 'ali', 'karim'], 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None) >
    # >>> cll.searchData('ali')
    # {0: ['jaon', 'john', 'ali', 'karim'], 6: 'ali', 7: 'karim ali'}
    # >>> cll.searchData(10)
    # {1: 10, 9: 10}
    # >>> cll.searchData(True)
    # {13: True}
    # >>> cll.searchData([1,2,3])
    # Search data type is unsupported.
    # {}
    def searchData(self, searchdata):
        if self.__head.next==None: return None
        try:
            if dataType(searchdata) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except Exception as e: print(e); return None
        # come to the beginning of the list and start searching
        self.__curNode=self.__head.next
        s=""; foundDict={}
        curnode=self.__curNode
        try:
            for i in range(self.__size):
                listdata=curnode.getData()
                index=curnode.getIndex()
                if dataType(searchdata) == 'str':
                    if dataType(listdata) in ['int','float','bool','NoneType']:
                        curnode=curnode.next
                        continue
                    elif dataType(listdata) =='str':
                        if searchdata in listdata:
                            foundDict[index]=listdata
                    elif dataType(listdata) in ['list','tuple']:
                        if searchdata in listdata:
                            foundDict[index]=listdata
                    elif dataType(listdata) == 'dict':
                        if searchdata in listdata.keys() or searchdata in listdata.values():
                            foundDict[index]=listdata
                elif dataType(searchdata) in ['int','float','NoneType']:
                    if dataType(listdata) in ['int','float','NoneType']:                    
                        if searchdata == listdata: foundDict[index]=listdata
                    elif dataType(listdata) in ['list','tuple']:
                        if searchdata in listdata:
                            foundDict[index]=listdata
                    elif dataType(listdata) == 'dict':                        
                        if searchdata in listdata.keys() or searchdata in listdata.values():
                            foundDict[index]=listdata
                elif dataType(searchdata) == 'bool':
                    if  dataType(listdata) == 'bool':
                        if searchdata==listdata: foundDict[index]=listdata
                    elif searchdata in ['list','tuple']:
                        if searchdata in listdata:
                            foundDict[index]=listdata
                    elif dataType(listdata) == 'dict':                        
                        if searchdata in listdata.keys() or searchdata in listdata.values():
                            foundDict[index]=listdata
                else:
                    raise ValueError("Search data type is unsupported.")
                curnode=curnode.next
        except ValueError as e: print(e); return None
        except Exception as e: print(e); return None
        return foundDict





    # rotateLeft(dataunits=1) rotates the circular doubly linked list left 
    # (anticlockwise) by the stated data units
    def rotateLeft(self, dataunits=1):
        if self.__head.next==None: return None
        try:
            if dataType(dataunits) != 'int' or dataunits<0:
                raise Exception("Number of data units must be a positive integer.")
        except Exception as e: print(e); return None
        if dataunits==0: return None
        # reducing the value of dataunits
        if dataunits>self.__size:
            dataunits=dataunits-self.__size*(dataunits//self.__size)
        self.seek(dataunits,0)
        self.__head.next=self.__curNode
        for i in range(self.__size):
            self.__curNode.setIndex(i)
            self.__curNode=self.__curNode.next





    # rotateRight(dataunits=1) rotates the circular doubly linked list rightward 
    # (clockwise) by the stated data units
    def rotateRight(self, dataunits=1):
        if self.__head.next==None: return None
        try:
            if dataType(dataunits) != 'int' or dataunits<0:
                raise Exception("Number of data units must be a positive integer.")
        except Exception as e: print(e); return None
        if dataunits==0: return None
        # reducing the value of dataunits
        if dataunits>self.__size:
            dataunits=dataunits-self.__size*(dataunits//self.__size)
        self.seek(self.__size-dataunits,0)        
        self.__head.next=self.__curNode
        for i in range(self.__size):
            self.__curNode.setIndex(i)
            self.__curNode=self.__curNode.next




    
    # clear(self) delinks all nodes from the head of the circular linked list
    # by initializing the link list
    # >>> cll=clnkl.CLinkedList()
    # >>> cll
    # <CLinked List: size=9, Data=(10, 20, 30, 40, 50, 'a', 'b', 'c', 'd') >
    # >>> cll.clear()
    # >>> cll
    # <CLinked List: size=0, Data=() >
    def clear(self):
        self.__init__(name=self.getName())     # data file loses all data
        




    # __len__(self) returns the size of the circular linked list when len(linkedList) used
    def __len__(self):
        return self.__size




    # __str__(self) stringify the circular linked list data when str(linkedList) used
    def __str__(self):
        return "<"+self.getName()+"[CLinkedList]: size="+str(self.__size)+", Data="+str(self.getAllData())+">"




    # __repr__(self) converts linked list into a printable representation
    # when repr(linkedList) is used
    # >>> cll=clnkl.CLinkedList()
    # >>> cll.append(125)
    # >>> cll.append(1.25)
    # >>> cll.append('hello world')
    # >>> cll.append(['hello',' world',74.12])
    # >>> cll.append(('hello',[4,8,7.2,None],' world',74.12))
    # >>> cll.append({2:45,'a':'abc','rolls':[12,14,13]})    
    # >>> cll
    # <CLinked List: size=6, Data=(125, 1.25, 'hello world', ['hello', ' world', 74.12], ('hello', [4, 8, 7.2, None], ' world', 74.12), {2: 45, 'a': 'abc', 'rolls': [12, 14, 13]}) >
    def __repr__(self):
        return self.__str__()



    # copy() copies the circular linked list to a new instance
    def copy(self):        
        newclnkl=CLinkedList(self.getName())
        if self.__head.next==None: return newclnkl
        tmpnodes=[]; i=0
        for data in self.getAllData():
            tmpnodes.append(Node(data=data,index=i)); i=i+1
        newclnkl.__size=i
        # building the forward links
        newclnkl.__head.next=tmpnodes[0]    # at head node
        newclnkl.__curNode=newclnkl.__head.next     # at tmpnodes[0]
        for i in range(newclnkl.__size-1):
            newclnkl.__curNode.next=tmpnodes[i+1]
            newclnkl.__curNode=newclnkl.__curNode.next
        newclnkl.__curNode.next=tmpnodes[0]
        newclnkl.__curNode=newclnkl.__curNode.next # at tmpnodes[0]
        # building the backward links
        for i in range(newclnkl.__size-1,0,-1):
            newclnkl.__curNode.prev=tmpnodes[i]
            newclnkl.__curNode=newclnkl.__curNode.prev
        tmpnodes[1].prev=tmpnodes[0]
        newclnkl.__curNode=newclnkl.__curNode.prev # at tmpnodes[0]
        return newclnkl








# ------------------------- File I/O Operations -----------------------------
# 
    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted when the
    # list instance is destroyed by del() function
    def setFilePreserve(self, preserve=True):
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve




    # setFileAddress(self, directory=datadir, filename=None) sets 
    # the absolute address of the .pdsf data file in the private variable __file
    def setFileAddress(self, directory=datadir, filename=None):
        try:
            # checking inputs 
            if dataType(directory) != 'str': 
                raise TypeError("Data type of file directory should be string.")                         
        except TypeError as e: print(e); return None
        if filename==None: filename=self.getName()
        else:
            try:
                if dataType(filename) != 'str': 
                    raise TypeError("Data type of file name should be string.")                
            except TypeError as e: print(e); return None
            filename=filename.strip()
        directory=directory.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFile(directory, filename)
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: print(e); return None
        


    
    # getFileAddress(self) returns the absolute address of the .pdsf data file
    def getFileAddress(self):
        if self.__fileaddr:
            return self.__fileaddr




    # save(self, directory=datadir, filename="dlinkedlist", enc=True) saves all data 
    # in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    def save(self, directory=datadir, filename=None, enc=True):
        if self.__head.next==None: return False
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Data type of file directory should be string.")
            if dataType(enc) != 'bool': 
                raise TypeError("Data type of enc (encrypt) should be boolean.")
        except TypeError as e: print(e); return False        
        # convert all the current data into string (Part 2)
        cur_node=self.__head.next # The first data
        s=""
        for i in range(self.__size):            
            data=cur_node.getData()
            s=s+u.data2str(data)+"\n" # '\n' is the data separator
            cur_node = cur_node.next
        s=s[0:len(s)-1]     # the last '\n' is removed
        # adding file header (Part 3)        
        # adding file header (35 character (24+10+1)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='CLINKEDLIST FILE HEADER:' + str(encrypt.randomInteger(10))
        # encrypt the data string (Part 4)
        if enc:            
            s=encrypt.encrypt(s,int(fileheader[33]))
        s=fileheader+'\n'+s
        # adding md5 hash at the beginning of the file (Part 5)
        md5hashstr=u.getHashCode(s,"md5")
        s="MD5:"+md5hashstr+"\n"+s    # Newly 37(4+32+1) characters are added    
        # second phase (final) encryption and encryption tagging (Part 6)
        if enc:
            s="[ENCRYPTED]"+'\n'+s
            s=encrypt.encrypt(s,10)
        else:
            s="[NOT ENCRYPTED]"+'\n'+s
        # convert string into byte array using 'utf-8' encoding (Part 7)
        ba=None # byte array
        try:
            ba=s.encode('utf-8') # converting string to bytearray 
        except Exception as e: print(e); return False
        # creating or opening .pcds data file and writing to the file (Part 8)
        if filename==None: filename=self.getName()
        else:
            try:
                if dataType(filename) != 'str': 
                    raise TypeError("Data type of file name should be string.")                
            except TypeError as e: print(e); return None
            filename=filename.strip()
        directory=directory.strip(); fileaddr=""
        try:
            fileaddr=u.createDataFile(directory, filename)
            fileaddr=os.path.abspath(fileaddr)
        except Exception as e: 
            print(e); print("List data are not saved."); return False
        fo=None
        try:
            fo=open(fileaddr,'wb')
            if not fo:
                print("Data file cannot be opened. Saving not successful.")
                self.__fileaddr=""
                return False
            fo.write(ba)
            fo.close()
            self.__fileaddr=fileaddr            
        except IOError as e: print(e); return False
        except Exception as e: print(e); return False
        if enc:
            print("Encrypted Data Saved Successfully into '"+self.__fileaddr+"'")
        else:
            print("Plain Data Saved Successfully into '"+self.__fileaddr+"'")
        return True





    # loadDataFromFile() function loads stack data in memory from the data file
    # File loading also occurs in 8 steps, but in reverse order of file saving
    # 8 steps: (1) checking inputs (2) reading the binary data file 
    # (3) decoding the data file with utf-8 (4) check the file encryption tag
    # (5) first phase decryption using keyid=10 (6) checking MD5 hash
    # (7) removing file header (8) loading string data into a list after conversion
    # >>> cll=clnkl.CLinkedList()
    # >>> cll
    # <CLinked List: size=0, Data=()>
    # >>> cll.loadDataFromFile()
    # ['125', '1.25', '"hello world"', '["hello","world",74.12]', '("hello",[4,8,7.2,None],"world",74.12)', '{2:45,"a":"abc","rolls":[12,14,13]}', '148.25', '"hello"']
    # >>> cll
    # <CLinked List: size=8, Data=(125, 1.25, 'hello world', ['hello', 'world', 74.12], ('hello', [4, 8, 7.2, None], 'world', 74.12), {2: 45, 'a': 'abc', 'rolls': [12, 14, 13]}, 148.25, 'hello')>
    def loadDataFromFile(self, fileaddr=None):
        # checking inputs (Part 1)
        if fileaddr==None: fileaddr=datadir+os.sep+self.getName()+".pcds"
        else:
            try:
                if dataType(fileaddr) != 'str': 
                    raise TypeError("Data type of file address should be string.")                
            except TypeError as e: print(e); return None
            fileaddr=fileaddr.strip()        
        if not u.checkDataFileAddr(fileaddr):
            return False
        # opening data file in read mode (Part 2)
        fileaddr=os.path.abspath(fileaddr)
        self.__fileaddr=fileaddr
        fo=None; s=""; bs=""        
        try:
            fo=open(fileaddr,'rb')
            # if file is blank
            fo.seek(0,2)
            filesize=fo.tell()
            if filesize==0:
                print("Data File is empty")                    
                return False
            # reading bytes from the data file in byte array
            fo.seek(0,0)            # come to the beginning of the file
            bs=fo.read(filesize)    # bs=binary byte string
            fo.close()
        except Exception as e: print(e); return False
        # decoding byte array into string (Part 3)
        try:            
            s=bs.decode('utf-8')                
        except Exception as e: print(e); return False
        # checking the encryption tag (Part 4)
        encrypted=False
        if '\v' in s:
            encflagstr=s.split('\v')[0]
        elif '\n' in s:
            encflagstr=s.split('\n')[0]
        if encflagstr=="[NOT ENCRYPTED]":
            encrypted=False; s=s[16:len(s)]
        elif encflagstr=="yo+sRFr-oli":
            encrypted=True; s=s[12:len(s)]
        # first phase decryption using keyid=10 (Part 5)
        if encrypted: s=encrypt.decrypt(s,10)
        # extracting and checking md5hash strings(Part 6)
        if len(s) < 38:
            print("File has no data. Loading is failed.")
            return False
        fileMD5=s[4:36]
        hdstr=s[37:len(s)] # hdstr=header+data string
        newMD5=u.getHashCode(hdstr,"md5")        
        try:            
            if newMD5 != fileMD5:
                raise Exception("Data file is corrupt as hash missmatch. Loading is failed.")
        except Exception as e: print(e); return False
        s=hdstr
        # removing file header and final decryption (Part 7)         
        try:
            # In the File Header, the last character is the keyid
            # Length of File Header = 35 (24 char+10 digits+'\n')
            if len(s) < 36:
                print("File has no data. Loading is failed")
                return False
            if s[0:24] == 'CLINKEDLIST FILE HEADER:':
                keyid=int(s[33])
                s=s[35:]  # leave the header part
                if encrypted:                                  
                    s=encrypt.decrypt(s,keyid)
            else: raise Exception("Data file is corrupt.")
        except Exception as e: print(e); return False
        # loading data into the linked list (Part 8)        
        sl=s.split('\n') # sl=string list
        try:
            self.clear() # head delinking, setting size to zero 
            self.__size = len(sl);
            curnode=self.__head;
            i=0
            while i < self.__size:
                newnode=Node(u.str2data(sl[i]),i)
                if i==0:
                    curnode.next=newnode
                    newnode.next=newnode; newnode.prev=newnode
                elif i==1:
                    curnode.next=newnode
                    newnode.next=curnode; curnode.prev=newnode                    
                else:                    
                    curnode.next=newnode; newnode.prev=curnode                    
                curnode=newnode
                i=i+1
            curnode.next=self.__head.next
            self.__head.next.prev=curnode            
        except Exception as e: 
            print(e); print("Data not loaded successfully."); return False
        print("Data Loaded Successfully from the file: '"+self.__fileaddr+"'")
        return True





    # removeDataFile(self) deletes the data file. If preserve is True, the
    # data file will not be deleted
    def removeDataFile(self):        
        if not self.__preserve:
            try:            
                os.remove(self.__fileaddr)
                return True
            except Exception as e: print(e); return False
        else:            
            print("CLinkedList data file is preserved and cannot be deleted.")
            return False

# ------------------------ END of clinkedlist.py file --------------------------







