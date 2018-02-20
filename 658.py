'''
Created on Feb 19, 2018

@author: peipei
'''
import unittest
class Test658(unittest.TestCase):
    def runTest(self):
        self.failUnlessEqual(findClosestElements([1,2,3,4,5],4,3),[1,2,3,4],"fail 1")
        self.failUnlessEqual(findClosestElements([1,2,3,4,5],4,-1),[1,2,3,4],"fail 2")
        self.failUnlessEqual(findClosestElements([1,2,3,3,6,6,7,7,9,9],8,8),[3,3,6,6,7,7,9,9],"fail 3")
        self.failUnlessEqual(findClosestElements([1,2,3,4,5],4,6),[2,3,4,5],"fail4")
        self.failUnlessEqual(findClosestElements([1,2,2,4,5], 4, 3),[1,2,2,4],"fail 5")
        
        self.failUnlessEqual(findClosestElements2([1,2,3,4,5],4,3),[1,2,3,4],"fail 1")
        self.failUnlessEqual(findClosestElements2([1,2,3,4,5],4,-1),[1,2,3,4],"fail 2")
        self.failUnlessEqual(findClosestElements2([1,2,3,3,6,6,7,7,9,9],8,8),[3,3,6,6,7,7,9,9],"fail 3")
        self.failUnlessEqual(findClosestElements2([1,2,3,4,5],4,6),[2,3,4,5],"fail4")
        self.failUnlessEqual(findClosestElements2([1,2,2,4,5], 4, 3),[1,2,2,4],"fail 5")


def suite():
    suite=unittest.TestSuite()
    suite.addTest(Test658())
    return suite

# class Solution(object):        
#     def findClosestElements(self, arr, k, x):
def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    n=len(arr)
    p,q=0,n-1
    l,r=0,n-1
    while l<=r:        
        mid=(l+r)//2
        if arr[mid]==x:
            p=q=mid
            break
        elif arr[mid]<x:
            l=mid+1
            p=mid
        else:
            r=mid-1
            q=mid        
#     print(p,q)
#     count=0
    if p==q==0:
        return arr[:k]
    elif p==q==n-1:
        return arr[-k:]
    elif p==q:
        p,q,count=p-1,q+1,1 
    else:
        count=0
#     print("count: ",count)
    while count<k:
        if p>=0 and q<=n-1:
            if x-arr[p]<=arr[q]-x:
                p-=1
            else:
                q+=1
        elif p<0:
            q+=1
        elif q>n-1:
            p-=1
        count+=1
#     print(p,q)
#     print("count: ",count)
    p,q=max(p+1,0),min(q-1,n-1)
    return arr[p:q+1]

def findClosestElements2(arr,k,x): 
    arr.sort(key=lambda i:abs(i-x)) 
    res=arr[:k]
    res.sort()
    return res            
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
    