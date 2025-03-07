class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #everything left of L pointer is our sorted answer

        L = 0
        R = 0 #O(2n) time, space O(1)
        while R < len(nums):
            count = 1
            while R+1 < len(nums) and nums[R] == nums[R+1]:
                R += 1
                count += 1
            for i in range(min(2, count)):
                nums[L] = nums[R]
                L+=1
            R+=1
        return L
        