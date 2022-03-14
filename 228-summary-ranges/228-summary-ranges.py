class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums = list(set(nums))
        nums.sort()
        count = 0
        new_list =[]
        if(len(nums)==1):
            new_list.append(str(nums[0]))
            return new_list
        for i in range(0,len(nums)-1):
            curr = nums[i]
            count+=1
            if(nums[i]+1==nums[i+1] and (i+1)<len(nums)):
                if(count==1):
                    first = curr
                last = nums[i+1]
                # print(nums[i],nums[i+1],count)
                if(nums[i+1]==nums[len(nums)-1] and(i+1)==(len(nums)-1)):
                    new_list.append(str(first)+"->"+str(last))
                    print(new_list)
                    break
                elif(nums[i+1]!=nums[len(nums)-1] and (i+1)==(len(nums)-1)):
                    new_list.append(str(last))
                    print(new_list)
                    
            else:
                # print(nums[i],nums[i+1],count)
                if(count>1):
                    count = 0
                    new_list.append(str(first)+"->"+str(last))
                    # print(new_list)
                    if(nums[i+1]==nums[len(nums)-1] and (i+1)==(len(nums)-1)):
                        new_list.append(str(nums[i+1]))
                        # print(new_list)
                        break
                    # print("print",nums[i],nums[i+1],count)
                else:
                    count = 0
                    new_list.append(str(nums[i]))
                    print(nums[i],nums[i+1])
                    print(new_list)
                    if(nums[i+1]==nums[len(nums)-1] and (i+1)==(len(nums)-1)):
                        new_list.append(str(nums[i+1]))
                        print(new_list)
                        break
                    # print("print",nums[i],nums[i+1],count)
                count = 0
        return new_list
                    
                                    
            
            
        