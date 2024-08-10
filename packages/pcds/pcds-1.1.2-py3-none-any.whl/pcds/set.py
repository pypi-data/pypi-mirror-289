'''
Module Description
--------------------
module filename: set.py
module name: set
Content: Functions: dataType(data)

        Class: Node, BinarySearchTree (Binary Search Tree)

Description: This python module creates a set data structure which has unique data
    with the following operations: union (AUB or A+B), intersection (A.B), 
    difference (A-B), and complement (A`= Universal-A) operations.

    Set Class:

        Properties: __bstree, __dataTuple

        Constructor: Set(data)

        Class Methods: addDataFromList(listdata), loadDataFromTuple(tupledata),
        deleteData(data), getSetData(), isNull(), __len__(), __str__(), __repr__(), 
        copy(), clear(), 

        setDataFileAddress(directory=datadir, filename="set"), getDataFileAddress(),        
        isFilePreserved(), setFilePreserve(preserve=True),
        save(directory=datadir, filename="set", enc=True),
        loadDataFromFile(fileaddr=datadir+os.sep+"set.pcds"), removeDataFile(),

        isEqual(set2), __eq__(right), __req__(left), __neq__(right), __rneq__(left), 
        union(set2), __add__(right), __radd__(left), intersect(set2), __xor__(right),
        subtract(set2), difference(set2), __sub__(right), __rsub__(left),
        isDisjoint(set2), isSuperset(set2), isSubset(set2)
        

    Suported Data Types: int, float, str, bool (False=0, True=1)

    Data are saved in a binary file with extension .pcds (python common data structure file)
    Data encryption is supported for security of data.

Author: A K M Aminul Islam
Last Modified: Saturday Aug 03 2024 09:15 AM
Version:1.0.0
Dependencies: utilities, encrypt, bstree, os

'''


from pcds import utilities as u
from pcds import encrypt
from pcds import bstree as bst
import os


import pcds
datadir=pcds.getDataDirectory()
version='1.0.0'



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



