'''
Package name: pcds (python common data structures)
Version: 1.1.0
Author: A K M Aminul Islam
Author_Email: aminul71bd@gmail.com
Company: Newtonia
Last Modified: Wednesday August 07 2024 8:00 PM 
Description: This package creates and manages the python's common data structures
Supported Data Structures: Queue, Priority Queue, Stack, Singly Linked List, 
    Doubly Linked List, Circular Linked List, Binary Search Tree, Set
Supported Data Types: int,float,str,bool,NoneType,list,tuple,dictionary
Coding Style: Camel Case
Module Versions: utilities(1.6.8), encrypt(1.0.2), queue(1.1.4), pqueue(1.0.1), 
    stack(1.2.3), linkedList(1.2.4), dlinkedList(1.2.5), clinkedList(1.0.1), 
    bstree(1.1.2), set(1.0.0)
Dependencies: os, hashlib, datetime, random, upmath
'''

__version__="1.1.0"
version=__version__
def getVersion():
    return __version__



import os
import hashlib
# from pcds import *
__all__=["queue","pqueue","stack","linkedlist","dlinkedlist","clinkedlist","bstree","set"]





# packageInfo() returns the basic information of this package named ntnds
def packageInfo():
    s=" Package Name:'pcds (python common data structures)'\n"
    s=s+" Package Version:'1.1.0'\n"
    s=s+" Author:'A K M Aminul Islam'\n"
    s=s+" Author_Email:'aminul71bd@gmail.com'\n"
    s=s+" Company:'Newtonia'\n"
    s=s+" Last Update:'Wednesday August 07 2024'\n"
    s=s+" Description:'This python package creates and manages the common data structures\n"
    s=s+" \tlike queue, priority queue, stack, singly linkedlist, doubly linked list,\n"
    s=s+" \t circular linkedlist, binary tree, set etc."
    s=s+"\n\tSupported Data Types: int, float, str, bool, NoneType, list, tuple, dictionary.'"
    print(s)





# packageInfoDict is a dictionary data structure containing the md5hashes of the 
# code modules 
__packageInfoDict={"version":"1.1.0","name":"pcds","md5hashes": 
    {"utilities":"b11d7571a88709bec9c4779247f7cb0e",
"encrypt":"a3d1f295a11fe469953a58431e8d3f34",
"queue":"af53f9da8a1a12c6862f53d138aa0803",
"pqueue":"f05ef3e0f624ae44b46ebc32e2eefe89",
"stack":"081552f2882515ef7f577fef47d189dc",
"linkedlist":"22ee86368e0564aee31a10fc9843ba30",
"dlinkedlist":"a7e057a0fca33fc49da0466c5137832d",
"clinkedlist":"e0a214c395f74a1d2c9b5758cafd7bbe",
"bstree":"b3ba1447f7ae3c07903870329d51a674",
"set":"cb6b7b9aeb128ba1751e36edf92d9550"
    }
}






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






# ---------------- data file directory and conf file ---------------------
# packageDir is the directory path that contains the package file __init__.py
# packageFile=__file__
packageDir=os.path.dirname(__file__)


# create conf file directory ()
__confDir=packageDir+os.sep+"conf"
if not os.path.exists(__confDir):
    os.makedirs(__confDir)




# get users home directory
homeDir=os.path.expanduser('~')


# create the default data directory in the users home directory
__dataDirectory=homeDir+os.sep+"pcds_data"
if not os.path.exists(__dataDirectory):
    os.makedirs(__dataDirectory)



# createCONFfile() creates pcds.conf file in the __confDir
def createCONFfile():
    global __dataDirectory
    global __confDir
    confFileAddr=__confDir+os.sep+'pcds.conf'
    if os.path.isfile(confFileAddr): return None  
    # conf file content
    s='PackageName="pcds"\n'
    s=s+'Version="'+__version__+'"\n'
    s=s+'Author="A K M Aminul Islam"\n'
    s=s+'AuthorEmail="aminul71bd@gmail.com"\n'
    s=s+'DataFileAddress="'+__dataDirectory+'"\n'
    s=s+'Description="This module contains python data structures like queue, stack, linked list, binary tree, set etc."\n'
    # creating .conf file and writing into it    
    try:
        if not os.path.exists(confFileAddr):
            fo=open(confFileAddr,'w')
            fo.write(s)
            fo.close()
            print("pcds.conf file is created.")
    except Exception as e: print(e); return None





