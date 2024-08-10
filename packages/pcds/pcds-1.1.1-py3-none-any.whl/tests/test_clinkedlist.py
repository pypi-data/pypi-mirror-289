'''
Test Module: test_clinkedlist.py
Test Module Name: test_clinkedlist
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Friday August 09 2024 4:00 PM
Version:1.1.1
Python Version:3.12.4
'''

version="1.1.1"


import unittest
import os
from pcds import clinkedlist as clnkl



# testing Node class
class TestNode(unittest.TestCase):
    # testing the constructor of Node class
    # Node constructor requires data and index
    def test___init__(self):
        n1=clnkl.Node()
        n2=clnkl.Node(index=0)
        n3=clnkl.Node(data=10,index=0)
        n4=clnkl.Node('hello',4)
        self.assertEqual("<Head Node at index -1>",repr(n1))
        self.assertEqual("<Node: None at index 0>",repr(n2))
        self.assertEqual("<Node: 10 at index 0>",repr(n3)) 
        self.assertEqual("<Node: 'hello' at index 4>",repr(n4))
        self.assertIsNone(n4.next)
        self.assertIsNone(n4.prev)      


    # testing setData(), getData() method
    def test_setData(self):
        n1=clnkl.Node(index=1)
        n1.setData('hello')
        self.assertEqual('hello',n1.getData())
        n1.setData(12.48)
        self.assertEqual(12.48,n1.getData())
        n1.setData(True)
        self.assertEqual(True,n1.getData())
        n1.setData([1,2,3])
        self.assertEqual([1,2,3],n1.getData())


    # testing setIndex(), getIndex() method
    def test_setIndex(self):
        n1=clnkl.Node()
        n1.setIndex(5)
        self.assertEqual(5,n1.getIndex())
        self.assertEqual(None,n1.setIndex(5.5))


    # testing __str__(), __repr__() method
    def test_str_repr(self):
        n1=clnkl.Node('hello world',2)
        s="<Node: 'hello world' at index 2>"
        self.assertEqual(s,str(n1))
        self.assertEqual(s,repr(n1))


