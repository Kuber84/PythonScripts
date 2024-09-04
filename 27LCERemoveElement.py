#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the #elements may be changed. Then return the number of elements in nums which are not equal to val.
#Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following #things:
#Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The no. of remaining elements of nums are not important as well as the size of nums.
#Return k.

#solution O(n) time O(1) space
#start 2 pointers 1 from beginning (where we will check if same as val & switch it out with the other pointer).
#other pointer from end - if it is same as val - decrement this pointer
#loop until these pointers dont cross each other.
#handle corner case of i&j same or i>j
#return the first pointer index+1

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,j=0,len(nums)-1
        while(i<j):
            if nums[j]==val:
                j-=1
                continue
            if nums[i]==val:
                nums[i]=nums[j]
                j-=1
            i+=1
        if i==j:
            if nums[i]==val:
                return j
            else:
                return j+1
        return j+1