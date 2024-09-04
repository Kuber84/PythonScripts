class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return len(s.split()[-1]) #using inbuilt fn split & the return len of last word
        rev=s[::-1].strip() #reverse & strip white space
        len1=0
        for l in rev:
            if l!=' ':
                len1+=1 #increase length until white space
            else:
                break
        return len1