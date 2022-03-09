class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int(''.join(map(str,digits)))
        print(digit,type(digit))
        digit+=1
        return [int(i) for i in str(digit)]