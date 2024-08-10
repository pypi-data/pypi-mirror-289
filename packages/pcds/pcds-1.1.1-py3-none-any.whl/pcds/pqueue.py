'''
Module Description
--------------------
module filename: pqueue.py (Priority Queue)
module name: pqueue (Priority Queue)
Content: dataType() function, PQueue class
Description: PQueue class creates a priority queue data structure. Priority value
    varies from 0 to 99. Greater the value, greater the priority.

    PQueue class public properties and methods
    -----------------------------------------
    PQueue(maxsize), getSize(), getMaxSize(), setMaxSize(), getDataString(),
    __len__(), __str__(), 
    __repr__(), __del__(), enQueue(data), deQueue(), clear(),  
    
    setFileAddress(directory="data", filename="pqueue"), getFileAddress(),
    setFilePreserve(preserve=True), isFilePreserved(), removeDataFile(),
    save(directory="data", filename="pqueue", enc=True), 
    loadDataFile(fileaddr=packroot+"os.sep"+"pcds_data"+os.sep+"pqueue.pcds"),
  
    Suported Data Types: int, float, str, bool, NoneType, tuple, list, dictionary

    Data are saved in a binary file with extension .pcds (python common data structure)

Author: A K M Aminul Islam
Email: aminul71bd@gmail.com

Last Modified: Wednesday August 07 2024 7:00 PM

Version:1.0.1

Dependencies: utilities, encrypt, os
'''
from pcds import utilities as u
from pcds import encrypt
import os



version='1.0.1'
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





# PQueue (Priority Queue) class creates an instance of a queue datastructure
#
class PQueue:
	
    __datalist=None # a private list holding data of the queue
    __maxsize=None  # Maximum size of the queue. If length > size, data dequeued
    __maxpriority=100 # holds the maximum priority value of the data to be set
    __minpriority=0 # holds the minimum priority value of the data to be set
    __size=None     # holds the current length of the queue (read only)
    __fileaddr=None # string holds the data file path with name
    __preserve=True # data file cannot be deleted unless __preserve is False


    # constructor function	
    def __init__(self, maxsize=100):
        try:
            # checking inputs
            if dataType(maxsize) != 'int': 
                raise TypeError("Error: Maxsize must be an integer data.")
            if maxsize < 1: 
                raise ValueError("Error: Maxsize must be a positive whole number.")
        except Exception as e: print(e); return None
        self.__maxsize=maxsize
        self.__datalist=[]
        self.__size=0        
  

    # -------------------------- setter and getter methods --------------------------
    # getSize(self) returns the current size (number of data) of the priority queue
    def getSize(self):
        if self.__maxsize==None: return None
        return self.__size




    # getMaxSize(self) returns the maximum size of the queue
    def getMaxSize(self):
        if self.__maxsize==None: return None
        return self.__maxsize




    # getMaxPriority(self) returns the maximum priority value to be set
    def getMaxPriority(self):
        return self.__maxpriority




    # getMinPriority(self) returns the minimum priority value to be set
    def getMinPriority(self):
        return self.__minpriority




    # changeMaxSize(self) changes the current maximum size of the queue
    # to the new given size
    def changeMaxSize(self, maxsize=100):
        try:
            # checking inputs
            if dataType(maxsize) != 'int': 
                raise TypeError("Error: Maxsize must be an integer data.")
            if maxsize < 1: 
                raise ValueError("Error: Maxsize must be a positive whole number..")
            if maxsize < self.__size:
                raise ValueError("Warning! The length of the queue cannot be less than the current size.")
        except Exception as e: print(e); return None
        self.__maxsize=maxsize



    
    # getDataString(self) shows current data in the queue in tuple-string form
    # problem: tuple([1])=(1,), but tuple([1,2])=(1,2)
    def getDataString(self):
        if self.__maxsize==None: return None
        if len(self.__datalist)==1: return "("+str(self.__datalist[0])+")"
        return str(tuple(self.__datalist))




   # __len__(self) returns the number of data in the queue
    def __len__(self):
        if self.__maxsize==None: return None
        return self.__size




    # __str__(self) returns a string of the queue instance with data
    def __str__(self):
        if self.__maxsize:
            return "<PriorityQueue ["+str(self.getSize())+"/"+str(self.getMaxSize())+"], Head:" + self.getDataString() + ":Tail>"
        else: return ""




    # __repr__(self) returns queue data in printable form
    def __repr__(self):        
        return self.__str__()



    # -------------------- main functions of the queue ----------------------
    # enQueue() function stores data in the queue according to its priority.
    # Greater the priority, closer the position to the head. The head data
    # has the highest priority. If queue becomes full, the head data is returned.
    def enQueue(self,data,priority=0):
        if self.__maxsize==None: return None
        try:
            if dataType(data) not in ['str','int','float','bool','NoneType','tuple','list','dict']:
                raise Exception("Error: Queue does not support the datatype given here.")
            if priority<self.__minpriority or priority>self.__maxpriority:
                raise Exception("Error: priority value must be between" + str(self.__minpriority) + " and "+ str(self.__minpriority) +".")
        except Exception as e: print(e); return None
        datadict={'data':data,'priority':priority}
        datainserted=False
        if self.__size==0: self.__datalist.append(datadict)
        #elif self.__size==1:
        #    if priority > self.__datalist[0]['priority']:
        #        self.__datalist.insert(0,datadict)
        #    else: self.__datalist.append(datadict)
        #elif self.__size > 1:
        else:
            for i in range(self.__size):
                if priority > self.__datalist[i]['priority']:
                    self.__datalist.insert(i,datadict); datainserted=True; break
            if not datainserted: self.__datalist.append(datadict)
        self.__size = self.__size + 1       
        if self.__size > self.__maxsize:
            print("Priority queue is full. So, head is dequeued.")
            return self.deQueue()




	
    # deQueue() function removes data from the head of the priority queue
    def deQueue(self):
        if self.__maxsize==None: return None
        if self.__size > 0:            
            head=self.__datalist[0]['data']
            del(self.__datalist[0])
            self.__size = self.__size - 1        
            return head
        else:
            print("Priority queue is empty.") 
            return None
            



    # clear() function removes all data from the queue
    def clear(self):
        if self.__maxsize==None: return None
        self.__init__(self.__maxsize)




    # copy() method copies the priority queue data structure to a new instance
    def copy(self):
        newstack=PQueue(self.__maxsize)
        for data in self.__datalist:
            newstack.__datalist.append(u.copy(data))
        newstack.__size=self.__size
        return newstack



