class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # for j in range(0,len(haystack)-len(needle)+1):
        #     if needle == haystack[j:j+len(needle)]:
        #         return j
        # return -1

#solution: scan from first letter then length-len(needle) cos for needle to exist shud exist at that index
#in the worst case. do string comparison at every index.

        for j in range(0, len(haystack) - len(needle) + 1):
            for k in range(0, len(needle)):
                if needle[k] != haystack[j + k]:
                    break
            if k == len(needle) - 1 and needle[k] == haystack[j + k]:
                return j
        return -1