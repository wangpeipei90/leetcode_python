'''
Created on Feb 19, 2018

@author: peipei
'''
import unittest
import bisect
class Test295(unittest.TestCase):
    def runTest(self):
        addNum(1)
        self.failUnlessEqual(findClosestElements([1,2,3,4,5],4,3),[1,2,3,4],"fail 1")



def suite():
    suite=unittest.TestSuite()
    suite.addTest(Test658())
    return suite

class MedianFinder(object): 
    def __init__(self):
               
    def addNum(self,num):
        
    
    def findMedian(self): 
    

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite())
#     res=findClosestElements([1,2,3,4,5],4,-1)
#     print(res)
#     res=findClosestElements([1,2,3,4,5],4,6)
#     print(res)
#     res=findClosestElements([1,2,3,4,5],4,3)
#     print(res)
#     res=findClosestElements([1,2,2,4,5],4,3)
#     print(res)
    