# testing CLinkedList class
class TestCLinkedList(unittest.TestCase):
    # testing the constructor of circular LinkedList class
    # CLinkedList constructor requires only a name, testing getHead(), getName()
    def test___init__(self):
        cll=clnkl.CLinkedList()
        s='<CLNKList[CLinkedList]: size=0, Data=()>'
        self.assertEqual(s,str(cll))
        cll2=clnkl.CLinkedList('myclinkedlist')
        s='<myclinkedlist[CLinkedList]: size=0, Data=()>'
        self.assertEqual(s,str(cll2))
        self.assertEqual('<Head Node at index -1>',str(cll2.getHead()))
        self.assertEqual('myclinkedlist',cll2.getName())



    # testing getCurrentIndex() method
    def test_getCurrentIndex(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertEqual(-1,cll.getCurrentIndex())
        cll.append("hello")
        cll.append(12.56)
        self.assertEqual(1,cll.getCurrentIndex())



    # testing tell() method which is as same as getCurrentIndex() method 
    def test_tell(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertEqual(-1,cll.tell())
        cll.append("hello")
        cll.append(12.56)
        self.assertEqual(1,cll.tell())



    # testing getCurrentNode() method 
    def test_getCurrentNode(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertEqual('<Head Node at index -1>',str(cll.getCurrentNode()))
        cll.append("hello")
        cll.append(12.56)
        self.assertEqual('<Node: 12.56 at index 1>',str(cll.getCurrentNode()))



    # testing getCurrentData() method 
    def test_getCurrentData(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertEqual('myclinkedlist',cll.getCurrentData())
        cll.append("hello")
        cll.append(12.56)
        self.assertEqual(12.56,cll.getCurrentData())



    # testing getSize() method 
    def test_getSize(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertEqual(0,cll.getSize())
        cll.append("hello")
        cll.append(12.56)
        self.assertEqual(2,cll.getSize())



    # testing append() method
    def test_append(self):
        n1=clnkl.Node(10,2)
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertIsNone(cll.append(n1))
        cll.append("hello")
        cll.append(12.56)
        self.assertEqual(2,cll.getSize())



    # testing addDataFromList() method
    def test_addDataFromList(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        cll.addDataFromList(l)
        s="<myclinkedlist[CLinkedList]: size=7, Data=(1, 3, 'hello', True, None, False, (7, 8, 9))>"
        self.assertEqual(s,str(cll))



    # testing addDataFromTuple() method
    def test_addDataFromTuple(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        t=(1,3,'hello',True,None,False,[7,8,9])
        cll.addDataFromTuple(t)
        s="<myclinkedlist[CLinkedList]: size=7, Data=(1, 3, 'hello', True, None, False, [7, 8, 9])>"
        self.assertEqual(s,str(cll))



    # testing moveNext(), moveLast(), movePrev(), moveFirst(), moveToHead() methods
    def test_move(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        cll.addDataFromList(l)
        self.assertEqual(6,cll.tell())
        self.assertEqual((7,8,9),cll.getCurrentData())
        cll.moveFirst()
        self.assertEqual(0,cll.tell())
        self.assertEqual(1,cll.getCurrentData())
        cll.moveNext()
        self.assertEqual(1,cll.tell())
        self.assertEqual(3,cll.getCurrentData())
        cll.moveNext()
        self.assertEqual(2,cll.tell())
        self.assertEqual('hello',cll.getCurrentData())
        cll.moveNext()
        self.assertEqual(True,cll.getCurrentData())
        cll.moveLast()
        self.assertEqual(6,cll.tell())
        self.assertEqual((7,8,9),cll.getCurrentData())
        cll.movePrev()
        self.assertEqual(5,cll.tell())
        self.assertEqual(False,cll.getCurrentData())
        cll.movePrev()
        self.assertEqual(4,cll.tell())
        self.assertEqual(None,cll.getCurrentData())
        cll.moveToHead()
        self.assertEqual(-1,cll.tell())
        self.assertEqual('myclinkedlist',cll.getCurrentData())



    # testing seek(offset,ref) method
    def test_seek(self): 
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        cll.addDataFromList(l)
        self.assertIsNone(cll.seek(2.5))
        self.assertIsNone(cll.seek('0'))       
        cll.seek(0,0)
        self.assertEqual(0,cll.tell())
        self.assertEqual(1,cll.getCurrentData())
        cll.seek(1,0)
        self.assertEqual(1,cll.tell())
        self.assertEqual(3,cll.getCurrentData())
        cll.seek(1,1)
        self.assertEqual(2,cll.tell())
        self.assertEqual('hello',cll.getCurrentData())
        cll.seek(1,1)
        self.assertEqual(3,cll.tell())
        self.assertEqual(True,cll.getCurrentData())
        cll.seek(1,1)
        self.assertEqual(4,cll.tell())
        self.assertEqual(None,cll.getCurrentData())
        cll.seek(-1,1)
        self.assertEqual(3,cll.tell())
        self.assertEqual(True,cll.getCurrentData())
        cll.seek(0,2)
        self.assertEqual(6,cll.tell())
        self.assertEqual((7,8,9),cll.getCurrentData())
        cll.seek(-1,2)
        self.assertEqual(5,cll.tell())
        self.assertEqual(False,cll.getCurrentData())
        cll.seek(-2,2)
        self.assertEqual(4,cll.tell())
        self.assertEqual(None,cll.getCurrentData())
        # seek() can move to head
        cll.seek(-1,0)
        self.assertEqual(6,cll.tell())
        self.assertEqual((7,8,9),cll.getCurrentData())
        cll.seek(-2,0)
        self.assertEqual(5,cll.tell())



    # testing getAllData() method
    def test_getAllData(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)
        t=(1, 3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,cll.getAllData())



    # testing convert2dict() method
    def test_convert2dict(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)
        d={'name':'myclinkedlist','class':'CLinkedList','size':7,0:1,1:3,2:'hello',3:True,4:14.5,5:False,6:(7,8,9)}
        self.assertEqual(d,cll.convert2dict())



    # testing getNodeAt(self,index=0) method
    def test_getNodeAt(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)        
        self.assertEqual('<Node: 1 at index 0>',str(cll.getNodeAt()))
        self.assertEqual("<Node: 'hello' at index 2>",str(cll.getNodeAt(2)))



    # testing getDataAt(self,index=0) method
    def test_getDataAt(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)        
        self.assertEqual(1,cll.getDataAt())
        self.assertEqual('hello',cll.getDataAt(2))



    # testing editDataAt(self,data,index=0) method
    def test_editDataAt(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)
        cll.editDataAt(data=10,index=0)
        self.assertEqual(10,cll.getDataAt())
        cll.editDataAt('hello world',2)
        self.assertEqual('hello world',cll.getDataAt(2))



    # testing insertDataAt(self,data,index=0) method
    def test_insertDataAt(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)
        # default insert index=0
        cll.insertDataAt(data=10);
        t=(10, 1, 3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,cll.getAllData())
        self.assertEqual(8,len(cll))

        cll.insertDataAt('world',4); 
        t=(10, 1, 3, 'hello', 'world', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,cll.getAllData())
        self.assertEqual(9,len(cll))

        cll.insertDataAt('end',9); 
        t=(10, 1, 3, 'hello', 'world', True, 14.5, False, (7, 8, 9), 'end')
        self.assertEqual(t,cll.getAllData())
        self.assertEqual(10,len(cll))



    # testing deleteDataAt(self,index=0) method
    def test_deleteDataAt(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        cll.addDataFromList(l)
        # default index=0
        cll.deleteDataAt();
        t=(3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,cll.getAllData())
        self.assertEqual(6,len(cll))

        cll.deleteDataAt(4); 
        t=(3, 'hello', True, 14.5, (7, 8, 9))
        self.assertEqual(t,cll.getAllData())
        self.assertEqual(5,len(cll))

        cll.deleteDataAt(4); 
        t=(3, 'hello', True, 14.5)
        self.assertEqual(t,cll.getAllData())
        self.assertEqual(4,len(cll))



    # testing searchData(self, searchdata) method
    def test_searchData(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        cll.addDataFromList(l)        
        d={0: ('jaon', 'john', 'ali', 'karim'), 6: 'ali', 7: 'karim ali'}
        self.assertEqual(d,cll.searchData('ali'))



    # testing rotateLeft(dataunits=1) and rotateRight(dataunits=1)
    # rotateLeft(dataunits=1) rotates the circular doubly linked list left 
    # (anticlockwise) by the stated data units
    # rotateRight(dataunits=1) rotates the circular doubly linked list rightward 
    # (clockwise) by the stated data units
    def test_rotateLeftRight(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        cll.addDataFromList(l)        
        self.assertEqual(16,cll.getSize())
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll.getDataAt(0))
        cll.rotateLeft(1)
        self.assertEqual(10,cll.getDataAt(0))
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll.getDataAt(15))
        cll.rotateLeft(2)
        self.assertEqual(30,cll.getDataAt(0))
        self.assertEqual(20,cll.getDataAt(15))
        cll.rotateRight(2)
        self.assertEqual(10,cll.getDataAt(0))
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll.getDataAt(15))
        cll.rotateRight(1)
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll.getDataAt(0))
        self.assertEqual(None,cll.getDataAt(15))



    # testing clear() method
    def test_clear(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        cll.addDataFromList(l)        
        self.assertEqual(16,cll.getSize())
        cll.clear()
        self.assertEqual(0,cll.getSize())



    # copy() copies the circular linked list to a new instance
    def test_copy(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        cll.addDataFromList(l)        
        self.assertEqual(16,cll.getSize())
        cll2=cll.copy()
        self.assertEqual(16,cll2.getSize())
        self.assertEqual('myclinkedlist',cll2.getName())
        cll2.rotateLeft(1)
        self.assertEqual(10,cll2.getDataAt(0))
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll2.getDataAt(15))
        cll2.rotateLeft(2)
        self.assertEqual(30,cll2.getDataAt(0))
        self.assertEqual(20,cll2.getDataAt(15))
        cll2.rotateRight(2)
        self.assertEqual(10,cll2.getDataAt(0))
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll2.getDataAt(15))
        cll2.rotateRight(1)
        self.assertEqual(('jaon', 'john', 'ali', 'karim'),cll2.getDataAt(0))
        self.assertEqual(None,cll2.getDataAt(15))




# ----------------------- Data File related methods -----------------------
    #
    # testing setFilePreserve(self, preserve=True), isFilePreserved() methods
    def test_setFilePreserve(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertTrue(cll.isFilePreserved())
        cll.setFilePreserve(False)
        self.assertFalse(cll.isFilePreserved())



    # testing setFileAddress(self, directory=datadir, filename=None)
    # and getFileAddress() methods
    def test_setFileAddress(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        #filename="clinkedlist"
        fileaddr=filedir+os.sep+"myclinkedlist.pcds"
        cll.setFileAddress(filedir)
        self.assertEqual(fileaddr, cll.getFileAddress())
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="clinkedlist2"
        fileaddr=filedir+os.sep+filename+".pcds"        
        cll.setFileAddress(filedir,filename)
        self.assertEqual(fileaddr, cll.getFileAddress())




    # testing save(self, directory=datadir, filename=None, enc=True) method
    def test_save(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        cll.addDataFromList(l)        
        self.assertEqual(16,cll.getSize())
        self.assertTrue(cll.save())
        # msg: Encrypted Data Saved Successfully into 'C:\Users\admin\pcds_data\myclinkedlist.pcds'
        self.assertTrue(cll.save(filename="clinkedlist2",enc=False))
        # msg: Plain Data Saved Successfully into 'C:\Users\admin\pcds_data\clinkedlist2.pcds'



    # testing loadDataFromFile(self, fileaddr=None) method
    def test_loadDataFromFile(self):
        self.test_save()
        cll=clnkl.CLinkedList('myclinkedlist')
        self.assertEqual(0,cll.getSize())
        cll.loadDataFromFile()
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\myclinkedlist.pcds'
        self.assertEqual(16,cll.getSize())
        fileaddr=os.path.expanduser('~')+"\\pcds_data\\clinkedlist2.pcds"
        cll.clear()
        self.assertEqual(0,cll.getSize())
        cll.loadDataFromFile(fileaddr)
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\clinkedlist2.pcds'
        self.assertEqual(16,cll.getSize())



    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        cll=clnkl.CLinkedList('myclinkedlist')
        #filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        #filename="myclinkedlist"
        #fileaddr=filedir+os.sep+filename+".pcds"
        cll.setFileAddress()
        fileaddr=cll.getFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            cll.setFilePreserve(False)
            self.assertTrue(cll.removeDataFile())
        filename="clinkedlist2"
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        fileaddr=filedir+os.sep+filename+".pcds"
        cll.setFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            cll.setFilePreserve(False)
            self.assertTrue(cll.removeDataFile())






if __name__ == '__main__':
    unittest.main()




