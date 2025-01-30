class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #nums = [i for i in nums if i!=val ]
        #return len(nums)
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
        

        