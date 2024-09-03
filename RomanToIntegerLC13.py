class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    #solution: brute force: add values, keep track of prev if prev letter value less than current letter
    #then add this value minus(-) the value already added
        # total=0
        # prevLetter = ''
        # for letter in s:
        #     if letter == 'M':
        #         if prevLetter == 'C':
        #             total+=800
        #         else:
        #             total+=1000
        #     elif letter == 'D':
        #         if prevLetter == 'C':
        #             total+=300
        #         else:
        #             total+=500
        #     elif letter == 'C':
        #         if prevLetter== 'X':
        #             total+=80
        #         else:
        #             total+=100
        #     elif letter == 'L':
        #         if prevLetter== 'X':
        #             total+=30
        #         else:
        #             total+=50
        #     elif letter == 'X':
        #         if prevLetter== 'I':
        #             total+=8
        #         else:
        #             total+=10
        #     elif letter == 'V':
        #         if prevLetter== 'I':
        #             total+=3
        #         else:
        #             total+=5
        #     elif letter=='I':
        #         total+=1
        #     prevLetter=letter
        # return total
#solution: create a dict with all denominations
#go through the letters from left to right and add denom values to total
#if the denom of the next letter is more than the current - subtract current denom
        total=0
        denom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i<len(s)-1 and denom[s[i]]<denom[s[i+1]]:
                total-=denom[s[i]]
            else:
                total+=denom[s[i]]
        return total