# ----------------------------- Set class ------------------------------
#class Set:
class Set:
    # private properties
    __bstree=bst.BinarySearchTree() # holds the binary search tree data structure   
    __dataTuple=()                  # python tuple to hold set data
    __preserve=True                 # data file cannot be deleted if preserve is True
    __fileaddr=""                   # holds the address of the data file


    # Set constructor (Set(), self.__class__())
    def __init__(self, data=None):        
        self.__bstree.clear(); self.__dataTuple=() 
        if data==None or data==[] or data==(): return None                
        try:
            if dataType(data) not in ['list','tuple']:
                raise ValueError("Error: Data should be provided as a python list or tuple.")            
        except Exception as e: print(e); return None
        self.__bstree.clear()       
        if dataType(data) =='list':
            self.__bstree.addDataFromList(data)
        elif dataType(data) =='tuple':
            self.__bstree.addDataFromTuple(data)        
        self.__bstree.buildTree()
        self.__bstree.sortTree(asc=True)
        self.__dataTuple=self.__bstree.getSortedData()
        self.__preserve=True
        self.__fileaddr=""



    # addDataFromList(self,listdata) adds list data into the set structure
    # Only the valid data types (int,float,str,bool) are added
    def addDataFromList(self,listdata):
        try:
            if dataType(listdata) != 'list':                
                raise ValueError("Error: Data argument is not a list.")
        except Exception as e: print(e); return None
        tmplist=list(self.__dataTuple) + listdata
        self.__bstree.clear()
        self.__bstree.addDataFromList(tmplist)
        self.__bstree.buildTree()
        self.__bstree.sortTree(asc=True)
        self.__dataTuple=self.__bstree.getSortedData()



    # addDataFromTuple(self,tupledata) adds tuple data into the set structure
    # Only the valid data types (int,float,str,bool) are added
    def addDataFromTuple(self,tupledata):
        try:
            if dataType(tupledata) != 'tuple':                
                raise ValueError("Error: Data argument is not a tuple.")
        except Exception as e: print(e); return None
        tmplist=list(self.__dataTuple) + list(tupledata)
        self.__bstree.clear()
        self.__bstree.addDataFromList(tmplist)
        self.__bstree.buildTree()
        self.__bstree.sortTree(asc=True)
        self.__dataTuple=self.__bstree.getSortedData()



    # deleteData(self,data) deletes the single data from the list if it is present
    def deleteData(self,data):
        try:
            if data==None:
                raise ValueError("Error: Data not given in deleteData().")
            if dataType(data) not in ['int','float','str','bool']:
                raise Exception("Error: Unsupported data type. Valid types are 'int','float','str','bool'.")
        except Exception as e: print(e); return None
        tmplist=list(self.__dataTuple)
        for i in range(len(tmplist)):
            if tmplist[i]==data:
                del(tmplist[i]); break
        self.__dataTuple=tuple(tmplist)



    # getSetData() returns sorted set data (in ascending order) in a tuple form
    def getSetData(self):
        return self.__dataTuple



    # isNull(self) returns True if it has no data
    def isNull(self):
        if len(self.__dataTuple)==0: return True
        else: return False



    # __len__(self) returns the number of unique data in the set
    def __len__(self):
        return len(self.__dataTuple)



    # __str__(self) stringifies set data when called by str(set)
    def __str__(self):
        if len(self.__dataTuple) == 0:
            return "<Set: size=0, data=()>"
        else:
            return "<Set: size="+str(len(self.__dataTuple))+", data="+str(self.__dataTuple)+">"



    # __repr__(self) prints data list when called by print(set)
    def __repr__(self):
        if len(self.__dataTuple) == 0:
            return "<Set: size=0, data=()>"
        else:
            return "<Set: size="+str(len(self.__dataTuple))+", data="+str(self.__dataTuple)+">"



    # copy(self) returns a copy of the current set instance
    def copy(self):
        newset=self.__class__()
        newset.addDataFromTuple(self.__dataTuple)
        return newset



    # clear(self) removes all data from the set structure
    def clear(self):
        self.__dataTuple=()
        self.__bstree.clear()
        self.__preserve=True
        self.__fileaddr=""


    # ------------------------- disk I/O functions -----------------------

    # setDataFileAddress(self, directory=datadir, filename="set") sets 
    # the absolute address of the .pcds data file in the private variable __fileaddr
    def setDataFileAddress(self, directory=datadir, filename="set"):
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Error: Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Error: Data type of file name should be string.")            
        except TypeError as e: print(e); return None
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFile(directory, filename)
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: print(e); return None
        


    
    # getDataFileAddress(self) returns the absolute address of the .pcds data file
    def getDataFileAddress(self):
        if self.__fileaddr:
            return self.__fileaddr



 
    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted by 
    # removeDataFile() function.
    def setFilePreserve(self, preserve=True):
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Error: Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve




    # save(self, directory=datadir, filename="set", enc=True) saves all data 
    # in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    def save(self, directory=datadir, filename="set", enc=True):
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Error: Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Error: Data type of file name should be string.")
            if dataType(enc) != 'bool': 
                raise TypeError("Error: Data type of enc (encrypt) should be boolean.")
            if len(self.__dataTuple) == 0:
                raise Exception("There is no data to be saved.")
        except TypeError as e: print(e); return False
        # convert all the current data into string (Part 2)        
        s=""
        for data in self.__dataTuple:        
            s=s+u.data2str(data)+"\n" # '\n' is the data separator
        s=s[0:len(s)-1]     # the last '\n' is removed
        # adding file header (Part 3)        
        # adding file header (35 character (24+10+1)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='SET FILE HEADER:' + str(encrypt.randomInteger(10))
        # encrypt the data string (Part 4)
        if enc:            
            s=encrypt.encrypt(s,int(fileheader[25]))
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
        except Exception as e: print(e);  return False        
        # creating or opening .pds data file and writing to the file (Part 8)
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:
            fileaddr=u.createDataFile(directory, filename)
            fileaddr=os.path.abspath(fileaddr)
        except Exception as e:
            print(e); print("Error: Data file is not found or cannot be created."); return False
        fo=None
        try:
            fo=open(fileaddr,'wb')
            if not fo:
                print("Error: Data file cannot be opened. Saving is failed.")
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
    def loadDataFromFile(self, fileaddr=datadir+os.sep+"set.pcds"):
        # checking inputs (Part 1)        
        if not u.checkDataFileAddr(fileaddr): return False           
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
                return None
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
            print("Error: File has no data. Loading is failed.")
            return False
        fileMD5=s[4:36]
        hdstr=s[37:len(s)] # hdstr=header+data string
        newMD5=u.getHashCode(hdstr,"md5")        
        try:            
            if newMD5 != fileMD5:
                raise Exception("Error: Data file is corrupt as hash missmatch. Loading is failed.")
        except Exception as e: print(e); return False
        s=hdstr
        # decrypting the data string into readable string(Part 7)         
        try:
            # In the File Header, the last character is the keyid
            # Length of File Header = 26 (16 char+10 digits+'\n')
            if len(s) < 26:
                print("Error: File has no data. Loading is failed")
                return False
            if s[0:16] == 'SET FILE HEADER:':
                keyid=int(s[25])
                s=s[27:]  # leave the header part 
                if encrypted:                                 
                    s=encrypt.decrypt(s,keyid)
            else: raise Exception("Error: Data file is corrupt.")
        except Exception as e: print(e); return False
        # loading data into the binary search tree (Part 8)        
        sl=s.split('\n') # sl=string list        
        try:
            self.__dataTuple=()
            tmplist=[]
            for strdata in sl:                
                tmplist.append(u.str2data(strdata))
            self.__dataTuple=tuple(tmplist)
        except Exception as e: 
            print(e); print("Error: Data loading failed."); return False
        print("Data Loaded Successfully from '"+self.__fileaddr+"'.")
        # Post loading work
        self.__bstree.clear()
        self.__bstree.addDataFromTuple(self.__dataTuple)
        self.__bstree.buildTree()
        self.__bstree.sortTree()
        return True



    # removeDataFile(self) deletes the data file when the preserve parameter is False.
    # If preserve is True, the data file will not be deleted    
    def removeDataFile(self):        
        if not self.__preserve:
            try:            
                os.remove(self.__fileaddr); return True
            except Exception as e: print(e); return False
        else:            
            print("Set data file is preserved and cannot be deleted.")
            return False