# ------------------------- File I/O Operations -----------------------------
#
    # setFileAddress(self, directory="data", filename="pqueue") sets 
    # the absolute address of the .pcds data file in the private variable __fileaddr
    # But, the file is not created physically
    def setFileAddress(self, directory=datadir, filename="pqueue"):
        if self.__maxsize==None: return None
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Error: Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Error: Data type of file name should be string.")            
        except TypeError as e: print(e); return None
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFileAddr(directory, filename)
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: print(e); return None




    # getDataFile(self) returns the absolute address of the .pdsf data file
    def getFileAddress(self):
        if self.__fileaddr:
            if self.__maxsize==None: return None
            return self.__fileaddr




    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        if self.__maxsize==None: return None
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted by 
    # removeDataFile() function
    def setFilePreserve(self, preserve=True):
        if self.__maxsize==None: return None
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Error: Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve




    # delete(self) deletes the data file. If preserve is True, the
    # data file will not be deleted    
    def removeDataFile(self):
        if self.__maxsize==None: return None
        if not self.__preserve:
            try: 
                if os.path.exists(self.__fileaddr) and os.path.isfile(self.__fileaddr):
                    os.remove(self.__fileaddr)
                    self.__fileaddr=None
                    return True
                else:
                    raise Exception("Priority queue data file does not exist.")
            except Exception as e: print(e); return False
        else:            
            print("Priority queue data file is preserved and cannot be deleted.")
            return False
         



    # save() saves all data in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    # >>>
    # >>> pq1=pq.PQueue(8)
    # >>> pq1.enQueue(40,5)
    # >>> pq1.enQueue(50,7)
    # >>> pq1.enQueue('ab',10)
    # >>> pq1.enQueue('hello',90)
    # >>> pq1.enQueue('ali',0)
    # >>> pq1.enQueue('khan',20)
    # >>> pq1.enQueue(10,2)
    # >>> pq1.enQueue('amin',1)
    # >>> pq1.enQueue('audry',50)
    # >>> pq1.enQueue('x',20)
    # >>> pq1.enQueue('y',50)
    # >>> pq1.enQueue('z',20)
    # >>>
    # >>> pq1
    # <PriorityQueue [12/100], Head:({'data': 'hello', 'priority': 90}, {'data': 'audry', 'priority': 50}, {'data': 'y', 'priority': 50}, {'data': 'khan', 'priority': 20}, {'data': 'x', 'priority': 20}, {'data': 'z', 'priority': 20}, {'data': 'ab', 'priority': 10}, {'data': 50, 'priority': 7}, {'data': 40, 'priority': 5}, {'data': 10, 'priority': 2}, {'data': 'amin', 'priority': 1}, {'data': 'ali', 'priority': 0}):Tail>
    # >>>
    # >>> pq1.save(enc=False,filename='pqueue2')
    # Plain Data Saved Successfully into 'C:\Users\admin\pcds_data\pqueue2.pcds'
    # True
    # >>>
    # >>> pq1.save()
    # Encrypted Data Saved Successfully into 'C:\Users\admin\pcds_data\pqueue.pcds'
    # True
    # >>> 
    def save(self, directory=datadir, filename="pqueue", enc=True):
        if self.__maxsize==None: return None
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Error: Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Error: Data type of file name should be string.")
            if dataType(enc) != 'bool': 
                raise TypeError("Error: Data type of enc (encrypt) should be boolean.")
        except TypeError as e: print(e); return False                       
        # convert all the current data into string (Part 2)        
        s="";i=0
        for item in self.__datalist:
            if i<self.__size-1:
                s=s+u.data2str(item)+"\n" # '\n' is the data separator
            else: 
                s=s+u.data2str(item) # '\n' not present
        # adding file header (Part 3)        
        # adding file header (29 character (19+10)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='PQUEUE FILE HEADER:' + str(encrypt.randomInteger(10))
        # encrypt the data string (Part 4)
        if enc:            
            s=encrypt.encrypt(s,int(fileheader[28]))
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
        # creating or opening .pdsf data file and writing to the file (Part 8)
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFile(directory, filename)            
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: 
            print(e); print("Error: List data are not saved."); return False
        fo=None
        try:
            fo=open(self.__fileaddr,'wb')
            if not fo:
                print("Error: Data file cannot be opened. Saving operation is failed.")
                self.__fileaddr=""
                return False
            fo.write(ba)
            fo.close()
            self.__fileaddr=fileaddr        
        except Exception as e: print(e); return False
        if enc:
            print("Encrypted Data Saved Successfully into '"+self.__fileaddr+"'")
        else:
            print("Plain Data Saved Successfully into '"+self.__fileaddr+"'")
        return True




    # loadDataFromFile() function loads pqueue data in memory from the data file
    # File loading also occurs in 8 steps, but in reverse order of file saving
    # 8 steps: (1) checking inputs (2) reading the binary data file 
    # (3) decoding the data file with utf-8 (4) check the file encryption tag
    # (5) first phase decryption using keyid=10 (6) checking MD5 hash
    # (7) removing file header (8) loading string data into a list after conversion
    # >>>
    # >>> pq1.loadDataFromFile('C:\\Users\\admin\\pcds_data\\pqueue2.pcds')
    # Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\pqueue2.pcds'
    # True
    # >>>
    # >>> pq1
    # <PriorityQueue [0/100], Head:():Tail>
    # >>> 
    # >>> pq1.loadDataFromFile('C:\\Users\\admin\\pcds_data\\pqueue2.pcds')
    # Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\pqueue2.pcds'
    # True
    # >>>
    # >>> pq1
    # <PriorityQueue [12/100], Head:('data":"hello","priority":90', {'data': 'audry', 'priority': 50}, {'data': 'y', 'priority': 50}, {'data': 'khan', 'priority': 20}, {'data': 'x', 'priority': 20}, {'data': 'z', 'priority': 20}, {'data': 'ab', 'priority': 10}, {'data': 50, 'priority': 7}, {'data': 40, 'priority': 5}, {'data': 10, 'priority': 2}, {'data': 'amin', 'priority': 1}, {'data': 'ali', 'priority': 0}):Tail>
    # >>>
    def loadDataFromFile(self, fileaddr=datadir+os.sep+"pqueue.pcds"):
        if self.__maxsize==None: return False
        # checking inputs (Part 1)
        if not u.checkDataFileAddr(fileaddr):
            return False
        # opening the binary data file to read data (Part 2)
        self.__fileaddr=os.path.abspath(fileaddr)        
        fo=None; s=""; bs=""        
        try:
            fo=open(self.__fileaddr,'rb')
            # if file is blank
            fo.seek(0,2)
            filesize=fo.tell()
            if filesize==0:
                print("Data File is empty")                    
                return False            
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
            print("File has no data. Loading is stopped.")
            return False
        fileMD5=s[4:36]
        hdstr=s[37:len(s)] # hdstr=header+data string
        newMD5=u.getHashCode(hdstr,"md5")        
        try:            
            if newMD5 != fileMD5:
                raise Exception("Error: Data file is corrupt as hash missmatch. Loading is failed.")
        except Exception as e: print(e); return False
        s=hdstr
        # decrypting the encrypted data string into readable string(Part 7)
        try:
            # In the File Header, the last character is the keyid
            # Length of File Header = 29 (18 char+10 digits+'\n')
            if len(s) < 30:
                print("File has no data. Loading is failed")
                return False
            if s[0:19] == 'PQUEUE FILE HEADER:':
                keyid=int(s[28])
                s=s[31:]  # leave the header part
                if encrypted:
                    s=encrypt.decrypt(s,keyid)                
            else: raise Exception("Data file is corrupt as file header is missing.")
        except Exception as e: print(e); return False
        # loading data into the data list (Part 8)        
        sl=s.split('\n') # sl=string list 
        sl=sl[0:len(sl)-1] # removing the last empty part    
        try:
            self.clear() # removing data            
            i=0
            for sdata in sl:
                self.__datalist.append(u.str2data(sdata))                
                i=i+1 
            self.__size = i
            # set the maxsize to the next tens (if size=25, maxsize=30)
            if self.__maxsize < self.__size: self.__maxsize = 10*(1+self.__size//10)
        except Exception as e:
            print(e); print("Error: Data not loaded successfully."); return False
        print("Data Loaded Successfully from the file: '"+self.__fileaddr+"'")
        return True

# ---------------------------- END of PQueue Class -------------------------------





