class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ''
        # if(len(strs)<2):
        #     return strs[0]
        # if(0>=len(strs[0])):
        #     return final
        for i in range(len(max(strs))):
            if(i>=len(strs[0])):
                return final
            string = strs[0][i]
            for s in strs[1:]:
                if(len(s)<=i or s[i]!=string):
                    return final
            final = final+string
        return final
        