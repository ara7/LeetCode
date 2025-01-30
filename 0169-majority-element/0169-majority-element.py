class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Sorting: Insertion sort
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j>=0 and key<nums[j]:
                nums[j+1] = nums[j]
                j = j - 1
            nums[j+1] = key
        return nums[len(nums)//2]
        #return nums[-1] #Wrong because: The majority element is defined as the element that appears more than n/2 times, and it will always appear at nums[len(nums) // 2] in the sorted array