# --------------------------- Set Operation Methods -------------------------------
    # isEqual(self,set2) returns true if two sets are identical
    def isEqual(self,set2):
        if self.__class__ != type(set2):
            return False
        # length check
        temptuple=set2.getSetData()
        if len(self.__dataTuple) != len(temptuple): return False
        # individual data check
        else:
            i=0
            for data in self.__dataTuple:
                if data != temptuple[i]: return False
                i=i+1
        return True


    # __eq__(self,right) returns True if right argument is a set and is same as the 
    # current set instance. Equal sets are identical. (A==B, A==10, A==[10])
    def __eq__(self,right):        
        return self.isEqual(right)


    # __req__(self,left) returns True if left argument is a set and is same as the 
    # current set instance. Equal sets are identical. (B==A, 10==A, [10]==A)
    def __req__(self,left):
        return self.isEqual(left)




    # __neq__(self,right) returns True if right argument is neither a set nor equal
    # to the current set instance. Equal sets are identical. (A!=B, A!=10, A!=[10])
    def __neq__(self,right):
        if self.__eq__(right): return False
        return True


    # __rneq__(self,left) returns True if left argument is neither a set nor equal
    # to the current set instance. Equal sets are identical. (B!=A, 10!=A, [10]!=A)
    def __rneq__(self,left):
        if self.__eq__(left): return False
        return True





    # union(self,set2) joins two sets to a new one ignoring the reduntant data (AUB)
    def union(self,set2):
        try:
            if self.__class__ != type(set2):
                raise TypeError("Error: Argument is not a set data structure.")
        except TypeError as e: print(e); return None
        newset=self.__class__()
        if self.isNull():
            newset=set2.copy()
        elif set2.isNull():
            newset=self.copy()
        elif self.__eq__(set2):
            newset=self.copy()
        else:
            tmplist=list(self.__dataTuple)
            tmplist=tmplist+list(set2.getSetData())
            newset.addDataFromList(tmplist)
        return newset


    # __add__(self,right) returns the result set after union operation (A+B)
    def __add__(self,right):
        return self.union(right)


    # __radd__(self,left) returns the result set after union operation (B+A)
    def __radd__(self,left):
        return self.union(left)



    # intersection(self,set2) returns a new set with only the common data
    def intersection(self,set2):
        try:
            if self.__class__ != type(set2):
                raise TypeError("Error: Argument is not a set data structure.")
        except TypeError as e: print(e); return None
        if self.isNull() or set2.isNull():
            return self.__class__()    # null set, same as Set()
        temptuple=set2.getSetData()
        tmplist=[]
        # searching set2 data in the current set
        self.__bstree.clear()
        self.__bstree.addDataFromTuple(self.__dataTuple)
        self.__bstree.buildTree() 
        for i in range(len(temptuple)):
            sresult=self.__bstree.searchTree(temptuple[i])
            if sresult != None:
                tmplist.append(temptuple[i])
        newset=Set()
        if len(tmplist)==0: return self.__class__()    # null set, same as Set()
        newset.addDataFromList(tmplist)
        return newset


    # __xor__(self,right) returns the common data of two sets (A^B)
    # It is alias as intersection() operation
    def __xor__(self,right):
        return self.intersection(right)


    # __rxor__(self,left) returns the common data of two sets (B^A)
    # It is alias as intersection() operation
    def __xor__(self,left):
        return self.intersection(left)




    # subtract(self,set2) subtracts set2 from the current set instance (A-B)
    def subtract(self,set2):
        try:
            if self.__class__ != type(set2):
                raise TypeError("Error: Argument is not a set data structure.")
        except TypeError as e: print(e); return None        
        if set2.isNull():
            return self.copy()
        elif self.isNull():
            return set2.copy()
        if self.isEqual(set2): return Set() # null set
        temptuple=set2.getSetData()
        commondata=[]
        # searching set2 data in the current set
        self.__bstree.clear()
        self.__bstree.addDataFromTuple(self.__dataTuple)
        self.__bstree.buildTree() 
        for i in range(len(temptuple)):
            sresult=self.__bstree.searchTree(temptuple[i])
            if sresult != None:
                commondata.append(temptuple[i])
        if len(commondata)==0: return self.copy()
        tmplist=[]        
        for data in self.__dataTuple:
            if data not in commondata: 
                tmplist.append(data)
        if tmplist==[]: return Set()
        newset=Set()                
        newset.addDataFromList(tmplist)
        return newset


    # difference(self,set2) removes the comman data from the current set(A-B)
    def difference(self,set2):
        return self.subtract(set2)


    #  __sub__(self,set2) removes the comman data from the current set(A-B)
    def __sub__(self,right):
        return self.subtract(right)


    # difference(self,left) removes the comman data from the current set(B-A)
    def __rsub__(self,left):
        try:
            if self.__class__ != type(left):
                raise TypeError("Error: Argument is not a set data structure.")
        except TypeError as e: print(e); return None
        if left.isNull():
            return self.copy()
        elif self.isNull():
            return left.copy()
        commondata=self.intersection(left)
        if len(commondata)==0: return left.copy()
        tmplist=[]
        for data in left.getSetData():
            if data not in commondata: 
                tmplist.append(data)
        newset=Set()                
        newset.addDataFromList(tmplist)
        return newset




    # isDisjoint(self,set2) returns True if two sets do not have any common data
    def isDisjoint(self,set2):
        commonset=self.intersection(set2)
        if commonset == Set(): return True
        return False




    # isSuperset(self,set2) returns True if the current set is a superset of set2
    # or set2 is a subset of the current set
    def isSuperset(self,set2):
        commonset=self.intersection(set2)
        if commonset == set2: return True
        return False




    # isSubset(self,set2) returns True if set2 is completely within the current set
    # which means set2 is a subset of the current set
    def isSubset(self,set2):
        commonset=self.intersection(set2)
        if self.isEqual(commonset): return True
        return False







# ------------------------- End of Set Class -----------------------------


