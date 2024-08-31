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

list1 = [1,2,3,0,0,0]
list2 = [2,5,8]
#Solution().mergeBf(list1,3,list2,3)
