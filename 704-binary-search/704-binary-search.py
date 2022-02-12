class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high-low)//2
            midvalue = nums[mid]
            if(midvalue==target):
                return mid
            
            elif(target<midvalue):
                high = mid-1
            
            else:
                low = mid+1
        return -1