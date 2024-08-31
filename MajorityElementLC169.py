#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=defaultdict(int)
        for i in nums:
            #if i not in count:
            #    count[i]=0
            count[i]+=1
        val=count.keys()[0]
        maxi=count.values()[0]
        for i,j in count.items():
            if j>maxi:
                maxi=j
                val=i
        return val
        #alternatively since the majority element is present more then n/2 - we can just check for hte first key,values
        #pair which had value greater than n//2
        #for key,val in count.items():
        #   if val>n//2:
        #       return key