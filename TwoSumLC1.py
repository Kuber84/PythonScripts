#Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
# O(nsquare) - bruteforce
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if (nums[i]+nums[j] == target):
#                 print("i{} j{}".format(i,j))
#             return [i,j]
# O(n)
    numToIndex = {}
    for i in range(len(nums)):
        if (target-nums[i] in numToIndex):
            return [i,numToIndex[target-nums[i]]]
        numToIndex[nums[i]] = i

arr = [int(x) for x in input("Enter list separated by space:").split()]
target = int(input("Enter target:"))
ret = twoSum(arr,target)
for x in ret:
    print (x)