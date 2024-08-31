class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x<4:
            return 1 if x else 0
        s, mid, e = 1, 0, x
        while s<=e:
            mid=(s+e)//2
            sq=mid*mid
            if sq==x:
                return mid
            elif sq>x:
                e=mid-1
            elif sq<x:
                s=mid+1
        return mid-1 if mid*mid > x else mid
print("enter number:")
num=int(input())
print("sqrt:"+str(Solution().mySqrt(num)))