# changeDataDirectory() changes the default data directory to a new directory
def changeDataDirectory(directory=""):
    try:
        # checking inputs            
        if dataType(directory) != 'str': 
            raise TypeError("Directory should be a string type data.")        
    except TypeError as e: print(e); return None
    directory=directory.strip()
    global __dataDirectory
    if __dataDirectory == directory: return None   
    try:        
        if directory=="" or directory=="pcds_data":            
            directory=__dataDirectory            
        else:
            if not os.path.isdir(directory):
                os.makedirs(directory)
            if os.path.basename(directory) != "pcds_data":
                directory=directory+os.sep+"pcds_data";
                os.makedirs(directory)  
    except Exception as e: print(e); return None    
    __dataDirectory=os.path.abspath(directory)
    saveDataDirectoryAddr()




# getDataDirectory() returns the default data directory set by the user
def getDataDirectory():
    global __dataDirectory
    if os.path.isdir(__dataDirectory):
        return __dataDirectory




# saveDataDirectoryAddr() saves the data file address in the text file 'pcds.conf'
def saveDataDirectoryAddr():
    global __confDir
    global __dataDirectory
    confFile=__confDir+os.sep+"pcds.conf"
    if os.path.isfile(confFile):
        isdatadirset=False
        s='DataFileAddress="'+__dataDirectory+'"\n'
        try:
            fo=open(confFile,'r+')
            linestr=fo.readline()
            # file pointer at the beginning of the second line
            linelength=len(linestr)
            while linestr:                
                if "DataFileAddress" in linestr:
                    # file pointer at the beginning of the next line
                    n=fo.tell()
                    remainingtext=fo.read()
                    fo.seek(n-linelength-1,0)
                    totalstr=s+remainingtext
                    fo.write(totalstr);
                    if len(s) < linelength:
                        fo.write((linelength-len(s))*'\0')
                    isdatadirset=True; break
                linestr=fo.readline()                
                linelength=len(linestr)
            fo.close()
        except Exception as e: print(e); return None
        if not isdatadirset:
            fo=open(confFile,'a'); fo.write(s); fo.close()




# readDataDirectoryAddr() reads data file address from 'pcds.conf' file
def readDataDirectoryAddr():
    global __confDir
    global __dataDirectory
    confFile=__confDir+os.sep+"pcds.conf"
    datadir="";
    if os.path.isfile(confFile):        
        fo=open(confFile,'r')
        linestr=fo.readline()
        while linestr:            
            if "DataFileAddress" in linestr:                
                datadir=linestr.split('"')[1] 
                break
            linestr=fo.readline()
        fo.close()
    if os.path.isdir(datadir):
        __dataDirectory=datadir #[1:len(datadir)-1]   # removing ', ', and \n

    



# create configuration file
confFileAddr=__confDir+os.sep+"pcds.conf"
if not os.path.isfile(confFileAddr): 
    createCONFfile()
else:
    readDataDirectoryAddr()










