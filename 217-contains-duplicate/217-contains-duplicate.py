class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for i in nums:
            if i in dict1.keys():
                dict1[i]+=1
            else:
                dict1[i]=1
        print(dict1)
        print(dict1.values())
        for i,j in dict1.items():
            if(j>1):
                return True
        return False
            
        