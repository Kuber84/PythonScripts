class Solution(object):
    @staticmethod
    def length_of_last_word(s):
        """
        :type s: str
        :rtype: int
        """
        #return len(s.split()[-1]) #using inbuilt fn split & the return len of last word
        #rev=s[::-1].strip() #reverse & strip white space
        # i=len(s)-1
        # flag=False
        # len1=0
        # while i>=0:
        #     if flag==False and s[i]==' ':
        #         i-=1
        #         continue
        #     else:
        #         flag=True
        #         if s[i]==' ':
        #             return len1
        #         len1+=1
        #         i-=1
        len1=0
        i=len(s)
        while i>0:
            i-=1
            if s[i]!=' ':
                len1+=1 #increase length until white space
            elif len1>0:
                return len1
        return len1