# ------------------- checking package integrity ------------------------
# getHashCode(datastr, algorithm="md5") creates the popular hashcode of the
# items of the following data types:
#   str, filestr, buffer_reader, int, float, bool, NoneType
# Supported Common Hash Algorithm: md5, sha1, sha256, sha512
# >>> pcds.getHashCode("hello world")
# '5eb63bbbe01eeed093cb22bb8f5acdc3'
# >>> pcds.getHashCode("hello world",'sha1')
# '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
# >>> pcds.getHashCode("hello world",'sha256')
# 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
# >>> pcds.getHashCode("hello world",'sha512')
#'309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
# >>>
# >>> pcds.getHashCode(12345)
# '827ccb0eea8a706c4c34a16891f84e7b'
# >>> pcds.getHashCode(1234.5)
# '3c80e9adacfdeab38845f2790aca3294'
# >>> pcds.getHashCode(True)
# 'f827cf462f62848df37c5e1e94a4da74'
# >>> pcds.getHashCode(False)
# 'f8320b26d30ab433c5a54546d21f414c'
# >>>
# >>> filestr='md5sums.txt'
# >>> fo=open(filestr,'rb')
# >>> pcds.getHashCode(fo)
# '0fb9cbc05d937fff428f7de759eb0021'
# >>> fo.close()
# >>> pcds.getHashCode(filestr)
# '0fb9cbc05d937fff428f7de759eb0021'
# >>>
def getHashCode(datastr, algorithm="md5"):
    buffreader=False; isfile=False; fileaddr=""; fo=None
    try:
        # checking inputs 
        if dataType(datastr) in ['int','float','bool','NoneType']:
            datastr=str(datastr)           
        elif dataType(datastr) == '_io.BufferedReader' and datastr: 
            buffreader=True; fo=datastr
        elif dataType(datastr) == 'str': 
            datastr=datastr.strip()
            if os.path.isfile(datastr):
                isfile=True; fileaddr=datastr
        else: raise TypeError("Unsupported data type to create hash code.")        
        if dataType(algorithm) != 'str': 
            raise TypeError("'algorithm' is a string type argument.")
        algorithm=algorithm.strip()
        if algorithm.upper() not in ['MD5','SHA1','SHA256','SHA512']: 
            raise ValueError("'algorithm' value must be in ['md5','sha1','sha256','sha512'].")
    except TypeError as e: print(e); return None              
    except ValueError as e: print(e); return None
    ba=None     # ba=bytearray
    if buffreader:
        try:            
            ba=fo.read()            
        except Exception as e: print(e); return None
    elif isfile:
        fo=open(fileaddr,'rb')
        ba=fo.read()
        fo.close()
    else:
        ba=datastr.encode('utf-8')
    result=None
    if algorithm.upper() == 'MD5':
        result=hashlib.md5(ba)
    elif algorithm.upper() == 'SHA1':
        result=hashlib.sha1(ba)
    elif algorithm.upper() == 'SHA256':
        result=hashlib.sha256(ba)
    elif algorithm.upper() == 'SHA512':
        result=hashlib.sha512(ba)
    return result.hexdigest()




# isPackageIntact() checks the integrity of the module files and returns true
# if all the modules are okay
def isPackageIntact():
    okay=True
    if not os.path.isfile(packageDir+os.sep+"utilities.py"):
        print("'utilities' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"utilities.py") != __packageInfoDict["md5hashes"]["utilities"]:
        print("'utilities' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"encrypt.py"):
        print("'encrypt' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"encrypt.py") != __packageInfoDict["md5hashes"]["encrypt"]:
        print("'encrypt' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"queue.py"):
        print("'queue' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"queue.py") != __packageInfoDict["md5hashes"]["queue"]:
        print("'queue' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"pqueue.py"):
        print("'pqueue' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"pqueue.py") != __packageInfoDict["md5hashes"]["pqueue"]:
        print("'pqueue' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"stack.py"):
        print("'stack' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"stack.py") != __packageInfoDict["md5hashes"]["stack"]:
        print("'stack' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"linkedlist.py"):
        print("'linkedList' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"linkedlist.py") != __packageInfoDict["md5hashes"]["linkedlist"]:
        print("'linkedList' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"dlinkedlist.py"):
        print("'dlinkedList' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"dlinkedlist.py") != __packageInfoDict["md5hashes"]["dlinkedlist"]:
        print("'dlinkedList' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"clinkedlist.py"):
        print("'clinkedlist' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"clinkedlist.py") != __packageInfoDict["md5hashes"]["clinkedlist"]:
        print("'clinkedlist' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"bstree.py"):
        print("'bstree' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"bstree.py") != __packageInfoDict["md5hashes"]["bstree"]:
        print("'bstree' module is altered."); okay=False

    if not os.path.isfile(packageDir+os.sep+"set.py"):
        print("'set' module file is missing."); okay=False
    if getHashCode(packageDir+os.sep+"set.py") != __packageInfoDict["md5hashes"]["set"]:
        print("'set' module is altered."); okay=False

    return okay



if not isPackageIntact():
    print("Package Integrity is failed. App is going to be stopped.")
    import sys
    sys.exit()
