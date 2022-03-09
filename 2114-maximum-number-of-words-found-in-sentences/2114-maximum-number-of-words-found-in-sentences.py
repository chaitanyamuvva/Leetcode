class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for i in sentences:
            if(len(i.strip().split(' '))>maxi):
                maxi = len(i.strip().split(' '))
        return maxi
        