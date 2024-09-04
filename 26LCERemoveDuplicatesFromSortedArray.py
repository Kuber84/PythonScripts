#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the unique elements in the order
# they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.

#solution:
#keep 2 pointers. one (j) compares if the next element same as cur element(i)
# & if its same then advances j else (its different) so it copies & changes cur
#finally return the index of cur element(i) + 1 (as index starts at 0).

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 1
        if len(nums) <= 1:
            return len(nums)
        cur = nums[i]
        while j < len(nums):
            if nums[j] != cur:
                i += 1
                nums[i] = nums[j]
                cur = nums[j]
            j += 1
        return i + 1
#solution from LC
#loop through all elements (j) from 1 to end
# if element same as prev number, then nothing to be done
# if element different from prev number, then advance i and copy this element into i.
        #i=1
        #for j in range(1,len(nums)):
        #    if nums[j]!=nums[j-1]:
        #        nums[i]=nums[j]
        #        i+=1
        #return i
