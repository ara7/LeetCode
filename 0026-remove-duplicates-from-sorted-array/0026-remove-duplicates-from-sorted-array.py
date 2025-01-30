class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #cache = {}
        k = 0
        for i in range(len(nums)):
            #if nums[i] not in cache.values():# 
            if i == 0 or nums[i] != nums[i-1]:
                nums[k] = nums[i] #cache[k] = nums[i]
                k+=1
        #nums = cache.values()
        '''The line nums = cache.values() doesn't modify the original list nums in-place; instead, it reassigns the local variable nums to a new object. '''
        return k
        