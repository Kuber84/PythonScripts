class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=''
        if not strs:
            return ''
        elif len(strs)==1:
            return strs[0]
        shortest=strs[0]
        for i in range(len(shortest)):
            flag = True
            for word in strs[1:]:
                if len(word)>i:
                    if shortest[i]!=word[i]:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                prefix+=strs[0][i]
            else:
                break
        return prefix
print(Solution().longest_common_prefix(['Apple','Apply','Appa']))