### 1.exhaustion
##
##class Solution:
##    def twoSum(nums, target):
##        lens = len(nums)
##        j=-1
##        for i in range(lens):
##            if (target - nums[i]) in nums:
##                if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
##                    continue
##                else:
##                    j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
##                    break
##        if j>0:
##            return [i,j]
##        else:
##            return []

### 2.modified exhaustion : only find answer in index before nums[i]
##
##class Solution:
##    def twoSum(nums, target):
##        lens = len(nums)
##        j=-1
##        for i in range(1,lens):
##            temp = nums[:i]
##            if (target - nums[i]) in temp:
##                j = temp.index(target - nums[i])
##                break
##        if j>=0:
##            return [j,i]

# 3.Hash - dict

class Solution:
    def twoSum(nums, target): # nums in list type
        hashmap = {} # dictionary
        for ind,num in enumerate(nums): # enumerate(list,start = 1)
            # enumerate: generate an iterator; The count of the current iteration
            # The value of the item at the current iteration
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
        
print(Solution.twoSum([1,2,5,7],3))

