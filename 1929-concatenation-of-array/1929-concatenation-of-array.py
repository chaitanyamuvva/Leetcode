class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final = [0]*n*2
        print(final,len(final))
        for i in range(n):
            final[i] = nums[i]
            final[i+n] = nums[i]
        return final