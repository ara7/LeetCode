class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #O(n) | instead of looping that gives O(n^2) complexity 
        #remove elements that are not helping while maintainig subarray
        #if left less than right ele remove it i.e if -ve prefix remove from current_Sum 
        maxSubArrSum = nums[0]
        current_Sum = 0
        for n in nums:
            if current_Sum < 0:
                current_Sum = 0
            current_Sum += n
            maxSubArrSum = max(maxSubArrSum, current_Sum)
        return maxSubArrSum
            