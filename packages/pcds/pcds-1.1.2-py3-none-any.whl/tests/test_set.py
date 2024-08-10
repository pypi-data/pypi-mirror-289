'''
Test Module: test_set.py
Test Module Name: test_set
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Friday August 09 2024 4:00 PM
Version:1.1.2
Python Version:3.12.4
'''

version="1.1.2"


import unittest
import os
from pcds import set
from pcds import utilities as u



# testing Set class
class TestSet(unittest.TestCase):
    # The following list and tupple have 25 data of which 5 are redundant
    listdata=[10,20,14,3,2.5,4.8,0,1,2,3,4,5,8,9,10,11,11,12,13,14,15,16,14,17,18]
    tupledata=(10,20,14,3,2.5,4.8,0,1,2,3,4,5,8,9,10,11,11,12,13,14,15,16,14,17,18)
    # testing the constructor of Set class
    # Set constructor supports list, tuple and Nonetype data
    def test___init__(self):
        nullset=set.Set()
        self.assertEqual(0,len(nullset))
        self.assertEqual("<Set: size=0, data=()>",str(nullset))
        # taking data from list        
        self.assertEqual(25,len(self.listdata))
        set1=set.Set(self.listdata)
        #<Set: size=20, data=(0, 1, 2, 2.5, 3, 4, 4.8, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20)>
        self.assertEqual(20,len(set1))
        # taking data from tuple        
        self.assertEqual(25,len(self.tupledata))
        set2=set.Set(self.tupledata)
        #<Set: size=20, data=(0, 1, 2, 2.5, 3, 4, 4.8, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20)>
        self.assertEqual(20,len(set2))
        # Two sets are equal when their data are equal in values and numbers
        self.assertTrue(set1==set2)
        # string and boolean data are also supported
        set3=set.Set([6,2,'a','b','ab',True,False,0,1,10])
        s="<Set: size=8, data=(False, True, 2, 6, 10, 'a', 'b', 'ab')>"
        self.assertEqual(8,len(set3))
        self.assertEqual(s,str(set3))



    # testing addDataFromList(listdata)
    def test_addDataFromList(self):
        set1=set.Set()
        set1.addDataFromList(self.listdata)        
        self.assertEqual(20,len(set1))
        s="<Set: size=20, data=(0, 1, 2, 2.5, 3, 4, 4.8, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20)>"
        self.assertEqual(s,str(set1))
        set2=set.Set([2,1,4,0])
        set2.addDataFromList([0,5,6,1,2,4])        
        self.assertEqual(6,len(set2))
        s="<Set: size=6, data=(0, 1, 2, 4, 5, 6)>"
        self.assertEqual(s,str(set2))
        # string and boolean data are also supported
        set3=set.Set([6,2,'a','b','ab',True,False,0,1,10])
        set3.addDataFromList([54,78,41,'a','c','xyz',50.45,'hello'])
        s="<Set: size=15, data=(False, True, 2, 6, 10, 41, 50.45, 54, 'a', 'b', 'c', 78, 'ab', 'xyz', 'hello')>"
        self.assertEqual(15,len(set3))
        self.assertEqual(s,str(set3))



    # testing addDataFromTuple(tupledata)
    def test_addDataFromTuple(self):
        set1=set.Set()
        set1.addDataFromTuple(self.tupledata)        
        self.assertEqual(20,len(set1))
        s="<Set: size=20, data=(0, 1, 2, 2.5, 3, 4, 4.8, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20)>"
        self.assertEqual(s,str(set1))
        set2=set.Set((2,1,4,0))
        set2.addDataFromTuple((0,5,6,1,2,4))
        self.assertEqual(6,len(set2))
        s="<Set: size=6, data=(0, 1, 2, 4, 5, 6)>"
        self.assertEqual(s,str(set2))
        # string and boolean data are also supported
        set3=set.Set((6,2,'a','b','ab',True,False,0,1,10))
        set3.addDataFromTuple((54,78,41,'a','c','xyz',50.45,'hello'))
        s="<Set: size=15, data=(False, True, 2, 6, 10, 41, 50.45, 54, 'a', 'b', 'c', 78, 'ab', 'xyz', 'hello')>"
        self.assertEqual(15,len(set3))
        self.assertEqual(s,str(set3))



    # deleteData(self,data) deletes the single data from the list if it is present
    def test_deleteData(self):
        set1=set.Set((6,2,'a','b','ab',True,False,0,1,10))
        self.assertEqual(8,len(set1))
        set1.deleteData(True)
        self.assertEqual(7,len(set1))
        s="<Set: size=7, data=(False, 2, 6, 10, 'a', 'b', 'ab')>"
        self.assertEqual(s,str(set1))
        set1.deleteData('ab')
        self.assertEqual(6,len(set1))
        s="<Set: size=6, data=(False, 2, 6, 10, 'a', 'b')>"
        self.assertEqual(s,str(set1))




    # testing clear(self) that deletes all the set data and binary tree data
    # producing a null set
    def test_clear(self):
        set1=set.Set((6,2,'a','b','ab',True,False,0,1,10))
        s="<Set: size=8, data=(False, True, 2, 6, 10, 'a', 'b', 'ab')>"
        self.assertEqual(8,len(set1))
        self.assertEqual(s,str(set1))
        set1.clear()
        s="<Set: size=0, data=()>"
        self.assertEqual(0,len(set1))
        self.assertEqual(s,str(set1))
        self.assertTrue(set1.isNull())




    # testing getDataFileAddress() and 
    # setDataFileAddress(self, directory=datadir, filename="set") functions
    def test_setDataFileAddress(self):
        set1=set.Set()
        self.assertIsNone(set1.getDataFileAddress())
        s=os.path.expanduser('~')+"\\pcds_data\\set.pcds"
        set1.setDataFileAddress()
        self.assertEqual(s,set1.getDataFileAddress())
        set1.setDataFileAddress(filename="set2")
        s=os.path.expanduser('~')+"\\pcds_data\\set2.pcds"
        self.assertEqual(s,set1.getDataFileAddress())




    # testing setFilePreserve(preserve=True) and isFilePreserved() functions
    def test_setFilePreserve(self):
        set1=set.Set((6,2,'a','b','ab',True,False,0,1,10))
        self.assertTrue(set1.isFilePreserved())
        set1.setFilePreserve(False)
        self.assertFalse(set1.isFilePreserved())




    # testing save(self, directory=datadir, filename="set", enc=True) and 
    # loadDataFromFile(self, fileaddr=datadir+os.sep+"set.pcds") functions    
    def test_save_load(self):
        set1=set.Set(self.listdata)
        set1.addDataFromList([54,78,41,'a','c','xyz',50.45,'hello'])
        set1.addDataFromList([14.23,85,'cd','pq','do',89])
        self.assertEqual(34,len(set1))
        self.assertTrue(set1.save())
        self.assertTrue(set1.save(filename="set2",enc=False))
        set2=set.Set()
        self.assertEqual(0,len(set2))
        self.assertTrue(set2.loadDataFromFile())
        self.assertEqual(34,len(set2))
        fileaddr=os.path.expanduser('~')+"\\pcds_data\\set2.pcds"
        set3=set.Set()
        self.assertEqual(0,len(set3))
        self.assertTrue(set3.loadDataFromFile(fileaddr))
        self.assertEqual(34,len(set3))




    # testing __eq__(self,right), __neq__(self,right) function
    def test_eq_neq(self):
        set1=set.Set(self.listdata)
        set2=set1.copy()
        set3=set.Set([54,78,41,'a','c','xyz',50.45,'hello'])
        set4=set.Set([14.23,85,'cd','pq','do',89])
        self.assertTrue(set1==set2)
        self.assertTrue(set1!=set3)
        self.assertTrue(set3!=set4)
        self.assertFalse(set1==10)
        self.assertFalse(10==set1)
        self.assertFalse(set1!=set2)




    # testing union(self,set2) function (A+B or A.union(B)) 
    def test_union(self):
        set1=set.Set([90,'a','b',80,70,1,2,10,20,'a','b','x',50,60,70,80,90])
        self.assertEqual(12,len(set1))
        set2=set1.copy()
        set3=set.Set([90,'a','b',80,70,90,80])
        self.assertEqual(5,len(set3))        
        set4=set.Set([90,'ab',80,70,80,'ab',90])
        self.assertEqual(4,len(set4))
        # A+B means A.union(B)
        self.assertEqual(6,len(set3+set4))
        self.assertEqual(12,len(set1+set2))
        self.assertEqual(12,len(set1+set3))




    # testing intersection(self,set2) function (A^B or A.intersection(B)) 
    def test_intersection(self):
        set1=set.Set([90,'a','b',80,70,1,2,10,20,'a','b','x',50,60,70,80,90])
        self.assertEqual(12,len(set1))
        set2=set1.copy()
        set3=set.Set([90,'a','b',80,70,90,80])
        self.assertEqual(5,len(set3))        
        set4=set.Set([90,'ab',80,70,80,'ab',90])
        set5=set.Set([62,42,32,'yz',12,52,22,75,85,'pq',95])
        self.assertEqual(11,len(set5))
        # A^B means A.intersection(B)
        self.assertEqual(3,len(set3^set4))
        self.assertEqual(12,len(set1^set2))
        self.assertEqual(5,len(set1^set3))
        self.assertEqual(0,len(set1^set5))
        self.assertEqual(0,len(set3^set5))
        self.assertEqual(0,len(set4^set5))




    # testing difference(self,set2) function (A-B or A.difference(B)) which is 
    # same as subtract(self,set2) function (A-B or A.subtract(B))
    def test_subtract(self):
        set1=set.Set([90,'a','b',80,70,1,2,10,20,'a','b','x',50,60,70,80,90])
        self.assertEqual(12,len(set1))
        set2=set1.copy()
        set3=set.Set([90,'a','b',80,70,90,80])
        self.assertEqual(5,len(set3))        
        set4=set.Set([90,'ab',80,70,80,'ab',90])
        set5=set.Set([62,42,32,'yz',12,52,22,75,85,'pq',95])
        self.assertEqual(11,len(set5))
        # A-B means A.subtract(B)
        self.assertEqual(0,len(set1-set2))
        self.assertEqual(7,len(set1-set3))
        self.assertEqual(9,len(set1-set4))
        self.assertEqual(12,len(set1-set5))
        self.assertEqual(0,len(set2-set1))
        self.assertEqual(0,len(set3-set1))
        self.assertEqual(1,len(set4-set1))
        self.assertEqual(11,len(set5-set1))
        self.assertEqual(0,len(set1-set1))




    # testing isSuperset(self,set2) function (A.isSuperset(B))
    def test_isSuperset(self):
        set1=set.Set([90,'a','b',80,70,1,2,10,20,'a','b','x',50,60,70,80,90])
        self.assertEqual(12,len(set1))
        set2=set1.copy()
        set3=set.Set([90,'a','b',80,70,90,80])
        self.assertEqual(5,len(set3))        
        set4=set.Set([90,'ab',80,70,80,'ab',90])
        set5=set.Set([62,42,32,'yz',12,52,22,75,85,'pq',95])
        self.assertEqual(11,len(set5))
        # A.isSuperset(B)
        self.assertTrue(set1.isSuperset(set2))
        self.assertTrue(set1.isSuperset(set3))
        self.assertFalse(set1.isSuperset(set4))
        self.assertFalse(set1.isSuperset(set5))
        self.assertFalse(set3.isSuperset(set1))
        self.assertFalse(set3.isSuperset(set4))
        self.assertFalse(set3.isSuperset(set5))




    # testing isSubset(self,set2) function (A.isSubset(B))
    def test_isSubset(self):
        set1=set.Set([90,'a','b',80,70,1,2,10,20,'a','b','x',50,60,70,80,90])
        self.assertEqual(12,len(set1))
        set2=set1.copy()
        set3=set.Set([90,'a','b',80,70,90,80])
        self.assertEqual(5,len(set3))        
        set4=set.Set([90,'ab',80,70,80,'ab',90])
        set5=set.Set([62,42,32,'yz',12,52,22,75,85,'pq',95])
        self.assertEqual(11,len(set5))
        # A.isSubset(B)
        self.assertTrue(set1.isSubset(set2))
        self.assertFalse(set1.isSubset(set3))
        self.assertFalse(set1.isSubset(set4))
        self.assertFalse(set1.isSubset(set5))
        self.assertTrue(set3.isSubset(set1))
        self.assertFalse(set3.isSubset(set4))
        self.assertFalse(set3.isSubset(set5))




    # testing isDisjoint(self,set2) function (A.isDisjoint(B))
    def test_isDisjoint(self):
        set1=set.Set([90,'a','b',80,70,1,2,10,20,'a','b','x',50,60,70,80,90])
        self.assertEqual(12,len(set1))
        set2=set1.copy()
        set3=set.Set([90,'a','b',80,70,90,80])
        self.assertEqual(5,len(set3))        
        set4=set.Set([90,'ab',80,70,80,'ab',90])
        set5=set.Set([62,42,32,'yz',12,52,22,75,85,'pq',95])
        self.assertEqual(11,len(set5))
        # A.isDisjoint(B)
        self.assertFalse(set1.isDisjoint(set2))
        self.assertFalse(set1.isDisjoint(set3))
        self.assertFalse(set1.isDisjoint(set4))
        self.assertTrue(set1.isDisjoint(set5))        
        self.assertFalse(set3.isDisjoint(set4))
        self.assertTrue(set3.isDisjoint(set5))
        self.assertTrue(set4.isDisjoint(set5))




if __name__ == '__main__':
    unittest.main()



