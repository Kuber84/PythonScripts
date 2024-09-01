#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

#Solution
#Not In place:
#create a new list & store nums1 -> this way can start populating result in nums1
#start at beginning of both arrays, add the lesser value to nums1 & keep moving pointer
#if nums3 reaches end(m) first, populate everything in nums2 to nums1
#if nums2 reaches end(n) first, populate everything in nums3 to nums1

class Solution(object):
    def mergeBf(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # bruteforce
        nums3=nums1[:]
        i,j,k=0,0,0
        if m==0:
            nums1[:]=nums2[:]
            print(nums1)
            return
        elif n==0:
            return
        while i<(m+n):
            if j<m and k<n:
                if nums3[j]<nums2[k]:
                    nums1[i]=nums3[j]
                    j+=1
                else:
                    nums1[i]=nums2[k]
                    k+=1
            elif j==m:
                nums1[i]=nums2[k]
                k+=1
            elif k==n:
                nums1[i]=nums3[j]
                j+=1
            i+=1
            print(nums1)
        # nums1=nums3[:]
        print(nums1)
        return

#o(m+n)time, o(1) space Solution:
#start comparing the 2 lists using m & n as indices & populate the greater of both at end of nums1
#if m reaches 0, populate from nums2
#if n reaches 0, populate from nums1 (most likely no need to do anything but let the algorithm run thru to end)
    def merge(self, nums1, m, nums2, n):
        if m==0:
            nums1[:]=nums2[:]
            print(nums1)
            return
        elif n==0:
            return
        i=m+n-1
        m-=1
        n-=1
        while(i>=0):
            if m>=0 and n>=0:
                if nums1[m]>nums2[n]:
                    nums1[i]=nums1[m]
                    m-=1
                else:
                    nums1[i]=nums2[n]
                    n-=1
            elif m<0:
                nums1[i]=nums2[n]
                n-=1
            elif n<0:
                nums1[i]=nums1[m]
                m-=1
            i-=1
            print("nums1 {} m {} n {}".format(nums1,m,n))

list1 = [1,2,3,0,0,0]
list2 = [2,5,6]
#Solution().mergeBf(list1,3,list2,3)
Solution().merge(list1,3,list2,3)