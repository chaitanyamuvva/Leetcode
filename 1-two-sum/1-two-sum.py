class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in store_dict:
                return [store_dict[target-nums[i]],i]
            store_dict[nums[i]] = i
        return [-1,-1]
            
        