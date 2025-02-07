class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        op_list = []
        for i in range(len(sorted_list)-2):
            #skip duplicate
            if i>0 and sorted_list[i]==sorted_list[i-1]: #important step to remove duplicates
                continue
            l = i+1
            r = len(sorted_list)-1
            target = -sorted_list[i]
            sum_2 = 0
            
            while (l<r): #prevent overlap
                sum_2 = sorted_list[l] + sorted_list[r]

                if sum_2 == target:
                    op_list.append([sorted_list[i],sorted_list[l], sorted_list[r]])
                    l+=1
                    r-=1
                    while l<r and sorted_list[l] == sorted_list[l-1]:
                        l+=1
                    while l<r and sorted_list[r] == sorted_list[r+1]:
                        r-=1
                elif (sum_2 < target):
                    l+=1
                elif (sum_2 > target):
                    r-=1
        return op_list
        