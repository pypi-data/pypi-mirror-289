'''
Test Module: test_pqueue.py
Test Module Name: test_pqueue (priority queue)
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Friday August 09 2024 4:00 PM
Version:1.1.1
Python Version:3.12.4
'''

version="1.1.1"


import unittest
import os
from pcds import pqueue as pq



class TestQueue(unittest.TestCase):
    # creating queue instances
    q1=pq.PQueue()
    q2=pq.PQueue(5)
    q3=pq.PQueue(maxsize=10)
    q4=pq.PQueue(maxsize=0)


    # testing the constructor function
    def test___init__(self):        
        self.assertIsInstance(self.q1,pq.PQueue)
        self.assertIsInstance(self.q2,pq.PQueue)
        self.assertIsInstance(self.q3,pq.PQueue)
        self.assertIsInstance(self.q4,pq.PQueue)



    # testing the enQueue(), __str__()    
    def test_enQueue(self):
        self.q1.enQueue(10,15)
        self.q1.enQueue(14.78,18)
        self.q1.enQueue('hello',25)
        self.q1.enQueue('abc',12)
        self.q1.enQueue(True,5)
        self.q1.enQueue(False,16)
        self.q1.enQueue(None,22)
        s="<PriorityQueue [7/100], Head:({'data': 'hello', 'priority': 25}, {'data': None, 'priority': 22}, {'data': 14.78, 'priority': 18}, {'data': False, 'priority': 16}, {'data': 10, 'priority': 15}, {'data': 'abc', 'priority': 12}, {'data': True, 'priority': 5}):Tail>"
        self.assertEqual(s,str(self.q1))

        # Queue of maxsize = 5
        self.q2.enQueue(10,20)
        self.q2.enQueue(14.78,30)
        self.q2.enQueue('hello',12)
        self.q2.enQueue('abc',5)
        self.q2.enQueue(True,35)        
        s="<PriorityQueue [5/5], Head:({'data': True, 'priority': 35}, {'data': 14.78, 'priority': 30}, {'data': 10, 'priority': 20}, {'data': 'hello', 'priority': 12}, {'data': 'abc', 'priority': 5}):Tail>"
        self.assertEqual(s,str(self.q2))

        self.assertEqual(True,self.q2.enQueue(False))
        s="<PriorityQueue [5/5], Head:({'data': 14.78, 'priority': 30}, {'data': 10, 'priority': 20}, {'data': 'hello', 'priority': 12}, {'data': 'abc', 'priority': 5}, {'data': False, 'priority': 0}):Tail>"
        self.assertEqual(s,str(self.q2))

        self.assertEqual(14.78,self.q2.enQueue(None))
        s="<PriorityQueue [5/5], Head:({'data': 10, 'priority': 20}, {'data': 'hello', 'priority': 12}, {'data': 'abc', 'priority': 5}, {'data': False, 'priority': 0}, {'data': None, 'priority': 0}):Tail>"
        self.assertEqual(s,str(self.q2))




    # testing the deQueue(), __str__()
    def test_deQueue(self):
        self.q1=pq.PQueue()
        self.q2=pq.PQueue(5)
        self.test_enQueue()
        self.assertEqual('hello',self.q1.deQueue())
        self.assertEqual(None,self.q1.deQueue())
        self.assertEqual(14.78,self.q1.deQueue())
        s="<PriorityQueue [4/100], Head:({'data': False, 'priority': 16}, {'data': 10, 'priority': 15}, {'data': 'abc', 'priority': 12}, {'data': True, 'priority': 5}):Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(False,self.q1.deQueue())
        self.assertEqual(10,self.q1.deQueue())
        self.assertEqual('abc',self.q1.deQueue())
        s="<PriorityQueue [1/100], Head:({'data': True, 'priority': 5}):Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(True,self.q1.deQueue())
        s="<PriorityQueue [0/100], Head:():Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(None,self.q1.deQueue())
        s="<PriorityQueue [0/100], Head:():Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(None,self.q1.deQueue())
        s="<PriorityQueue [0/100], Head:():Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(10,self.q2.deQueue())
        s="<PriorityQueue [4/5], Head:({'data': 'hello', 'priority': 12}, {'data': 'abc', 'priority': 5}, {'data': False, 'priority': 0}, {'data': None, 'priority': 0}):Tail>"
        self.assertEqual(s,str(self.q2))

        self.assertEqual('hello',self.q2.deQueue())
        s="<PriorityQueue [3/5], Head:({'data': 'abc', 'priority': 5}, {'data': False, 'priority': 0}, {'data': None, 'priority': 0}):Tail>"
        self.assertEqual(s,str(self.q2))




    # testing getMaxSize(), changeMaxSize() methods
    def test_changeMaxSize(self):
        self.assertEqual(None,self.q4.getMaxSize())
        self.q4=pq.PQueue(5)
        self.assertEqual(5,self.q4.getMaxSize())
        self.q4.enQueue(15,35)
        self.q4.enQueue('hi',25)
        self.q4.enQueue([1,2,3,'hello',(4,7,8)],8)
        self.q4.enQueue({1:'ali',2:'khan',3:'haque'},28)
        s="<PriorityQueue [4/5], Head:({'data': 15, 'priority': 35}, {'data': {1: 'ali', 2: 'khan', 3: 'haque'}, 'priority': 28}, {'data': 'hi', 'priority': 25}, {'data': [1, 2, 3, 'hello', (4, 7, 8)], 'priority': 8}):Tail>"
        self.assertEqual(s,str(self.q4))




    # testing getSize(), __len__() method
    def test_getSize(self):
        self.q1=pq.PQueue()
        self.q2=pq.PQueue(5)
        self.test_enQueue()        
        self.assertEqual(7,self.q1.getSize())
        self.assertEqual(5,self.q2.getSize())
        self.assertEqual(7,len(self.q1))
        self.assertEqual(5,len(self.q2))




    # testing copy() method
    def test_copy(self):
        q1=pq.PQueue()
        q1.enQueue(15,16)
        q1.enQueue(10.45,20)
        q1.enQueue('world',5)
        q1.enQueue(True,25)
        q1.enQueue(None,10)
        q1.enQueue(False,30)
        q1.enQueue([1,2,3,'hello',(4,7,8)],22)
        q1.enQueue([1,2,3,'hello',(4,7,8)],18)
        self.assertEqual(8,len(q1))
        q2=q1.copy()
        self.assertEqual(8,len(q2))




    # testing setFileAddress(self, directory=datadir, filename="queue", enc=True) 
    # and getFileAddress() methods
    def test_setFileAddress(self):
        q1=pq.PQueue()        
        q1.setFileAddress()
        s=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"pqueue.pcds"
        self.assertEqual(s,q1.getFileAddress())
        q1.setFileAddress(filename="pqueue2")
        s=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"pqueue2.pcds"
        self.assertEqual(s,q1.getFileAddress())




    # testing isFilePreserved() and setFilePreserve() methods
    def test_setFilePreserved(self):
        q1=pq.PQueue()
        q2=pq.PQueue(0)
        self.assertEqual(True,q1.isFilePreserved())
        self.assertEqual(None,q2.isFilePreserved())
        q1.setFilePreserve(False)
        self.assertEqual(False,q1.isFilePreserved())
 



    # testing clear() method
    def test_clear(self):
        self.q1=pq.PQueue()
        self.q2=pq.PQueue(5)
        self.test_enQueue()        
        self.assertEqual(7,self.q1.getSize())
        self.assertEqual(5,self.q2.getSize())
        self.q1.clear()
        self.assertEqual(0,self.q1.getSize())
        self.assertEqual(100,self.q1.getMaxSize())
        self.q2.clear()
        self.assertEqual(0,self.q2.getSize())
        self.assertEqual(5,self.q2.getMaxSize())




    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        q1=pq.PQueue()
        directory=os.path.expanduser('~')+os.sep+"data"+os.sep+"pcds_data"
        q1.setFileAddress(directory,"mypqueue")
        fileaddr=os.path.expanduser('~')+os.sep+"data"+os.sep+"pcds_data"+os.sep+"mypqueue.pcds"
        self.assertEqual(fileaddr,q1.getFileAddress())
        q1.setFilePreserve(False)
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            self.assertTrue(q1.removeDataFile())




    # testing data file I/O operations
    # testing save() method
    def test_save(self):
        q1=pq.PQueue()        
        q1.enQueue(10,12)
        q1.enQueue([1,2,3,(4,7,9)],15)
        q1.enQueue('hello',5)
        q1.enQueue('world',30)
        q1.enQueue({1:10,2:15,3:[40,50]},25)
        q1.enQueue(14.78,18)
        q1.enQueue(True,15)
        q1.enQueue(False,20)
        q1.enQueue(None,22)
        self.assertEqual(9,len(q1))
        self.assertTrue(q1.save())
        dirstr=os.path.expanduser('~')+os.sep+"pcds_data"
        self.assertTrue(q1.save(directory=dirstr,filename="pqueue2",enc=False))



    # testing loadDataFromFile() method
    def test_loadDataFromFile(self):
        q1=pq.PQueue()
        self.assertEqual(0,len(q1))
        self.assertTrue(q1.loadDataFromFile())
        self.assertEqual(9,len(q1))
        q1.clear()
        fileaddr=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"pqueue2.pcds"
        self.assertTrue(q1.loadDataFromFile(fileaddr))
        self.assertEqual(q1.getSize(),len(q1))





# running the main() of unittest
if __name__=='__main__':
    unittest.main()













